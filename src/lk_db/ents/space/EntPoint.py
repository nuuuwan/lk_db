import json

from lk_db.ents.space.EntSpace import EntSpace


class EntPoint(EntSpace):
    @staticmethod
    def norm(lat_lng_str):
        [lat, lng] = json.loads(lat_lng_str)
        return f'{lat:.6f}N,{lng:.6f}E'
