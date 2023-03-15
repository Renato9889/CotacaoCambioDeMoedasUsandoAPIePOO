from conversor_de_moedas import ConversorDeMoedasUniversal
import PySimpleGUI as sg
import xml.etree.ElementTree as ET

tree = ET.parse('moedas.xml')
root = tree.getroot()
listaMoedas = []
listaTags = []

for desc in root:
    listaMoedas.append(desc.text+ " - "+desc.tag)

listaMoedas.sort()

sg.theme('GreenMono')  # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Selecione uma moeda'),sg.Combo(listaMoedas)],
            [sg.Text('Selecione outra moeda'),sg.Combo(listaMoedas)],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
# Create the Window


window = sg.Window('Cotação de Moeda', layout, size=(1000,500), finalize=True)


# Event Loop to process "events" and get the "values" of the inputs

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    moeda1 = values[0].split('-')
    moeda2 = values[1].split('-')
    moeda1 = moeda1[1].lstrip()
    moeda2 = moeda2[1].lstrip()

    if(moeda2!=moeda1):
        objeto = ConversorDeMoedasUniversal(moeda1,moeda2)
        sg.popup("Valor de Comprar: "+ objeto.get_informacoes()['bid']+"\n",
                  "Valor de Venda: "+ objeto.get_informacoes()['ask']+"\n",
                  "Variação: "+ objeto.get_informacoes()['varBid']+"\n",
                 "Porcetagem Variação: "+ objeto.get_informacoes()["pctChange"]+"%"+"\n",
                 "Máximo: "+objeto.get_informacoes()["high"]+"\n",
                 "Mínimo: " + objeto.get_informacoes()["low"] + "\n",title = "Cotação",
                  )
    else:
        sg.popup_error('ERRO, MOEDAS SELECIONADAS SÃO IGUAIS')




window.close()