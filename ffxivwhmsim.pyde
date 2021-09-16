'''
@author Kiwi
@date 2021.09.09

I'm trying to implement a wall to wall dungeon pull simulator 
for FFXIV's white mage class.

commit schedule
.   draw an icon :P be able to tint the alpha to make it look unavailable
.   font: meiryo is the ffxiv font
.   method to resize 48x48 border shadow and overlay on top of icon 
.   add little circle that animates. use arc!
.       see https://puu.sh/IadsX/d92dbbdd1c.jpg
.   cooldown effect
.       contour? blendmode? blendmode cannot restore lost alpha
.   custom pShape with contour. this caused crashes
.   noFill inner shape? doesn't work unless your "shape" is the stroke :P
    timer class for the 2.5s GCD, among others
        .isfinished? or global gamestates of GCD-locked, oGCD-locked?
        when I perform an action
.   create 3 spells: benison, holy, regen
        record sounds
        rip images
    push hotkey to activate empty spell + sound
    state based model: 
        GCD ready: 2.5s after GCD ability, queue-ing ready 75% of the way
        oGCD ready: while GCD is cooling down or not. oGCDs have anim_lock
    cooldown circle animation
    spell types: GCD cast, GCD instant, oGCD
    spell queue system
    display UI
        white mage recorded sounds and icons
    player class and HP
    tank class: autonomous. model incoming damage 
    tank incoming damage simulation

additions
    lily gauge
    yellow proc dashed outline effect
    add tank cooldown rotation
    spell evolution: speed, potency, mana
  
'''

def setup():
    global benison, holy, regen, border, cooldown, benison_alpha_full, action
    
    colorMode(HSB, 360, 100, 100, 100)
    rectMode(CENTER)
    size(640, 360, P2D)
    
    mono = createFont("Meiryo-01.ttf", 12)
    # mono = createFont("MeiryoUI-03.ttf", 12)
    textFont(mono)
    # noSmooth()
    
    cooldown = 0 # ranges from 0-100%
    benison_alpha_full = True
    action = False # no GCD action execution atm
    
    # unlike the other images, border.png is a transparent glass frame that's off center
    # it actually provides shading on all four sides;
    #     3 pixels each side
    #     1 px on top
    #     5 px on bottom
    # this essentially makes the center 42x42
    # we can use draw_icon as is, or resize to 38 and resize the icons to 32x32
    #     modify x and y coordinates in draw_icon to -3, -1.5 instead of -6, -3
    border = loadImage("border.png")
    border.resize(76, 76)
    benison = loadImage("whm/divine benison.png")
    holy = loadImage("whm/holy.png")
    regen = loadImage("whm/regen.png")
    

def draw():
    global benison, holy, regen, border, cooldown, benison_alpha_full, action
        
    background(209, 95, 33)
        
    if benison_alpha_full:
        draw_icon(benison, 100, width/2, height/2)
    else:
        draw_icon(benison, 75, width/2, height/2)
    draw_icon(holy, 100, width/2+68, height/2)    
    draw_icon(regen, 100, width/2+68+68, height/2)

    
    # remember that bit-shifting twice to the right is dividing by 4
    fill(0, 0, 100, 100)
    text("Divine Benison, Holy, and Regen\n[Cody Berry, Lv.72 White Mage]", width>>2, height>>2)
    
    # this needs to be calculated to fit the start, stop arguments as they are positive
    # clockwise starting at 0 vs our timer which is clockwise starting at PI/2
    # negative arguments aren't allowed?
    
    # fills the arc so when cooldown ranges from 0-100, the arc completes 2π
    if action:
        c = map(cooldown, 0, 100, -PI/2, 3*PI/2)
        if c > 3*PI/2:
            benison_alpha_full = True
        else:            
            noStroke()
            # winry: drawing background color over it simulates icon transparency
            fill(209, 95, 33, 20)
            rect(width/2+32, height/2+32, 64, 64)
            
            stroke(0, 0, 100)
            strokeWeight(1.5)
            blendMode(ADD)
            fill(0, 0, 100, 15)
            arc(width/2+32, height/2+32, 62, 64, -PI/2, c, PIE)
            blendMode(BLEND)
    cooldown += 0.6
    
    
# displays a 64x64 icon and adjusts the border appropriately
def draw_icon(img, a, x, y):
    # a is the alpha value
    tint(0, 0, 100, a)
    image(img, x, y)
    tint(0, 0, 100, 100)
    image(border, x-6, y-3)   

def mousePressed():
    global action, cooldown, benison_alpha_full
    action = True
    benison_alpha_full = False
    cooldown = 0
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
