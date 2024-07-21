import random
import time

atis_sayi = 0
cem1 = 0
cem2 = 0

def pl1():
    print("Player1 oynayir: \n")
    global cem1
    player1 = random.randint(1,6)
    player1_2ci_zer = random.randint(1,6)
    
    
    print_dice(player1)
    print_dice(player1_2ci_zer)
    
    cem1 += player1 + player1_2ci_zer 
    print(f"Player 1 rolls: {player1} and {player1_2ci_zer} - Total score: {cem1}")
    time.sleep(1)
    return cem1

def pl2():
    print("Player2 oynayir: \n")
    global cem2
    player2 = random.randint(1,6)
    player2_2ci_zer = random.randint(1,6)
    
    
    print_dice(player2)
    print_dice(player2_2ci_zer)
    
    cem2 += player2 + player2_2ci_zer  
    print(f"Player 2 rolls: {player2} and {player2_2ci_zer} - Total score: {cem2}")
    time.sleep(1)
    return cem2

def print_dice(value):
    if value == 1:
        print(" -----------")
        print("|           |")          
        print("|           |")
        print("|     *     |")
        print("|           |")
        print("|           |")
        print("|           |")
        print(" -----------")
    elif value == 2:
        print(" -----------")
        print("|           |")          
        print("|           |")
        print("|     *     |")
        print("|       *   |")
        print("|           |")
        print("|           |")
        print(" -----------")
    elif value == 3:
        print(" -----------")
        print("|           |")          
        print("|           |")
        print("|   *       |")
        print("|     *     |")
        print("|       *   |")
        print("|           |")
        print(" -----------")
    elif value == 4:
        print(" -----------")
        print("|           |")          
        print("|   *   *   |")
        print("|           |")
        print("|   *   *   |")
        print("|           |")
        print("|           |")
        print(" -----------")
    elif value == 5:
        print(" -----------")
        print("|           |")          
        print("|   *   *   |")
        print("|     *     |")
        print("|   *   *   |")
        print("|           |")
        print("|           |")
        print(" -----------")
    elif value == 6:
        print(" -----------")
        print("|           |")          
        print("|   *   *   |")
        print("|           |")
        print("|   *   *   |")
        print("|           |")
        print("|   *   *   |")
        print(" -----------")

def oyun():
    global atis_sayi, cem1, cem2

    while atis_sayi < 5:
        pl1()
        time.sleep(1)
        pl2()
        atis_sayi += 1

    if cem1 > cem2:
        print(f"1ci oyuncu {cem1} xali var, 2ci oyuncunun ise {cem2} xali var, ona gorede 1ci oyuncu qazandi")
    elif cem2 > cem1:
        print(f"1ci oyuncunun {cem1} xali var, buna gorede 2ci oyuncu {cem2} xali ile oyunu udur")
    else:
        print(f"Her iki oyuncunun {cem1} xali var, oyun berabere bitdi")

oyun()
