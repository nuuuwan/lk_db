"""Utils."""
import re
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('lk_db')


def snake_to_camel(s):
    return s.replace('_', ' ').title().replace(' ', '')

def camel_to_snake(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
