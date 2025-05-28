#programmametodiDEFINITIVO

from pprint import pprint

with open("SONDAGGIOGIUSTO.csv", "r", encoding='utf-8') as f:
   
    righe = f.readlines()

    dati = []
    for riga in righe:
    
        colonne = riga.strip().split(",")
        
        dati.append(colonne)

#==========================================================

counterA = 0
counterB = 0
intersez = 0   
domanda = input("A quale domanda sei interessato? ")
domanda1 = input("A quale domanda vuoi confrontarlo? ")
risposta = input("Quale risposta stai cercando? ")
risposta1 = input("A cosa vuoi confrontarlo? ")

#==========================================================




'''if 'Quanti anni hai' or 'età' in domanda:
      domanda = 1
elif 'Dove vivi' in domanda:
      domanda = 2
elif 'Se vivi in Italia, in che parte di essa vivi' in domanda:
        domanda = 3
elif 'Quanto è grande il comune in cui vivi' or 'comune' in domanda:
        domanda = 4
elif "Quanto reputi importante la cura dell'ambiente circostante" or 'ambiente' in domanda:
        domanda = 5
elif "Qual è il tuo genere" or 'genere' in domanda:
        domanda = 6
elif 'Qual è la tua occupazione?' or 'occupazione' or 'lavoro' in domanda:
        domanda = 7
elif 'Se necessiti di fare un pagamento di 20 euro per un qualunque servizio come preferisci pagare?' or 'preferenza' in domanda:
        domanda = 8
elif 'Se preferisci pagare via carta perché?' or 'carta' in domanda:
        domanda = 9 
elif 'Se invece la tua preferenza è il contante perché?' or 'contante' in domanda:
        domanda = 10
elif 'Quante volte al mese mediamente prelevi denaro?' or 'frequenza' in domanda:
        domanda = 11
elif 'Quanto è lontano il punto in cui prelievi più spesso?' or 'distanza' in domanda:
        domanda = 12
elif 'Che mezzo usi per andare a prelevare?' or 'mezzo' in domanda:
        domanda = 13'''

#========================================================================================
for i in range(len(dati[0])):
        if domanda in dati[0][i]:
                domanda = i
for i in range(len(dati)):
        domanda = int(domanda)
        domanda1 = int(domanda1)
        if dati[i][domanda1] == risposta1:
                counterB += 1 ##funziona 
                if dati[i][domanda] == risposta and dati[i][domanda1] == risposta1:
                        intersez += 1
                
        else:
                domanda = int(domanda)
                if dati[i][domanda] == risposta:
                        counterA += 1
                # A piedi/Bicicletta   
               

print("La prob condizionata è : ", intersez/(counterB), 'la prob di b è:', counterB)
