import openpyxl

wb = openpyxl.load_workbook("C:\\Users\\konhotom\\Desktop\\exemple.xlsx")
pages = wb.sheetnames
pg1 = wb['Fiche_de_paie']
data1 = pg1['E12'].value
data2 = pg1['F12'].value
salaire_brut = data1*data2
TAUX = int(input("A quel taux votre TVA est inscrite(1,2,3,4):"))
if TAUX == 1 :
    TVA = 0.2
elif TAUX == 2 :
    TVA = 0.1
elif TAUX == 3 :
    TVA = 0.055
elif TAUX == 4 :
    TVA = 0.021
TVA = TVA * salaire_brut
print("LA TVA vous retire:", TVA, "euro de votre salaire brut , votre salaire net est donc de :" ,salaire_brut - TVA , "euro")
