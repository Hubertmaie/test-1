#IDENTITE

oAge = str(input("Quel age avez vous ? "))
while not oAge.isdigit():
    print("Veuillez entrer un nombre entier")
    oAge = str(input("Quel age avez vous ? "))
#oAge = int(oAge)
#if oAge >=18:
#	print ("bravo")
#elif oAge <18:
#	print ("dommage")
#	
#oGenre = str(input ("Quel est votre genre ? H/F "))
#if oGenre == "H":
#	print ("Homme")
	