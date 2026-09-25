import json
import deal
# Сохраняет transactions в deals.json
def save_data():
    with open("deals.json", "w", ) as f:
        json.dump(deal.transactions, f, ensure_ascii=False)

# Загружает transactions из deals.json
def load_data():
    try:
        with open("deals.json", "r") as f:
            deal.transactions = json.load(f)
    except FileNotFoundError:
        print("Файла нет")