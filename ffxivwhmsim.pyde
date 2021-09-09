'''
@author Kiwi
@date 2021.09.09

I'm trying to implement a wall to wall dungeon pull simulator 
for FFXIV's white mage class.

commit schedule
   timer for the 2.5s GCD, among others
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
   add tank cooldown rotation
   spell evolution: speed, potency, mana
  
'''


def setup():
    colorMode(HSB, 360, 100, 100, 100)
    rectMode(CENTER)
    size(640, 360)

def draw():    
    background(209, 95, 33)
    square(mouseX, mouseY, 50)

def mousePressed():
    print(millis())
