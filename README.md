<h1 align="center"> Cotação e Cambio de Moedas Usando Python, API, Interface e POO</h1>

![Imagem da Tela](https://user-images.githubusercontent.com/38532053/225432040-068c9129-3066-4f9a-b04d-61322f84f2fd.png)

<p align="justify">Este repositório disponibiliza um projeto feito por mim que teve como finalidade aplicar conhecimentos de python, API, inteface grafica e programação orietada a objetos.
A aplicação é uma ferramenta que faz a cotação e cambio entre moedas do mundo todo, ela exibe as informações de cotação, 
valor de compra, valor de venda, variação, porcentagem de variação, máximo e mínimo. </p>
<p align="justify">O projeto foi desenvolvido em python, onde se ulilizou as bibliotecas, <a href="https://www.pysimplegui.org/en/latest/">PySimpleGUI</a>
para a interfacce gráfica, <a href="https://docs.python.org/3/library/xml.html">XML Processing Modules</a> para trabalhar com XML, e a
 <a href="https://pypi.org/project/requests/">Requests</a>, que e propria do python, para lidar com a API.</P>
 <p align="justify">Foi usada a <a href="https://docs.awesomeapi.com.br/api-de-moedas">API de Cotações</a> da AwesomeAPI, uma api funcional, simples e acessível.
 Essa API traz cotações em tempo real com mais de 150 moedas, é possivel com ela fazer converções e exibir informações e períodos de cotação</p> 
 <p align="justify">Optei por usar orientação a objetos, assim criei uma classe que recebe as informações da API e do XML, a partir da interface o usuario é capaz de
 selecionar as moedas e assim se instancia um objeto de cotação, logo com objeto, é exibido as informações na interface para o usuario poder vizualizar. A abaixo é mostrado
 passo a passo como funciona a aplicação.</p>
 <h2>Passo 1 - Selecione uma moeda</h2>
<img src = "https://user-images.githubusercontent.com/38532053/225451248-e7325fe3-32f8-4011-8143-57325fe4b2e6.png">
<h2>Passo 2 - Selecione outra moeda</h2>
<img src = "https://user-images.githubusercontent.com/38532053/225451340-0e6ab073-01e1-45b4-92cd-1a076965ea6f.png">
<h2>Passo 3 - Confirme em OK para ver a cotação das moedas</h2>
<img src = "https://user-images.githubusercontent.com/38532053/225451445-c0618e6c-ee4f-4309-a38a-48cb4e131ace.png">
<h2>✉Respostas da aplicação</h2>
<p>Caso não exista as informações de cotação das moedas é exibido um alerta</p>
<img src = "https://user-images.githubusercontent.com/38532053/225451507-2d7d7958-018f-486b-8471-313b4d64fc99.png">
<p>Caso não seja selecionado as moedas é alertado que os campos estão vazios</p>
<img src = "https://user-images.githubusercontent.com/38532053/225453382-78f503bd-57d9-436a-81ba-cb9ee1412dcc.png">
<p>Caso as moedas sejam iguais tambem é exibido uma tela de alerta</p>
<img src = "https://user-images.githubusercontent.com/38532053/225453377-3696f3e0-9b64-4cf3-9cfc-73ec4c811f61.png">

## ✔️ Técnicas e tecnologias utilizadas
- ``Python3``
- ``PyCharm``
- ``Paradigma de orientação a objetos``
- ``API``
- ``Interface Gráfica``
