import json

from kivy.network.urlrequest import UrlRequest


class Httpclient:
    def get_pizzas(self,on_complete,on_error,on_failure):
        url="http://127.0.0.1:8000/menu/api/getpizzas"


        def donnee_recu(req,result):
            data=json.loads(result)
            pizza_dict=[]
            for i in data:
                pizza_dict.append(i['fields'])

            if on_complete:
                on_complete(pizza_dict)
        def erreur(req, error):

            if on_error:
                on_error(str(error))
        def echec_de_connexion(req, echec):

            if on_failure:
                on_failure("Erreur serveur :"+str(req.resp_status))
        req=UrlRequest(url,on_success=donnee_recu,on_error=erreur,on_failure=echec_de_connexion) #appel asynchrone

