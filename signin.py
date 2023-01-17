from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from http_signin import Sign_in

Builder.load_file("signin.kv")

class Signin(FloatLayout):
    """def __init__(self,**kwargs):
        super().__init__(**kwargs)

        Sign_in.sign_in(self.donnee_du_serveur,self.error_serveur,self.echec_serveur)

    def donnee_du_serveur(self, pizzas_dict):
        pizzas_dict=self.valeur
        return pizzas_dict"""
    pass

    def error_serveur(self, error):
        self.erreur = error

    def echec_serveur(self, echec):
        self.erreur = echec

    email = StringProperty("email@gmail.com")
    password = StringProperty("password")
    def valeur(self,widget1,widget2):
        self.email=widget1.value
        self.password=widget2.value
        dict={"email":self.email,"password":self.password}
        return dict