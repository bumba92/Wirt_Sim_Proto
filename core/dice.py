import random

def roll(Seiten, anzahl=1, modifikator=0):
    result = 0
    wurf = 0
    for i in range(anzahl):
        wurf = random.randint(1, Seiten)
        result = result + wurf
    result = result + modifikator
    return result 

# Testbereicht
if __name__ == "__main__":
    print("1W20:", roll(20))
    print(" 3W6:", roll(6, 3)) 
    print("2W8+5:", roll(8, 2, 5))