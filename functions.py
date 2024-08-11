from graphics import *
import math

class Battleships:
    def __init__(self, x, y, health, damage, slope, one, y_increase, destinationx, destinationy, movements, type, unique_identifier):
        self.x = x
        self.y = y
        #x and y are the respsective coordinates for the ship
        self.slope = slope
        self.one = one
        self.y_increase = y_increase
        #Variables that are responsible for how the ship moves.
        #Slope is simply the slope between the points of the center of the ship and it's destination.
        #one is the increase/decrease in the x-axis. It is default set to 1, and may turn to -1 depending on if the ship is moveing up/down the x-axis, but otherwise is generally not modified.
        #y_increase is the increase/decrease in the x-axis. It is the one that varies more, based on multiplying the slope by variable one, to get amount increased in y-axis every increase by variable one.
        
        self.destinationx = destinationx
        self.destinationy = destinationy
        self.movements = movements
        #Variables responsible for tracking the destination/times moved for each ship
        #Variables destinationx and destinationy are the x and y coords for the ship's destination
        #Movements tracks number of times that ship moves. (Nessesary, since slope, one, and y_increase all default equal to 0. Therefore, code must check if ship has moved first before 
        #automatically inputing one/y_increase into move())

        self.type = type

        self.health = health
        self.damage = damage
        self.planes = 0
        self.state_defence = True

        self.unique_identifier = unique_identifier
#Class for all battleships. Each battleships has specalized variables that are set, and others that can be changed depending on what the code wants from the class.



class Carriers:
    def __init__(self, x, y, slope, one, y_increase, destinationx, destinationy, movements, type, unique_identifier):
        self.x = x
        self.y = y
        #x and y are the respsective coordinates for the ship
        self.slope = slope
        self.one = one
        self.y_increase = y_increase
        #Simple mathmatical variables representing the amount that the ship has to increase allong x-axis (one), y-axis (y_increase), and slope between ship and it's destination (slope)

        self.destinationx = destinationx
        self.destinationy = destinationy
        self.movements = movements
        #Variables tracking the coords of the destinatino the ship is heading towards, and the amount of times the ship has moved.

        self.type = type
        #Type of the ship

        self.health = 60
        self.damage = 3
        self.ammo = 6
        #Set variables that for the sake of simplicity and not repeating functions in main(), are pernamently set.

        self.unique_identifier = unique_identifier
        #Unique identifier for the ship
#Class for carriers, simaler idea to battlehsips, but note that they can create missles



class Planes:
    def __init__(self, x1, y1, destinationx, destinationy, slope, one, y_increase, movements, type):
        self.x1 = x1
        self.y1 = y1
        #Coords for the object

        self.slope = slope
        self.one = one
        self.y_increase = y_increase
        #Mathamatical variables (See earlier classes if you want to know more about their details, same idea here)

        self.destinationx = destinationx
        self.destinationy = destinationy
        self.movements = movements
        #Variables for the destination of the ship and the amount of times it has moved.

        self.health = 5
        self.damage = 2
        #Set variables (Health is not important for missles, just leftover from earlier plans for missles (or planes))

        self.type = type
        #Type of object.
#Class for missles, simaler to the two other classes, though it is a lot simpler
#Note: This function has been residually named "planes", as the original plan invisioned a more complicated system of rotateing planes which was too hard to implemnt.




###########################################################################
#Drawing functions related to createing circles and notifying players that an event has happened
###########################################################################
def draw_place(clicked2, window):
#Function run in order to tell player that they have clicked on player ships
    c = Circle((clicked2), 10)
    c.draw(window)
    c.setOutline("white")
    ##############Visual-Seperators##############
    time.sleep(0.05)
    c2 = Circle((clicked2), 20)
    c2.draw(window)
    c2.setOutline("white")
    ##############Visual-Seperators##############
    time.sleep(0.05)
    c.undraw()
    c3 = Circle((clicked2), 30)
    c3.draw(window)
    c3.setOutline("white")
    ##############Visual-Seperators##############
    time.sleep(0.05)
    c2.undraw()
    c4 = Circle((clicked2), 40)
    c4.draw(window)
    c4.setOutline("white")
    ##############Visual-Seperators##############
    time.sleep(0.05)
    c3.undraw()
    time.sleep(0.05)
    c4.undraw()
