from kivy.app import App
from kivy.lang import Builder
from kivy.properties import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import CoverBehavior

from http_client import Httpclient
from models import Pizza


class Pizzawidget(BoxLayout):
    nom=StringProperty()
    ingredient=StringProperty()
    prix=NumericProperty()
    vegetarienne=BooleanProperty()


class Main(FloatLayout):
    recycleview=ObjectProperty(None)
    erreur=StringProperty("")
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        """self.pizzas=[
            Pizza("4 fromages", "Chèvre,emmental,brie,conte", 9.5, True),
            Pizza("Chorizo", "tomate,chorizo,brie,conte", 9.5, False),
            Pizza("Calzone", "Chèvre,emmental,brie,conte", 9.5, False),
            Pizza("4 fromages", "Chèvre,emmental,brie,conte", 9.5, False)
        ]"""
        Httpclient().get_pizzas(self.donnee_du_serveur,self.error_serveur,self.echec_serveur)
    """def on_parent(self,widget,parent):
        self.recycleview.data=[pizza.get_dictionnaire() for pizza in self.pizzas]"""
    def donnee_du_serveur(self,pizzas_dict):
        self.recycleview.data=pizzas_dict
    def error_serveur(self,error):
        self.erreur=error
    def echec_serveur(self,echec):
        self.erreur=echec


class PizzaApp(App):
    pass
PizzaApp().run()
