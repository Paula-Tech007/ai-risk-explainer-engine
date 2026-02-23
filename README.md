# 🧠 Motor de Explicabilidade de Risco com IA (XAI para SOC)

Este projeto demonstra a aplicação de Explainable AI (XAI) em um contexto de Security Operations Center (SOC).

Ao invés de apenas gerar um score de risco, o sistema explica **por que** um indicador foi classificado como ameaça, aumentando transparência, auditabilidade e confiança nas decisões automatizadas.

---

## 🚀 Funcionalidades

* Classificação de risco (baixo → crítico)
* Explicações interpretáveis (human-readable)
* Nível de confiança da decisão
* Score breakdown por fator de risco
* Rastreamento de requisições (UUID + timestamp)
* Sistema de logging simples
* API pronta para integração com n8n / SOAR

---

## 🧠 Arquitetura

```
ai-security-explainability-lab/
│
├── app.py                # API principal (Flask)
│
├── engine/
│   ├── explainer.py     # geração de explicações
│   ├── rules.py         # cálculo de score e breakdown
│
├── utils/
│   └── logger.py        # persistência de logs
│
├── requirements.txt
└── README.md
```

---

## 🔄 Fluxo da Aplicação

1. Recebe dados via endpoint `/explicar`
2. Processa as features de risco
3. Calcula classificação e nível de confiança
4. Gera explicações interpretáveis
5. Retorna resposta estruturada
6. Registra log da requisição

---

## 📥 Exemplo de Entrada

```json
{
  "risk_score": 85,
  "features": {
    "abuse_score": 90,
    "malicious_reports": 12,
    "geo_risk": "high"
  }
}
```

---

## 📤 Exemplo de Saída

```json
{
  "request_id": "uuid-exemplo",
  "timestamp": "2026-02-23T12:00:00",
  "classificacao": "crítico",
  "risk_score": 85,
  "confianca": "alta",
  "explicacao": [
    "Score alto de abuso contribuiu significativamente para o risco",
    "Múltiplos reports maliciosos aumentaram a confiança da ameaça",
    "Origem geográfica de alto risco impactou a pontuação"
  ],
  "score_breakdown": {
    "abuse_score": 40,
    "malicious_reports": 24,
    "geo_risk": 20
  },
  "impacto": "Este indicador apresenta risco com base em sinais correlacionados de ameaça"
}
```

---

## ⚙️ Como Executar

```bash
pip install -r requirements.txt
python app.py
```

---

## 🔌 Endpoint

**POST** `/explicar`

---

## 🧪 Teste rápido (curl)

```bash
curl -X POST http://127.0.0.1:5000/explicar \
-H "Content-Type: application/json" \
-d '{
  "risk_score": 85,
  "features": {
    "abuse_score": 90,
    "malicious_reports": 12,
    "geo_risk": "high"
  }
}'
```

---

## 🧠 Casos de Uso

* Automação de SOC
* Explainable AI (XAI) aplicada à segurança
* Auditoria de decisões automatizadas
* Enriquecimento de threat intelligence
* Governança de IA

---

## 💡 Diferencial

Este projeto vai além da detecção de ameaças:

* Explica decisões automatizadas de forma clara
* Aumenta a confiança em sistemas baseados em IA
* Facilita auditoria e compliance
* Reduz o efeito "caixa-preta" em segurança cibernética

---

## 🛡️ Por que isso é importante?

Sistemas modernos de segurança baseados em IA não podem ser "caixa-preta".

Este projeto demonstra como tornar decisões:

* transparentes
* explicáveis
* auditáveis

Esses são requisitos fundamentais em ambientes corporativos e regulados.

---

## 🔮 Próximos Passos

* Integração com LLM para explicações mais avançadas
* Integração direta com n8n
* Dashboard de visualização de decisões
* Persistência em banco de dados (ex: PostgreSQL)

---

## 👩‍💻 Autora

**Paula Sabino**
🔗 GitHub: https://github.com/Paula-Tech007
