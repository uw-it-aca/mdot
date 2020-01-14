from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.


class Sponsor(models.Model):
    name = models.CharField(max_length=50)
    netid = models.CharField(max_length=8)
    title = models.CharField(max_length=50)
    email = models.EmailField(max_length=40)
    department = models.CharField(max_length=30)
    unit = models.CharField(max_length=30)


class Manager(models.Model):
    name = models.CharField(max_length=50)
    netid = models.CharField(max_length=8)
    email = models.EmailField(max_length=40)


class App(models.Model):
    name = models.CharField(max_length=50)
    primary_language = models.CharField(max_length=20)  # abbreviations?
    ios_platform = models.BooleanField(default=False)
    android_platform = models.BooleanField(default=False)
    app_manager = models.ForeignKey(Manager)
    app_sponsor = models.ForeignKey(Sponsor)
    # requestor = models.OneToOneField(User)    # problem saving this
    request_date = models.DateTimeField(auto_now_add=True)
    app_sponsor_agreed = models.BooleanField(default=False)


class Agreement(models.Model):
    app = models.ForeignKey(App)
    agree_time = models.DateTimeField(auto_now_add=True)
    sponsor = models.ForeignKey(Sponsor)


class SponsorForm(ModelForm):
    class Meta:
        model = Sponsor
        fields = '__all__'
        labels = {

        }
        help_texts = {

        }
        error_messages = {

        }


class ManagerForm(ModelForm):
    class Meta:
        model = Manager
        fields = '__all__'
        labels = {

        }
        help_texts = {

        }
        error_messages = {

        }


class AppForm(ModelForm):
    class Meta:
        model = App
        fields = ['name', 'primary_language', 'ios_platform',
                  'android_platform']
        labels = {
            'android_platform':
                'Add to the University of Washington Google Play Store',
            'ios_platform':
                'Add to the University of Washington Apple Store',
        }
        help_texts = {
            'primary_language': '(ENG for English)',
        }
        error_messages = {

        }
