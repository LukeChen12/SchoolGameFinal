from graphics import *
from functions import *
import random
#Importing functions

def checking_move(ship_object, ship_image, objects_list, objects_list_org, side_ships_list, opp_ships_list, side_missle_list, opp_missle_list, win, ship_box, timer):
    check_distance_enemy_dictonary = {}
    if ship_object.type == 3 and len(opp_ships_list) != 0 and len(side_ships_list) != 0:
        for opp in opp_ships_list:
            if opp.type == 1 or opp.type == 2 and len(opp_ships_list) != 0 and len(side_ships_list) != 0: #Test
                opp_image = objects_list_org[opp]
                check_distance_enemy_dictonary[calc_dist(ship_image.getAnchor().getX(), ship_image.getAnchor().getY(), opp_image.getAnchor().getX(), opp_image.getAnchor().getY())] = opp_image
            if len(check_distance_enemy_dictonary) != 0:
                moveing_target = check_distance_enemy_dictonary[min(check_distance_enemy_dictonary)]
            else:
                return
        #Code that calculates the ship closest to the inputed ship, and returns it as moveing_target
        #If there are no player ships left, then the function returns to the code without changeing the ship in any way.
        for side in side_ships_list:
            if side.type == 3 and side.health > 30:
                side.state_defence = True
            else:
                side.state_defence = False
        #Simple action to make the enemy ai battleships change states from a defensive mode to an offensive mode after they get bellow a certian health level
            side_image = objects_list_org[side]
            if calc_dist(ship_image.getAnchor().getX(), ship_image.getAnchor().getY(), side_image.getAnchor().getX(), side_image.getAnchor().getY()) < 35 and side.type != 6 and ship_object.type != 6 and side.unique_identifier != ship_object.unique_identifier:
                ship_object.slope = 0
                ship_object.one = 0
                ship_object.y_increase = 0
            #This is a very specific check for the other ships on the same side as the enemy. That is, if this ship is within a certian range of any one
            #of the other enemy ships, and the ship has a unique indentifier diffrent from the ship being looped through, the ship stops moveing, to stop enemy ships from mergeing together following the same player ship
            #(Remember, every enemy ship is in the enemy_ships_list, so you have to be able to tell when you're just checking the distance from the same ship)
        if check_in_box(moveing_target.getAnchor().getX(), moveing_target.getAnchor().getY(), side_image.getAnchor().getX(), side_image.getAnchor().getY(), ship_box) == False:
            ship_object.destinationx = moveing_target.getAnchor().getX()
            ship_object.destinationy = moveing_target.getAnchor().getY()
        #Otherwise, if all other conditions previously incleded are True (ie: there are still player ships remaining, and the enemy ship being looped through is a carrier), 
        #then the position of the nearest player ship is the new destination of the enemy ship.
                

    elif ship_object.type == 4 and len(opp_ships_list) != 0 and len(side_ships_list) != 0:
        for opp in opp_ships_list:
            if opp.type == 1 or opp.type == 2:
                opp_image = objects_list_org[opp]
                check_distance_enemy_dictonary[calc_dist(ship_image.getAnchor().getX(), ship_image.getAnchor().getY(),\
                opp_image.getAnchor().getX(), opp_image.getAnchor().getY())] = opp_image
        #Check to construct a list of all ship distances to find the shortest one.

        if len(check_distance_enemy_dictonary) != 0:
            moveing_target = check_distance_enemy_dictonary[min(check_distance_enemy_dictonary)]
        else:
            return
        #Simaler idea to above, only for carriers. If there are still player ships remaining, then new target is assigned to closest player ship, else, return to code without running missle function
        if timer%343 == 0:
            create_missles(ship_image, ship_object, moveing_target.getAnchor().getX(), moveing_target.getAnchor().getY(), objects_list, objects_list_org, side_missle_list, opp_missle_list, side_ships_list, opp_ships_list, win)
        #Function to create missles if timer has run to number that will only divide itself (ie: function only runs every 342 seconds.)



def airstrike(player_ships_list, objects_organized, timer, window, strikeing, strikeing_target, small_circle, small_warning, strikeing_list, time_wait, time_wait_between, target_hit_size, damage):
#Function
    timer += 1 
    #No matter what, the timer will be added onto every time the airstrike function is run. 
    if strikeing == False and len(player_ships_list) != 0:
        ran_player_target_image = objects_organized[random.choice(player_ships_list)]
        strikeing_target = Point(ran_player_target_image.getAnchor().getX() + random.randint(-30, 30), ran_player_target_image.getAnchor().getY() + random.randint(-30, 30))
        strikeing = True
        #If the airstrike is currently not running, then it automatically takes the positions of the ships, finds a random one, and turns strikeing to True, to avoid re-running function.
        #This also serves to keep function from re-definieng the strike target in between diffrent airstrike stages.
    if timer == time_wait - time_wait_between:
        small_warning = Image(strikeing_target, "red_airstrike_warning.png")
        small_warning.draw(window)
        strikeing_list.append(small_warning)
    #Stage one of the airstrike, just draws smallest circle and warning png.
    elif timer == time_wait:
        small_circle = Circle((strikeing_target), target_hit_size)
        small_circle.draw(window)
        strikeing_list.append(small_circle)
        small_circle.setOutline("red")
        time.sleep(0.05)
    #Stage 2. Since it allways comes after stage 1, small_warning will allways be returned into the function from earlier, meaning it will still exist
    elif timer == time_wait + time_wait_between:
        c2 = Circle((strikeing_target), target_hit_size + 8)
        c2.draw(window)
        c2.setOutline("red")
        strikeing_list.append(c2)
        time.sleep(0.05)

        small_circle.undraw()
        small_warning.undraw()
        c2.undraw()

        strikeing = False
        timer = 0

        for drawed in strikeing_list:
            drawed.undraw()

        for player_ships in player_ships_list:
            player_ships_image = objects_organized[player_ships]
            if calc_dist(player_ships_image.getAnchor().getX(), player_ships_image.getAnchor().getY(), strikeing_target.getX(), strikeing_target.getY()) <= target_hit_size + 8 and player_ships.type != 5:
                player_ships.health -= damage
    #Stage 3. Undraws all circles and strike warnings which are all returned to the main function and later back into the airstrike function, meaning by stage 3, the functino will have all 3 circles drawn and defined. 
    return strikeing, strikeing_target, small_circle, small_warning, timer
    #return statement.