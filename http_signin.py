import json

from kivy.network.urlrequest import UrlRequest

class Sign_in:
    def sign_in(self,on_complete,on_error,on_failure):
        url="http://127.0.0.1:8000/sign_up/"

        def donnee_recu(req, result):
            data = json.dumps(result)
            if on_complete:
                on_complete(data)

        def erreur(req, error):

            if on_error:
                on_error(str(error))

        def echec_de_connexion(req, echec):

            if on_failure:
                on_failure("Erreur serveur :" + str(req.resp_status))

        req = UrlRequest(url, on_success=donnee_recu, on_error=erreur, on_failure=echec_de_connexion)  # appel asynchrone