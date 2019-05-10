import os
import pandas as pd
import numpy as np
import pandas as pd
import pymongo
import json
from flask_pymongo import PyMongo
from flask import Flask, jsonify, render_template

app = Flask(__name__)
MONGO_URL = os.environ.get('MONGO_URI')
if not MONGO_URL:
    MONGO_URL = "mongodb://localhost:27017/gene_db" 

app.config["MONGO_URI"] = MONGO_URL
mongo = PyMongo(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gene_variants")
def plot_data():
    data = mongo.db.gene_variants
    output = []
    for x in data.find():
        output.append({'Class' : x['Class'],'Gene' : x['Gene'], 'Variation':x['Variation']})
    return jsonify(output)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/api/variation", methods=['GET'])
def get_api():
    # return render_template("api.html")
    api = mongo.db.gene_variants

    output = []
    for x in api.find():
        output.append({'Gene' : x['Gene'], 'Variation' : x['Variation']})
    
    return jsonify({'result': output})

@app.route("/api/class", methods=['GET'])
def get_class():
    # return render_template("api.html")
    api = mongo.db.gene_variants

    output = []
    for x in api.find():
        output.append({'Class' : x['Class'], 'Gene' : x['Gene']})
    
    return jsonify({'result': output})

@app.route("/api/geneData", methods=['GET'])
def get_geneData():
    # return render_template("api.html")
    api = mongo.db.geneData

    output = []
    for x in api.find():
        output.append({'Gene Symbol' : x['Gene Symbol'], 'Name' : x['Name'], 'Tumour Types(Somatic)' : x['Tumour Types(Somatic)'],
        'Tissue Type' : x['Tissue Type'], 'Molecular Genetics':x['Molecular Genetics'], 'Role in Cancer': x['Role in Cancer']})
    
    return jsonify({'result': output})

@app.route("/api/geneData/<gene>")
def get_gene(gene):
    results = mongo.db.geneData.find({'Gene Symbol': gene})
    output = []
    for x in results:
        output.append({'Gene Symbol' : x['Gene Symbol'], 'Name' : x['Name'], 'Tumour Types(Somatic)' : x['Tumour Types(Somatic)'],
        'Tissue Type' : x['Tissue Type'], 'Molecular Genetics':x['Molecular Genetics'], 'Role in Cancer': x['Role in Cancer']})
    
    return jsonify({'result': output})
if __name__ == "__main__":
    app.run(debug=True)