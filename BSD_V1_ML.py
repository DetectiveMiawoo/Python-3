import time 

time.sleep(2)
print(" Created by Detective Miawoo")
time.sleep(2)
print(" Please wait...")
time.sleep(1)

print(" Only 2 language avaible right now ")
time.sleep(1)
print(" TR for Turkish \n" + " ENG for English")
time.sleep(1.5)


while True:
	
	d = input (" choose your language:")
	time.sleep(1)

	if( d == "TR" or d == "tr" or d == "Tr" or d == "tR"):
		
		time.sleep(0.8)
		print (" yükleniyor...")
		time.sleep(1) #1 saniye delay
		print (" lütfen bekleyin")
		time.sleep(1) #1 saniye delay
		print (" sistem hazır!")
		time.sleep(1) #1 saniye delay
		
		x_tr = input(" lütfen isminizi girin:")
		time.sleep(0.5)
		print(" Bekleyin...")
		time.sleep(1.5)
		
		while True:
			
			print (" Merhaba", x_tr , ", lütfem sisteme giriş yapmak için devam yazın \n"  "                 yada \n"   " sistemden çıkmak için çıkış yazın --------------- \n")
			
			e_tr = input("-")
			
			time.sleep(0.5) #50 salise delay
			
			if (e_tr == "devam" or e_tr == "Devam"):
				time.sleep(0.5)
				print(" Hoşgeldin", x_tr)
				time.sleep(0.5)
				break

			elif (e_tr == "çıkış" or e_tr  == "Çıkış"):
				time.sleep(1)
				print(" Tamam! ")
				time.sleep(0.5)
				print (" sistem 3 saniye içinde kapanacak")
				time.sleep(0.5)
				print (" sistem 2 saniye içinde kapanacak")
				time.sleep(0.5)
				print (" sistem 1 saniye içinde kapanacak")
				time.sleep(0.5)
				print(" Hoşçakal")
				time.sleep(3)
				quit()
				break

			else:
				time.sleep
				print( "Hmm birşeyler yanlış gibi" )
				time.sleep(0.5)
				print("Lütfen Tekrar Deneyin                                                    ")
				time.sleep(1)
				continue

		time.sleep(1)

		print(" Tamam!", x_tr ," bir şifre şeç \n" + "en fazla 16 karakter ve 5 karakterden uzun olmalıdır. \n")
		time.sleep(0.9)
	
		while True:
			
			y_tr = input (" Güçlü bir şifre seç " + x_tr + ":")
			time.sleep(0.8)
			
			if (len(y_tr) < 4):
				print(" Oh hayır!" + " Çok kısa gibi gözüküyor.")
				time.sleep(0.7)
				print(" Lütfen tekrar dene")
				time.sleep(0.5)
				continue
	
			elif (len(y_tr) > 17):
				print(" Oh hayır!" + "Çok uzun gibi gözüküyor")
				time.sleep(0.7)
				print(" Lütfen tekrar dene")
				time.sleep(0.5)
				continue
		
			else:
				break

		
		yy_tr = input(" Lütfen şifreni onayla: ")
		time.sleep(1)
		
		if ( yy_tr == y_tr ):
			print(" Lütfen bekle...")
			time.sleep(1)
			print(" Giriş bilgilerin onaylanıyor...")
			time.sleep(0.5)
			print(" Lütfen bekle...") 
			time.sleep(2)
			print(" Tamamdır! Hazır!")
			time.sleep(1)
			print (" Şifre Onaylandı")
			time.sleep(3)
			print(" sistem sizi 3 saniye içerisinde satın alım bölümüne yönlendirecek")
			time.sleep(1)
			print(" sistem sizi 2 saniye içerisinde satın alım bölümüne yönlendirecek")
			time.sleep(1)
			print(" sistem sizi 1 saniye içerisinde satın alım bölümüne yönlendirecek ")
			time.sleep(2)
			print(" Opss! Birşeyler yanlış gitti :(")
			time.sleep(1.5)
			print(" Yardım ve destek için lütfen destek sayfamızı ziyaret edin.")
			time.sleep(1)
			print(" www.b&e-studios.net ")
			time.sleep(2)
			print(" sistem kapanıyor...")
			time.sleep(5)
			quit()

		else:
			print(" Giriş bilgilerin onaylanıyor... ")
			time.sleep(1)
			print(" Birşeyler yanlış gitti :( ")
			time.sleep(0.5)
			print (" sistem 3 saniye içinde kapanacak")
			time.sleep(0.5)
			print (" sistem 2 saniye içinde kapanacak")
			time.sleep(0.5)
			print (" sistem 1 saniye içinde kapanacak")
			time.sleep(0.5)
			print(" Hoşçakal")
			quit()
	 	
#------------	 	
	 	
	elif( d == "ENG" or d == "eng" or d == "Eng" or d == "ENg" or d == "eNG" or d == "eNg" or d == "enG" or d == "EnG" ):
		
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

	else:
		time.sleep(1.5)
		print(" Language could not found")
		time.sleep(4)
		continue