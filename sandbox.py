from graphics import *
from functions import Battleships, Carriers
from main import main_mechanics

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

#####################################################
def sandbox_level(win, win_box, moveing_amount_time_ships):
    global run_times, objects_list, objects_list_org, player_ships_list, enemy_ships_list, player_missle_list, enemy_missle_list
    while True:
        if run_times < 1:
            text_explain = Text(Point(500, 50), "This is an interactive Sandbox where you can place however many player and enemy battleships & Carriers,\n and plan out stratagies or simulations with diffrent combinations of objects and starting positions.")
            text_explain.draw(win)
            text_explain.setStyle("bold")
            text_explain.setTextColor("white")
            text_explain.setSize(18)

            text_explain_2 = Text(Point(500, 98), "Press the key P to place a player ship, and the letter E to place an AI-controlled ship.\n To choose between placeing a battleship or a carrier, press the letter key B or C respectively.")
            text_explain_2.draw(win)
            text_explain_2.setStyle("bold")
            text_explain_2.setTextColor("white")
            text_explain_2.setSize(15)

            text_explain_3 = Text(Point(500, 146), "Once the key L is pressed, then all placeing of ships will halt, and the normal program involveing the running of ships will continue.\nYou may start placeing ships at any area.")
            text_explain_3.draw(win)
            text_explain_3.setStyle("bold")
            text_explain_3.setTextColor("white")
            text_explain_3.setSize(15)
            run_times += 1
        #Check to see if the game has run for less then 1 time, the following code is only run once, needs to set up text explaining sandbox

            ships_placed_player = 0
            ships_placed_enemy = 0
            #Variables to track number of ships placed by each. 
            #Note: This is used to create unqiue identiies for each ship, which is nessesary to make sure that ships don't try to attack each other.
            while True:
                key_input_intro = win.getKey()
                #Loop will continueally check for new inputs
                if key_input_intro == "P" or key_input_intro == "p":
                #Checking if player is putting in a player ship
                    if run_times == 1:
                        text_explain.undraw()
                        text_explain_2.undraw()
                        text_explain_3.undraw()
                        run_times = 2
                    key_input_intro = win.getKey()
                    #If the run_times accumulator is equal to 1 (And it will only equal to one if it has drawn the into text only once), then the text will be undrawn and the accumulator set to 2 to keep this from happening again.
                    if key_input_intro == "B" or key_input_intro == "b":
                        location_put = win.getMouse()
                        player_bat_1 = Battleships(location_put.getX(), location_put.getY(), 200, 5, 0, 0, 0, 0, 0, 0, 1, 100 + ships_placed_player)
                        player_bat_01 = Image(Point(player_bat_1.x, player_bat_1.y), "battleshipblueicon.gif")
                        player_bat_01.draw(win)
                        objects_list.append(player_bat_1)
                        objects_list_org[player_bat_1] = player_bat_01
                        player_ships_list.append(player_bat_1)
                        ships_placed_player += 1
                    #Check to create a player battleship, add accumulator for ships_placed_player to 100 in order to give each ship a unique identity, then add 1 to accumulator to change number each time a player ship is created.

                    elif key_input_intro == "C" or key_input_intro == "c":
                        location_put = win.getMouse()
                        player_car_1 = Carriers(location_put.getX(), location_put.getY() + 100, 0, 0, 0, 0, 0, 0, 2, 100 + ships_placed_player)
                        player_car_01 = Image(Point(location_put.getX(), location_put.getY()), "carrierblueicon.gif")
                        player_car_01.draw(win)
                        objects_list.append(player_car_1)
                        objects_list_org[player_car_1] = player_car_01
                        player_ships_list.append(player_car_1)
                        ships_placed_player += 1
                    #Same as above but for player carriers.


                elif key_input_intro == "E" or key_input_intro == "e":
                #Checking if player is putting in an enemy (ai) ship.
                    if run_times == 1:
                        text_explain.undraw()
                        text_explain_2.undraw()
                        text_explain_3.undraw()
                        run_times = 2
                    #Simaler idea as the equivilant code in the player if statement.
                    key_input_intro = win.getKey()
                    if key_input_intro == "B" or key_input_intro == "b":
                        location_put = win.getMouse()
                        enemey_bat_1 = Battleships(location_put.getX(), location_put.getY(), 200, 5, 0, 0, 0, 0, 0, 0, 3, 200 + ships_placed_enemy)
                        enemey_bat_01 = Image(Point(location_put.getX(), location_put.getY()), "battleshipredicon.gif")
                        enemey_bat_01.draw(win)
                        objects_list.append(enemey_bat_1)
                        objects_list_org[enemey_bat_1] = enemey_bat_01
                        enemy_ships_list.append(enemey_bat_1)
                        ships_placed_enemy += 1
                    #Check to create an enemy battleship. Simaler idea as createing the player battleships/carriers, but with diffrent acculumators, and adding accumulator to 200 instead of 100 to create unique indentifier.

                    elif key_input_intro == "C" or key_input_intro == "c":
                        location_put = win.getMouse()
                        enenmy_car_1 = Carriers(location_put.getX(), location_put.getY(), 0, 0, 0, 0, 0, 0, 4, 200 + ships_placed_enemy)
                        enenmy_car_01 = Image(Point(location_put.getX(), location_put.getY()), "carrierredicon.gif")
                        enenmy_car_01.draw(win)
                        objects_list.append(enenmy_car_1)
                        objects_list_org[enenmy_car_1] = enenmy_car_01
                        enemy_ships_list.append(enenmy_car_1)
                        ships_placed_enemy += 1
                    #Simaler idea as the code above, only for carriers.
                

                elif key_input_intro == "L" or key_input_intro == "l":
                    if run_times == 1:
                        text_explain.undraw()
                        text_explain_2.undraw()
                        text_explain_3.undraw()
                        run_times = 2
                    #Simaler idea as the equivilant code in the player if statement.
                    player_win = main_mechanics(win, win_box, 1000, True, 75, 8, 30, 4, objects_list, objects_list_org, player_ships_list, enemy_ships_list, player_missle_list, enemy_missle_list, timer_missle, moveing_amount_time_ships)
                    run_times = 0
                    return
                
                #When the player clicks "L", then the code assumes that they want to start the simulation. The code will then run main_mecanics, run the game untill one of the fail states is activated, and return to main menu loop.