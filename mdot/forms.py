from django.utils.safestring import mark_safe
from django import forms


class ReviewForm(forms.Form):
    campus_audience = forms.CharField(
        widget=forms.widgets.Textarea(),
        label='What UW audiences does your application target?')
    campus_need = forms.CharField(
        widget=forms.widgets.Textarea(),
        label='What broad UW campus need does your application address?')
    sponsor_name = forms.CharField(label='Name:')
    sponsor_netid = forms.CharField(label='UW NetID:')
    sponsor_email = forms.EmailField(label='Email:')
    dev_name = forms.CharField(label='UW NetID:')
    dev_email = forms.EmailField(label='Email:')
    support_name = forms.CharField(label='Name:')
    support_email = forms.EmailField(label='Email:')
    support_contact = forms.CharField(
        widget=forms.widgets.Textarea(),
        label='Other contact information:',
        required=False)
    ats_review = forms.BooleanField(
        required=False,
        label=mark_safe(
            ('Accessibility review with '
             '<a href="http://www.washington.edu/accessibility/" '
             'title="Accessible Technology Services">UW-IT ATS</a>')),
        label_suffix='')
    ux_review = forms.BooleanField(
        required=False,
        label=mark_safe(
            ('Usability review with '
             '<a href="http://depts.washington.edu/ux/consultation/" '
             'title="ACA User Experience Team">ACA UX team</a>')),
        label_suffix='')
    brand_review = forms.BooleanField(
        required=False,
        label=mark_safe(
            ('Consulted <a href="http://www.washington.edu/brand/"> '
             'UW Brand Guidelines</a>')),
        label_suffix='')
    app_documentation = forms.URLField(
        label='URL for app documentation:',
        required=False)
    app_code = forms.CharField(
        widget=forms.widgets.Textarea(),
        label='How can we review the app?')
    anything_else = forms.CharField(
        widget=forms.widgets.Textarea(),
        label='Anything else that we should know?',
        required=False)
