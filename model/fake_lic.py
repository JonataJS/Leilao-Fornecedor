import json

class Fake_Lic():
    def __init__(self):
        self.lic = []
        self.start_lic()


    def start_lic(self):
        self.lic =[
        {"bidding":1,"date":"13/09/2017","supplier":"Odebretch","value":550000, "produto": "Monitor"},
        {"bidding":1,"date":"14/09/2017","supplier":"W Koerich","value":450000, "produto": "Armario"},
        {"bidding":2,"date":"14/09/2017","supplier":"Seu Ze","value":20000, "produto": "Mesa"},
        {"bidding":2,"date":"14/09/2017","supplier":"Illuminati","value":19000, "produto": "Cadeira"}]


        # self.lic = {
        #     'id' : 1,
        #     'nome': 'Lic1',
        #     'requerente' : 'Req 1',
        #     'data_inicio': '14/09/17',
        #     'data_fim': '15/09/17',
        #     'produtos': {
        #         1 :{
        #             'produto': 'cadeira',
        #             'quantidade' : 4
        #         },
        #         2: {
        #             'produto': 'mesa',
        #             'quantidade': 1
        #         }
        #     },
        #     'lance_atual': 0
        # }

    def get_json(self):
        return json.dumps(self.lic)
