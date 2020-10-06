# Created by DetevtiveMiawoo		
import time		
		
time.sleep(2)
print(" Created by DetectiveMiawoo")
time.sleep(2)
print(" Please wait...")
time.sleep(1)
		
print (" loading...")
time.sleep(1) #1 saniye delay
print (" please wait")
time.sleep(1) #1 saniye delay
print (" system ready!")
time.sleep(1) #1 saniye delay

x = input(" please enter your name:")
time.sleep(0.5)
print(" Wait...")
time.sleep(1.5)

while True:
	
			print (" Hi ", x , ", please write continue for enter the system \n"  "                 or \n"   " write exit for exit from the system --------------- \n")

			e = input("-")

			time.sleep(0.5) #50 salise delay
			if (e == "Continue" or e == "continue"):
	 			time.sleep(0.5)
	 			print(" Welcome", x)
	 			time.sleep(0.5)
	 			break

			elif (e == "Exit" or e == "exit"):
				      time.sleep(1)
				      print(" Ok! ")
				      time.sleep(0.5)
				      print (" system closing in 3")
				      time.sleep(0.5)
				      print (" system closing in 2")
				      time.sleep(0.5)
				      print (" system closing in 1")
				      time.sleep(0.5)
				      print(" Bye Bye")
				      time.sleep(3)
				      quit()
				      break

			else:
				time.sleep
				print( " Hmm somethings looking wrong" )
				time.sleep(0.5)
				print(" Please try again                                                    ")
				time.sleep(1)
				continue

time.sleep(1)

print(" okay!", x ,"choose a passwod \n" + " (max 16 latters and must be longer than 5 letters \n")
time.sleep(0.9)

while True:
			
			y = input (" Please Choose a Strong Password " + x + ":")
			time.sleep(0.8)
	
			if (len(y) < 4):
				print(" oh no!" + " its looking too short")
				time.sleep(0.7)
				print(" pls try again")
				time.sleep(0.5)
				continue
	
			elif (len(y) > 17):
				print(" oh no!" + " its looking too long")
				time.sleep(0.7)
				print(" pls try again")
				time.sleep(0.5)
				continue
		
			else:
				break

yy = input(" Correct your password:")

if ( yy == y ):
	 		print(" please wait...")
	 		time.sleep(1)
	 		print(" your entry data is correcting...")
	 		time.sleep(0.5)
	 		print(" Please wait...") 
	 		time.sleep(2)
	 		print(" OK! Done!")
	 		time.sleep(1)
	 		print (" Password Corrected ")
	 		time.sleep(3)
	 		print(" system will direct you to the purchase path in 3")
	 		time.sleep(1)
	 		print(" system will direct you to the purchase path in 2")
	 		time.sleep(1)
	 		print(" system will direct you to the purchase path in 1")
	 		time.sleep(2)
	 		print(" opss sometings went wrong :(")
 			time.sleep(1.5)
 			print(" please our support page for yoor problem.")
 			time.sleep(1)
 			print(" www.b&e-studios.net ")
 			time.sleep(2)
 			print(" system closing...")
 			time.sleep(5)
 			quit()

else:
			print(" Pleas wait your entry data is correcting")
			time.sleep(1)
			print(" sometings went wrong :( ")
			time.sleep(0.5)
			print (" system closing in 3")
			time.sleep(0.5)
			print (" system closing in 2")
			time.sleep(0.5)
			print (" system closing in 1")
			time.sleep(0.5)
			print(" bye bye")
			quit()