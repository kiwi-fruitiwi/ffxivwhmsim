'''
@author Kiwi
@date 2021.09.09

I'm trying to implement a wall to wall dungeon pull simulator 
for FFXIV's white mage class.

commit schedule
.   draw an icon :P be able to tint the alpha to make it look unavailable
.   font: meiryo is the ffxiv font
.   method to resize 48x48 border shadow and overlay on top of icon 
    add little circle that animates
        see https://puu.sh/IadsX/d92dbbdd1c.jpg
    timer for the 2.5s GCD, among others
        when I perform an action
    create 3 spells: benison, holy, regen
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
    global benison, holy, regen, border
    
    colorMode(HSB, 360, 100, 100, 100)
    rectMode(CENTER)
    size(640, 360)
    
    mono = createFont("Meiryo-01.ttf", 12)
    # mono = createFont("MeiryoUI-03.ttf", 12)
    textFont(mono)
    noSmooth()
    
    # unlike the other images, border.png is a transparent glass frame that's off center
    # it actually provides shading on all four sides;
    #     3 pixels each side
    #     1 px on top
    #     5 px on bottom
    # this essentially makes the center 42x42
    border = loadImage("icons/border.png")
    border.resize(76,76)
    benison = loadImage("icons/divine benison.png")
    holy = loadImage("icons/holy.png")
    regen = loadImage("icons/regen.png")
    

def draw():
    global benison, holy, regen, border
        
    background(209, 95, 33)
    
    draw_icon(benison, 100, width/2, height/2)    
    draw_icon(holy, 80, width/2+68, height/2)    
    draw_icon(regen, 50, width/2+68+68, height/2)

    
    # remember that bit-shifting twice to the right is dividing by 4
    text("Divine Benison, Holy, and Regen\n[Cody Berry, Lv.72 White Mage]", width>>2, height>>2)


# displays a 64x64 icon and adjusts the border appropriately
def draw_icon(img, a, x, y):
    # a is the alpha value
    tint(0, 0, 100, a)
    image(img, x, y)
    tint(0, 0, 100, 100)
    image(border, x-6, y-3)   
    

def mousePressed():
    print(millis())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
