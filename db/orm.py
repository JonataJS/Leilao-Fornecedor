from db.pee import *
import json
from playhouse.shortcuts import model_to_dict, dict_to_model
__all__=["Orm", "model_to_dict"]

class Orm():

    def __init__(self):
        pass

    def crt_tables(self):
        db.create_tables([Fornecedor])

    def crt_forn(self,params=None):
        if not params:
            forn = Fornecedor.create()
            return forn

        t = dict_to_model(Fornecedor, params, ignore_unknown=True)
        t.save()
        return t


    def get_forn(self,x):
        try:
            return Fornecedor.get(id=x)
        except:
            return None

    def del_forn(self):
        t = Fornecedor.delete()
        t.execute()

    def get_forns(self):
        dic = []
        x = 1
        while self.get_forn(x) != None:
            dic.append(model_to_dict(Fornecedor.get(id=x)))
            x+=1
        return dic

    def get_json_forns(self):
        dic = []
        x = 1
        while self.get_forn(x) != None:
            atual = model_to_dict(Fornecedor.get(id=x))
            del atual['passwd']
            dic.append(atual)
            x+=1

        return json.dumps(dic)
