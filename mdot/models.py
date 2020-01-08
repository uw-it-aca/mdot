from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.

class Sponsor(models.Model):
    name = models.CharField(max_length = 50)
    netid = models.CharField(max_length = 8)
    title = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 30)
    department = models.CharField(max_length = 30)
    unit = models.CharField(max_length = 30)


class Manager(models.Model):
    name = models.CharField(max_length = 50)
    netid = models.CharField(max_length = 8)


class App(models.Model):
    # define platforms
    name = models.CharField(max_length = 50)
    primary_language = models.CharField(max_length = 20)  # are we using abbreviations?
    request_date = models.DateTimeField(auto_now_add = True)
    app_manager = models.ForeignKey(Manager)
    app_sponsor = models.ForeignKey(Sponsor)
    app_sponser_agreed_date = models.DateTimeField(auto_now = True)
    app_sponser_agreed = models.BooleanField(default = False)


class Agreement(models.Model):
    app = models.ForeignKey(App)
    agree_time = models.DateTimeField(auto_now_add = True)
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
        fields = ['name', 'primary_language']
        labels = {
        }
        help_texts = {

        }
        error_messages = {

        }