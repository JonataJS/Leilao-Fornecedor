import json

class Fake_Fab():
    def __init__(self):
        self.fab = []
        self.start_fab()


    def start_fab(self):
        self.fab = [ {"id": "1", "nome": "Fabricante1",
	                   "produtos": [{
                                "nome": "Cadeira",
                                "custo": 40},
                             {
                                "nome": "Mesa",
                                "custo": 80}
                            ]},
                    {"id": "2", "nome": "Fabricante2",
                    "produtos": [{
                                "nome": "Armario",
                                "custo": 150 },
                                {
                                "nome": "Monitor",
                                "custo": 300}
                                ]}]


    def get_json(self):
        return json.dumps(self.fab)
