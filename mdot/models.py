from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.


class Platform(models.Model):
    name = models.CharField(max_length=15)
    app_store = models.CharField(max_length=30)

    def __str__(self):
        return self.app_store


class Sponsor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    netid = models.CharField(max_length=16)
    email = models.EmailField(max_length=256)
    title = models.CharField(max_length=50)
    department = models.CharField(max_length=30)
    unit = models.CharField(max_length=30)


class Manager(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    netid = models.CharField(max_length=16)
    email = models.EmailField(max_length=256)


class App(models.Model):
    name = models.CharField(max_length=50)
    primary_language = models.CharField(max_length=20)
    platform = models.ManyToManyField(Platform)
    app_manager = models.ForeignKey(Manager)
    app_sponsor = models.ForeignKey(Sponsor)
    requestor = models.ForeignKey(User)
    request_date = models.DateTimeField(auto_now_add=True)


class Agreement(models.Model):
    app = models.ForeignKey(App)
    agree_time = models.DateTimeField(auto_now_add=True)


class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = "__all__"


class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = "__all__"


class AppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ["name", "primary_language", "platform"]
        labels = {
            "platform": "Add to the University of Washington"
        }

    def __init__(self, *args, **kwargs):
        super(AppForm, self).__init__(*args, **kwargs)
        self.fields["primary_language"].widget.attrs["placeholder"] = "e.g. English"
        self.fields["platform"].widget = forms.CheckboxSelectMultiple()
        self.fields["platform"].queryset = Platform.objects.all()
