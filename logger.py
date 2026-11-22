from datetime import datetime

LOG_FILE = "history.log"


def log(input, output):
  with open(LOG_FILE, "a", encoding="utf-8") as f:
    f.write(f"'{datetime.now()}' Запрос: {input} >>> Ответ: {output}\n")
