from fetch_post_data import fetch_post_data
import json,time

with open("miner_data_payload.json") as f:
	miner_data_payload = json.load(f)

# with open("raw_complete_miner_data.txt","w") as f:
# 	f.write(json.dumps(raw_complete_miner_data))

def fetch_complete_raw_miner_data():
	raw_complete_miner_data = []

	raw_complete_miner_data.append(fetch_post_data(miner_data_payload)["rows"][0])
	exit_flag = 1
	while(exit_flag):
		while True:
			try:
				raw_miner_data = (fetch_post_data(miner_data_payload)["rows"])
			except:
				continue
			break
		last_miner = raw_miner_data[-1]["data"]["miner"]
		miner_data_payload["lower_bound"] = last_miner
		raw_complete_miner_data.extend(raw_miner_data[1:])
		# print(len(raw_miner_data))
		if(len(raw_miner_data)==1):
			exit_flag = 0
		time.sleep(1)
	miner_data_payload["lower_bound"] = ""
	return raw_complete_miner_data
	
# print(len(fetch_complete_raw_miner_data()))

# raw_miner_data = fetch_post_data(miner_data_payload)["rows"]
# print(raw_miner_data)

# last_miner = raw_miner_data[-1]["data"]["miner"]
# print(last_miner)

# miner_data_payload["lower_bound"] = last_miner
# raw_miner_data = fetch_post_data(miner_data_payload)["rows"]
# print(raw_miner_data[0]["data"]["miner"])

# miner_data_payload["index_position"] = 2
# print(len(fetch_post_data(miner_data_payload)["rows"]))