#Function repeatly creates circles, draws them, sets their color outline as white, waits, re-draws a larger circle, and undraws the smaller one repeatly
#This is the main use of the [time] functions



def hit(clicked2, window):
    c = Circle((clicked2), 8)
    c.draw(window)
    c.setOutline("white")
    time.sleep(0.03)
    c2 = Circle((clicked2), 18)
    c2.draw(window)
    c2.setOutline("white")
    time.sleep(0.03)
    c.undraw()
    time.sleep(0.03)
    time.sleep(0.03)
    c2.undraw()
#Simaler function as draw_place(), but notifying player that a ship has taken damage, wich is shorter to avoid lagging the game.




###########################################################################
#Checking to see if any ship needs to stop moveing (ie: Has reached it's destination point)
###########################################################################
def check_dest_stop_obj(ship_class, ship_image, input, objects_list, objects_list_org, player_ships_list, enemy_ships_list, player_missle_list, enemy_missle_list):
    if ship_class.type == 1 or ship_class.type == 2:
        if ship_class.movements != 0:
            if int(ship_image.getAnchor().getX()) <= int(ship_class.destinationx) + 15\
                and int(ship_image.getAnchor().getX()) >= int(ship_class.destinationx) - 15\
                and int(ship_image.getAnchor().getY()) <= int(ship_class.destinationy) + 15\
                and int(ship_image.getAnchor().getY()) >= int(ship_class.destinationy) - 15:
                ship_class.one = 0
                ship_class.y_increase = 0
                ship_class.slope = 0
            elif input == "q":
                ship_class.one = 0
                ship_class.y_increase = 0
                ship_class.slope = 0
    #Check to see if the player ships are near the destination of the ship, or if the player enters 'q' to quit, then the ships will stop moveing to keep them going out of bounds.

    elif ship_class.type == 3 or ship_class.type == 4 and ship_class.movements != 0 and \
        int(ship_image.getAnchor().getX()) <= int(ship_class.destinationx) + 15\
        and int(ship_image.getAnchor().getX()) >= int(ship_class.destinationx) - 15\
        and int(ship_image.getAnchor().getY()) <= int(ship_class.destinationy) + 15\
        and int(ship_image.getAnchor().getY()) >= int(ship_class.destinationy) - 15:
        ship_class.one = 0
        ship_class.y_increase = 0
        ship_class.slope = 0
    #Check to see if the enemey ships are near the destination of the ship, if so, then the ships stop moveing to keep them from going out of bounds
    
    elif ship_class.type == 5 and \
        int(ship_image.getAnchor().getX()) <= int(ship_class.destinationx) + 15\
        and int(ship_image.getAnchor().getX()) >= int(ship_class.destinationx) - 15\
        and int(ship_image.getAnchor().getY()) <= int(ship_class.destinationy) + 15\
        and int(ship_image.getAnchor().getY()) >= int(ship_class.destinationy) - 15:
        ship_image.undraw()
        objects_list.remove(ship_class)
        player_missle_list.remove(ship_class)
        player_ships_list.remove(ship_class)
        del objects_list_org[ship_class]
    #If the object is a player missle and is near the destination of the ship, then completely undraw and delete from all lists to avoid haveing to track misssles moveing out of bounds.
    #Note: Since the missle dissapears after reaching it's desination, then most missles will never reach the edge of the screen, but it is still good to have anyways.
    
    elif ship_class.type == 6 and \
        int(ship_image.getAnchor().getX()) <= int(ship_class.destinationx) + 15\
        and int(ship_image.getAnchor().getX()) >= int(ship_class.destinationx) - 15\
        and int(ship_image.getAnchor().getY()) <= int(ship_class.destinationy) + 15\
        and int(ship_image.getAnchor().getY()) >= int(ship_class.destinationy) - 15:
        enemy_missle_list.remove(ship_class)
        enemy_ships_list.remove(ship_class)
        ship_image.undraw()
        objects_list.remove(ship_class)
        del objects_list_org [ship_class]
    #Simaler to if statment above, only reversed for enemy missles
