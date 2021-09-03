from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import FieldError
from django.forms import inlineformset_factory
from django.utils.timezone import *

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


class Agreement(models.Model):
    app = models.ForeignKey('App', on_delete=models.CASCADE)
    agree = models.NullBooleanField(default=None)
    agree_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.app.name


class App(models.Model):
    name = models.CharField(max_length=50)
    primary_language = models.CharField(max_length=20)
    platform = models.ManyToManyField(Platform)
    app_manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    manager_contact = models.CharField(default=str(Manager.email),
                                       editable=False)
    app_sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    sponsor_contact = models.CharField(default=str(Sponsor.email),
                                       editable=False)
    requestor = models.ForeignKey(User, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def sponsor_contact(self):
        return self.app_sponsor.email

    def manager_contact(self):
        return self.app_manager.email

    def app_platform(self):
        return ", ".join([p.app_store for p in self.platform.all()])

    # finds app's corresponding agreement time if it exists
    def status(self):
        # return self.app_agreement.agree
        if not Agreement.objects.all().filter(app__name=self.name).exists():
            return "Pending"
        else:
            dates = Agreement.objects.all().filter(app__name=self.name)
            agreements = []
            for date in dates:
                agreements.append(date)

            # method to sort agreements by agree time
            def time(agreement):
                return agreement.agree_time

            agreements.sort(key=time)
            print(agreements[-1].agree_time)
            time = str(time(agreements[-1]).
                       strftime('%b %d, %Y, %I:%M %p'))
            if agreements[-1].agree:
                return "Agreed on " + time
            else:
                return "Denied on " + time

    sponsor_contact = property(sponsor_contact)
    manager_contact = property(manager_contact)
    agreed_to = property(status)
    platforms = property(app_platform)

    app_agreement = models.CharField(Agreement, default=str(agreed_to),
                                     editable=False, max_length=150)


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


class AgreementForm(forms.ModelForm):
    class Meta:
        model = Agreement
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AgreementForm, self).__init__(*args, **kwargs)
        self.fields["agree"].widget = forms.NullBooleanSelect()


class AppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ["name", "primary_language", "platform"]
        labels = {
            "name": "Application Name",
            "platform": "Distribution Platform"
        }

    def has_changed(self):
        return True

    def __init__(self, *args, **kwargs):
        super(AppForm, self).__init__(*args, **kwargs)
        self.fields["primary_language"] \
            .widget.attrs["placeholder"] = "e.g. English"
        self.fields["platform"].widget = forms.CheckboxSelectMultiple()
        self.fields["platform"].queryset = Platform.objects.all()
