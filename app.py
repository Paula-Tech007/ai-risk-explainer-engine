from flask import Flask, request, jsonify
from engine.explainer import gerar_explicacao, nivel_confianca, classificar
from engine.rules import calcular_breakdown
from utils.logger import registrar_log
import uuid
from datetime import datetime

app = Flask(__name__)

@app.route("/explicar", methods=["POST"])
def explicar():
    data = request.json

    request_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()

    features = data.get("features", {})
    risk_score = data.get("risk_score", 0)

    explicacao = gerar_explicacao(features)
    confianca = nivel_confianca(risk_score)
    classificacao = classificar(risk_score)
    breakdown = calcular_breakdown(features)

    response = {
        "request_id": request_id,
        "timestamp": timestamp,
        "classificacao": classificacao,
        "risk_score": risk_score,
        "confianca": confianca,
        "explicacao": explicacao,
        "score_breakdown": breakdown,
        "impacto": "Este indicador apresenta risco com base em sinais correlacionados de ameaça"
    }

    registrar_log(response)

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)