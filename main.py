import random
import time

def win():
    print "YOU SAVED THE VILLAGE! THEY THANK YOU AND GIVE YOU A COW AS A REWARD..."

def gameOver():
    print "GAME OVER, YOU LOSE, FOOL"
    retry = raw_input("\n\nWant to try again? (y/n)\n\n").lower()
    if retry == "y":
        game()
    else:
        quit()

def game():

    gold = 30
    character_hp = 100
    weapon_damage = 5
    monster_damage = 15
    monster_payout = 25
    armors = [""]
    weapons = ["fists"]

    MONSTERS = {
        "goblin":50,
        "draugr":75,
        "wolf":100,
        "dragon":150,
        }

    name = raw_input("\nWhat is your name?\n\n").title()

    while name == "":
        name = raw_input("\nWhat is your name?\n\n").title()

    print "\nWelcome", name, ", Enjoy Your Adventure!\n"


    WEAPONS_STORE={
        "sword":70,
        "axe":60, 
        "mace":37, 
        "dagger":22
    }
    
    ARMOR_STORE={
        "shoes":40,
        "armor":55,
        "gloves":45,
        "helmet":50,
        "shield":60
    }
    '''weapons'''
    store = raw_input("\nDo you want to buy weapons? (y/n)\n\n").lower()

    if store == "y":
        print "\nWEAPON\t\tCOST\n"

        for items in WEAPONS_STORE:
            print items, "\t\t", WEAPONS_STORE[items], "\n"

        print "\nYou have", gold, "gold\n\n"
        weapon_purchase = raw_input("Which weapon would you like to buy?\n\n").lower()
        
        while weapon_purchase not in WEAPONS_STORE or weapon_purchase in weapons:
            weapon_purchase = raw_input("Which weapon would you like to buy?\n\n").lower()

        if weapon_purchase in WEAPONS_STORE and weapon_purchase not in weapons:

            if gold >= WEAPONS_STORE[weapon_purchase]:
                print "you bought a(n)", weapon_purchase, "\n"
                gold -= WEAPONS_STORE[weapon_purchase]
                weapons.append(weapon_purchase)
                print "\nyou have", gold, "gold\n"
                print "\nWeapons(s) you own\n"
                for items in weapons:
                    print items 

            elif gold <= WEAPONS_STORE[weapon_purchase]:
                print "not enough gold"
    
        elif store == "n":
            print "time to buy armor"
        

    '''armor'''
    shop = raw_input("\nDo you want to buy armor?(y or n)\n\n").lower()
    
    if shop == "y":
        print "\nARMOR\t\tCOST\t\n"

    for items in ARMOR_STORE:
        print items, "\t\t", ARMOR_STORE[items], "\n"

    print "\nYou have", gold, "gold\n\n"
    armor_purchase = raw_input("What armor would you like to buy?\n\n").lower()

    while armor_purchase in ARMOR_STORE and armor_purchase not in armors:

        if gold >= ARMOR_STORE[armor_purchase]:
            print "you bouht a(n)", armor_purchase, "\n"
            gold -= ARMOR_STORE[armor_purchase]
            armors.append(armor_purchase)
            print "\nyou have", gold, "gold\n"
            print "\nArmor you own\n"
            for items in armors:
                print items

        elif gold <= ARMOR_STORE[armor_purchase]:
            print "not enough gold"
            
        print "\nYour armor is now", armors,"\n"
    
    if shop == "n":

        print "\nTime to destroy a monster from the village!\n\n"
        print "\nMONSTERS\tHEALTH\t\n\n"
        
    for monster in MONSTERS:
            print monster, "\t\t", MONSTERS[monster], "\n"

    monchoice = raw_input("Which Monster do you want to fight?\n\n").lower()
        
    if monchoice in MONSTERS:

          print "\n Good Luck! Banish the", monchoice, "from the village"

    else:

         print "That monster is not in the village"

    while monchoice not in MONSTERS:
                
        monchoice = raw_input("Which Monster do you want to fight?\n\n").lower()

    print "\nWEAPONS YOU OWN\n"

    for weapon in weapons:

          print weapon, "\n"

    weapuse = raw_input("Which weapon would you like to use?\n\n" ).lower()

    if weapuse in weapons:

         print "\nWise choice", name, "You shall use the", weapuse,".", monchoice, "shall not pass"

         if weapuse == "fists":

               while character_hp > 0 and MONSTERS[monchoice] > 0:
                 rand = random.randint(3, 7)
                 pdmg = weapon_damage + rand
                 mdmg = monster_damage
                 if shoes in armor:
                     mdmg -= 2
                 if armor in armor:
                     mdmg -= 4
                 if gloves in armor:
                     mdmg -= 2
                 if helmet in armor:
                     mdmg -= 3
                 if shield in armor:
                     mdmg -= 3
                 print monchoice, "has", MONSTERS[monchoice], "health lef\n\n"
                 time.sleep(1.5)
                 print "The", monchoice, "attacked you by", mdmg
                 character_hp -= mdmg
                 if character_hp <= 0:
                    gameOver()

                 print name,", your health is now", character_hp
                 time.sleep(1.5)            

                 print "\n You attacked the", monchoice, "with the", weapuse, "for", pdmg, "damage!"
                 MONSTERS[monchoice] -= pdmg
                 time.sleep(1.5)
                    

                 print monchoice, "has", MONSTERS[monchoice], "health left\n\n"
                 time.sleep(1.5)

         elif weapuse == "dagger":

               while character_hp > 0 and MONSTERS[monchoice] > 0:
                 rand = random.randint(4, 8)
                 pdmg = weapon_damage + rand
                 mdmg = monster_damage
                 if shoes in armor:
                     mdmg -= 2
                 if armor in armor:
                     mdmg -= 4
                 if gloves in armor:
                     mdmg -= 2
                 if helmet in armor:
                     mdmg -= 3
                 if shield in armor:
                     mdmg -= 3
                 character_hp -= mdmg
                 print monchoice, "has", MONSTERS[monchoice], "health lef\n\n"
                 time.sleep(1.5)
                 print "The", monchoice, "attacked you by", mdmg
                 character_hp -= mdmg
                 if character_hp <= 0:
                    gameOver()

                 print name,", your health is now", character_hp
                 time.sleep(1.5)            

                 print "\n You attacked the", monchoice, "with the", weapuse, "for", pdmg, "damage!"
                 MONSTERS[monchoice] -= pdmg
                 time.sleep(1.5)
                        

                 print monchoice, "has", MONSTERS[monchoice], "health left\n\n"
                 time.sleep(1.5)

         elif weapuse == "mace":

            while character_hp > 0 and MONSTERS[monchoice] > 0:
                rand = random.randint(9, 17)
                pdmg = weapon_damage + rand
                mdmg = monster_damage
                if shoes in armor:
                     mdmg -= 2
                if armor in armor:
                     mdmg -= 4
                if gloves in armor:
                     mdmg -= 2
                if helmet in armor:
                     mdmg -= 3
                if shield in armor:
                     mdmg -= 3
                character_hp -= mdmg
                print monchoice, "has", MONSTERS[monchoice], "health lef\n\n"
                time.sleep(1.5)
                print "The", monchoice, "attacked you by", mdmg
                character_hp -= mdmg
                if character_hp <= 0:
                    gameOver()

                print name,", your health is now", character_hp
                time.sleep(1.5)            

                print "\n You attacked the", monchoice, "with the", weapuse, "for", pdmg, "damage!"
                MONSTERS[monchoice] -= pdmg
                time.sleep(1.5)
                    

                print monchoice, "has", MONSTERS[monchoice], "health left\n\n"
                time.sleep(1.5)
                
                  

         elif weapuse == "axe":

            while character_hp > 0 and MONSTERS[monchoice] > 0:
                rand = random.randint(10, 20)
                pdmg = weapon_damage + rand
                mdmg = monster_damage
                if shoes in armor:
                     mdmg -= 2
                if armor in armor:
                     mdmg -= 4
                if gloves in armor:
                     mdmg -= 2
                if helmet in armor:
                     mdmg -= 3
                if shield in armor:
                     mdmg -= 3
                character_hp -= mdmg
                print monchoice, "has", MONSTERS[monchoice], "health lef\n\n"
                time.sleep(1.5)
                print "The", monchoice, "attacked you by", mdmg
                character_hp -= mdmg
                if character_hp <= 0:
                    gameOver()

                print name,", your health is now", character_hp
                time.sleep(1.5)            

                print "\n You attacked the", monchoice, "with the", weapuse, "for", pdmg, "damage!"
                MONSTERS[monchoice] -= pdmg
                time.sleep(1.5)
                    

                print monchoice, "has", MONSTERS[monchoice], "health left\n\n"
                time.sleep(1.5)

         elif weapuse == "sword":

            while character_hp > 0 and MONSTERS[monchoice] > 0:
                rand = random.randint(15, 23)
                pdmg = weapon_damage + rand
                mdmg = monster_damage
                if shoes in armor:
                     mdmg -= 2
                if armor in armor:
                     mdmg -= 4
                if gloves in armor:
                     mdmg -= 2
                if helmet in armor:
                     mdmg -= 3
                if shield in armor:
                     mdmg -= 3
                character_hp -= mdmg
                print monchoice, "has", MONSTERS[monchoice], "health left\n\n"
                time.sleep(1.5)
                print "The", monchoice, "attacked you by", mdmg
                character_hp -= mdmg
                if character_hp <= 0:
                    gameOver()

                print name,", your health is now", character_hp
                time.sleep(1.5)            

                print "\n You attacked the", monchoice, "with the", weapuse, "for", pdmg, "damage!"
                MONSTERS[monchoice] -= pdmg
                time.sleep(1.5)
                   

                print monchoice, "has", MONSTERS[monchoice], "health left\n\n"
                time.sleep(1.5)

         else:

            print name, "\nYou don't own the,", weapuse, "fool"

            while weapuse not in weapons:
             
                weapuse = raw_input("\nWhat weapon will you use?\n\n").lower()
                print "\nWise choice", name, "you will use the", weapuse, "agains the", monchoice
    
                if MONSTERS[monchoice] <= 0:
                    print "\nThe", monchoice, "has been destroyed, good work", name,"!"
                    character_hp == 100
                    gold += monster_payout
                    print "\nYou Have", gold, "gold\n"
                if monChoice == "Dragon":
                    win()
                del MONSTERS[monchoice]

                  
game()