#General purpose of the function is to check when an object should stop moveing because it's near a wall.



###########################################################################
#Functions that deal with strictly math operations
###########################################################################  
def detect_health(object, object_image, objects_total_list, objects_total_list_org, objects_resticted_list):
#Function that checks the object's health property.
    if object.health <= 0:
        object_image.undraw()
        objects_total_list.remove(object)
        objects_resticted_list.remove(object)
        del objects_total_list_org [object]
    #If the health is below 0, then the object is deleted from every one of the lists it's in.



def calc_slope(x1, y1, x2, y2, ship):
    ship.movements +=1
    #Adding to movements variable of the ship, since 
    ship.slope, ship.y_increase, ship.one = 0, 0, 0
    if int(x2) - int(x1) == 0 or int(x1) - int(x2) == 0:
        ship.one = 0
    elif int(y2) - int(y1) == 0 or int(y1) - int(y2) == 0:
        ship.y_increase = 0
    #In the rare cases that the two points share either an x or y axis, then the slope or y_increase must be changed to match this diffrence (ie: change in the shared axis must be 0)
    else:
        if int(x2) > int(x1) and int(y2) > int(y1):
            ship.y_increase = abs(ship.y_increase*1)
            ship.one = 1
        elif int(x2) < int(x1) and int(y2) < int(y1):
            ship.y_increase = -abs(ship.y_increase*-1)
            ship.one = -1
        elif int(x2) > int(x1) and int(y2) < int(y1):
            ship.y_increase = -abs(ship.y_increase*-1)
            ship.one = 1
        elif int(x2) < int(x1) and int(y2) > int(y1):
            ship.y_increase = abs(ship.y_increase*1)
            ship.one = -1
        #Depending on if the area that the ship wants to move in is closer to the upper left, upper right, lower left, or lower right corners, the slope and y_increase may change.
        #This is because to go closer to the upper-left corner, the slope and y_increase must be negative, in order to decrease the position of the boat -one and -y_increase on their respective axies.
        ship.slope = ((int(y2) - int(y1))/(int(x2) - int(x1)))
        ship.y_increase = ship.slope*ship.one
        #Setting variables

    if x2 == x1:
        ship.y_increase = ship.y_increase*0.06
        ship.one = ship.one*0.06
    #Simple idea to try to reduce the fact that the boat moves much quicker when moveing vertically (allong y_axis) for some reason.
    #Note: Glitch likely due to increaseing y_increase variable the closer the two points are to haveing the same x-axis.
    if int(x2) > int(x1):
        if x2 - x1 < 80 and x2 - x1 > 60:
            ship.y_increase = ship.y_increase*0.92
            ship.one = ship.one*0.75
        elif x2 - x1 < 60 and x2 - x1 > 40:
            ship.y_increase = ship.y_increase*0.48
            ship.one = ship.one*0.55
        elif x2 - x1 < 40 and x2 - x1 > 20:
            ship.y_increase = ship.y_increase*0.24
            ship.one = ship.one*0.4
        elif x2 - x1 < 20 and x2 - x1 > 10:
            ship.y_increase = ship.y_increase*0.12
            ship.one = ship.one*0.2
        elif x2 - x1 < 10:
            ship.y_increase = ship.y_increase*0.06
            ship.one = ship.one*0.06
    elif int(x2) < int(x1):
        if x1 - x2 < 80 and x2 - x1 > 60:
            ship.y_increase = ship.y_increase*0.92
            ship.one = ship.one*0.75
        elif x1 - x2 < 60 and x2 - x1 > 40:
            ship.y_increase = ship.y_increase*0.48
            ship.one = ship.one*0.55
        elif x1 - x2 < 40 and x2 - x1 > 20:
            ship.y_increase = ship.y_increase*0.24
            ship.one = ship.one*0.4
        elif x1 - x2 < 20 and x2 - x1 > 10:
            ship.y_increase = ship.y_increase*0.12
            ship.one = ship.one*0.2
        elif x1 - x2 < 10:
            ship.y_increase = ship.y_increase*0.06
            ship.one = ship.one*0.06
    #Simaler ideas here, trying to reduce the impact this glitch has on the system by multiplying y_increase and one by smaller numbers
    return ship.y_increase, ship.slope, ship.one
    #Returns new object variables 



