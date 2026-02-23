import json
from datetime import datetime
import os

ARQUIVO_LOG = "logs.json"


def registrar_log(data):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "dados": data
    }

    if not os.path.exists(ARQUIVO_LOG):
        with open(ARQUIVO_LOG, "w") as f:
            json.dump([log_entry], f, indent=4)
    else:
        with open(ARQUIVO_LOG, "r+") as f:
            logs = json.load(f)
            logs.append(log_entry)
            f.seek(0)
            json.dump(logs, f, indent=4)