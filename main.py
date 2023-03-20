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

sg.theme('TealMono')  # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Selecione uma moeda'),sg.Combo(listaMoedas)],
            [sg.Text('Selecione outra moeda'),sg.Combo(listaMoedas)],
            [sg.Button('Ok'), sg.Button('Cancel')],
            [sg.Image(r'pg.png',size=(1000,500))]
            ]
# Create the Window


window = sg.Window('Cotação e Câmbio de Moedas', layout, size=(1000,600), finalize=True)


# Event Loop to process "events" and get the "values" of the inputs

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    if(values[0] and values[1] == ""):
        sg.popup_error('ERRO, VERIFIQUE SE AS MOEDAS FORAM SELECIONADAS')
    elif(values[0]!=values[1]):
        moeda1 = values[0].split('-')
        moeda2 = values[1].split('-')
        moeda1 = moeda1[1].lstrip()
        moeda2 = moeda2[1].lstrip()
        objeto = ConversorDeMoedasUniversal(moeda1,moeda2)
        if(objeto.get_informacoes() != "Error"):
            sg.popup("         Cotação - "+objeto.get_informacoes()['name']+"         \x00\n",
                "Valor de Compra: "+ objeto.get_informacoes()['bid']+"\n",
                  "Valor de Venda: "+ objeto.get_informacoes()['ask']+"\n",
                  "Variação: "+ objeto.get_informacoes()['varBid']+"\n",
                 "Porcetagem Variação: "+ objeto.get_informacoes()["pctChange"]+"%"+"\n",
                 "Máximo: "+objeto.get_informacoes()["high"]+"\n",
                 "Mínimo: " + objeto.get_informacoes()["low"] + "\n",title = objeto.get_informacoes()['name'],
                  )
    else:
        sg.popup_error('ERRO, MOEDAS SELECIONADAS SÃO IGUAIS OU OS CAMPOS ESTÃO VAZIOS')




window.close()
