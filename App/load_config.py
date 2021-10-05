import json

with open("./config.json", "r", encoding="utf-8") as file:
    data = json.load(file)

    TOKEN = data.get("token")
    DATABASE_PATH = data.get("database_path")

    RBC_LINK = data.get("links")["rbc"]
    KREMLIN_LINK = data.get("links")["kremlin"]
    LENTA_LINK = data.get("links")["lenta"]

    START_TEXT = data.get("message_texts")["start"]
    HELP_TEXT = data.get("message_texts")["help"]

    ON_RBC_TEXT = data.get("message_texts")["notify_rbc_on"]
    OFF_RBC_TEXT = data.get("message_texts")["notify_rbc_off"]

    ON_KREMLIN_TEXT = data.get("message_texts")["notify_kremlin_on"]
    OFF_KREMLIN_TEXT = data.get("message_texts")["notify_kremlin_off"]

    ON_LENTA_TEXT = data.get("message_texts")["notify_lenta_on"]
    OFF_LENTA_TEXT = data.get("message_texts")["notify_lenta_off"]
