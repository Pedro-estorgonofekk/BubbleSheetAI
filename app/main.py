from flask import Flask
from services.generation import Generation
from services.message import HelloWorld
from services.recognition import Recognition

app = Flask(__name__)

@app.route('/', methods=['GET'])
def Mensagem():
    return HelloWorld()

@app.route('/gerar-gabarito', methods=['POST'])
def SheetGeneration():
    return Generation()

@app.route('/corrigir-gabarito', methods=['POST'])
def SheetCorrection():
    return Recognition()

app.run(debug=True, port=3000)