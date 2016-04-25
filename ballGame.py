from tkinter import *
import random

####################################
# customize these functions
####################################

def init(data):
    data.margin = 10
    data.boardWidth = data.width - data.margin*2
    data.boardHeight = data.height - data.margin*2
    data.blockLength = data.boardHeight//6
    data.blockWidth = 10
    data.block2cy = data.height//2
    data.block1cy = data.height//2
    data.scoreLeft = 6843
    data.scoreRight = 6581
    initBall(data)
    data.blockStep = 4


def initBall(data):
    data.ballcx = data.width//2
    data.ballcy = data.height//2
    data.ballR = data.blockLength//4
    data.ballDir = [random.choice([-7,-5,-3,3,5,7]),
                    random.choice([-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7])]
    data.counter = 0

def drawBoard(canvas, data):
    canvas.create_rectangle(data.margin, data.margin, data.width-data.margin,
        data.height-data.margin, fill = 'black')
    canvas.create_line(data.width//2, data.margin, data.width//2,
        data.height-data.margin, fill = 'white', width = 3)
    canvas.create_text(data.margin+data.boardWidth//4, data.margin, 
        anchor = 'n', text = '{0}'.format(data.scoreLeft), font = 'Times 26',
        fill = 'white')
    canvas.create_text(data.margin+3*data.boardWidth//4, data.margin, 
        anchor = 'n', text = '{0}'.format(data.scoreRight), font = 'Times 26',
        fill = 'white')

def drawBall(canvas, data):
    canvas.create_oval(data.ballcx-data.ballR, data.ballcy-data.ballR,
        data.ballcx+data.ballR, data.ballcy+data.ballR, fill = 'white')

def drawBlock(canvas, data):
    canvas.create_rectangle(data.margin, data.block1cy-data.blockLength//2,
        data.margin+data.blockWidth,data.block1cy+data.blockLength//2,
        fill = 'white')
    canvas.create_rectangle(data.width-data.margin-data.blockWidth, 
        data.block2cy-data.blockLength//2, data.width-data.margin,
        data.block2cy+data.blockLength//2,
        fill = 'white')

def hitEdge(data):
    if (((data.ballcy - data.ballR) <= data.margin) or
        (data.ballcy + data.ballR) >= (data.height-data.margin)):
        data.ballDir[1] *= -1

def outOfBoard(data):
    if data.ballcx-data.ballR <= data.margin:
        data.scoreRight += 1
        initBall(data)
    elif data.ballcx+data.ballR >= data.width-data.margin:
        data.scoreLeft += 1
        initBall(data)

def hitBlock(data):
    if (data.ballcy > data.block1cy-data.blockLength//2 and 
        data.ballcy < data.block1cy+data.blockLength//2 and
        data.ballcx-data.ballR <= data.margin+data.blockWidth):
        data.ballDir[0] *= -1
    elif (data.ballcy > data.block2cy-data.blockLength//2 and 
        data.ballcy < data.block2cy+data.blockLength//2 and
        data.ballcx+data.ballR >= data.width - data.margin - data.blockWidth):
        data.ballDir[0] *= -1

def moveBlock(data):
    if data.ballcx < data.width//2:
        if data.block1cy < data.ballcy:
            data.block1cy += data.blockStep
        elif data.block1cy > data.ballcy:
            data.block1cy -= data.blockStep
    else:
        if data.block1cy < data.height//2:
            data.block1cy += data.blockStep
        elif data.block1cy > data.height//2:
            data.block1cy -= data.blockStep
    if data.ballcx > data.width//2:
        if data.block2cy < data.ballcy:
            data.block2cy += data.blockStep
        elif data.block2cy > data.ballcy:
            data.block2cy -= data.blockStep
    else:
        if data.block2cy < data.height//2:
            data.block2cy += data.blockStep
        elif data.block2cy > data.height//2:
            data.block2cy -= data.blockStep

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    if event.keysym == 'r':
        init(data)

def timerFired(data):
    data.ballcx += data.ballDir[0]
    data.ballcy += data.ballDir[1]
    data.counter += 1
    if data.counter % 100 == 0:
        data.ballDir[0] *= 1.1
    if data.counter >= 2000:
        initBall(data)
        data.counter = 0
    hitEdge(data)
    outOfBoard(data)
    hitBlock(data)
    moveBlock(data)

def redrawAll(canvas, data):
    drawBoard(canvas,data)
    drawBall(canvas, data)
    drawBlock(canvas, data)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(600, 400)
