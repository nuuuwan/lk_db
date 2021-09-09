from utils import www

from lk_db.ents.space.EntPoint import EntPoint
from lk_db.ents.space.EntRegion import EntRegion


class EntProvince(EntRegion):
    @classmethod
    def get_data_list(cls):
        data_list = www.read_tsv(cls.get_remote_data_list_url())
        return list(
            map(
                lambda d: {
                    'id': d['id'],
                    'name': d['name'],
                    'country_id': d['country_id'],
                    'fips': d['fips'],
                    'centroid': EntPoint.norm(d['centroid']),
                    'centroid_altitude': d['centroid_altitude'],
                },
                data_list,
            )
        )
