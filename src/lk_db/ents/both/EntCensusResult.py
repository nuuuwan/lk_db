import os

from utils import dt, filex, timex, www

from lk_db import _utils
from lk_db._utils import log
from lk_db.ents.both.EntRegionSnap import EntRegionSnap


class EntCensusResult(EntRegionSnap):
    @staticmethod
    def get_census_metadata():
        metadata_url = os.path.join(
            'https://raw.githubusercontent.com/nuuuwan/gig-data/master/census',
            'meta.json',
        )
        return www.read_json(metadata_url)

    @staticmethod
    def build_sub_classes():
        metadata = EntCensusResult.get_census_metadata()
        for metadatum in metadata.values():
            table_id = metadatum['table_id']
            class_name = 'Ent' + _utils.snake_to_camel(table_id)
            timex.get_unixtime()
            class_content = f'''# Auto Generated - DO NOT EDIT!

from lk_db.ents.both.EntCensusResult import EntCensusResult


class {class_name}(EntCensusResult):

'''
            class_file = f'src/lk_db/ents/both/census/{class_name}.py'
            filex.write(class_file, class_content)
            log.info(f'Wrote {class_file}')

    @classmethod
    def get_table_id(cls):
        return _utils.camel_to_snake(cls.__name__.replace('Ent', ''))

    @classmethod
    def get_data_list(cls):
        table_id = cls.get_table_id()
        remote_url = os.path.join(
            'https://raw.githubusercontent.com',
            'nuuuwan/gig-data/master/census',
            f'data.{table_id}.tsv',
        )
        data_list = www.read_tsv(remote_url)
        return data_list


if __name__ == '__main__':
    EntCensusResult.build_sub_classes()
