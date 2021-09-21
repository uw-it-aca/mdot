from datetime import timedelta

from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Create your models here.

# assumes NetID conforms to personal or shared NetID requirements
netid_validator = RegexValidator(
    regex='^[a-z][0-9a-z]{0,7}$', message='NetID must be valid.')


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
        error_messages={'required': 'Please enter a valid NetID'},
    )
    email = models.EmailField(max_length=256)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


AGREEMENT_CHOICES = [
    ('agreed', 'Agreed'),
    ('denied', 'Denied'),
    ('removed', 'Removed'),
]


class Agreement(models.Model):
    app = models.ForeignKey('App', on_delete=models.CASCADE)
    status = models.CharField(choices=AGREEMENT_CHOICES,
                              max_length=20,
                              default='')
    agree_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.app.name

    def clean(self):
        if self.status == '':
            raise ValidationError('Please select a status '
                                  'for the agreement.')

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Agreement, self).save(*args, **kwargs)


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

    def status(self):
        dates = Agreement.objects.filter(app__name=self.name)
        if not dates.exists():
            return "Pending"
        else:
            agreements = [date for date in dates]

            # method to sort agreements by agree time
            def time(agreement):
                return agreement.agree_time

            agreements.sort(key=time)
            # time adjusted back 7 hours due to disparity (temp fix?)
            time = (agreements[-1].agree_time - timedelta(hours=7))\
                .strftime('%b %d, %Y, %I:%M %p')
            if agreements[-1].status == 'agreed':
                return "Agreed on " + time
            elif agreements[-1].status == 'denied':
                return "Denied on " + time
            else:  # agreements[-1].status == 'removed':
                return 'Removed on ' + time

    sponsor_contact = property(sponsor_contact)
    manager_contact = property(manager_contact)
    platforms = property(app_platform)


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
