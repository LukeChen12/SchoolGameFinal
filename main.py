#Test file: WORK IN PROGRESS    
from graphics import *
from functions import *
from functions_ai import *
from copy import *
#Importing important functions for the game

import time
import random
 
run_times = 0
#Accumulator that tracks how many times the while True loop runs
ship_box = (45, 22) 
#Dimentions for the hit-box for the ships

objects_list = []
#List of objects (representing the ships/missles created from classes)
objects_list_org = {}
#Organized dictionary of objects paired with each respective image

player_ships_list = []
enemy_ships_list = []
#List of objects for player and enmey ships (Equivilant of specalized objects_list)

player_missle_list = []
enemy_missle_list = []
#List of objects for player and enemy missles (Equvilant of specalized objects_list for missles)

timer_missle = 0
timer_airstrike = 0
strikeing = False
strikeing_target = Point(0, 0)
small_circle = Circle(Point(0,0), 0)
small_warning = Point(0, 0)
#Timer for the ai missles and ai airstrikes

#####################################################
def main_mechanics(win, win_box, level_number, airstrikes_yes_no, time_wait, time_wait_between, target_hit_size, damage, objects_list, objects_list_org, player_ships_list, enemy_ships_list, player_missle_list, enemy_missle_list, timer_missle, moveing_amount_time_ships):
    global run_times#, objects_list, objects_list_org, player_ships_list, enemy_ships_list, player_missle_list, enemy_missle_list, timer_missle
    while True:
    #Loop that goes on for the entire game 
        if run_times < 1:
        #Check to see if the game has run for less then 1 time, the following code is only run once, needs to set up ships/window  
            timer_airstrike = 0
            strikeing = False
            strikeing_target = Point(0, 0)
            small_circle = Circle(Point(0,0), 0)
            small_warning = Point(0, 0)
            strikeing_list = []
            #Simple setting variables for the ai Airstrike function


            if level_number == 1:
            #Ships set up for the first level
                player_bat_1 = Battleships(100, 315, 60, 8, 0, 0, 0, 0, 0, 0, 1, 101)
                player_bat_01 = Image(Point(player_bat_1.x, player_bat_1.y), "battleshipblueicon.gif")

                player_car_1 = Carriers(player_bat_1.x + 40, player_bat_1.y + 40, 0, 0, 0, 0, 0, 0, 2, 103)
                player_car_01 = Image(Point(player_car_1.x, player_car_1.y), "carrierblueicon.gif")
                #Setting up player ship objects from classes
                ##########################################################
                player_bat_01.draw(win)
                objects_list.append(player_bat_1)
                objects_list_org[player_bat_1] = player_bat_01
                player_ships_list.append(player_bat_1)
                ##########################################################
                player_car_01.draw(win)
                objects_list.append(player_car_1)
                objects_list_org[player_car_1] = player_car_01
                player_ships_list.append(player_car_1)
                ##########################################################
                #Drawing up player ships and adding them to lists of objects


                enenmy_bat_1 = Battleships(900, 210, 100, 8, 0, 0, 0, 0, 0, 0, 3, 201)
                enenmy_bat_01 = Image(Point(enenmy_bat_1.x, enenmy_bat_1.y), "battleshipredicon.gif")

                enenmy_bat_2 = Battleships(900, 420, 100, 8, 0, 0, 0, 0, 0, 0, 3, 202)
                enenmy_bat_02 = Image(Point(enenmy_bat_2.x, enenmy_bat_2.y), "battleshipredicon.gif")
                #Setting up enemy ships as classes
                ##########################################################
                enenmy_bat_01.draw(win)
                objects_list.append(enenmy_bat_1)
                objects_list_org[enenmy_bat_1] = enenmy_bat_01
                enemy_ships_list.append(enenmy_bat_1)
                ##########################################################
                enenmy_bat_02.draw(win)
                objects_list.append(enenmy_bat_2)
                objects_list_org[enenmy_bat_2] = enenmy_bat_02
                enemy_ships_list.append(enenmy_bat_2)
                ##########################################################
                #Drawing up enemy ships



            elif level_number == 2:
            #Ships set up for the second level
                player_bat_1 = Battleships(100, 315, 80, 8, 0, 0, 0, 0, 0, 0, 1, 101)
                player_bat_01 = Image(Point(player_bat_1.x, player_bat_1.y), "battleshipblueicon.gif")

                player_car_1 = Carriers(player_bat_1.x + 40, player_bat_1.y + 40, 0, 0, 0, 0, 0, 0, 2, 103)
                player_car_01 = Image(Point(player_car_1.x, player_car_1.y), "carrierblueicon.gif")
                #Setting up player ship objects from classes
                ##########################################################
                player_bat_01.draw(win)
                objects_list.append(player_bat_1)
                objects_list_org[player_bat_1] = player_bat_01
                player_ships_list.append(player_bat_1)
                ##########################################################
                player_car_01.draw(win)
                objects_list.append(player_car_1)
                objects_list_org[player_car_1] = player_car_01
                player_ships_list.append(player_car_1)
                ##########################################################
                #Drawing up player ships and adding them to lists of objects


                enenmy_bat_1 = Battleships(900, 315, 120, 8, 0, 0, 0, 0, 0, 0, 3, 201)
                enenmy_bat_01 = Image(Point(enenmy_bat_1.x, enenmy_bat_1.y), "battleshipredicon.gif")

                enenmy_car_1 = Carriers(enenmy_bat_1.x + 40, enenmy_bat_1.y + 100, 0, 0, 0, 0, 0, 0, 4, 203)
                enenmy_car_01 = Image(Point(enenmy_car_1.x, enenmy_car_1.y), "carrierredicon.gif")
                #Setting up enemy ships as classes
                ##########################################################
                enenmy_bat_01.draw(win)
                objects_list.append(enenmy_bat_1)
                objects_list_org[enenmy_bat_1] = enenmy_bat_01
                enemy_ships_list.append(enenmy_bat_1)
                ##########################################################
                enenmy_car_01.draw(win)
                objects_list.append(enenmy_car_1)
                objects_list_org[enenmy_car_1] = enenmy_car_01
                enemy_ships_list.append(enenmy_car_1)
                ##########################################################
                #Drawing up enemy ships



            elif level_number == 3:
            #Ships set up for the third level
                player_bat_1 = Battleships(100, 210, 100, 8, 0, 0, 0, 0, 0, 0, 1, 101)
                player_bat_01 = Image(Point(player_bat_1.x, player_bat_1.y), "battleshipblueicon.gif")

                player_bat_2 = Battleships(100, 420, 100, 8, 0, 0, 0, 0, 0, 0, 1, 102)
                player_bat_02 = Image(Point(player_bat_2.x, player_bat_2.y), "battleshipblueicon.gif")

                player_car_1 = Carriers(player_bat_1.x + 40, player_bat_1.y + 40, 0, 0, 0, 0, 0, 0, 2, 103)
                player_car_01 = Image(Point(player_car_1.x, player_car_1.y), "carrierblueicon.gif")

                #Setting up player ship objects from classes
                ##########################################################
                player_bat_01.draw(win)
                objects_list.append(player_bat_1)
                objects_list_org[player_bat_1] = player_bat_01
                player_ships_list.append(player_bat_1)
                ##########################################################
                player_bat_02.draw(win)
                objects_list.append(player_bat_2)
                objects_list_org[player_bat_2] = player_bat_02
                player_ships_list.append(player_bat_2)
                ##########################################################
                player_car_01.draw(win)
                objects_list.append(player_car_1)
                objects_list_org[player_car_1] = player_car_01
                player_ships_list.append(player_car_1)
                ##########################################################
                #Drawing up player ships and adding them to lists of objects


                enenmy_bat_1 = Battleships(900, 210, 140, 8, 0, 0, 0, 0, 0, 0, 3, 201)
                enenmy_bat_01 = Image(Point(enenmy_bat_1.x, enenmy_bat_1.y), "battleshipredicon.gif")

                enenmy_bat_2 = Battleships(900, 420, 140, 8, 0, 0, 0, 0, 0, 0, 3, 202)
                enenmy_bat_02 = Image(Point(enenmy_bat_2.x, enenmy_bat_2.y), "battleshipredicon.gif")

                enenmy_car_1 = Carriers(enenmy_bat_1.x + 40, enenmy_bat_1.y + 100, 0, 0, 0, 0, 0, 0, 4, 203)
                enenmy_car_01 = Image(Point(enenmy_car_1.x, enenmy_car_1.y), "carrierredicon.gif")
                #Setting up enemy ships as classes
                ##########################################################
                enenmy_bat_01.draw(win)
                objects_list.append(enenmy_bat_1)
                objects_list_org[enenmy_bat_1] = enenmy_bat_01
                enemy_ships_list.append(enenmy_bat_1)
                ##########################################################
                enenmy_bat_02.draw(win)
                objects_list.append(enenmy_bat_2)
                objects_list_org[enenmy_bat_2] = enenmy_bat_02
                enemy_ships_list.append(enenmy_bat_2)
                ##########################################################
                enenmy_car_01.draw(win)
                objects_list.append(enenmy_car_1)
                objects_list_org[enenmy_car_1] = enenmy_car_01
                enemy_ships_list.append(enenmy_car_1)
                ##########################################################
                #Drawing up enemy ships



            elif level_number == 4:
            #Ships set up for the fourth level
                player_bat_1 = Battleships(100, 210, 120, 8, 0, 0, 0, 0, 0, 0, 1, 101)
                player_bat_01 = Image(Point(player_bat_1.x, player_bat_1.y), "battleshipblueicon.gif")

                player_bat_2 = Battleships(100, 420, 120, 8, 0, 0, 0, 0, 0, 0, 1, 102)
                player_bat_02 = Image(Point(player_bat_2.x, player_bat_2.y), "battleshipblueicon.gif")

                player_car_1 = Carriers(player_bat_1.x + 40, player_bat_1.y + 40, 0, 0, 0, 0, 0, 0, 2, 103)
                player_car_01 = Image(Point(player_car_1.x, player_car_1.y), "carrierblueicon.gif")

                #Setting up player ship objects from classes
                ##########################################################
                player_bat_01.draw(win)
                objects_list.append(player_bat_1)
                objects_list_org[player_bat_1] = player_bat_01
                player_ships_list.append(player_bat_1)
                ##########################################################
                player_bat_02.draw(win)
                objects_list.append(player_bat_2)
                objects_list_org[player_bat_2] = player_bat_02
                player_ships_list.append(player_bat_2)
                ##########################################################
                player_car_01.draw(win)
                objects_list.append(player_car_1)
                objects_list_org[player_car_1] = player_car_01
                player_ships_list.append(player_car_1)
                ##########################################################
                #Drawing up player ships and adding them to lists of objects


                enenmy_bat_1 = Battleships(900, 210, 160, 8, 0, 0, 0, 0, 0, 0, 3, 201)
                enenmy_bat_01 = Image(Point(enenmy_bat_1.x, enenmy_bat_1.y), "battleshipredicon.gif")

                enenmy_bat_2 = Battleships(900, 420, 160, 8, 0, 0, 0, 0, 0, 0, 3, 202)
                enenmy_bat_02 = Image(Point(enenmy_bat_2.x, enenmy_bat_2.y), "battleshipredicon.gif")

                enenmy_car_1 = Carriers(enenmy_bat_1.x + 40, enenmy_bat_1.y + 100, 0, 0, 0, 0, 0, 0, 4, 203)
                enenmy_car_01 = Image(Point(enenmy_car_1.x, enenmy_car_1.y), "carrierredicon.gif")

                enenmy_car_2 = Carriers(enenmy_bat_2.x + 40, enenmy_bat_2.y + 100, 0, 0, 0, 0, 0, 0, 4, 204)
                enenmy_car_02 = Image(Point(enenmy_car_2.x, enenmy_car_2.y), "carrierredicon.gif")
                #Setting up enemy ships as classes
                ##########################################################
                enenmy_bat_01.draw(win)
                objects_list.append(enenmy_bat_1)
                objects_list_org[enenmy_bat_1] = enenmy_bat_01
                enemy_ships_list.append(enenmy_bat_1)
                ##########################################################
                enenmy_bat_02.draw(win)
                objects_list.append(enenmy_bat_2)
                objects_list_org[enenmy_bat_2] = enenmy_bat_02
                enemy_ships_list.append(enenmy_bat_2)
                ##########################################################
                enenmy_car_01.draw(win)
                objects_list.append(enenmy_car_1)
                objects_list_org[enenmy_car_1] = enenmy_car_01
                enemy_ships_list.append(enenmy_car_1)
                ##########################################################
                enenmy_car_02.draw(win)
                objects_list.append(enenmy_car_2)
                objects_list_org[enenmy_car_2] = enenmy_car_02
                enemy_ships_list.append(enenmy_car_2)
                ##########################################################
                #Drawing up enemy ships
                


            elif level_number == 5:
            #Ships set up for the fourth level
                player_bat_1 = Battleships(100, 210, 120, 8, 0, 0, 0, 0, 0, 0, 1, 101)
                player_bat_01 = Image(Point(player_bat_1.x, player_bat_1.y), "battleshipblueicon.gif")

                player_bat_2 = Battleships(100, 420, 120, 8, 0, 0, 0, 0, 0, 0, 1, 102)
                player_bat_02 = Image(Point(player_bat_2.x, player_bat_2.y), "battleshipblueicon.gif")

                player_car_1 = Carriers(player_bat_1.x + 40, player_bat_1.y + 40, 0, 0, 0, 0, 0, 0, 2, 103)
                player_car_01 = Image(Point(player_car_1.x, player_car_1.y), "carrierblueicon.gif")

                player_car_2 = Carriers(player_bat_2.x + 40, player_bat_2.y + 40, 0, 0, 0, 0, 0, 0, 2, 103)
                player_car_02 = Image(Point(player_car_2.x, player_car_2.y), "carrierblueicon.gif")

                #Setting up player ship objects from classes
                ##########################################################
                player_bat_01.draw(win)
                objects_list.append(player_bat_1)
                objects_list_org[player_bat_1] = player_bat_01
                player_ships_list.append(player_bat_1)
                ##########################################################
                player_bat_02.draw(win)
                objects_list.append(player_bat_2)
                objects_list_org[player_bat_2] = player_bat_02
                player_ships_list.append(player_bat_2)
                ##########################################################
                player_car_01.draw(win)
                objects_list.append(player_car_1)
                objects_list_org[player_car_1] = player_car_01
                player_ships_list.append(player_car_1)
                ##########################################################
                player_car_02.draw(win)
                objects_list.append(player_car_2)
                objects_list_org[player_car_2] = player_car_02
                player_ships_list.append(player_car_2)
                ##########################################################
                #Drawing up player ships and adding them to lists of objects


                enenmy_bat_1 = Battleships(900, 126, 160, 8, 0, 0, 0, 0, 0, 0, 3, 201)
                enenmy_bat_01 = Image(Point(enenmy_bat_1.x, enenmy_bat_1.y), "battleshipredicon.gif")

                enenmy_bat_2 = Battleships(900, 252, 160, 8, 0, 0, 0, 0, 0, 0, 3, 202)
                enenmy_bat_02 = Image(Point(enenmy_bat_2.x, enenmy_bat_2.y), "battleshipredicon.gif")

                enenmy_bat_3 = Battleships(900, 378, 160, 8, 0, 0, 0, 0, 0, 0, 3, 202)
                enenmy_bat_03 = Image(Point(enenmy_bat_3.x, enenmy_bat_3.y), "battleshipredicon.gif")

                enenmy_bat_4 = Battleships(900, 504, 160, 8, 0, 0, 0, 0, 0, 0, 3, 202)
                enenmy_bat_04 = Image(Point(enenmy_bat_4.x, enenmy_bat_4.y), "battleshipredicon.gif")

                enenmy_car_1 = Carriers(enenmy_bat_1.x + 40, enenmy_bat_1.y + 100, 0, 0, 0, 0, 0, 0, 4, 203)
                enenmy_car_01 = Image(Point(enenmy_car_1.x, enenmy_car_1.y), "carrierredicon.gif")

                enenmy_car_2 = Carriers(enenmy_bat_2.x + 40, enenmy_bat_2.y + 100, 0, 0, 0, 0, 0, 0, 4, 204)
                enenmy_car_02 = Image(Point(enenmy_car_2.x, enenmy_car_2.y), "carrierredicon.gif")
                #Setting up enemy ships as classes
                ##########################################################
                enenmy_bat_01.draw(win)
                objects_list.append(enenmy_bat_1)
                objects_list_org[enenmy_bat_1] = enenmy_bat_01
                enemy_ships_list.append(enenmy_bat_1)
                ##########################################################
                enenmy_bat_02.draw(win)
                objects_list.append(enenmy_bat_2)
                objects_list_org[enenmy_bat_2] = enenmy_bat_02
                enemy_ships_list.append(enenmy_bat_2)
                ##########################################################
                enenmy_bat_03.draw(win)
                objects_list.append(enenmy_bat_3)
                objects_list_org[enenmy_bat_3] = enenmy_bat_03
                enemy_ships_list.append(enenmy_bat_3)
                ##########################################################
                enenmy_bat_04.draw(win)
                objects_list.append(enenmy_bat_4)
                objects_list_org[enenmy_bat_4] = enenmy_bat_04
                enemy_ships_list.append(enenmy_bat_4)
                ##########################################################
                enenmy_car_01.draw(win)
                objects_list.append(enenmy_car_1)
                objects_list_org[enenmy_car_1] = enenmy_car_01
                enemy_ships_list.append(enenmy_car_1)
                ##########################################################
                enenmy_car_02.draw(win)
                objects_list.append(enenmy_car_2)
                objects_list_org[enenmy_car_2] = enenmy_car_02
                enemy_ships_list.append(enenmy_car_2)
                ##########################################################
                #Drawing up enemy ships
            elif level_number == 1000:
                pass
            else:
                break
            #This is specifcally if the function manages to get 0 ships of any kind inputed. If so, then just immediately switch back to menu.
            
            if level_number != 1000:
                level_number_display = Text(Point(50, 24), str("Level: " + str(level_number)))
                level_number_display.draw(win)
                level_number_display.setTextColor("white")
                level_number_display.setStyle("bold")
                level_number_display.setSize(18)
            #Assumeing that code imputs a level that has not been written in, then continue on, as that level is likely the sanbox level, which creates as many ships as needed.
            #We have to use pre-set ships as the battleships and carriers need unique identifiers to ensure they don't lock onto each other, which are harder to implement with for loops
            run_times += 1
            #Adding run_times to make sure that boats are only drawn once


    
        key_input = win.checkKey()
        #Setting key input in case user wants to quit game or game needs a new input source 


        if len(enemy_ships_list) == 0 and len(player_ships_list) == 0:
            note = Text(Point(500, 600), "No ships remaining.... Returning to Main")
            note.draw(win)
            note.setSize(20)
            note.setTextColor("white")
            note.setStyle("bold")
            time.sleep(5)
            #Setting and drawing in text for win conditions, depending on specific level numbers.
            for obj in player_ships_list:
                image = objects_list_org[obj]
                image.undraw()
                time.sleep(1)
            #Undrawing all images in player_ships_list. (Don't have to undraw enemy ships, because len(enemy_ships_list) == 0 means there are no enemy ships left)
            player_ships_list.clear()
            objects_list.clear()
            objects_list_org.clear()
            run_times = 0
            #Clearing out other lists and resetting run_times accumulator
            if airstrikes_yes_no != False:
                for images_drawn in strikeing_list:
                    images_drawn.undraw()
            #Looping though any remaining items in strikeing_list and undrawing them
            if level_number != 1000:
                level_number_display.undraw()
            #Undrawing the level number display, but only if the level is not sandbox (ie: has display)
            note.undraw()
            return False
            #Returning that the player won (All enemy ships dead)


        elif len(enemy_ships_list) == 0:
        #Note: checks for length of enemy ships list. If equals to zero (Because all ships have despawned/deleted from low health), then erase rest of ships/objects/images
            if level_number == 1000:
                note = Text(Point(500, 600), "You Have Won!")
            elif level_number < 4:
                note = Text(Point(500, 600), "You Have Won! Prepare To Go Against The Next Level.")
            elif level_number == 4 and moveing_amount_time_ships != 0.5:
                note = Text(Point(500, 570), "You Have Won Against Every Level We've Implmeneted! Congragulations!")
            elif level_number == 4 and moveing_amount_time_ships == 0.5:
                note = Text(Point(500, 600), "You Have Won! Prepare To Go Against Our Final,\n Windows OS exclusive level!!!.")
            elif level_number == 5:
                note = Text(Point(500, 600), "You Have Won Against Every Level We've Implmeneted! Congragulations!\nYou Can Continue To Play With sandbox If You Want To Play Further!")
            note.draw(win)
            note.setSize(20)
            note.setTextColor("white")
            note.setStyle("bold")
            time.sleep(5)
            #Setting and drawing in text for win conditions, depending on specific level numbers.
            for obj in player_ships_list:
                image = objects_list_org[obj]
                image.undraw()
                time.sleep(1)
            #Undrawing all images in player_ships_list. (Don't have to undraw enemy ships, because len(enemy_ships_list) == 0 means there are no enemy ships left)
            player_ships_list.clear()
            objects_list.clear()
            objects_list_org.clear()
            run_times = 0
            #Clearing out other lists and resetting run_times accumulator
            if airstrikes_yes_no != False:
                for images_drawn in strikeing_list:
                    images_drawn.undraw()
            #Looping though any remaining items in strikeing_list and undrawing them
            if level_number != 1000:
                level_number_display.undraw()
            #Undrawing the level number display, but only if the level is not sandbox (ie: has display)
            note.undraw()
            return True
            #Returning that the player won (All enemy ships dead)
        

        elif len(player_ships_list) == 0:
            if level_number == 1000:
                note = Text(Point(500, 600), "You Have Lost...")
            else:
                note = Text(Point(500, 600), "You Have Lost... Try Again From The Top.")
            note.draw(win)
            note.setSize(20)
            note.setTextColor("white")
            note.setStyle("bold")
            time.sleep(5)
            for obj in enemy_ships_list:
                    image = objects_list_org[obj]
                    image.undraw()
                    time.sleep(1)
            enemy_ships_list.clear()
            objects_list.clear()
            objects_list_org.clear()
            run_times = 0
            if airstrikes_yes_no != False:
                for images_drawn in strikeing_list:
                    images_drawn.undraw()
            if level_number != 1000:
                level_number_display.undraw()
        #Simaler idea as the equivilant loop, only checking player ships instead.
            note.undraw()
            return False
            #Returning that the player lost (All player ships dead, at least one enemy ship remaining)


        if key_input == "q":
            if level_number == 1000:
                note = Text(Point(500, 600), "You Have Won!")
            elif level_number < 4:
                note = Text(Point(500, 600), "You Have Won! Prepare To Go Against The Next Level.")
            elif level_number == 4 and moveing_amount_time_ships != 0.5:
                note = Text(Point(500, 570), "You Have Won Against Every Level We've Implmeneted! Congragulations!")
            elif level_number == 4 and moveing_amount_time_ships == 0.5:
                note = Text(Point(500, 600), "You Have Won! Prepare To Go Against Our Final,\n Windows OS exclusive level!!!.")
            elif level_number == 5:
                note = Text(Point(500, 600), "You Have Won Against Every Level We've Implmeneted! Congragulations!\nYou Can Continue To Play With sandbox If You Want To Play Further!")
            note.draw(win)
            note.setSize(20)
            note.setTextColor("white")
            note.setStyle("bold")
            time.sleep(5)
            for obj in enemy_ships_list:
                image = objects_list_org[obj]
                image.undraw()
                time.sleep(1)
            for obj in player_ships_list:
                image = objects_list_org[obj]
                image.undraw()
                time.sleep(1)
            enemy_ships_list.clear()
            player_ships_list.clear()
            objects_list.clear()
            objects_list_org.clear()

            run_times = 0
            if airstrikes_yes_no != False:
                for images_drawn in strikeing_list:
                    images_drawn.undraw()
            if level_number != 1000:
                level_number_display.undraw()
            note.undraw()
            return True
        #Check for special cheat code.
        

    
        clicked = win.checkMouse()
        #Check to see if the player clicks on an object
        if (clicked != None):
        #Have to check if the click equals anythign first, otherwise the code may take in NULL as information, which messes up the code, since you can't imput NULL into any calculations
            for obj in objects_list:
                ship = objects_list_org[obj]
                #Have to assign temporary variable to it's designated value (ship == image)

                if obj.health <= 0:
                    ship.undraw()
                    objects_list.remove(obj)
                    del objects_list_org [obj]
                #Check to see if the ship is bellow 0 health, if so, then remove from all potential lists it's in
                    if obj.type == 1 or obj.type == 2:
                        player_ships_list.remove(obj)
                    elif obj.type == 3 or obj.type == 4:
                        enemy_ships_list.remove(obj)
                    elif obj.type == 5:
                        player_ships_list.remove(obj)
                        player_missle_list.remove(obj)
                    elif obj.type == 6:
                        enemy_ships_list.remove(obj)
                        enemy_missle_list.remove(obj)
                    #Each object is also located inside a type-specific list, so depending on type, we remove it from diffrent lists.

                if obj.type == 1 or obj.type == 2:
                    check_enemy_ships(win, obj, ship, objects_list_org, objects_list, enemy_ships_list)
                    obj.x = ship.getAnchor().getX()
                    obj.y = ship.getAnchor().getY()
                #Checking distance from all enemey ships to see if ship health needs to be decreased, and then setting object coordinates to the image's X and Y coords.
                elif obj.type == 3 or obj.type == 4:
                    check_enemy_ships(win, obj, ship, objects_list_org, objects_list, player_ships_list)
                    obj.x = ship.getAnchor().getX()
                    obj.y = ship.getAnchor().getY()
                #Same for enemy ships, only checking for player ships

                if obj.type == 1:###########################################
                    if check_in_box(ship.getAnchor().getX(), ship.getAnchor().getY(), clicked.getX(), clicked.getY(), ship_box) == True:
                        detect_health(obj, ship, objects_list, objects_list_org, enemy_ships_list)
                        health_signal = Text(Point(930, 610), str("Ship Health: " + str(round(obj.health))))
                        health_signal.draw(win)
                        health_signal.setTextColor("white")
                        health_signal.setSize(14)
                        health_signal.setStyle("bold")
                        #Createing text to show the health of the ship

                        draw_place(Point(ship.getAnchor().getX(), int(ship.getAnchor().getY())), win)
                        #If player ship is clicked on, then the ship has a small animation run around it to show the user that the click has been registerd
                        checking_click_in_choose_box(ship, obj, win, objects_list, objects_list_org, player_ships_list, player_missle_list, enemy_missle_list, enemy_ships_list)
                        #Checking if the player has clicked on the ship/chosen to move/change state of battleship
                        health_signal.undraw()
                        #Undrawing text displaying health afterwards
                #Runs specific code for player battleships to check what the player wants to do with the ship.


                elif obj.type == 2:###########################################
                    if check_in_box(int(ship.getAnchor().getX()), int(ship.getAnchor().getY()), int(clicked.getX()), int(clicked.getY()), ship_box) == True:
                        detect_health(obj, ship, objects_list, objects_list_org, enemy_ships_list)
                        health_signal = Text(Point(915, 610), str("Ship Health: " + str(round(obj.health))))
                        health_signal.draw(win)
                        health_signal.setTextColor("white")
                        health_signal.setSize(14)
                        health_signal.setStyle("bold")
                        #Createing text to show the health of the ship

                        draw_place(Point(ship.getAnchor().getX(), int(ship.getAnchor().getY())), win)
                        #If player ship is clicked on, then the ship has a small animation run around it to show the user that the click has been registerd
                        checking_click_in_choose_box(ship, obj, win, objects_list, objects_list_org, player_ships_list, player_missle_list, enemy_missle_list, enemy_ships_list)
                        #Checking if the player has clicked on the ship/chosen to move/launch missles from ship
                        health_signal.undraw()
                        #Undrawing text displaying health afterwards
                #Runs specific code for player carriers to check what the player wants to do with the ship.


                elif obj.type == 3:##################################################
                    #move(ship, clicked, ship_box, win, obj, key_input)
                    checking_move(obj, ship, objects_list, objects_list_org, enemy_ships_list, player_ships_list, enemy_missle_list, player_missle_list, win, ship_box, timer_missle)
                    #Ship Ai
                #Simpler ai to make sure the enemmy ships don't miss anything

                elif obj.type == 4:##################################################
                    #move(ship, clicked, ship_box, win, obj, key_input)
                    checking_move(obj, ship, objects_list, objects_list_org, enemy_ships_list, player_ships_list, enemy_missle_list, player_missle_list, win, ship_box, timer_missle)
                    #Ship Ai
                #Simaler idea here.

            check_dest_stop_obj(obj, ship, key_input, objects_list, objects_list_org, player_ships_list, enemy_ships_list, player_missle_list, enemy_missle_list)
            ship.move(obj.one*moveing_amount_time_ships, obj.y_increase*moveing_amount_time_ships)
            #Function that checks if the object is near the edges of the screen, if so, stops ship.

        else:
            for obj in objects_list:
                ship = objects_list_org[obj]
            #Looping in objects_list and assigning a variable to it's equivilant image. 
            #This loop is used if the player has not clicked on anything.
                check_dest_stop_obj(obj, ship, key_input, objects_list, objects_list_org, player_ships_list, enemy_ships_list, player_missle_list, enemy_missle_list)
                #Checking if the ship should stop moveing if it is too close next to the edges of the scree

                if ship.getAnchor().getX() <= 0 + 15 or ship.getAnchor().getY() < 0 + 15 or ship.getAnchor().getX() >= win_box[0] - 15 or ship.getAnchor().getY()  >= win_box[1] - 15:
                    pass
                #First if statement makes sure that any ship near the edge of the screen does not move out of view of the player
                else:
                    if obj.type == 1 or obj.type == 2:
                        check_enemy_ships(win, obj, ship, objects_list_org, objects_list, enemy_ships_list)
                        check_dest_stop_obj(obj, ship, key_input, objects_list, objects_list_org, player_ships_list, enemy_ships_list, player_missle_list, enemy_missle_list)
                        #Basic functions to check if ship has nearby enemy ships, and if ship should stop moveing.
                        ship.move(obj.one*moveing_amount_time_ships, obj.y_increase*moveing_amount_time_ships)
                        detect_health(obj, ship, objects_list, objects_list_org, player_ships_list)
                        #Functions that just move the ships and detect for any nearby enmey ships. If nearby, then minus some health from player ship
                    
                    elif obj.type == 3 or obj.type == 4:
                        check_enemy_ships(win, obj, ship, objects_list_org, objects_list, player_ships_list) 
                        check_dest_stop_obj(obj, ship, key_input, objects_list, objects_list_org, player_ships_list, enemy_ships_list, player_missle_list, enemy_missle_list) 
                        #Basic functions to check if ship has nearby player ships, and if ship should stop moveing.
                        if obj.destinationx != 0 and obj.destinationy != 0:
                            calc_slope(ship.getAnchor().getX(), ship.getAnchor().getY(), obj.destinationx, obj.destinationy, obj)
                        #This is a very specific if statment, since I had to implment ship.destinationx and .destinationy as 0 when createing them as classes, 
                        #they end up allways moveing to the upper top corner unless I implment this check before setting y_movement and one to their inputs.
                        checking_move(obj, ship, objects_list, objects_list_org, enemy_ships_list, player_ships_list, enemy_missle_list, player_missle_list, win, ship_box, timer_missle)
                        #AI function for ship   
                        ship.move(obj.one*moveing_amount_time_ships, obj.y_increase*moveing_amount_time_ships)
                        detect_health(obj, ship, objects_list, objects_list_org, enemy_ships_list)
                        #Move the ship and detect the ship's health. If health is bellow/equal to zero, then undraw and delete object/image.

                    elif obj.type == 5 or obj.type == 6:
                        ship.move(1.3*obj.one*moveing_amount_time_ships, 1.3*obj.y_increase*moveing_amount_time_ships)
                    #For missles, just move.

        

        if airstrikes_yes_no == True:
            strikeing, strikeing_target, small_circle, small_warning, timer_airstrike = airstrike(player_ships_list, objects_list_org, timer_airstrike, win, strikeing, strikeing_target, small_circle, small_warning, strikeing_list, time_wait, time_wait_between, target_hit_size, damage)
        #If the function input puts airstrikes_yes_no as True (ie: Airstrikes will be implmented in the level, then run airstrikes() function.
    


        timer_missle += 1
        run_times += 1
        #Add to timer_missle accumulator



        if moveing_amount_time_ships == 1:
            pass
        elif moveing_amount_time_ships == 0.5:
            time.sleep(0.04)
        #Check to see if the player is on a windows laptop. If so, then use time.sleep() to wait in order to allow the player to be able to respond to ai.
