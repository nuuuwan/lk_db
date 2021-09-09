import json
import os

from utils import www


class Ent(object):
    @classmethod
    def get_short_name(cls):
        return cls.__name__.replace('Ent', '').lower()

    @classmethod
    def get_remote_data_list_url(cls):
        ent_short_name = cls.get_short_name()
        return os.path.join(
            'https://raw.githubusercontent.com/nuuuwan/gig-data/master',
            f'{ent_short_name}.tsv',
        )

    @classmethod
    def get_data_list(cls):
        return www.read_tsv(cls.get_remote_data_list_url())

    @classmethod
    def print_first(cls):
        print(json.dumps(cls.get_data_list()[0], indent=2))
