import vk_api
from datetime import datetime
token = "d1c0f581ec0c85e9e38797a9222da2b85154af4406ea86df9f24fc9bf6e7e612afacc8c668edb766c11e3"
vk = vk_api.VkApi(token=token)
vk._auth_token()


print('Бот успешно активирован!')

WHITELISTED_USERS = {447367229: -999}
check = 5
current_datetime = datetime.now()
print(WHITELISTED_USERS)







def base(name, mail, gender, date, address, telephone1, telephone2, Parent1, Parent2, info):
    global id
    vk.method("messages.send", {"peer_id": id,
                                "message": f"ᛜ ФИО:\n{name}\nᛜ Почта:\n{mail}\nᛜ Пол:\n{gender}\nᛜ Дата рождения:\n{date}\nᛜ Адрес проживания (предположительно):\n{address}\nᛜ Телефон 1:\n{telephone1}\nᛜ Телефон 2:\n{telephone2}\nᛜ Первый родитель:\n{Parent1}\nᛜ Второй родитель:\n{Parent2}\nᛜ Прочие контакты:\n{info}",
                                "random_id": 0})


def Bot():
    try:
        global id
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})


        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "алексеева":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="Алексеева Анна Юрьевна",
                         mail="anna190315@mail.ru",
                         gender="ж",
                         date="11.04.2003",
                         address="ул. Полярная, дом 8, кв. 190",
                         telephone1="8-(499)-798-13-37",
                         telephone2="8(916)082-34-05",
                         Parent1="Алексеева Наталья Александровна",
                         Parent2="Алексеев Юрий Петрович",
                         info="8 916 550 41 24\nNATALY190315@mail.ru\n8 985 464 54 92")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                                "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                                "random_id": 0})

            elif body.lower() == "/base":
                if WHITELISTED_USERS.get(id) < check:
                    vk.method("messages.send", {"peer_id": id,
                                                "message": f"ᛜ Список фамилий:\n"
                                                           f"Алексеева\n"
                                                           f"Бет\n"
                                                           f"Бесфамильный\n"
                                                           f"Лаптев\n"
                                                           f"Минаева\n"
                                                           f"Незнанов\n"
                                                           f"Клименко\n"
                                                           f"Зинчевская\n"
                                                           f"Глотова\n"
                                                           f"Измайлов\n"
                                                           f"Запорожцев\n"
                                                           f"Павленко\n"
                                                           f"Пастухова\n"
                                                           f"Пушилин\n"
                                                           f"Пушилина\n"
                                                           f"Раентович\n"
                                                           f"Райсян\n"
                                                           f"Сергеева\n"
                                                           f"Терентьев\n"
                                                           f"Шевченко\n"
                                                           f"Юровская\n"
                                                           f"Козлова\n"
                                                           f"Меньшенина\n"
                                                           f"Жуков\n"
                                                           f"Сибиленков\n"
                                                           f"Гнусаров\n"
                                                           f"Гребень\n"
                                                           f"Егорова\n"
                                                           f"",
                                                "random_id": 0})
                else:
                    vk.method("messages.send", {"peer_id": id,
                                                "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                                "random_id": 0})


            elif body.lower() == "бет":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="Бет Анастасия Алексеевна",
                         mail="-",
                         gender="ж",
                         date="01.09.2003",
                         address="ул. Полярная, дом 17 к.2, кв. 45",
                         telephone1="-",
                         telephone2="-",
                         Parent1="Маргарян Татьяна Николаевна",
                         Parent2="-",
                         info="8 909 634 81 25")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                                "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                                "random_id": 0})
            elif body.lower() == "бесфамильный":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="Бефсамильный Антон Васильевич",
                         mail="-",
                         gender="м",
                         date="21.02.2003",
                         address="пр. Шокальского, дом 13 к.1, кв. 56",
                         telephone1="8-(926)-677-10-78",
                         telephone2="-",
                         Parent1="Косарева Ирина Анатольевна",
                         Parent2="Бесфамильный Василий Юрьевич",
                         info="8 977 251 17 60")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                                "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                                "random_id": 0})

            elif body.lower() == "лаптев":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="Лаптев Андрей Михайлович",
                         mail="-",
                         gender="м",
                         date="30.12.2002",
                         address="пр. Шокальского, дом 3 к.1, кв. 165",
                         telephone1="8-(985)-366-71-94",
                         telephone2="-",
                         Parent1="Лаптева Ирина Владимировна",
                         Parent2="Лаптев Михаил Леонидович",
                         info="8 916 887 13 66")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                                "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                                "random_id": 0})

            elif body.lower() == "минаева":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="Минаева Алена Юрьевна",
                         mail="alena-minaeva-2015@mail.ru",
                         gender="ж",
                         date="21.11.2003",
                         address="пр Шокальского, дом 12 к.1, кв. 219",
                         telephone1="8-(499)-479-50-73",
                         telephone2="8-(965)-295-57-77",
                         Parent1="Минаева Оксана Валерьевна",
                         Parent2="Минаев Юрий Иванович",
                         info="8 905 792 06 16\noksanay@inbox.ru\n8 909 942 05 62")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                                "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                                "random_id": 0})

            elif body.lower() == "незнанов":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="Незнанов Глеб Михайлович",
                         mail="-",
                         gender="м",
                         date="20.12.2003",
                         address="ул. Сухонская, дом 1 к.1, кв. 24",
                         telephone1="8-(495)-472-06-58",
                         telephone2="8-(915)-268-69-59",
                         Parent1="Волис Елена Владимировна",
                         Parent2="Незнанов Михаил Юрьевич",
                         info="8 910 493 88 74\nelena_volis@mail.ru\n8 917 500 64 09\nM.NEZNANOV@tamp.ru")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                                "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                                "random_id": 0})

            elif body.lower() == "клименко":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="Клименко Ксения Максимовна",
                         mail="-", gender="ж",
                         date="10.10.2003",
                         address="ул. Полярная, дом 2 к.1, кв. 242",
                         telephone1="8-(977)-282-79-16",
                         telephone2="-",
                         Parent1="Миронова Евгения Алексеевна",
                         Parent2="Клименко Андрей Александрович",
                         info="8 916 705 94 62")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                                "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                                "random_id": 0})

            elif body.lower() == "зинчевская":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="Зинчевская Вера Алексеевна ",
                         mail="-",
                         gender="ж",
                         date="03.05.2004",
                         address="пр Шокальского, дом 5 к.1, кв. 141",
                         telephone1="8-(977)-937-38-68",
                         telephone2="-",
                         Parent1="Зинчевская (Кутилина) Елена Владимировна",
                         Parent2="Зинчевский Евгений Андреевич",
                         info="8 901 704 87 81")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                                "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                                "random_id": 0})

            elif body.lower() == "глотова":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="Глотова Анастасия Ильинична",
                         mail="********03@BK.ru",
                         gender="ж",
                         date="02.03.2003",
                         address="пр Шокальского, дом 11 к.1, кв. 175",
                         telephone1="477-94-06",
                         telephone2="8-(929)-931-56-98",
                         Parent1="Минаева Оксана Валерьевна",
                         Parent2="Минаев Юрий Иванович",
                         info="8 905 792 06 16\noksanay@inbox.ru\n8 909 942 05 62")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                                "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                                "random_id": 0})

            elif body.lower() == "измайлов":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="Измайлов Марат Дамирович",
                         mail="marat_iz2003@mail.ru",
                         gender="м",
                         date="14.06.2003",
                         address="ул Полярная, дом 8 к.1, кв. 63",
                         telephone1="8-(499)-477-45-26",
                         telephone2="8-(926)-404-00-49",
                         Parent1="Измайлова Диляра Раисова",
                         Parent2="Измайлов Дамир Александрович",
                         info="8 916 705 94 62")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                                "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                                "random_id": 0})

            elif body.lower() == "запорожцев":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="Запорожцев Максим Александрович", mail="-", gender="м", date="04.11.2003",
                         address="Грибки,ул.Спортивная, дом 5 к.1, кв. 218", telephone1="8-(915)-005-69-90", telephone2="-",
                         Parent1="Запорожцева Елена Валерьевна", Parent2="Запорожцева Александр Юрьевич",
                         info="8 903 208 28 00")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                                "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                                "random_id": 0})

            elif body.lower() == "павленко":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="Павленко Илья Павлович", mail="-", gender="м", date="07.03.2003",
                     address="ул. Полярная, дом 8 к.1, кв. 257", telephone1="8-(916)-341-29-30", telephone2="-",
                     Parent1="Павленко Светлана Николаевна", Parent2="-", info="8 985 090 98 23")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                                "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                                "random_id": 0})

            elif body.lower() == "пастухова":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="Пастухова Ксения Валерьевна", mail="-", gender="ж", date="13.03.2003",
                         address="пр. Шокальского, дом 3 к.1, кв. 132", telephone1="8-(958)-819-24-99", telephone2="-",
                         Parent1="Пастухова Ольга Александровна", Parent2="Пастухов Валерий Александрович",
                         info="8 916 935 57 35")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                                "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                                "random_id": 0})

            elif body.lower() == "пушилин":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="Пушилин Виталий Юрьевич", mail="-", gender="м", date="21.09.2003",
                         address="ул. Молодцова, дом 3 к.1, кв. 33", telephone1="8-(903)-775-30-99", telephone2="-",
                         Parent1="Пушилина Елена Николаевна", Parent2="-",
                         info="8 925 901 08 57\n8 903 566 24 02\npu.ln@mail.ru")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                                "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                                "random_id": 0})

            elif body.lower() == "пушилина":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="Пушилина Надежда Юрьевна", mail="-", gender="ж", date="21.01.2003",
                     address="ул. Молодцова, дом 3 к.1, кв. 33", telephone1="8-(964)-799-21-99", telephone2="-",
                     Parent1="Пушилина Елена Николаевна", Parent2="-",
                     info="8 925 901 08 57\n8 903 566 24 02\npu.ln@mail.ru")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                                "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                                "random_id": 0})

            elif body.lower() == "раентович":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="Раентович Андрей Дмитриевич", mail="-", gender="м", date="23.07.2003",
                     address="ул. Дежнева, дом 14 к.1, кв. 6", telephone1="8-(499)-477-57-06",
                     telephone2="8-(967)-204-03-29",
                     Parent1="Раентович Валентина Юрьевна", Parent2="Раентович Дмитрий Александрович",
                     info="8 910 406 57 30\nAUR11@yandex.ru\n8-(916)-124-68-39")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                                "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                                "random_id": 0})


            elif body.lower() == "райсян":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="Райсян Катэрина Норайровна", mail="raysyan.katerina@mail.ru", gender="ж", date="01.07.2003",
                     address="ул. Полярная, дом 8 к.1, кв. 149", telephone1="8-(495)-656-88-35",
                     telephone2="8-(964)-537-40-62",
                     Parent1="Райсян Карина Новиковна", Parent2="Райсян Норайр Мельсикович",
                     info="8 962 977 82 10\n8 905 761 80 08\nkarina.ray@bk.ru")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                                "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                                "random_id": 0})

            elif body.lower() == "сергеева":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="Сергеева Эвелина Владимировна", mail="-", gender="ж", date="21.12.2002",
                     address="ул. Заповедная, дом 6 к.1, кв. 83", telephone1="8-(916)-395-85-45", telephone2="477-94-35",
                     Parent1="Сергеева Галина Владимировна", Parent2="-",
                     info="8 (917) 573 08 59\ngalinasergeeva70@gmail.com")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                                "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                                "random_id": 0})



            elif body.lower() == "терентьев" or body.lower() == "тюлень":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="Терентьев Иван Игоревич", mail="vanechka03@inbox.ru", gender="м", date="22.07.2003",
                     address="пр. Шокальского, дом 1 к.1, кв. 228", telephone1="8-(495)-602-74-25",
                     telephone2="8-(967)-275-54-75",
                     Parent1="Терентьева Елена Юрьевна", Parent2="Терентьев Игорь Борисович",
                     info="8 (905) 526 25 10\n8 906 764 01 65\nlenusya67@inbox.ru")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                                "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                                "random_id": 0})

            elif body.lower() == "шевченко":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="Шевченко Снежана Вячеславовна",
                     mail="-",
                     gender="ж",
                     date="25.01.2004",
                     address="ул. Полярная, дом 10 к.1, кв. 37",
                     telephone1="8-(916)-395-85-45",
                     telephone2="477-94-35",
                     Parent1="Шевченко Оксана Валерьевна",
                     Parent2="Шевченко Вячеслав Викторович",
                     info="8 (964) 773 90 08")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                                "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                                "random_id": 0})

            elif body.lower() == "юровская":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="Юровская Елизавета Андреевна",
                     mail="-",
                     gender="ж",
                     date="-",
                     address="Москва",
                     telephone1="8-(985)-146-40-47",
                     telephone2="-",
                     Parent1="Юровская Елена Викторовна",
                     Parent2="Юровский Андрей Ататольевич",
                     info="8 (916) 127 65 23\n8 985 763 77 81\ninst: _.yurovskaya._")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                            "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                            "random_id": 0})

            elif body.lower() == "козлова":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="Козлова Валерия Дмитриевна",
                     mail="-",
                     gender="ж",
                     date="06.03.2003",
                     address="пр. Шокальского, дом 11 к.1, кв. 135",
                     telephone1="8-(967)-229-48-57",
                     telephone2="-",
                     Parent1="Козлова Татьяна Александровна",
                     Parent2="Козлов Дмитрий Викторович",
                     info="8 (965) 144 15 91\nСестра - https://vk.com/id293414887\nВ москве с 2010 г.\ninst: lera_kozlova_13")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                            "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                            "random_id": 0})

            elif body.lower() == "меньшенина":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="Меньшенина Ольга Сергеевна",
                     mail="-",
                     gender="ж",
                     date="20.07.2003",
                     address="пр. Шокальского, дом 11 к.1, кв. 171",
                     telephone1="8-(965)-582-05-19",
                     telephone2="-",
                     Parent1="Меньшенина Марина Владимировна",
                     Parent2="Меньшенин Сергей Олегович",
                     info="8 (964) 767 70 54")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                            "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                            "random_id": 0})

            elif body.lower() == "жуков":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="Жуков Дмитрий Игоревич",
                         mail="-",
                         gender="м",
                         date="15.06.2003",
                         address="ул. Полярная, дом 12 к.1, кв. 163",
                         telephone1="8-(903)-233-86-74",
                         telephone2="-",
                         Parent1="Жукова Ольга Анатольевна",
                         Parent2="Жуков Игорь Валерьевич",
                         info="8 (905) 508 96 72\nмама - https://vk.com/id5966706")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                                "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                                "random_id": 0})

            elif body.lower() == "сибиленков":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="Сибиленков Павел Андреевич",
                         mail="-",
                         gender="м",
                         date="14.10.2003",
                         address="ул. Полярная, дом 16 к.1, кв. 70",
                         telephone1="8-(985)-935-12-90",
                         telephone2="-",
                         Parent1="Сибиленкова Елена Викторовна",
                         Parent2="Сибиленков Игорь Борисовчи",
                         info="8 (910) 465 05 60")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                                "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                                "random_id": 0})
            elif body.lower() == "гнусаров":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="Гнусаров Игорь Алексеевич",
                         mail="-",
                         gender="м",
                         date="18.06.2003",
                         address="ул. Полярная, дом 8 к.1, кв. 198",
                         telephone1="8-(985)-397-66-33",
                         telephone2="-",
                         Parent1="Гнусарова Елена Николаевна",
                         Parent2="-",
                         info="8 (916) 222 48 83")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                                "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                                "random_id": 0})


            elif body.lower() == "гребень":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="Гребень Данили Игоревич",
                         mail="-",
                         gender="м",
                         date="19.06.2003",
                         address="ул. Молодцова, дом 2 к.1, кв. 197",
                         telephone1="8-(916)-232-62-43",
                         telephone2="-",
                         Parent1="Гребень Виктория Борисовна",
                         Parent2="Гребень Игорь Владимирович",
                         info="8 (910) 478 16 43")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                                "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                                "random_id": 0})
            elif body.lower() == "егорова":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="егорова Полина Викторонва",
                         mail="-",
                         gender="м",
                         date="09.05.2003",
                         address="ул. Полярная, дом 16 к.1, кв. 20",
                         telephone1="8-(916)-274-83-75",
                         telephone2="-",
                         Parent1="Егорова Наталья Александровна",
                         Parent2="Егоров Виктор Александрович",
                         info="8 (915) 175 26 73")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                                "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                                "random_id": 0})
            elif body.lower() == "гульбандян":
                if WHITELISTED_USERS.get(id) < check:
                    base(name="Гульбандян Стефан Игоревич",
                         mail="-",
                         gender="м",
                         date="07.12.2002",
                         address="Янтарный проезд, дом 15 к.1, кв. 54",
                         telephone1="8-(919)-966-54-31",
                         telephone2="-",
                         Parent1="Пуйто Анна Борисовна",
                         Parent2="-",
                         info="8 (916) 315 90 91\n8 (901) 902 90 91")
                    WHITELISTED_USERS[id] = WHITELISTED_USERS.get(id) + 1
                    print(WHITELISTED_USERS)
                else:
                    vk.method("messages.send", {"peer_id": id,
                                                "message": f"ᛜ У вас закончилась возможность смотреть информацию (Каждый день в 0:00 чекер сбрасывается)",
                                                "random_id": 0})



            else:
                if len(body) > 3:
                    vk.method("messages.send",
                              {"peer_id": id, "message": "ᛜ Увы, этого человека пока что нету в базе :(", "random_id": 0})
                else:
                    vk.method("messages.send",
                              {"peer_id": id, "message": "ᛜ Введите фамилию:", "random_id": 0})
    except Exception:
        vk.method("messages.send",
                  {"peer_id": id, "message": "ᛜ У вас нету лицензии.", "random_id": 0})

while True:
    current_datetime = datetime.now()
    if current_datetime.hour == 15 and current_datetime.minute == 30 and current_datetime.second == 1:
        for i in WHITELISTED_USERS:
            if WHITELISTED_USERS.get(i) > 0:
                WHITELISTED_USERS[int(i)] = 0
        print("Настало время очистить чеки. Время 0:00")
        print(WHITELISTED_USERS)
    Bot()
































