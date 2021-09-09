from lk_db.ents.time.EntMoment import EntMoment


class EntCensus(EntMoment):
    @classmethod
    def get_data_list(cls):
        return [
            {'id': 'census_2012', 'time': '2012'},
        ]


if __name__ == '__main__':
    EntCensus.print_all()
