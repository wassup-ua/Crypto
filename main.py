import deal




while True:
	print("""
	[1]. Трейдинг
	[0]. Выход
		""")
	user_number = input("Выбери номер: ")
	if user_number == "1":
		print("""
			[1]. Добавить сделку
			[2]. Смотреть сделки
			[3]. Удалить сделку
			[0]. Выйти
			""")
		user_num1 = input("Выбери номер: ")
		if user_num1 == "1":
			deal.deal_get()
		elif user_num1 == "2":
			deal.deal_show()
		elif user_num1 == "3":
			deal.deal_delete()
		elif user_num1 == "0":
			break
			
	elif user_number  == "0":
			break



				