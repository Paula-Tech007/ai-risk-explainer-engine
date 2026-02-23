def calcular_breakdown(features):
    breakdown = {}

    breakdown["abuse_score"] = min(features.get("abuse_score", 0) * 0.4, 40)
    breakdown["malicious_reports"] = min(features.get("malicious_reports", 0) * 2, 30)
    breakdown["geo_risk"] = 20 if features.get("geo_risk") == "high" else 5

    return breakdown