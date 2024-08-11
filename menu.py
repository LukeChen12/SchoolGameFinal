from graphics import *
from functions import *
from main import main_mechanics
from sandbox import sandbox_level
#Importing of functions from graphics as well as functions I created (functions, main, sandbox_level)

win_box_starting = (1000, 630)
win_box_main = (1000, 630)
#Dimentions for the game windows (Diffrent in case one needs to be a diffrent size)
run_through_start_menu = 0
#Accumulator to see how many times player has returned to start menu
run_through_draw_frame = 0
#Accumulator to see if the second frame is drawn.

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

while True:
    if run_through_start_menu  == 0:
        moveing_amount_time_ships = 0 #Setting basic variables
        win = GraphWin("Impact Starting Screen", win_box_starting[0], win_box_starting[1])
        win.setBackground(color_rgb(8, 15, 51))
        #Drawing screen and setting background color

        text_info = Text(Point(500, 50), "Press W if you are playing on Windows\nPress any other key if you are playing on Mac")
        text_info.setSize(20)
        text_info.setTextColor("white")
        text_info.setStyle("bold")
        text_info.draw(win)
        window_if = win.getKey()
        if window_if == "W" or window_if == "w":
            moveing_amount_time_ships = 0.5
            text_info.undraw()
        else:
            moveing_amount_time_ships = 1
            text_info.undraw()
        #Check to see if the player is on a windows laptop.
        
        back_image = Image(Point(500, 315), "frame3.gif")
        back_image.draw(win)
        run_through_start_menu = 2
    #Intial set up for the start menu. The accumulator run_through_start_menu is checked to see if it equal to zero, if so, create window, set color, image, and draw image.
    #Note: Since the accumulator will never be reset back to zero, this code will only run once unless the entire program is closed and re-opened.
    elif run_through_start_menu == 1:
        back_image = Image(Point(500, 315), "frame3.gif")
        back_image.draw(win)
        run_through_start_menu = 2
    #Secondary set up for when player fails one of the levels or returns to menu. We only draw the image here, because we don't want to create a new window, we want to re-use the same one.
    #Note: This is why we have to seperate the intial creation of the window and start menu from every other time that the start menu is opened (When we don't need to create the window)
    #Note: run_through_start_menu is set to 2 here in order to ensure that neither if statements above are triggered.
    


    clicked_box_level = win.getMouse()
    if clicked_box_level.getX() < 400 and clicked_box_level.getX() > 180 and \
        clicked_box_level.getY() < 260 and clicked_box_level.getY() > 180:
        win.setBackground(color_rgb(8, 15, 51))
        back_image.undraw()
        sandbox_level(win, win_box_starting, moveing_amount_time_ships)
        run_through_start_menu = 1
    #Function that runs the "sandbox" or "testing" level, where the user can place ships and test ideas/stratagies.
    #Accumulator run_through_start_menu will be reset to one, to allow back_image to be redrawn without re-createing a new window
    
    elif clicked_box_level.getX() < 400 and clicked_box_level.getX() > 130 and \
        clicked_box_level.getY() < 475 and clicked_box_level.getY() > 400:
        win.setBackground(color_rgb(8, 15, 51))
        back_image.undraw()
        #Simple check if clicked on area near text "Play Main Levels", if so, then undraw image, set backgroun color
        player_win = main_mechanics(win, win_box_main, 1, False, 80, 10, 30, 4, objects_list, objects_list_org, player_ships_list, enemy_ships_list, player_missle_list, enemy_missle_list, timer_missle, moveing_amount_time_ships)
        if player_win == True:
            player_win = main_mechanics(win, win_box_main, 2, True, 75, 8, 30, 4, objects_list, objects_list_org, player_ships_list, enemy_ships_list, player_missle_list, enemy_missle_list, timer_missle, moveing_amount_time_ships)
        else:
            run_through_start_menu = 1
            continue
        if player_win == True:
            player_win = main_mechanics(win, win_box_main, 3, True, 70, 6, 32, 5, objects_list, objects_list_org, player_ships_list, enemy_ships_list, player_missle_list, enemy_missle_list, timer_missle, moveing_amount_time_ships)
        else:
            run_through_start_menu = 1
            continue
        if player_win == True:
            player_win = main_mechanics(win, win_box_main, 4, True, 60, 5, 34, 6, objects_list, objects_list_org, player_ships_list, enemy_ships_list, player_missle_list, enemy_missle_list, timer_missle, moveing_amount_time_ships)
        else:
            run_through_start_menu = 1
            continue
        if player_win == True and moveing_amount_time_ships == 0.5:
            player_win = main_mechanics(win, win_box_main, 5, True, 60, 5, 34, 6, objects_list, objects_list_org, player_ships_list, enemy_ships_list, player_missle_list, enemy_missle_list, timer_missle, moveing_amount_time_ships)
        else:
            run_through_start_menu = 1
            continue
        #Special level which only runs if the player has inputed windows as their operateing system (Because if windows is inputed as system, then moveing_amount_time_ships would be set to 0.5)
        run_through_start_menu = 1
        #List of levels, all go in cronological order, each level right after the other. 
        #Set return value to a variable (If the player wins, then variable is True, if not, then False) that tells the code if the player won the level. (ie: Had ships surviveing whent the AI didn't)
        #After each level, take the return value in the form of the variable. 
        #If player won, (True) then run next level, if not, then reset run_throuhg_start_menu to redraw the mneu (Not re-create the window), and continue to start at the begeining of the While loop.
    
    elif clicked_box_level.getX() < 280 and clicked_box_level.getX() > 40 and \
        clicked_box_level.getY() < 365 and clicked_box_level.getY() > 280:
        win.setBackground(color_rgb(8, 15, 51))
        back_image.undraw()
        frame_guide_1 = Image(Point(500, 308), "frame_guide_1.gif")
        frame_guide_1.draw(win)
        while True:
            letter_input = win.checkKey()
            if letter_input == "C" or letter_input == "c":
                frame_guide_1.undraw()
                if run_through_draw_frame == 1:
                    frame_guide_2.undraw()
                run_through_start_menu = 1
                break
            elif letter_input == "N" or letter_input == "n" and run_through_draw_frame != 1:
                frame_guide_2 = Image(Point(500, 308), "frame_guide_2.gif")
                frame_guide_2.draw(win)
                run_through_draw_frame = 1
        #Infinite loop that goes on until user inputs C.
    #Simpler code for the instruction page in the game, just does simaler set up as the other conditional did above.