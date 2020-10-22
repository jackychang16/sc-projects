"""
File: my_drawing
Name:JackyChang
----------------------
"""

from campy.graphics.gobjects import GOval, GRect,GPolygon,GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause

VY = 5
DELAY = 30


def main():
    window = GWindow(width=1000, height=700, title="Mike")

    background = GRect(1000,700)
    background.filled = True
    background.fill_color = "cornsilk"
    window.add(background)

    hand = GPolygon()
    hand.add_vertex((490,400))
    hand.add_vertex((500,470))
    hand.add_vertex((380,340))
    hand.add_vertex((380,340))
    hand.filled = True
    hand.fill_color = "limegreen"
    hand.color = "limegreen"
    window.add(hand)

    r_hand =GPolygon()
    r_hand.add_vertex((835, 470))
    r_hand.add_vertex((820, 535))
    r_hand.add_vertex((960, 595))
    r_hand.filled = True
    r_hand.fill_color = "limegreen"
    r_hand.color = "limegreen"
    window.add(r_hand)


    l_ear = GPolygon()
    l_ear.add_vertex((830, 224))
    l_ear.add_vertex((815, 160))
    l_ear.add_vertex((780, 180))
    l_ear.filled = True
    l_ear.fill_color = 'forestgreen'
    l_ear.color = 'forestgreen'
    window.add(l_ear)

    r_ear = GPolygon()
    r_ear.add_vertex((580, 180))
    r_ear.add_vertex((545, 160))
    r_ear.add_vertex((530, 224))
    r_ear.filled = True
    r_ear.fill_color = 'forestgreen'
    r_ear.color = 'darkkhaki'
    window.add(r_ear)



    face = GOval(400,450)
    face.filled = True
    face.fill_color ="greenyellow"
    face.color = "greenyellow"
    window.add(face,480,150)

    mouth = GOval(280, 330)
    mouth.filled = True
    mouth.fill_color = "darkolivegreen"
    # mouth.color = "darksage"
    window.add(mouth, 555, 230)

    # mouth_upper = GOval(310, 390)
    # mouth_upper.filled = True
    # mouth_upper.fill_color = "greenyellow"
    # mouth_upper.color = "greenyellow"
    # window.add(mouth_upper, 530, 130)

    teeth_1 = GPolygon()
    teeth_1.add_vertex((800,460))
    teeth_1.add_vertex((750,460))
    teeth_1.add_vertex((775,520))
    teeth_1.filled = True
    teeth_1.fill_color = "white"
    teeth_1.color = "white"
    window.add(teeth_1)

    teeth_2 = GPolygon()
    teeth_2.add_vertex((770, 480))
    teeth_2.add_vertex((685, 480))
    teeth_2.add_vertex((725, 540))
    teeth_2.filled = True
    teeth_2.fill_color = "white"
    teeth_2.color = "white"
    window.add(teeth_2)

    teeth_3 = GPolygon()
    teeth_3.add_vertex((720, 485))
    teeth_3.add_vertex((635, 485))
    teeth_3.add_vertex((685, 545))
    teeth_3.filled = True
    teeth_3.fill_color = "white"
    teeth_3.color = "white"
    window.add(teeth_3)

    teeth_4 = GPolygon()
    teeth_4.add_vertex((660, 485))
    teeth_4.add_vertex((610, 490))
    teeth_4.add_vertex((645, 540))
    teeth_4.filled = True
    teeth_4.fill_color = "white"
    teeth_4.color = "white"
    window.add(teeth_4)

    greenyellow = GRect(100,100)
    greenyellow.filled = True
    greenyellow.fill_color ="greenyellow"
    greenyellow.color = "greenyellow"
    window.add(greenyellow,735,270)


    mouth_upper1 =GOval(350,210)
    mouth_upper1.filled =True
    mouth_upper1.fill_color = "greenyellow"
    mouth_upper1.color ="greenyellow"
    window.add(mouth_upper1,490,290)

    inner_face = GOval(240,260)
    inner_face.filled = True
    inner_face.fill_color = "white"
    window.add(inner_face,560,180)

    eye = GOval(120,120)
    eye.filled = True
    eye.fill_color = 'green'
    window.add(eye,620,235)

    inner_eye = GOval(60,60)
    inner_eye.filled = True
    inner_eye.fill_color = "black"
    window.add(inner_eye,650,265)

    eye_ball = GOval(20,20)
    eye_ball.filled = True
    eye_ball.fill_color ='white'
    eye_ball.color = 'white'
    window.add(eye_ball,651,265)



    l_leg = GPolygon()
    l_leg.add_vertex((574,567))
    l_leg.add_vertex((612,585))
    l_leg.add_vertex((600,700))
    l_leg.add_vertex((590,700))
    l_leg.filled =True
    l_leg.fill_color ="limegreen"
    l_leg.color ="limegreen"
    window.add(l_leg)

    r_leg = GPolygon()
    r_leg.add_vertex((747, 585))
    r_leg.add_vertex((785, 566))
    r_leg.add_vertex((770, 700))
    r_leg.add_vertex((759, 700))
    r_leg.filled = True
    r_leg.fill_color = "limegreen"
    r_leg.color ="limegreen"
    window.add(r_leg)


    stancode = GLabel("stanCode")
    stancode.color = "crimson"
    stancode.font = "Times New Roman-120"
    window.add(stancode,50,250)
    #
    # global VY
    #
    # while True:
    #     stancode.move(0,VY)
    #
    #     if stancode.y - stancode.height <= 0 or stancode.y >320:
    #         VY = -VY
    #     pause(DELAY)
    #
    #     if stancode.y >320:
    #         hand.move(0,VY*4)
    #
    #     if stancode.y - stancode.height <=0 :
    #         window.add(hand,500,400)
    #         hand.move(0,VY*1)
    #         hand.move(0, VY * 1)
    #         hand.move(0, VY * 1)
    #         hand.move(0, VY * 1)






if __name__ == '__main__':
    main()
