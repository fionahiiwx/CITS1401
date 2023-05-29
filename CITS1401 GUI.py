import CITS1401_graphics as gx

def main():
    win = gx.GraphWin()

    p1 = gx.Point(25, 80)
    p1.draw(win)
    p2 = gx.Point(180, 190)
    p2.draw(win)

    for px in range(50, 151):
        pt = gx.Point(px, px)
        pt.draw(win)

    l = gx.Line(p1, p2)
    l.draw(win)

    rec = gx.Rectangle(p1,p2)
    rec.setFill("lightblue")
    rec.draw(win)

    rec.move(10,10)

    # Circle(point for centre of circle, radius)
    circle = gx.Circle(gx.Point(100,100), 45)
    circle.setFill("pink")
    circle.draw(win)

    # Text(cntre, word)
    text = gx.Text(gx.Point(80,80), "This is CITS1401")
    text.draw(win)

    oval = gx.Oval(gx.Point(20, 150), gx.Point(180, 199))
    oval.draw(win)

    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()