def calc_dist(x1, y1, x2, y2):
    dist = (x2 - x1)**2 + (y2 - y1)**2
    dist = math.sqrt(dist)
    return dist
#Function that simply calculates and returns distance. 
#x1 and y1 are the x and y coords for the first point, x2 and y2 the coords for the other one.



###########################################################################
#Functions that deal with object interactions
###########################################################################
def check_in_box(x1, y1, x2, y2, box_dim):
    #x1 and y1 are coordinates of middle of boat
    #x2 and y2 are coordinates of clicked point
    if x2 <= x1 + box_dim[0] and x2 >= x1 - box_dim[0] and y2 <= y1 + box_dim[1] and y2 >= y1 - box_dim[1]:
        return True
    else:
        return False
#Function returns True if point is in object's hit box, False if not



def checking_click_in_choose_box(ship_image, ship_obj,  win, objects_list, objects_list_org, player_ships_list, player_missle_list, enemy_missle_list, enemy_ships_list):
#Function to run if the player has clicked on a ship, to create a menu for the player to choose options.
    if ship_obj.type == 2:   
        if ship_image.getAnchor().getY() <= 315:
            sign = Image(Point(ship_image.getAnchor().getX(), ship_image.getAnchor().getY() + 30), "blue_sign_car.gif")
            sign.draw(win)
            clicked2 = win.getMouse()
            #If the player clicks on a carrier, and the ship is on the upper half of the y-axis, then the sign is placed bellow the ship
        else:
            sign = Image(Point(ship_image.getAnchor().getX(), ship_image.getAnchor().getY() - 30), "blue_sign_car.gif")
            sign.draw(win)
            clicked2 = win.getMouse()
            #If the player clicks on a carrier, and the ship is on the lower half of the y-axis, then the sign is placed above the ship
    elif ship_obj.type == 1 and ship_obj.state_defence == True:
        if ship_image.getAnchor().getY() <= 315:
            sign = Image(Point(ship_image.getAnchor().getX(), ship_image.getAnchor().getY() + 30), "blue_sign_bat_figh.gif")
            sign.draw(win)
            clicked2 = win.getMouse()
        else:
            sign = Image(Point(ship_image.getAnchor().getX(), ship_image.getAnchor().getY() - 30), "blue_sign_bat_figh.gif")
            sign.draw(win)
            clicked2 = win.getMouse()
            #If the player is a battleship and is on offensive (fight) mode, then the menu with the sign to change to defensive mode is drawn
            #Notes: The sign still also has the movement icon as well, and there are still simaler checks for the position of the ship allong the y-axis too
    elif ship_obj.type == 1 and ship_obj.state_defence == False:
        if ship_image.getAnchor().getY() <= 315:
            sign = Image(Point(ship_image.getAnchor().getX(), ship_image.getAnchor().getY() + 30), "blue_sign_bat_def.gif")
            sign.draw(win)
            clicked2 = win.getMouse()
        else:
            sign = Image(Point(ship_image.getAnchor().getX(), ship_image.getAnchor().getY() - 30), "blue_sign_bat_def.gif")
            sign.draw(win)
            clicked2 = win.getMouse()
            #The opposite code is here for ships that are on defensive mode
    #Initial check if statemnt to see if the menu needs to be placed bellow or above the ship

    if clicked2.getX() < sign.getAnchor().getX() and clicked2.getX() > sign.getAnchor().getX() - 20 and \
        clicked2.getY() < sign.getAnchor().getY() + 13 and clicked2.getY() > sign.getAnchor().getY() - 14:
        if ship_obj.type == 2:
            sign.undraw()
            clicked3 = win.getMouse()
            create_missles(ship_image, ship_obj, clicked3.getX(), clicked3.getY(), objects_list, objects_list_org, player_missle_list, enemy_missle_list, player_ships_list, enemy_ships_list, win)
        elif ship_obj.type == 1 and ship_obj.state_defence == False:
            sign.undraw()
            ship_obj.state_defence = True
        elif ship_obj.type == 1 and ship_obj.state_defence == True:
            sign.undraw()
            ship_obj.state_defence = False
    #First check to see if the left-most box is clicked on. If so, check if the ship is a battleship or carrier. If carrier, then create missles thorugh create_missles function.
    #Otherwise, if battleship, check which state defence/offense is on, and display the sign with a symbol representing the opposite side to allow player to change states.
    elif clicked2.getX() > sign.getAnchor().getX() and clicked2.getX() < sign.getAnchor().getX() + 20 and \
        clicked2.getY() < sign.getAnchor().getY() + 13 and clicked2.getY() > sign.getAnchor().getY() - 14:                    
        sign.undraw()
        clicked2 = win.getMouse()
        ship_obj.destinationx = int(clicked2.getX())
        ship_obj.destinationy = int(clicked2.getY())
    #Second check to see if right-most box is clicked on, if so, then create a new clicked to find a new destination, and re-assign the ship's destination there.
        if (clicked2 != None):
            draw_place(clicked2, win)
            ship_obj.movements +=1
            calc_slope(int(ship_image.getAnchor().getX()), int(ship_image.getAnchor().getY()), int(clicked2.getX()), int(clicked2.getY()), ship_obj)
            #After re-assigning destination coords, re-calculate slope, and add to object movements to ensure that object can move.
    else:
        sign.undraw()
    #If the player clicks on any other area that is not inside the choice boxes to move/launch missles/change state, then the sign is undrawn anyways, to avoid haveing the sign remain after the code moves on



