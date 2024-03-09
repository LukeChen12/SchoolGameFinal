#Test file: DO NOT TAKE SERIOUSLY
#Ull be fine prob
from graphics import *
run_times = 0
one = 0
slope = 0
save_click = 0
y_increase = 0

ship_box = (20, 10)


def ship_movement(ship, clicked, slope, save_click):
    x = ship.getAnchor().getX()
    y = ship.getAnchor().getY()
    slope = (y - clicked.getY())/(x - clicked.getX())
    save_click = clicked
    circ = Circle(save_click, 50)
    circ.draw(win)
    return save_click, slope


while True:
    if run_times < 1:
        win = GraphWin("Sea", 500, 500)
        win.setBackground(color_rgb(8, 15, 51))
        org_coords = (250, 250)
        
        battleship = Image(Point(org_coords[0], org_coords[1]), "C:/Users/user/Downloads/VSCODE Files/Python work/ShipProject/battleshipblueicon.gif")
        carrier = Image(Point(battleship.getAnchor().getX() - 50, battleship.getAnchor().getY() - 50), "C:/Users/user/Downloads/VSCODE Files/Python work/ShipProject/carrierblueicon.gif")
        in_group = True
        
        battleship.draw(win)
        carrier.draw(win)
        run_times += 1

    clicked = win.checkMouse()
    #clicked.draw(win)

    if (clicked != None):
        #ship_movement(battleship, clicked, slope, save_click)
        if (battleship.getAnchor().getY() - clicked.getY()) == 0:
            one = 0
            if battleship.getAnchor().getY() < clicked.getY():
                y_increase = y_increase*-1
            else:
                y_increase = y_increase*1
        elif (battleship.getAnchor().getX() - clicked.getX()) == 0:
            y_increase = 0
        else:
            slope = (battleship.getAnchor().getY() - clicked.getY())/(battleship.getAnchor().getX() - clicked.getX())
        circ = Circle(clicked, 50)
        circ.draw(win)
            
        if battleship.getAnchor().getX() > clicked.getX():
            one = -1           
        else:
            one = 1
        if battleship.getAnchor().getY() > clicked.getY():
            y_increase = y_increase*-1           
        else:
            y_increase = y_increase*1
    
    print(battleship.getAnchor().getX())

    y_increase = slope*one

    time.sleep(0.1)
    battleship.move(one, y_increase)
    if in_group == True:
        carrier.move(one, y_increase)

    """if (clicked != None):
        if (save_click.getX() < (battleship.getAnchor().getX() + ship_box[0]) and
        clicked.getX() > battleship.getAnchor().getX() - ship_box[0] and
        clicked.getY() < battleship.getAnchor().getY() + ship_box[1] and
        clicked.getY() > battleship.getAnchor().getY() - ship_box[1]):
            y_increase = 0
            one = 0"""
