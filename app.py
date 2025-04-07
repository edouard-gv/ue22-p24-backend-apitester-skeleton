import pathlib as pl

import numpy as np
import pandas as pd

from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

data = pl.Path(__file__).parent.absolute() / "data"

# Charger les données CSV
associations_df = pd.read_csv(data / "associations_etudiantes.csv")
evenements_df = pd.read_csv(data / "evenements_associations.csv")


@app.route("/api/alive", methods=["GET"])
def is_alive():
    return {"message": "Alive"}, 200


@app.route("/api/associations", methods=["GET"])
def associations():
    return associations_df["id"].transpose().to_list()


@app.route("/api/association/<int:id>", methods=["GET"])
def association(id):
    if id in associations_df.id:
        return associations_df[associations_df.id == id].transpose()[0].to_json()
    else:
        return {"error": "Association not found"}, 404


@app.route("/api/evenements", methods=["GET"])
def evenements():
    return evenements_df["id"].transpose().to_list()


@app.route("/api/evenement/<int:id>", methods=["GET"])
def evenement(id):
    if id in evenements_df.id:
        return evenements_df[evenements_df.id == id].transpose()[0].to_json()
    else:
        return {"error": "Event not found"}, 404


@app.route("/api/association/<int:id>/evenements", methods=["GET"])
def association_evenements(id):
    if id in associations_df.id:
        return list(
            evenements_df[evenements_df.association_id == id]
            .transpose()
            .to_dict()
            .values()
        )
    else:
        return {"error": "Association not found"}, 404


@app.route("/api/association/type/<type>", methods=["GET"])
def association_par_type(type):
    return list(
        associations_df[associations_df.type == type].transpose().to_dict().values()
    )


if __name__ == "__main__":
    app.run(debug=False)
