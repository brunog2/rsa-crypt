import os
import sys
sys.path.append('modules')

from flask import Flask, request, jsonify

from generate1 import Gen
from crypt1 import Crypt
from decrypt1 import Decrypt

app = Flask(__name__)

def createFile(fileName, content):
    path = '../public'
    isExist = os.path.exists(path)

    if not isExist:    
        os.makedirs(path)

    filePath = path+"/"+fileName+".txt"
    arquivo = open(filePath, "w+")
    arquivo.write(content)
    arquivo.close()

@app.after_request
def set_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    return response

@app.route("/genKey", methods=["POST"])
def genKey():
    print("quero gerar")
    p = request.json["p"]
    q = request.json["q"]
    
    e = None
    print(p)
    
    if "e" in request.json:
        e = request.json["e"]
    
    genKey = Gen(p, q, e).gen()

    if "message" not in genKey:
        createFile("key", "n: {}\ne: {}".format(genKey["n"], genKey["e"]))

    return jsonify(genKey)

    
@app.route("/crypt", methods=["POST"])
def crypt():
    print("cryptar")
    text = request.json["text"]
    n = request.json["n"]
    e = request.json["e"]

    print("n", n, e)

    encryptedText = Crypt(text, n, e).crypt()
    
    if "message" not in encryptedText:
        createFile("encrypted-text", encryptedText["encryptedText"])

    return jsonify(encryptedText)


@app.route("/decrypt", methods=["POST"])
def decrypt():
    p = request.json["p"]
    q = request.json["q"]
    e = request.json["e"]
    text = request.json["text"].split()

    decryptedText = Decrypt(text, p, q, e).decrypt()

    if "message" not in decryptedText:
        createFile("decrypted-text", decryptedText["decryptedText"])

    return jsonify(decryptedText)