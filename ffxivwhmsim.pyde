'''
@author Kiwi
@date 2021.09.09

I'm trying to implement a wall to wall dungeon pull simulator 
for FFXIV's white mage class.

commit schedule
.   draw an icon :P be able to tint the alpha to make it look unavailable
.   font: meiryo is the ffxiv font
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
    global benison, holy, regen
    
    colorMode(HSB, 360, 100, 100, 100)
    rectMode(CENTER)
    size(640, 360)
    
    mono = createFont("Meiryo-01.ttf", 12)
    # mono = createFont("MeiryoUI-03.ttf", 12)
    textFont(mono)
    noSmooth()
    
    benison = loadImage("icons/divine benison.png")
    holy = loadImage("icons/holy.png")
    regen = loadImage("icons/regen.png")
    

def draw():
    global benison, holy, regen
        
    background(209, 95, 33)
    
    # this is the alpha tint for images
    tint(0, 0, 100, 100)
    image(benison, width/2, height/2)
    
    
    tint(0, 0, 100, 80)
    image(holy, width/2+68, height/2)
    
    
    tint(0, 0, 100, 40)
    image(regen, width/2+68+68, height/2)
    # image(benison, mouseX, mouseY)
    
    # remember that bit-shifting twice to the right is dividing by 4
    text("Divine Benison, Holy, and Regen\nCody Berry", width>>2, height>>2)
    

def mousePressed():
    print(millis())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
