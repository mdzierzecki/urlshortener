from django.test import TestCase
from mainapp.models import Url


# python manage.py test --pattern="tests_models.py"
class ModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        obj = Url.objects.create(target_url="https://www.evernote.com/")
        obj.save()
        Url.assign_shortcode(obj, "http://127.0.0.1")


class EventModelTestCase(ModelTestCase):

    def test_model_all(self):
        obj = Url.objects.get(pk=1)
        self.assertEqual(obj.target_url, "https://www.evernote.com/")
        self.assertEqual(obj.full_url, "{}/{}".format("http://127.0.0.1", obj.shortcode))
