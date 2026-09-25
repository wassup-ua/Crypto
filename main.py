import deal
import Save_Load

Save_Load.load_data()
while True:
    print("""
    [1]. Трейдинг
    [0]. Выход
        """)
    user_number = input("Выбери номер: ")
    if user_number == "1":
        while True:
            print("""
                [1]. Добавить сделку
                [2]. Смотреть сделки
                [3]. Изменить сделку
                [4]. Удалить сделку
                [5]. Статистика
                [0]. Выйти
                """)
            user_num1 = input("Выбери номер: ")
            if user_num1 == "1":
                deal.deal_get()
            elif user_num1 == "2":
                if len(deal.transactions) == 0:
                    print("У вас нет сделок ❌")
                else:
                    deal.deal_show()
            elif user_num1 == "3":
                if len(deal.transactions) == 0:
                    print("У вас нет сделок ❌")
                else:
                    deal.deal_edit()
            elif user_num1 == "4":
                if len(deal.transactions) == 0:
                    print("У вас нет сделок ❌")
                else:
                    deal.deal_delete()
            elif user_num1 == "5":
                deal.statistics()

            elif user_num1 == "0":
                break
            else:
                print("Такого номера нет в меню ❌")

    elif user_number  == "0":
            break
    else:
        print("Такого номера нет в меню ❌")


