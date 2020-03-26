
import sys #POUR ARRTER LE PROGRAMME A UN NIVEAU BIEN SPECIFIQUE; Puis sys.exit(1) à ajouter au niveau ou l'on veut s'arreter

def ges_name():
	nom=str()
	prenom=str()
	nom=input("Comment vous appelez-vous?  ")
	prenom=input("Quel est votre prenom?  ")

	N=str(nom) 
	P=str(prenom)
	Vnom=nom.isalpha()
	Vprenom=prenom.isalpha()
		#isapha :booléenne Renvoie True si les caractères dans cette chaîne sont alphabétiques et il y a au moins un caractère
		#Vnom et Vprenom servent a la verification
		#print("votre nom compte",len(N),"caractere")
		#print("votre prenom compte",len(P),"caractere")

                         #Gérer le probleme de caractere à saisir 1/ caractere aphabetique 2/ longueur des caracteres
	if  Vnom==True and Vprenom==True :
		if(len(N)>10 or len(P)>10):
			print("Le nom et le prenom ne doivent pas exceder 10 caracteres")
			print("relancez le programme pour réessayer")
		if(len(N)<3 or len(P)<3):
			print("Le nom et le prenom doivent contenir plus de 3 caracteres")
			print("relancez le programme pour réessayer")
		else:
			print("Bienvenu à vous ",prenom,nom)
	else:
		print("veuillez entrer que des caracteres ALPHABETIQUE")
		print("relancez le programme pour réessayer")
		sys.exit(1)						
def cal_moy():
	note1=input("Entrer votre premiere note: "  )
	note2=input("Entrer votre seconde note: "  )
	note3=input("Entrer votre troisieme note: "  )
	Vnote1=note1.isdigit()
	Vnote2=note2.isdigit()
	Vnote3=note3.isdigit()
		#booléenne Renvoie True si cette chaîne ne contient que des caractères numériques.

	if  Vnote1==True and Vnote2==True and Vnote3==True :
		Total=float(note1)+float(note2)+float(note3)
		Moyenne=float(Total/3) #gerer les decimal avec un float
		print("votre moyenne est ",Moyenne)
		print("") 
	else:
		print("veuillez entrer que des caracteres NUMERIQUE")
		print("relancez le programme pour réessayer")
		sys.exit(1)

						#GESTION DES MENTIONS
							#Calcule arithmetique de la moyenne de 3 notes
"""def mention():
	if (Moyenne>=16):
		print("tres bon travail ",prenom,nom," Vous avez obtenu la mention TRES BIEN")
	elif(Moyenne>=14 and Moyenne<=16):
		print("bien travaillé mais vous pouvez faire mieux ",prenom,"Vous avez obtenu la mention BIEN")
	elif(Moyenne>=12 and Moyenne<=14):
		print("Pas mauvais mais vous devez redoubler d'éffort",prenom,"Vous avez obtenu la mention ASSEZ-BIEN")
	elif(Moyenne>=10 and Moyenne<=12):
		print("Rien n'est encore perdu, améliorez-vous et n'abandonnez pas",prenom,"Vous avez obtenu la mention PASSABLE")
	else:
		print("Ce n'est pas bon, vous devez vous remettre auy travail ",prenom,"Vous avez obtenu la mention FAIBLE")"""

def main():
	print("Calcule arithmetique de la moyenne de clase")
	print(ges_name())
	print(cal_moy())
	#print(mention())
if __name__ == '__main__':
	main()




