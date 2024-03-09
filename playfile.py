from graphics import *

def main():
    win = GraphWin("Sea", 500, 500)
    win.setBackground(color_rgb(8, 15, 51))
    org_coords = (250, 250)
    
    battleship = Image(Point(org_coords[0], org_coords[1]), "C:/Users/user/Downloads/VSCODE Files/Python work/ShipProject/battleshipblueicon.gif")
    carrier = Image(Point(100, 100), "C:/Users/user/Downloads/VSCODE Files/Python work/ShipProject/carrierblueicon.gif")
    battleship.draw(win)
    carrier.draw(win)
    clicked = win.getMouse()
    clicked.draw(win)
    #p = Line(Point(clickPoint[0], clickPoint[1]), Point(org_coords[0], org_coords[1]))
    #p.draw(win)

    slope = (org_coords[1] - clicked[1])/(org_coords[0] - clicked[0])
    
    if org_coords[0] > clicked[0]:
        one = -1
    else:
        one = 1

    y_increase = one*slope

    while True:
        time.sleep(0.1)
        battleship.move(one, y_increase)
    
 
"""
    while True:
        time.sleep(0.1)
        k = win.getKey() 
        if k == "Right":
            battleship.move(3, -3)
"""
main()

    



