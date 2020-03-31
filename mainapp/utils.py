from django.apps import apps
import random
import string
import re


def random_string(length=5):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def shortcode_generator(length=5):
    url = apps.get_model('mainapp.Url')  # circular import issue
    shortcode = random_string(length)
    is_unique = False

    while not is_unique:
        shortcode = random_string(length)
        try:
            obj = url.objects.get(shortcode=shortcode)
            is_unique = False
        except url.DoesNotExist:
            is_unique = True

    return shortcode


def is_url(path):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(regex, path) is not None
