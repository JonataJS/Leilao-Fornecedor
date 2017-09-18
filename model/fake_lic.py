import json

class Fake_Lic():
    def __init__(self):
        self.lic = []
        self.start_lic()


    def start_lic(self):
        self.lic =[
        {"id":1,"name":"Material para restauração da ponte","value": 5000 ,"applicant":"Prefeitura de Florianópolis","status":1,"start_date":"12/09/2017","end_date":"10/01/2018","products":[{"product_name":"Cimento (1kg)","product_id":"59bd6da9b4e2250012a99627","quantity":20},{"product_name":"Cadeira","product_id":"59bc25fd871a1a00127e86b9","quantity":1000}]},
        {"id":2,"name":"Papel para o banheiro do CTC", "value": 2000, "applicant":"Universidade Federal de Santa Catarina","status":1,"start_date":"17/09/2017","end_date":"22/02/2018","products":[{"product_name":"Papel Higiênico (6 unidades)","product_id":"59bed804c5c22800120f3e2c","quantity":200}]}
        ]


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
