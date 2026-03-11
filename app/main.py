from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def mensagem():
    print("relou uordi")
    return("relou uordi")

@app.route('/gerar-gabarito', methods=['POST'])
def mensagem():
    print("Geração de gabarito")
    return("Geração de gabarito")

@app.route('/corrigir-gabarito', methods=['POST'])
def mensagem():
    print("Correção de gabarito")
    return("Correção de gabarito")

app.run(debug=True, port=3000)