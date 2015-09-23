from django.test import TestCase, Client


class MdotTemplateTest(TestCase):

    def test_http_protocol(self):
        c = Client()
        response = c.get('/')

        self.assertFalse("url('http:" in response.content)

    def test_https_protocol(self):
        c = Client()
        response = c.get('/')

        self.assertFalse("url('https:" in response.content)
