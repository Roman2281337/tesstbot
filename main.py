from datetime import datetime

import vk_api
import time
import tk

token = tk.token
vk = vk_api.VkApi(token=token)
vk._auth_token()

"""НАСТРОЙКИ"""
owner_id = 447367229


now = datetime.now()
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
    time.sleep(1)
    now = datetime.now()
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


