import requests
import json
import time

status_code = 0
#When live, status_code = 1 else = 2
#Use time.sleep(1800) to check the status every 30 mins
def get_status_code():
	global live_ststus
	url = 'https://api.live.bilibili.com/room/v1/Room/room_init?id=4480901'
	raw_data = requests.get(url)
	status_code = raw_data.json()['data']['live_status']
	if status_code == 1:
		record =time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		print('Live ok, time: '+str(record))
		time.sleep(1800)
		get_status_code()
	else:
		record =time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		post_url = 'https://sc.ftqq.com/$sercret.send' + 'text=Live Stream Stopped?'
		#Use Server chan sending the message
		print('Live down, time: '+str(record))
		requests.get(post_url)
		time.sleep(1800)
		get_status_code()

get_status_code()