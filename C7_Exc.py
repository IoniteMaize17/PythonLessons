import time
note = ""
while True:
	print("(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Quit\n")
	selection = int(input("Please select one: "))
		
	if selection == 1:
		print(note)
	elif selection == 2:
		note_text = input("Write a new note: ")
		note_time = time.strftime("%X %x")
		note = note_text + ":::" + note_time
	elif selection == 3:
		note = ""
	elif selection == 4:
		print("Notebook shutting down, thank you.")
		break


'''import time		

time.strftime("%X %x")
'19:01:34 01/03/09'''