import json

class Fake_transacao():
    def __init__(self):
        pass

    def get_transacao(self):
        trans = {
            'Produtos': {
                'ProdutoA' : 2,
                'ProdutoC' : 3
            },
            'data_inicio': '20/08/2017',
            'data_fim': '22/08/2017',
            'lance_inicial' : 600
        }
        return json.dumps(trans)
