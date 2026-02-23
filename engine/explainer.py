def gerar_explicacao(features):
    explicacoes = []

    if features.get("abuse_score", 0) > 80:
        explicacoes.append("Score alto de abuso contribuiu significativamente para o risco")

    if features.get("malicious_reports", 0) > 10:
        explicacoes.append("Múltiplos reports maliciosos aumentaram a confiança da ameaça")

    if features.get("geo_risk") == "high":
        explicacoes.append("Origem geográfica de alto risco impactou a pontuação")

    if not explicacoes:
        explicacoes.append("Nenhum fator de risco significativo detectado")

    return explicacoes


def nivel_confianca(score):
    if score > 80:
        return "alta"
    elif score > 50:
        return "média"
    return "baixa"


def classificar(score):
    if score > 80:
        return "crítico"
    elif score > 60:
        return "alto"
    elif score > 30:
        return "médio"
    return "baixo"