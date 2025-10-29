from flask import Flask, request
from flask_cors import CORS
import requests
import Naive
import Mlp
import Svm
import Sgd

app = Flask(__name__)

CORS(app)
CORS(app, resources={"/*": {"origins": "localhost:5173/"}})

@app.route("/", methods = ["get"])
def home():
    return "ROTA HOME, vá para /svm, /naive, /mlp, /sgd"

@app.route("/mlp", methods = ["get"])
def mlp():
    filtro = request.args.get("filtro", default=1, type=int)
    fold = request.args.get("fold", default=0, type=int)
    quant = 100
    request_positivos = requests.get(
        "https://store.steampowered.com/appreviews/381210?json=1",
        params={"language":"brazilian",
                "review_type":"positive",
                "num_per_page":quant,
                "day_range":"365",
                "filter_offtopic_activity":filtro})
    
    request_negativos = requests.get(
        "https://store.steampowered.com/appreviews/381210?json=1",
        params={"language":"brazilian",
                "review_type":"negative",
                "num_per_page":quant,
                "day_range":"365",
                "filter_offtopic_activity":filtro})
    
    resposta = Mlp.organizar_dataset(
        request_positivos.json().get("reviews"),
        request_negativos.json().get("reviews"), 
        quant, fold)
    
    return resposta

@app.route("/naive", methods = ["get"])
def naive():
    filtro = request.args.get("filtro", default=1, type=int)
    fold = request.args.get("fold", default=0, type=int)
    quant = 100
    request_positivos = requests.get(
        "https://store.steampowered.com/appreviews/381210?json=1",
        params={"language":"brazilian",
                "review_type":"positive",
                "num_per_page":quant,
                "day_range":"365",
                "filter_offtopic_activity":filtro})
    
    request_negativos = requests.get(
        "https://store.steampowered.com/appreviews/381210?json=1",
        params={"language":"brazilian",
                "review_type":"negative",
                "num_per_page":quant,
                "day_range":"365",
                "filter_offtopic_activity":filtro})
    
    resposta = Naive.organizar_dataset(
        request_positivos.json().get("reviews"),
        request_negativos.json().get("reviews"), 
        quant, fold)
    
    return resposta

@app.route("/svm", methods = ["get"])
def svm():
    filtro = request.args.get("filtro", default=1, type=int)
    fold = request.args.get("fold", default=0, type=int)
    quant = 100
    request_positivos = requests.get(
        "https://store.steampowered.com/appreviews/381210?json=1",
        params={"language":"brazilian",
                "review_type":"positive",
                "num_per_page":quant,
                "day_range":"365",
                "filter_offtopic_activity":filtro})
    
    request_negativos = requests.get(
        "https://store.steampowered.com/appreviews/381210?json=1",
        params={"language":"brazilian",
                "review_type":"negative",
                "num_per_page":quant,
                "day_range":"365",
                "filter_offtopic_activity":filtro})
    
    resposta = Svm.organizar_dataset(
        request_positivos.json().get("reviews"),
        request_negativos.json().get("reviews"), 
        quant, fold)
    
    return resposta

@app.route("/sgd", methods = ["get"])
def sgd():
    filtro = request.args.get("filtro", default=1, type=int)
    fold = request.args.get("fold", default=0, type=int)
    quant = 100
    request_positivos = requests.get(
        "https://store.steampowered.com/appreviews/381210?json=1",
        params={"language":"brazilian",
                "review_type":"positive",
                "num_per_page":quant,
                "day_range":"365",
                "filter_offtopic_activity":filtro})
    
    request_negativos = requests.get(
        "https://store.steampowered.com/appreviews/381210?json=1",
        params={"language":"brazilian",
                "review_type":"negative",
                "num_per_page":quant,
                "day_range":"365",
                "filter_offtopic_activity":filtro})
    
    resposta = Sgd.organizar_dataset(
        request_positivos.json().get("reviews"),
        request_negativos.json().get("reviews"), 
        quant, fold)
    
    return resposta



if __name__ == "__main__":
    app.run(debug=True)

