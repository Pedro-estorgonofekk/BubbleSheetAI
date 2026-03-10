from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def mensagem():
    print("relou uordi")
    return("relou uordi")

app.run(debug=True, port=3000)