###########################################################################
#Functions that deal with enemy health
###########################################################################
def check_enemy_ships(win, ship, ship_image, objects_list_org, objects_list, enemy_ships_list): 
    for e_ships in enemy_ships_list:
        e_ships_image = objects_list_org[e_ships]
        if e_ships.type == 1 or e_ships.type == 3:
            if calc_dist(ship_image.getAnchor().getX(), ship_image.getAnchor().getY(), e_ships_image.getAnchor().getX(), e_ships_image.getAnchor().getY()) < 64:
                if ship.type == 1 or ship.type == 3:
                    if ship.state_defence == True:
                        if e_ships.state_defence == True:
                            ship.health -= e_ships.damage/2
                            e_ships.health -= ship.damage/2
                        else:
                            ship.health -= e_ships.damage
                            e_ships.health -= ship.damage
                    else:
                        if e_ships.state_defence == True:
                            ship.health -= e_ships.damage
                            e_ships.health -= ship.damage
                        else:
                            ship.health -= e_ships.damage*2
                            e_ships.health -= ship.damage*2
                else:
                    if e_ships.state_defence == True:
                        ship.health -= e_ships.damage/2
                        e_ships.health -= ship.damage/2
                    else:
                        ship.health -= e_ships.damage
                        e_ships.health -= ship.damage
                hit(Point(ship_image.getAnchor().getX(), ship_image.getAnchor().getY()), win)
        #Check if the opposeing ship is a battleship, if so, then check if the distance is close enough. If so, then check if defending ship is a battleship.
        #Depending on if the ships are battelships, and if they are on defence or offence, then each ship may take diffrent amounts of damage depending on how those states interact.

        elif e_ships.type == 2 or e_ships.type == 4: 
            if calc_dist(ship_image.getAnchor().getX(), ship_image.getAnchor().getY(), e_ships_image.getAnchor().getX(), e_ships_image.getAnchor().getY()) < 64: 
                if ship.type == 1 or ship.type == 3 and ship.state_defence == True:
                    ship.health -= e_ships.damage/2
                    e_ships.health -= ship.damage
                    hit(Point(ship_image.getAnchor().getX(), ship_image.getAnchor().getY()), win)
                else:
                    ship.health -= e_ships.damage
                    e_ships.health -= ship.damage*2
                    hit(Point(ship_image.getAnchor().getX(), ship_image.getAnchor().getY()), win)
        #Check if the opposeing ship is a carrier, if so, then check if the distance is close enough. If so, then depending on if the defending ship is a carrier or battleship, both ships will take diffrent amounts of damage.

        elif e_ships.type == 5 or e_ships.type == 6:
            if calc_dist(ship_image.getAnchor().getX(), ship_image.getAnchor().getY(), e_ships_image.getAnchor().getX(), e_ships_image.getAnchor().getY()) < 30:
                ship.health -= e_ships.damage
        #Check if the opposeing ship is a missle. If so, then calculate distance, if nearby, then have the ship take damage.
    return win, ship, ship_image, objects_list_org, enemy_ships_list
