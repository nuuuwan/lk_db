import os

from utils import filex, timex, www

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
            class_name = 'Ent' + table_id.replace('_', ' ').title()
            timex.get_unixtime()
            class_content = '''# Auto Generated {ut}
            '''
            class_file = f'src/lk_db/ents/both/{class_name}'
            filex.write(class_file, class_content)
            log.info(f'Wrote {class_file}')


if __name__ == '__main__':
    EntCensusResult.build_sub_classes()