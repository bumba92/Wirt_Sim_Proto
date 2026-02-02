tav = {
    "name": "Prototype",
    "att_Arbeiter"  : 0, #Attraktivität für Arbeiter
    "att_Buerger"   : 0, #Attraktivität für Bürger
    "att_reich"     : 0, #Attraktivität für Reiche
    "att_adel"      : 0, #Attraktivität für Adel
    "plaetze"       : 0, #Plätze in der Taverne
    "pers_ungel": 0, #ungelerntes Personal
    "pers_geler": 0, #gelerntes Personal
    "Pers_Profi": 0, #Professionelles Personal
    "Lohn_ungel"    : 0.2, # Gehalt ungelerntes Personal pro Tag
    "Lohn_geler"    : 1.0,# Gehalt für gelerntes Personal
    "Lohn_Profi"    : 2.0, # Gehalt für Profis
    "Steuern"       : 0.0, #Steuern in % vom Gewinn
    "Kosten_Getrae" : 0.0, #Kosten Getränkt pro Tag
    "Kosten_Essen"  : 0.0, #Kosten Essen pro tag
    "Preis_Arbeiter": 0.25, #Preis für einfaches Essen & Trinken
    "Preis_Buerger" : 0.5,  #Preis für mittleres Essen und Getränke
    "Preis_Reich"   : 1.0,  #Preis für gutes Essen und Trinken
    "Preis_Adel"    : 2.0  #Preis für nobles Essen und Getränke

}

def calc_personal(taverne):
    kosten_ungel = taverne["Pers_ungel"] * taverne["Lohn_ungel"]
    kosten_geler = taverne["Pers_geler"] * taverne["Lohn_geler"]
    kosten_profi = taverne["Pers_Profi"] * taverne["Lohn_Profi"]
    return kosten_geler + kosten_ungel + kosten_profi


tav["Pers_ungel"] = 5
tav["Pers_geler"] = 2
tav["Pers_Profi"] = 0

print("Personalkosten: ",calc_personal(tav))
