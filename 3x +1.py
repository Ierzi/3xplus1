# 3x +1!

seed = 0

# Commande
def main(nombre):
    if (nombre % 2) == 0:
        # Ce nombre est pair
        nombre = nombre / 2
    elif (nombre % 2) == 1:
        # Ce nombre n'est pas pair
        nombre = nombre * 3 + 1
    return nombre


while True:
    seed = seed + 1

    number = seed
    


    while number != 1:
        number = main(number)
        
        
    
    if number == 1:
        print(seed, "ne marche pas")
    