from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
import os
import pandas as pd
from datetime import datetime
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

relatos = []
comentarios = {}

# Simulando planilha Excel com informações de peças
pecas_info = pd.DataFrame([
    {"Catalog": "123", "Description": "Parafuso", "MvAvgPrice": 2.50},
    {"Catalog": "456", "Description": "Arruela", "MvAvgPrice": 1.00},
    {"Catalog": "789", "Description": "Rolamento", "MvAvgPrice": 15.75},
])

@app.route("/")
def index():
    return render_template("index.html", relatos=reversed(relatos), comentarios=comentarios)

@app.route("/relatar", methods=["GET", "POST"])
def relatar():
    if request.method == "POST":
        titulo = request.form.get("titulo")
        executor = request.form.get("executor")
        descricao = request.form.get("descricao")
        area = request.form.get("area")
        subarea = request.form.get("subarea")
        equipamento = request.form.get("equipamento")

        fotos = request.files.getlist("fotos")
        foto_paths = []
        for foto in fotos:
            if foto.filename:
                filename = f"{uuid.uuid4().hex}_{secure_filename(foto.filename)}"
                path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                foto.save(path)
                foto_paths.append(path)

        pecas = []
        total = 0
        for i in range(10):  # até 10 peças por relato
            catalog = request.form.get(f"catalog_{i}")
            desc = request.form.get(f"desc_{i}")
            qtd = request.form.get(f"qtd_{i}")
            if catalog and qtd:
                try:
                    qtd = int(qtd)
                    price_row = pecas_info[pecas_info["Catalog"] == catalog]
                    price = float(price_row["MvAvgPrice"].values[0]) if not price_row.empty else 0
                    custo_total = price * qtd
                    total += custo_total
                    pecas.append({"catalog": catalog, "desc": desc, "qtd": qtd, "custo": custo_total})
                except:
                    continue

        relatos.append({
            "titulo": titulo,
            "executor": executor,
            "descricao": descricao,
            "area": area,
            "subarea": subarea,
            "equipamento": equipamento,
            "fotos": foto_paths,
            "pecas": pecas,
            "custo_total": total,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M")
        })
        return redirect(url_for('index'))

    return render_template("relatar.html")

@app.route("/comentar/<int:relato_id>", methods=["POST"])
def comentar(relato_id):
    nome = request.form.get("nome")
    mensagem = request.form.get("mensagem")
    if relato_id not in comentarios:
        comentarios[relato_id] = []
    comentarios[relato_id].append({"nome": nome, "mensagem": mensagem})
    return redirect(url_for("index"))

@app.route("/exportar")
def exportar():
    dados = []
    for i, r in enumerate(relatos):
        for p in r["pecas"]:
            dados.append({
                "Título": r["titulo"],
                "Executor": r["executor"],
                "Área": r["area"],
                "Subárea": r["subarea"],
                "Equipamento": r["equipamento"],
                "Peça (Catálogo)": p["catalog"],
                "Descrição Peça": p["desc"],
                "Quantidade": p["qtd"],
                "Custo": p["custo"],
                "Data": r["data"]
            })
    df = pd.DataFrame(dados)
    file_path = "relatos_exportados.xlsx"
    df.to_excel(file_path, index=False)
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
