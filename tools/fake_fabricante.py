import json

class Fake_fabricante():
    def __init__(self):
        self.fabricantes  = self.get_fabricantes()



    def get_fabricantes(self):
        return {
            'FabricanteA' : {
                'ProdutoA' : 100,
                'ProdutoB' : 50,
                'ProdutoC' : 130

            },
            'FabricanteB': {
                'ProdutoB': 75,
                'ProdutoA': 80,
                'ProdutoD': 40
            },
            'FabricanteC' : {
                'ProdutoC': 115,
                'ProdutoA' : 110,
                'ProdutoE' : 15
            }
        }

    def get_jfabr(self):
        return json.dumps(self.fabricantes)
