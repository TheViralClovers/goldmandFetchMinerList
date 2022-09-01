from fetch_miner_data import fetch_complete_raw_miner_data
import time
from win10toast import ToastNotifier
toaster = ToastNotifier()

print("Starting process please wait, may take a while.......")

def fetch_miners_on_land():
	complete_raw_miner_data = fetch_complete_raw_miner_data()
	miners_list = []
	for raw_miner_data in complete_raw_miner_data:
		if(raw_miner_data["data"]["land"]=="1099732772168"):
			miner_wallet = raw_miner_data["data"]["miner"]
			miners_list.append(miner_wallet)
	return miners_list

curr_miners_list = fetch_miners_on_land()

print("Current wallets registered on your land are :")
for wallet in curr_miners_list:
	print(wallet)
print("Listening for changes")

while(1):
	new_miners_list = fetch_miners_on_land()
	if(not(len(list(set(new_miners_list).symmetric_difference(set(curr_miners_list)))))):
		# print("no changes")
		pass
	else:
		print("change has occured")
		newly_joined_miners = list(set(new_miners_list)-set(curr_miners_list))
		miners_that_left = list(set(curr_miners_list)-set(new_miners_list))
		if(len(newly_joined_miners)):
			toaster.show_toast("Congrats",f"{newly_joined_miners} has joined the land")
		if(len(miners_that_left)):
			toaster.show_toast("Oh no!",f"{miners_that_left} has left the land")
		curr_miners_list = new_miners_list
	time.sleep(10)