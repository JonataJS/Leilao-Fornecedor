import json

class Fake_Lic():
    def __init__(self):
        self.lic = []
        self.start_lic()


    def start_lic(self):
        self.lic = {
            'id' : 1,
            'nome': 'Lic1',
            'requerente' : 'Req 1',
            'data_inicio': '14/09/17',
            'data_fim': '15/09/17',
            'produtos': {
                1 :{
                    'produto': 'cadeira',
                    'quantidade' : 4
                },
                2: {
                    'produto': 'mesa',
                    'quantidade': 1
                }
            },
            'lance_atual': 0
        }

    def get_json(self):
        return json.dumps(self.lic)
