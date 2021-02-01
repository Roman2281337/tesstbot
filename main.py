from datetime import datetime, timedelta
import vk_api
import time

token = "ef441637e7cf33dbd2fa1f66d3c6a8ff68b0ee76b0fe6546b85ed88d15ca5d525aff6da309f134ea45441"

vk = vk_api.VkApi(token=token)
vk._auth_token()

"""НАСТРОЙКИ"""
owner_id = 447367229


now = datetime.now() + timedelta(hours=3)
years = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
hour = now.strftime("%H")
minute = now.strftime("%M")
second = now.strftime("%S")
print(f"{day}.{month}.{years} | {hour}:{minute}")
like = vk.method("likes.getList", {"type": "photo", "owner_id": owner_id, "item_id": "457252443", "random_id": 0})
count_like = like['count']
vk.method("status.set", {"text": f"{day}.{month}.{years} | {hour}:{minute} | На аве {count_like}♥", "random_id": 0})


print("статус изменен")



old_hour = hour
old_minute = minute

while True:
    try:
        time.sleep(1)
        now = datetime.now() + timedelta(hours=3)
        years = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")
        hour = now.strftime("%H")
        minute = now.strftime("%M")
        second = now.strftime("%S")

        if old_hour != hour or old_minute != minute:
            like = vk.method("likes.getList",{"type": "photo", "owner_id": owner_id, "item_id": "457252443", "random_id": 0})
            count_like = like['count']
            vk.method("status.set", {"text": f"{day}.{month}.{years} | {hour}:{minute} | На аве {count_like}♥", "random_id": 0})
            print("статус изменен")
            old_hour = hour
            old_minute = minute
    except Exception as e:
        print(e)
    



