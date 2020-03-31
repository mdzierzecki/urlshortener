from django.apps import apps
import random
import string


def random_string(length=5):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def shortcode_generator(length=5):
    url = apps.get_model('mainapp.Url')  # circular import issue
    shortcode = random_string(length)
    is_unique = False

    while not is_unique:
        shortcode = random_string(length)
        try:
            return url.objects.get(shortcode=shortcode)
            is_unique = False
        except url.DoesNotExist:
            is_unique = True

    return shortcode


