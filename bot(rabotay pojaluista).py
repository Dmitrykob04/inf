import requests

API_link = "https://api.telegram.org/bot5916023815:AAHb_7-LdkQNPR61OtiLafeGumAAROMb5nY"

updates = requests.get(API_link + "/getUpdates?offset=-1").json()

print(updates)

message = updates["result"][0]["message"]
chat_id = message["from"]["id"]
text = message["text"]

sent_message = requests.get(API_link + f"/sendMessage?chat_id={chat_id}&text=Здравствуй, ты написал {text}")
