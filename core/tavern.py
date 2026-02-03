tav = {
    "name": "Prototype",
    "att_Arbeiter"  : 0, #Attraktivität für Arbeiter
    "att_Buerger"   : 0, #Attraktivität für Bürger
    "att_reich"     : 0, #Attraktivität für Reiche
    "att_adel"      : 0, #Attraktivität für Adel
    "plaetze"       : 0, #Plätze in der Taverne
    "pers_ungel": 0, #ungelerntes Personal
    "pers_geler": 0, #gelerntes Personal
    "pers_Profi": 0, #Professionelles Personal
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
from dice import roll


def calc_personal(taverne):
    kosten_ungel = taverne["pers_ungel"] * taverne["Lohn_ungel"]
    kosten_geler = taverne["pers_geler"] * taverne["Lohn_geler"]
    kosten_profi = taverne["pers_Profi"] * taverne["Lohn_Profi"]
    return kosten_geler + kosten_ungel + kosten_profi

def calc_gaeste(taverne):
    arbeiter = roll(6, 2) + taverne["att_Arbeiter"]
    buerger = roll(6, 1) + taverne["att_Buerger"]
    reich = roll(4, 1) + taverne["att_reich"]
    adel = roll(2, 1) + taverne["att_adel"]
    return arbeiter, buerger, reich, adel

def calc_income(taverne, gaeste):
    inc_arbeiter = gaeste[0]*taverne["Preis_Arbeiter"]
    inc_buerger = gaeste[1]*taverne["Preis_Arbeiter"]
    inc_reich = gaeste[2]*taverne["Preis_Reich"]
    inc_adel = gaeste[3]*taverne["Preis_Adel"]
    return inc_arbeiter + inc_buerger + inc_reich + inc_adel

tav["pers_geler"] = 3

gaeste = calc_gaeste(tav)
einnahmen = calc_income(tav,gaeste)
personalkosten = calc_personal(tav)
gewinn = einnahmen - personalkosten    
print("======TagesÜbersicht======")
print(f"Gäste:{gaeste[0]} Arbeiter, {gaeste[1]} Bürger, {gaeste[2]} Reiche, {gaeste[3]} Adelige")
print(f"Einnahmen: {einnahmen}")
print(f"Tagesgewinn: {gewinn}")
