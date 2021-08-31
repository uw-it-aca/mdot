from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import FieldError
import re

# Create your models here.

# assumes NetID conforms to personal or shared NetID requirements
netid_validator = RegexValidator(
    regex='^[a-z][0-9a-z]{0,7}$', message='NetID must be valid')


class Platform(models.Model):
    name = models.CharField(max_length=15)
    app_store = models.CharField(max_length=30)

    def __str__(self):
        return self.app_store


class Sponsor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    netid = models.CharField(max_length=16, validators=[netid_validator])
    email = models.EmailField(max_length=256)
    title = models.CharField(max_length=50)
    department = models.CharField(max_length=30)
    unit = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Manager(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    netid = models.CharField(
        max_length=16,
        validators=[netid_validator],
        error_messages={'required': 'Please enter a valid NetID'}
    )
    email = models.EmailField(max_length=256)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class App(models.Model):
    name = models.CharField(max_length=50)
    primary_language = models.CharField(max_length=20)
    platform = models.ManyToManyField(Platform)
    app_manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    app_sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    requestor = models.ForeignKey(User, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Agreement(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    agree = models.BooleanField(default=True)
    agree_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.app.name


class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = "__all__"
        labels = {
            "netid": "UW NetID"
        }


class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = "__all__"
        labels = {
            "netid": "UW NetID"
        }


class AppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ["name", "primary_language", "platform"]
        labels = {
            "name": "Application Name",
            "platform": "Distribution Platform"
        }

    def __init__(self, *args, **kwargs):
        super(AppForm, self).__init__(*args, **kwargs)
        self.fields["primary_language"] \
            .widget.attrs["placeholder"] = "e.g. English"
        self.fields["platform"].widget = forms.CheckboxSelectMultiple()
        self.fields["platform"].queryset = Platform.objects.all()
