transactions = []


def deal_get():
	data_deal = input("Напиши дату сделки: ")
	coin_name = input("Напиши название актива: ").upper()
	while True:
		profit_lesion = input("Ваша сделка \n[1]. Прибыльная \n[2]. Убыточная")
		if profit_lesion == "1":
			pro_les = float(input("Напиши сколько составила ваша прибыль:"))
			plus_minus = "+"
			break
		elif profit_lesion == "2":
			pro_les = float(input("Напиши сколько составил ваш убыток:"))
			plus_minus = "-"
			break
		else:
			print("Такого номера нет в меню")
	comment = input("Напишите ваш комментарий по сделки: ").capitalize()
	print("Вы добавили сделку:")
	print(f"""
		{data_deal}
		COIN: {coin_name}
		{plus_minus} {pro_les} USDT
		Ваш комментарий: {comment}
		""")

	trade = {
		"data": data_deal,
		"coin": coin_name,
		"p_l": pro_les,
		"p_m": plus_minus,
		"comment": comment,
		}

	transactions.append(trade)


def deal_show():
	for num, transaction in enumerate(transactions, 1):
		print(f"{num}. {transaction['data']}. COIN: {transaction['coin']}. {transaction['p_m']} {transaction['p_l']} USDT ")


def deal_delete():
	deal_show()
	delete_num_user = int(input("Напиши номер сделки для удаления: "))
	del transactions[delete_num_user - 1]

