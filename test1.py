#IDENTITE 1

oAge = raw_input("Quel age avez vous ? ")
while not oAge.isdigit():
    print("Veuillez entrer un nombre entier")
    oAge = raw_input("Quel age avez vous ? ")
oAge = int(oAge)
if oAge >=18:

	oGenre = raw_input ("Quel est votre genre ? H/F ")
	if oGenre == str("H"):
		print ("Homme")
	elif oGenre == str("F"):
		print ("Femme")
	elif oGenre != str("H") + oGenre != str("F"):
		print ("erreur")

elif oAge <18:
	print ("dommage")

