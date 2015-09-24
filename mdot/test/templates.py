from django.test import TestCase, Client
import mdot_rest.models as resource_models
import datetime
from mock import patch


class MdotTemplateTest(TestCase):

    def setUp(self):
        self.default_date = datetime.datetime(1945, 11, 03, 12, 03, 34)
        with patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = self.default_date

            self.resource1 = resource_models.UWResource.objects.create(
                title='ITConnect',
                feature_desc='This is a test.',
                image=u'http://localhost:8000/media/uploads/httpthis.png',
                featured=True,
                accessible=True,
                responsive_web=True,
                campus_seattle=True,
                campus_tacoma=False,
                campus_bothell=False,
                published=True)

            self.resource2 = resource_models.UWResource.objects.create(
                title='https',
                feature_desc='This is a test.',
                image=u'http://localhost:8000/media/uploads/httpsthis.png',
                featured=True,
                accessible=True,
                responsive_web=True,
                campus_seattle=True,
                campus_tacoma=False,
                campus_bothell=False,
                published=True)

            self.intended_audience1 = \
                resource_models.IntendedAudience.objects.create(
                    audience='Students')

            self.intended_audience1.save()

            self.intended_audience1.resource.add(self.resource1)
            self.intended_audience1.resource.add(self.resource2)

            self.resource_link1 = resource_models.ResourceLink.objects.create(
                link_type='IOS',
                resource=self.resource1,
                url='uw.edu/itconnect')
            self.resource_link1 = resource_models.ResourceLink.objects.create(
                link_type='IOS',
                resource=self.resource2,
                url='uw.edu/itconnect')

            self.resource1.save()
            self.resource2.save()

            self.intended_audience1.save()

            self.resource_link1.save()

            self.client = Client()

    def test_http_protocol(self):
        """
        Ensure the http is removed from the beginning of the url.
        """
        response = self.client.get('/')

        self.assertFalse("url('http:" in response.content)

    def test_https_protocol(self):
        """
        Ensure the https is removed from the beginning of the url.
        """
        response = self.client.get('/')

        self.assertFalse("url('https:" in response.content)

    def test_http_in_middle(self):
        """
        Ensure the http is not removed from the middle of the url.
        """
        response = self.client.get('/api/v1/uwresources/?title=ITConnect')

        self.assertFalse("url('http:" in response.content)
        self.assertTrue("/media/uploads/httpthis.png" in response.content)

    def test_https_in_middle(self):
        """
        Ensure the https is not removed from the middle of the url.
        """
        response = self.client.get('/api/v1/uwresources/?title=https')

        self.assertFalse("url('https:" in response.content)
        self.assertTrue("/media/uploads/httpsthis.png" in response.content)