#Function that runs for every ship, and checks if the ship has any opposeing ships nearby, and if the ship needs to lose health because of that.
#Note: In order to speed up and make ship interactions more dangerous, all ship interactions besides ship-missle interactions have both ships lose health.



###########################################################################
#Functions that deal with missles
###########################################################################
def create_missles(image, ship, clickedx, clickedy, objects_list, objects_list_org, player_missle_list, enemy_missle_list, side_ships_list, enemy_ships_list, win):
#Function that creates new missles and addes them to object lists if the ship running create_missles has enough ammo left.
    if ship.type == 2 and ship.ammo > 0:
        player_missle_1 = Planes(image.getAnchor().getX(), image.getAnchor().getY(), clickedx, clickedy, 1, 0, 0, 0, 5)
        player_missle_01 = Image(Point(image.getAnchor().getX(), image.getAnchor().getY()), "blue_missle.gif")
        calc_slope(image.getAnchor().getX(), image.getAnchor().getY(), clickedx, clickedy, player_missle_1)
        #Creates a missle and calculates basic variables like slope for it

        player_missle_01.draw(win)
        objects_list.append(player_missle_1)
        objects_list_org[player_missle_1] = player_missle_01
        player_missle_list.append(player_missle_1)
        side_ships_list.append(player_missle_1)
        ship.ammo -= 1
        #Adds newly created missle to lists of objects, draws it, and minuses 1 from the ammo fo the ship
    elif ship.type == 4 and ship.ammo > 0:
        enemy_missle_1 = Planes(image.getAnchor().getX(), image.getAnchor().getY(), clickedx, clickedy, 1, 0, 0, 0, 6)
        enemy_missle_01 = Image(Point(image.getAnchor().getX(), image.getAnchor().getY()), "red_missle.gif")

        enemy_missle_01.draw(win)
        objects_list.append(enemy_missle_1)
        objects_list_org[enemy_missle_1] = enemy_missle_01
        player_missle_list.append(enemy_missle_1)
        side_ships_list.append(enemy_missle_1)
        ship.ammo -= 1 
        calc_slope(image.getAnchor().getX(), image.getAnchor().getY(), clickedx, clickedy, enemy_missle_1)
        #Same, but for enemy ai ships, so with diffrent lists.