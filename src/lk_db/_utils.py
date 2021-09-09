"""Utils."""

import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('lk_db')


def to_camel(s):
    return s.replace('_', ' ').title().replace(' ', '')
