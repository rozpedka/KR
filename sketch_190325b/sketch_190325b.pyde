def setup():
    size(400,400)
    textSize(100)
    textAlign(LEFT)
    c = color(255, 204, 0)
def draw():
    background(0)
    #if mousePressed:
    text("K", height/2-60, width/2)
    text("R", height/2, width/2)
    if (mouseX >= 155 and mouseX <=200):
        fill(255, 204, 0)
        text("K", height/2-60, width/2)
        fill(255)
    if keyPressed:
        text("R", height/2, width/2)
    if (mouseX >= 200 and mouseX <=255):
        fill(255,0,255)
        text("R", height/2, width/2)
        fill(255)
    if keyCode == 39:
        text("K", height/2-60, width/2)
        fill(255, 204, 0)
        text("R", height/2, width/2)
        fill(255)
    if keyPressed:
        fill(155)
        if key =='K' or key =='k':
            fill(255,0,0)
            text("K", height/2-60, width/2)
            fill(155)
            
    if keyPressed:
        fill(155)
        if key =='R' or key =='r':
            fill(255,0,0)
            text("R", height/2, width/2)
            fill(155)
    s = createShape()
    s.beginShape()
    s.fill(100, 0, 100)
    s.noStroke()
    s.vertex(100, height/3*2)
    s.vertex(150, height/3*2-20)
    s.vertex(width/2, height/3*2)
    s.vertex(width-150, height/3*2+20)
    s.endShape(CLOSE)
    shape(s, 25, 25)
