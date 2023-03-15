import re
import requests
from xml.dom import minidom
import xml.etree.ElementTree as ET
import PySimpleGUI as sg
class ConversorDeMoedasUniversal():
    def __init__(self,moeda1,moeda2):
        if self._moeda_e_valida(moeda1) & self._moeda_e_valida(moeda2):
            uniao = str(moeda1+"-"+moeda2)
            self.cotacaodasmoedas = self._cotacao(uniao)
    def _moeda_e_valida(self,moeda):
        with open("moedas.xml",'r',encoding='utf-8') as f:
            xml = minidom.parse(f)
            ExisteMoeda = xml.getElementsByTagName(moeda)
            if(len(ExisteMoeda)!=0):
                return True
            else:
                return False
    def _verificar(self,tag):
        tree = ET.parse('conversoes.xml')
        root = tree.getroot()
        listaTags = []
        for desc in root:
            listaTags.append(desc.tag)
        if tag in listaTags:
            return True
        else:
            return False
    def _cotacao(self,moeda):
        url = "https://economia.awesomeapi.com.br/last/{}".format(moeda)
        req = requests.get(url)
        dados = req.json()
        dadoserror = {'zero':0}
        if(self._verificar(moeda)==True):
            moeda = re.sub("-", "", moeda)
            return dados[moeda]
        else:
            return sg.popup_error('NÃO FOI POSSIVEL FAZER A COTAÇÃO DAS MOEDAS!!!')


    #def __str__(self):
   #     return self.format_moeda()

    #def _format_moeda(self):
    #    return "{}".format(self._cotacaodasmoedas["name"])

    def get_informacoes(self):
        return self.cotacaodasmoedas

    def coversao(self):
        return self.cotacaodasmoedas["bid"]