import random
import time

class Controller():

	def __init__(self, sit="OFF", volume= 0, channel_list = ["NatGeo"], current_channel="NatGeo"):
		self.sit = sit
		self.volume = volume
		self.channel_list = channel_list
		self.current_channel = current_channel

	def open(self):
		if(self.sit == "ON"):
			print("TV is already ON.")
		else:
			self.sit = "ON"
			print("TV will be open.")

	def close(self):
		if(self.sit == "OFF"):
			print("TV is already OFF.")
		else:
			self.sit = "OFF"
			print("TV will be close.")

	def change_volume(self):
		while(True):
			ans = input("Volume off '<'\nVolume on '>'\nExit 'exit'\nChoose: ")

			if(ans == "exit"):
				break

			if(ans == "<"):
				if(self.volume <= 0):
					print("You cannot volume off any more.")
				else:
					self.volume -= 1
					print("Current volume: ",self.volume)

			elif(ans == ">"):
				if(self.volume >= 100):
					print("You canot volume on any more.")
				else:
					self.volume += 1
					print("Current volume: ",self.volume)

			else:
				print("Unknown command!")

			print("\n----------------\n")

	def add_channel(self, name):
		self.channel_list.append(name)
		time.sleep(1)
		print("Channel was added.")

	def randomly_change(self):
		random_number = random.randint(0, len(self.channel_list) - 1)
		self.current_channel = self.channel_list[random_number]
		print("Channel was changed.\nCurrent channel name: ",self.current_channel)

	def __len__(self):
		return len(self.channel_list)

	def __str__(self):
		return "---All the information---\nTV Current Situation: {}\nTV Current Volume: {}\nTV Channel List: {}\nTV Current Channel: {}".format(self.sit, self.volume, self.channel_list, self.current_channel)
	


def main():

	tv1 = Controller()

	print("""
		-----------TV System-----------
		1. ON
		2. OFF
		3. Change Volume
		4. Add Channel
		5. Learn Channel Num
		6. Change Randomly Channel
		7. TV Info
		8. Exit
		""")

	while(True):

		command = input("Please, enter your command: ")

		if(command == "8"):

			print("The system will shut down now.")
			time.sleep(1)
			break

		elif(command == "1"):
			tv1.open()

		elif(command == "2"):
			tv1.close()

		elif(command == "3"):
			tv1.change_volume()

		elif(command == "4"):
			name = input("Please, enter the channel name: ")
			tv1.add_channel(name)

		elif(command == "5"):
			print("The number of channels: ", len(tv1))

		elif(command == "6"):
			tv1.randomly_change()

		elif(command == "7"):
			print(tv1)

		else:
			print("Unknown Command!")




if __name__ == "__main__":
	main()	
