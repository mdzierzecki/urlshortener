from django.test import TestCase
from mainapp.models import Url
from mainapp.forms import ShorteningForm


# python manage.py test --pattern="tests_forms.py"
class FormTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        obj = Url.objects.create(target_url="https://www.evernote.com/")
        obj.save()
        Url.assign_shortcode(obj, "http://127.0.0.1")


class EventFormTestCase(FormTestCase):
    def test_valid_form(self):
        obj = Url.objects.get(pk=1)
        data = {'target_url': "https://www.evernote.com/"}
        form = ShorteningForm(data=data)
        print(form.errors)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data.get('target_url'), obj.target_url)



