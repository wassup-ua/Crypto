transactions = []





def deal_get():
	data_deal = input("Напиши дату сделки: ")
	coin_name = input("Напиши название актива: ").upper()
	profit_lesion = input("Ваша сделка \n[1]. Прибыльная \n[2]. Убыточная")
	if profit_lesion == "1":
		pro_les = float(input("Напиши сколько составила ваша прибыль:"))
		plus_minus = "+"
	elif profit_lesion == "2":
		pro_les = float(input("Напиши сколько составил ваш убыток:"))
		plus_minus = "-"
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


	tread = {
		"data": data_deal,
		"coin": coin_name,
		"p_l": pro_les,
		"p_m": plus_minus,
		"comment": comment,
		}

	transactions.append(tread)