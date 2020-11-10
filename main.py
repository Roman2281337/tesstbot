import vk_api
from datetime import datetime
import time
import requests

token = "785b2302edff3b90ba86d162f6d7b7de4916adb1411883c1a1bb9fd205e29438b4d145f4c3eb1e887801f"
vk = vk_api.VkApi(token=token)
vk._auth_token()
#НА HEROKU на 3 часа меньше
print('Бот успешно активирован!')
print(datetime.now())



array = []

def Bot():
    print("Идет поиск уроков...")
    now = datetime.now()
    day_ = int(now.strftime("%d"))
    k = 192684000
    for i in range(999):
        try:
            r = requests.get("https://dnevnik.mos.ru/vcs/links?scheduled_lesson_id=" + str(k)).json()
            s = r['_embedded']['link_views'][0]['start_date_time']
            d1 = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S+03:00")
            day = int(d1.strftime("%d"))

            if day >= day_:
                array.append(r)
                #print(str(r['_embedded']['link_views'][0]['scheduled_lesson_id']),end=",")
            k = k + 1
        except Exception:
            k=k+1
    print("Поиск уроков закончен\n")




def arbus():
    print(".",end="")
    time.sleep(1)
    #str
    now = datetime.now()
    month_ = now.strftime("%m")
    day_ = now.strftime("%d")
    hour_ = now.strftime("%H")
    minute_ = now.strftime("%M")

    if hour_ == "05" and int(minute_) == 25:
        print("start")
        for i in range(len(array)):
            s = array[i]['_embedded']['link_views'][0]['start_date_time']
            d1 = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S+03:00")
            month = d1.strftime("%m")
            day = d1.strftime("%d")
            hour = d1.strftime("%H")
            minute = d1.strftime("%M")
            if hour == "05" and int(minute)-5 == int(minute_) and int(day_) == int(day):
                text = (f"\nДата урока: {day}-{month}-2020\nВремя начала урока: {hour}:{minute} " + "\nСсылка: " +array[i]['_embedded']['link_views'][0]['link_url'])
                vk.method("messages.send", {"peer_id": 2000000002, "message": text, "random_id": 0})
                print("Сообщение отправлено!")
                time.sleep(60)
                break





    if hour_ == "06" and int(minute_) == 25:
        print("start")
        for i in range(len(array)):
            s = array[i]['_embedded']['link_views'][0]['start_date_time']
            d1 = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S+03:00")
            month = d1.strftime("%m")
            day = d1.strftime("%d")
            hour = d1.strftime("%H")
            minute = d1.strftime("%M")
            if hour == "06" and int(minute) - 5 == int(minute_) and int(day_) == int(day):
                text = (f"\nДата урока: {day}-{month}-2020\nВремя начала урока: {hour}:{minute} " + "\nСсылка: " +
                        array[i]['_embedded']['link_views'][0]['link_url'])
                vk.method("messages.send", {"peer_id": 2000000002, "message": text, "random_id": 0})
                print("Сообщение отправлено!")
                time.sleep(60)
                break



    if hour_ == "07" and int(minute_) == 25:
        print("start")
        for i in range(len(array)):
            s = array[i]['_embedded']['link_views'][0]['start_date_time']
            d1 = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S+03:00")
            month = d1.strftime("%m")
            day = d1.strftime("%d")
            hour = d1.strftime("%H")
            minute = d1.strftime("%M")
            if hour == "07" and int(minute) - 5 == int(minute_) and int(day_) == int(day):
                text = (f"\nДата урока: {day}-{month}-2020\nВремя начала урока: {hour}:{minute} " + "\nСсылка: " +
                        array[i]['_embedded']['link_views'][0]['link_url'])
                print(text)
                print("Идет отправка сообщения...")
                vk.method("messages.send", {"peer_id": 2000000002, "message": text, "random_id": 0})
                print("Сообщение отправлено!")
                time.sleep(60)
                break



    if hour_ == "08" and int(minute_) == 20:
        print("start")
        for i in range(len(array)):
            s = array[i]['_embedded']['link_views'][0]['start_date_time']
            d1 = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S+03:00")
            month = d1.strftime("%m")
            day = d1.strftime("%d")
            hour = d1.strftime("%H")
            minute = d1.strftime("%M")
            if hour == "08" and int(minute) - 5 == int(minute_) and int(day_) == int(day):
                text = (f"\nДата урока: {day}-{month}-2020\nВремя начала урока: {hour}:{minute} " + "\nСсылка: " +
                        array[i]['_embedded']['link_views'][0]['link_url'])
                print(text)
                print("Идет отправка сообщения...")
                vk.method("messages.send", {"peer_id": 2000000002, "message": text, "random_id": 0})
                print("Сообщение отправлено!")
                time.sleep(60)
                break



    if hour_ == "09" and int(minute_) == 25:
        print("start")
        for i in range(len(array)):
            s = array[i]['_embedded']['link_views'][0]['start_date_time']
            d1 = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S+03:00")
            month = d1.strftime("%m")
            day = d1.strftime("%d")
            hour = d1.strftime("%H")
            minute = d1.strftime("%M")
            if hour == "09" and int(minute) - 5 == int(minute_) and int(day_) == int(day):
                text = (f"\nДата урока: {day}-{month}-2020\nВремя начала урока: {hour}:{minute} " + "\nСсылка: " +
                        array[i]['_embedded']['link_views'][0]['link_url'])
                print(text)
                print("Идет отправка сообщения...")
                vk.method("messages.send", {"peer_id": 2000000002, "message": text, "random_id": 0})
                print("Сообщение отправлено!")
                time.sleep(60)
                break


    if hour_ == "10" and int(minute_) == 25:
        print("start")
        for i in range(len(array)):
            s = array[i]['_embedded']['link_views'][0]['start_date_time']
            d1 = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S+03:00")
            month = d1.strftime("%m")
            day = d1.strftime("%d")
            hour = d1.strftime("%H")
            minute = d1.strftime("%M")
            if hour == "10" and int(minute) - 5 == int(minute_) and int(day_) == int(day):
                text = (f"\nДата урока: {day}-{month}-2020\nВремя начала урока: {hour}:{minute} " + "\nСсылка: " +
                        array[i]['_embedded']['link_views'][0]['link_url'])
                print(text)
                print("Идет отправка сообщения...")
                vk.method("messages.send", {"peer_id": 2000000002, "message": text, "random_id": 0})
                print("Сообщение отправлено!")
                time.sleep(60)
                break



    if hour_ == "11" and int(minute_) == 25:
        print("start")
        for i in range(len(array)):
            s = array[i]['_embedded']['link_views'][0]['start_date_time']
            d1 = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S+03:00")
            month = d1.strftime("%m")
            day = d1.strftime("%d")
            hour = d1.strftime("%H")
            minute = d1.strftime("%M")
            if hour == "11" and int(minute) - 5 == int(minute_) and int(day_) == int(day):
                text = (f"\nДата урока: {day}-{month}-2020\nВремя начала урока: {hour}:{minute} " + "\nСсылка: " +
                        array[i]['_embedded']['link_views'][0]['link_url'])
                print(text)
                print("Идет отправка сообщения...")
                vk.method("messages.send", {"peer_id": 2000000002, "message": text, "random_id": 0})
                print("Сообщение отправлено!")
                time.sleep(60)
                break





    if hour_ == "12" and int(minute_) == 20:
        print("start")
        for i in range(len(array)):
            s = array[i]['_embedded']['link_views'][0]['start_date_time']
            d1 = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S+03:00")
            month = d1.strftime("%m")
            day = d1.strftime("%d")
            hour = d1.strftime("%H")
            minute = d1.strftime("%M")
            if hour == "12" and int(minute) - 5 == int(minute_) and int(day_) == int(day):
                text = (f"\nДата урока: {day}-{month}-2020\nВремя начала урока: {hour}:{minute} " + "\nСсылка: " +
                        array[i]['_embedded']['link_views'][0]['link_url'])
                print(text)
                print("Идет отправка сообщения...")
                vk.method("messages.send", {"peer_id": 2000000002, "message": text, "random_id": 0})
                print("Сообщение отправлено!")
                time.sleep(60)
                break


Bot()
while True:
    arbus()
