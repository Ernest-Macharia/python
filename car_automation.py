instruction = ""
started = False
while True:
	command = input("> ").lower()
	if command == "start":
		if started:
			print("Car has already started")
		else:
			started = True
			print("The car has started..")
	elif command == "stop":
		if not started:
			print("Car has already stopped")
		else:
			started = False
			print("The car has stopped")
	elif command == "help":
		print('''
The commands to use are:
start - to start the car
stop - to stop the car
quit - to quit the car commands
				''')
	elif command == "quit":
		break
	else:
		print("The command is not known")
