import Save_Load


transactions = []


def deal_get():
    date_deal = input("Напиши дату сделки: ")
    coin_name = input("Напиши название актива: ").upper()
    while True:
        print("Ваша сделка \n[1].🟢Прибыльная \n[2].🔴Убыточная")
        profit_lesion = input("Выбери ответ: ")
        if profit_lesion == "1":
            while True:
                try:
                    pro_les = float(input("🟢 Напиши сколько составила ваша прибыль: "))
                    plus_minus = "+"
                    break
                except ValueError:
                    print("❌ Введите цифры")
            break
        elif profit_lesion == "2":
            while True:
                try:
                    pro_les = float(input("🔴 Напиши сколько составил ваш убыток: "))
                    plus_minus = "-"
                    break
                except ValueError:
                    print("❌ Введите цифры")
            break
        else:
            print("Такого номера нет в меню ❌")
    comment = input("Напишите ваш комментарий по сделки: ").capitalize()
    print("✅ Вы добавили сделку:")
    print(f"""
        {date_deal}
        COIN: {coin_name}
        {plus_minus} {pro_les} USDT💲
        Ваш комментарий: {comment}
        """)

    trade = {
        "date": date_deal,
        "coin": coin_name,
        "p_l": pro_les,
        "p_m": plus_minus,
        "comment": comment,
        }

    transactions.append(trade)
    Save_Load.save_data()


def deal_show():
    print("📊Ваши сделки:")
    for num, transaction in enumerate(transactions, 1):
        print(f"{num}. {transaction['date']}. COIN: {transaction['coin']}. {transaction['p_m']} {transaction['p_l']} USDT ")


def deal_delete():
    deal_show()
    while True:
       try:
           user_num_delete = int(input("Напиши номер сделки для удаления или 0 для выхода: "))
       except ValueError:
           print("❌ Введите цифры")
           continue

       if user_num_delete == 0:
          return

       if user_num_delete < 1 or user_num_delete > len(transactions):
          print("Такой сделки нет ❌")
          continue

       del transactions[user_num_delete - 1]
       print("Вы удалили сделку ✅")
       Save_Load.save_data()
       return



def statistics():
    if len(transactions) == 0:
        print("У вас нет сделок ❌")
        return
    else:
        total_profit = 0
        total_loss = 0
        total_progit_loss = 0
        profit_deal = 0
        loss_deal = 0
        max_profit_deal = {"p_l": 0}
        max_loss_deal = {"p_l": 0}

        for deal in transactions:
            if deal["p_m"] == "+":
                total_profit += deal["p_l"]
                total_progit_loss += deal["p_l"]
                profit_deal += 1
                if deal["p_l"] > max_profit_deal["p_l"]:
                    max_profit_deal = deal
            elif deal["p_m"] == "-":
                total_loss += deal["p_l"]
                total_progit_loss -= deal["p_l"]
                loss_deal += 1
                if deal["p_l"] > max_loss_deal["p_l"]:
                    max_loss_deal = deal
    total_profit_loss = total_profit - total_loss
    percent_profit_deal = (profit_deal / len(transactions)) * 100
    print("📊Ваши сделки:")
    print(f"Процент прибыльных: {percent_profit_deal}%")
    print(f"Получилось заработать: {total_profit_loss} USDT.")

    print(f"🟢Прибыльных сделок: {profit_deal}")
    print(f"🟢Заработано на прибыльных сделках: {total_profit} USDT.")

    print(f"🔴Убыточных сделок: {loss_deal}")
    print(f"🔴Потерянно на убыточных сделках: {total_loss} USDT.")


    if profit_deal > 0:
        print(f"Самая прибыльная сделка: {max_profit_deal['date']} - COIN: {max_profit_deal['coin']}, {max_profit_deal['p_l']} USDT.")

    if loss_deal > 0:
        print(f"Самая убыточная сделка: {max_loss_deal['date']} - COIN: {max_loss_deal['coin']}, {max_loss_deal['p_l']} USDT.")




