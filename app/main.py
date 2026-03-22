from flask import Flask, request, jsonify
from services.generator import GerarGabarito
from services.message import HelloWorld
from services.recognition import Recognition

app = Flask(__name__)

@app.route('/', methods=['GET'])
def Mensagem():
    return HelloWorld()

@app.route('/gerar-gabarito', methods=['POST'])
def SheetGeneration():
    data = request.get_json()
    
    
    path = GerarGabarito(
        testID=data.get("testID")
    )
    
    return jsonify({"mensagem": "Gabarito gerado!", "path": path}), 201

@app.route('/corrigir-gabarito', methods=['POST'])
def SheetCorrection():
    return Recognition()

app.run(debug=True, port=3000)