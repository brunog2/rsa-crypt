import os
import sys
sys.path.append('modules')

import ast
from flask import Flask, request, jsonify

from generate1 import Gen
from crypt1 import Crypt
from decrypt1 import Decrypt

app = Flask(__name__)
path = '../public'
isExist = os.path.exists(path)

def createFile(fileName, content):
    path = '../public'
    isExist = os.path.exists(path)
    if not isExist:    
        os.makedirs(path)

    filePath = path+"/"+fileName+".txt"
    arquivo = open(filePath, "w+")
    arquivo.write(content)
    arquivo.close()

def openFile(fileName):
        filePath = path+"/"+fileName+".txt"
        arquivo = open(filePath, "r")
        fileContent = arquivo.read()
        arquivo.close()
        return fileContent

@app.after_request
def set_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    return response

@app.route("/genKey", methods=["POST"])
def genKey():    
    print("quero gerar")
    p = int(request.json["p"])
    q = int(request.json["q"])
    
    e = None
    print(p)
    
    if "e" in request.json:
        e = int(request.json["e"])

    genKey = Gen(p, q, e).gen()
    print("genkey", genKey)
    if "message" not in genKey:
        createFile("key", "{{'n': {}, 'e': {}}}".format(genKey["n"], genKey["e"]))

    return jsonify(genKey)
    
    
@app.route("/crypt", methods=["POST"])
def crypt():   
    text = request.json["text"]
    n = int(request.json["n"])
    e = int(request.json["e"])

    encryptedText = Crypt(text, n, e).crypt()
    
    if "message" not in encryptedText:
        createFile("encrypted-text", encryptedText["encryptedText"])

    return jsonify(encryptedText)


@app.route("/getFile", methods=["GET"])
def getKey():
    fileName = request.args.get('file')   
    fileContent = openFile(fileName)
    return jsonify(ast.literal_eval(fileContent))
        

@app.route("/decrypt", methods=["POST"])
def decrypt():
    p = int(request.json["p"])
    q = int(request.json["q"])
    e = int(request.json["e"])
    text = request.json["text"].split()

    decryptedText = Decrypt(text, p, q, e).decrypt()

    if "message" not in decryptedText:
        createFile("decrypted-text", decryptedText["decryptedText"])

    return jsonify(decryptedText)