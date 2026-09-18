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
		"data": date_deal,
		"coin": coin_name,
		"p_l": pro_les,
		"p_m": plus_minus,
		"comment": comment,
		}

	transactions.append(trade)


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
       return







