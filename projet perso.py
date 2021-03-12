salaire = float(input("Entrer votre salaire mensuel:"))
print("1 = TAUX normal")
print("2 = TAUX intermédiare ")
print("3 = TAUX réduit ")
print("2 = TAUX super réduit ")
TAUX = int(input("A quel taux votre TVA est inscrite(1,2,3,4):"))
if TAUX == 1 :
    TVA = 0.2
elif TAUX == 2 :
    TVA = 0.1
elif TAUX == 3 :
    TVA = 0.055
elif TAUX == 4 :
    TVA = 0.021
TVA = TVA * salaire
print("LA TVA vous retire:", TVA, "euro de votre salaire brut , votre salaire net est donc de :" ,salaire - TVA , "euro")