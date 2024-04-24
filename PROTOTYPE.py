#############################################################
#Author: Sanjay Suthakaran
#Description: Turn Based Battle Sim Prototype
#Date Created: Dec 21 2021
#Last Modified: Jan 19 2022
#############################################################

###NOTES###
#This was a grade 12 final project created by me to become familiar with python.
#Character sprites are from Shovel Knight, Terraria, and Castlevania.
#BGM is from Shovel Knight, Deltarune, and Final Fantasy VII


###LIBRARIES###
from winsound import *
from pygraphics1 import *
import time
import random
#PlaySound("rude buster.wav", SND_ALIAS | SND_ASYNC)


###TITLE SCREEN###
class Win:
    def mainmenu(self):
        win = GraphWin("Prototype", 500, 500)
        win.setCoords(0.0, 0.0, 5.0, 5.0)
        win.setBackground("black")

        #TITLE
        PlaySound("title.wav", SND_ALIAS | SND_ASYNC)
        title = Text(Point(2.5,3),"TURN-BASED BATTLE\nSIMULATOR!!")
        title.setSize(30)
        title.setFace("courier")
        title.setTextColor("white")
        title.draw(win)

        #PLAY BUTTON
        play = Rectangle(Point(1.5,2),Point(3.5,1))
        play.setOutline("white")
        play.draw(win)
        text = Text(Point(2.5,1.5),"PLAY!")
        text.setTextColor("red")
        text.setFace("courier")
        text.setSize(20)
        text.draw(win)
        while True:
            playbutton = win.getMouse()
            x = playbutton.getX()
            y = playbutton.getY()
            if 1.5 <= x <= 3.5 and 1 <= y <= 2:
                title.undraw()
                play.undraw()
                playbutton.undraw()
                text.undraw()
                self.difficulty(win)

    def difficulty(self,win):
        title = Text(Point(2.5, 3), "DIFFICULTY!?")
        title.setSize(30)
        title.setFace("courier")
        title.setTextColor("white")
        title.draw(win)

        easy = Rectangle(Point(0.5, 2), Point(2.4, 1))
        easy.setOutline("white")
        easy.draw(win)
        textez = Text(Point(1.4, 1.5), "EASY")
        textez.setTextColor("lime")
        textez.setFace("courier")
        textez.setSize(20)
        textez.draw(win)

        challenging = Rectangle(Point(2.6, 2), Point(4.5, 1))
        challenging.setOutline("white")
        challenging.draw(win)
        textchg = Text(Point(3.6, 1.5), "CHALLENGING!")
        textchg.setTextColor("yellow")
        textchg.setFace("courier")
        textchg.setSize(18)
        textchg.draw(win)

        while True:
            playbutton = win.getMouse()
            x = playbutton.getX()
            y = playbutton.getY()

            #IF EASY IS CHOSEN
            if 0.5 <= x <= 2.4 and 1 <= y <= 2:
                easy.undraw()
                title.undraw()
                textez.undraw()
                challenging.undraw()
                textchg.undraw()
          #      difficulty = "easy"
                self.easybattle(win)

            #IF CHALLENGING IS CHOSEN
            elif 2.6 <= x <= 4.5 and 1<= y <= 2:
                easy.undraw()
                title.undraw()
                textez.undraw()
                challenging.undraw()
                textchg.undraw()
              #  difficulty = "challenging"
                calcium = False

                self.challengingbattle(win,calcium)


    #EASY DIFFICULTY
    def easybattle(self,win):
        PlaySound("rude buster.wav", SND_ALIAS | SND_ASYNC)
        time.sleep(1)
        Image(Point(2.5,2.5),"background.png").draw(win)

        #PLAYER
        specter = Image(Point(1, 2), "specter1.png")
        specter.draw(win)
        playerhp = 100

        #ENEMY
        #slime = Image(Point(4, 1.5), "slime1.png")
        #slime.draw(win)
        enemyhp = 150

        specter.undraw()
        #slime.undraw()

        #BATTLE
        while enemyhp >= 0 or playerhp >= 0:
            vanish = False
            defend = False
            specter = Image(Point(1, 2), "specter1.png")
            specter.draw(win)
            vanish = ""

            slime = Image(Point(4, 1.5), "slime1.png")
            slime.draw(win)

            GUI = Rectangle(Point(0, 1), Point(5, 0))
            GUI.setFill("black")
            GUI.draw(win)


            dialoguebox = Rectangle(Point(0, 5), Point(5, 4.5))
            dialoguebox.setFill("black")
            dialoguebox.draw(win)
            dialogue = Text(Point(1.3, 4.7), "* A puny slime appears!!")
            dialogue.setFace("courier")
            dialogue.setTextColor("white")
            dialogue.draw(win)


            playerhpdisplay = Text(Point(1.3, 3), "HP: " + str(playerhp))
            playerhpdisplay.setTextColor("white")
            playerhpdisplay.draw(win)

            enemyhpdisplay = Text(Point(4, 3), "HP: " + str(enemyhp))
            enemyhpdisplay.setTextColor("white")
            enemyhpdisplay.draw(win)

            attackbox = Rectangle(Point(0.2, 0.7), Point(1.2, 0.3))
            attackbox.setOutline("white")
            attackbox.draw(win)
            attack = Text(Point(0.7, 0.5), "ATTACK")
            attack.setFace("courier")
            attack.setTextColor("red")
            attack.draw(win)

            defendbox = Rectangle(Point(1.4, 0.7), Point(2.4, 0.3))
            defendbox.setOutline("white")
            defendbox.draw(win)
            defend = Text(Point(1.9, 0.5), "DEFEND")
            defend.setFace("courier")
            defend.setTextColor("light blue")
            defend.draw(win)

            healbox = Rectangle(Point(2.6, 0.7), Point(3.6, 0.3))
            healbox.setOutline("white")
            healbox.draw(win)
            heal = Text(Point(3.1, 0.5), "HEAL")
            heal.setFace("courier")
            heal.setTextColor("lime")
            heal.draw(win)

            fleebox = Rectangle(Point(3.8, 0.7), Point(4.8, 0.3))
            fleebox.setOutline("white")
            fleebox.draw(win)
            flee = Text(Point(4.3, 0.5), "FLEE")
            flee.setFace("courier")
            flee.setTextColor("yellow")
            flee.draw(win)

            action = win.getMouse()
            x = action.getX()
            y = action.getY()

            #ATTACK
            if 0.2 <= x <= 1.2 and 0.3 <= y <= 0.7:
                dialogue.undraw()

                fleebox.undraw()
                flee.undraw()
                healbox.undraw()
                heal.undraw()
                defendbox.undraw()
                defend.undraw()
                attackbox.undraw()
                attack.undraw()

                dialogue = Text(Point(1.3, 4.7), "* Choose an attack!")
                dialogue.setFace("courier")
                dialogue.setTextColor("white")
                dialogue.draw(win)

                grimslashbox = Rectangle(Point(0.5,0.7),Point(2,0.3))
                grimslashbox.setOutline("white")
                grimslashtext = Text(Point(1.25,0.5),"GRIM SLASH")
                grimslashtext.setFace("courier")
                grimslashtext.setTextColor("white")
                grimslashtext.draw(win)
                grimslashbox.draw(win)

                #Note: I found it difficult to implement curse so I added vanish which lets you avoid any damage for one turn
                vanishbox = Rectangle(Point(4.5, 0.7), Point(3, 0.3))
                vanishbox.setOutline("white")
                vanishtext = Text(Point(3.7, 0.5), "VANISH")
                vanishtext.setFace("courier")
                vanishtext.setTextColor("white")
                vanishtext.draw(win)
                vanishbox.draw(win)

                action = win.getMouse()
                x = action.getX()
                y = action.getY()

                #GRIM SLASH   #did NOT add crit to easy difficulty because it would be a little too easy
                if 0.5 <= x <= 2 and 0.3 <= y <= 0.7:
                    vanishbox.undraw()
                    vanishtext.undraw()
                    dialogue.undraw()

                    dialogue = Text(Point(1.5, 4.7), "* You used GRIM SLASH...")
                    dialogue.setFace("courier")
                    dialogue.setTextColor("white")
                    dialogue.draw(win)

                    count = 4
                    dmg = 50
                    specter.undraw()
                    while count != 0:
                        gif1 = Image(Point(1, 2), "specter1.png")
                        gif1.draw(win)
                        # time.sleep(1)
                        time.sleep(0.08)
                        gif1.undraw()
                        gif2 = Image(Point(1, 2), "specter2.png")
                        gif2.draw(win)

                        # time.sleep(1)
                        time.sleep(0.08)
                        gif2.undraw()
                        gif3 = Image(Point(1, 2), "specter3.png")
                        gif3.draw(win)
                        # time.sleep(1)
                        time.sleep(0.08)
                        gif3.undraw()
                        gif4 = Image(Point(1, 2), "specter4.png")
                        gif4.draw(win)
                        time.sleep(0.08)
                        gif4.undraw()
                        count = count - 1

                    specterattack = Image(Point(1.5, 2), "specterattack1.png")
                    specterattack.draw(win)
                    time.sleep(0.08)
                    specterattack.undraw()
                    specterattack = Image(Point(1.5, 2), "specterattack2.png")
                    specterattack.draw(win)
                    time.sleep(0.08)
                    specterattack.undraw()
                    specterattack = Image(Point(1.5, 2), "specterattack3.png")
                    specterattack.draw(win)
                    time.sleep(0.08)

                    accuracy = random.randint(1, 5)
                    #accuracy = 3
                    if accuracy == 3:
                        count = 5
                        while count != 0:
                            miss = Image(Point(4, 2), "miss.png")
                            miss.draw(win)
                            time.sleep(0.09)
                            miss.undraw()
                            time.sleep(0.09)
                            count = count - 1
                        dmg = 0


                    else:

                        count = 2
                        while count != 0:
                            slime.undraw()
                            slime = Image(Point(4.1, 1.5), "slime1.png")
                            slime.draw(win)
                            time.sleep(0.08)
                            slime.undraw()
                            slime = Image(Point(4, 1.5), "slime1.png")
                            slime.draw(win)
                            time.sleep(0.08)
                            slime.undraw()
                            slime = Image(Point(3.9, 1.5), "slime1.png")
                            slime.draw(win)
                            time.sleep(0.08)
                            slime.undraw()
                            slime = Image(Point(4, 1.5), "slime1.png")
                            slime.draw(win)
                            time.sleep(0.08)
                            count = count - 1

                            count = 4
                            while count != 0:
                                specterattack.undraw()
                                #enemyhpdisplay.undraw()
                              #  enemyhpdisplay = Text(Point(4, 3), "HP: " + str(enemyhp - dmg))
                               # enemyhpdisplay.setTextColor("white")
                              #  enemyhpdisplay.draw(win)
                                if dmg == 0:
                                    dialogue.undraw()
                                    dialogue = Text(Point(1.2, 4.7), "* You MISSED!!")
                                    dialogue.setFace("courier")
                                    dialogue.setTextColor("white")
                                    dialogue.draw(win)
                                else:
                                    dialogue.undraw()

                                    crit = random.randint(1,5)
                                    #crit = 1
                                    if crit == 1:
                                        dmg = 75
                                        dialogue = Text(Point(1.4, 4.7), "* CRITICAL HIT! " + str(dmg) + " DMG!")
                                        dialogue.setFace("courier")
                                        dialogue.setTextColor("white")
                                        dialogue.draw(win)
                                        #time.sleep(2)
                                    else:
                                        dialogue = Text(Point(1.4, 4.7), "* You hit it for " + str(dmg) + " DMG!")
                                        dialogue.setFace("courier")
                                        dialogue.setTextColor("white")
                                        dialogue.draw(win)
                                gif1 = Image(Point(1, 2), "specter1.png")
                                gif1.draw(win)
                                # time.sleep(1)
                                time.sleep(0.08)
                                gif1.undraw()
                                gif2 = Image(Point(1, 2), "specter2.png")
                                gif2.draw(win)

                                # time.sleep(1)
                                time.sleep(0.08)
                                gif2.undraw()
                                gif3 = Image(Point(1, 2), "specter3.png")
                                gif3.draw(win)
                                # time.sleep(1)
                                time.sleep(0.08)
                                gif3.undraw()
                                gif4 = Image(Point(1, 2), "specter4.png")
                                gif4.draw(win)
                                time.sleep(0.08)
                                gif4.undraw()
                                count = count - 1

                    specterattack.undraw()

                    specter = Image(Point(1, 2), "specter1.png")
                    specter.draw(win)

                    enemyhp = enemyhp - dmg
                    enemyhpdisplay.undraw()
                    enemyhpdisplay.draw(win)
                    if enemyhp <= 0:
                        dialogue.undraw()
                        dialogue = Text(Point(1.4, 4.7), "* YOU WIN!!!")
                        dialogue.setFace("courier")
                        dialogue.setTextColor("lime")
                        dialogue.draw(win)
                        time.sleep(2)
                        attack.undraw()
                        attackbox.undraw()
                        defend.undraw()
                        defendbox.undraw()
                        heal.undraw()
                        healbox.undraw()
                        flee.undraw()
                        fleebox.undraw()
                        dialogue.undraw()
                        dialoguebox.undraw()
                        playerhpdisplay.undraw()
                        enemyhpdisplay.undraw()
                        slime.undraw()
                        specter.undraw()
                        self.victory(win)


                #VANISH

                if 3 <= x <= 4.5 and 0.3 <= y <= 0.7:
                    vanish = True
                    grimslashtext.undraw()
                    grimslashbox.undraw()
                    dialogue.undraw()

                    dialogue = Text(Point(1.5, 4.7), "* You used VANISH...")
                    dialogue.setFace("courier")
                    dialogue.setTextColor("white")
                    dialogue.draw(win)

                    #SPECTER VANISH ANIMATION
                    count = 3
                    specter.undraw()
                    while count != 0:
                        gif1 = Image(Point(1, 2), "specter1.png")
                        gif1.draw(win)
                        # time.sleep(1)
                        time.sleep(0.08)
                        gif1.undraw()
                        gif2 = Image(Point(1, 2), "specter2.png")
                        gif2.draw(win)

                        # time.sleep(1)
                        time.sleep(0.08)
                        gif2.undraw()
                        gif3 = Image(Point(1, 2), "specter3.png")
                        gif3.draw(win)
                        # time.sleep(1)
                        time.sleep(0.08)
                        gif3.undraw()
                        gif4 = Image(Point(1, 2), "specter4.png")
                        gif4.draw(win)
                        time.sleep(0.08)
                        gif4.undraw()
                        count = count - 1
                    count = 0
                    while count != 5:
                        specter = Image(Point(1, 2), "specter1.png")
                        specter.draw(win)
                        time.sleep(0.04)
                        specter.undraw()
                        specter = Image(Point(1.2, 2), "specter1.png")
                        specter.draw(win)
                        time.sleep(0.04)
                        specter.undraw()
                        specter = Image(Point(1, 2), "specter1.png")
                        specter.draw(win)
                        time.sleep(0.04)
                        specter.undraw()
                        specter = Image(Point(0.9, 2), "specter1.png")
                        specter.draw(win)
                        time.sleep(0.04)
                        specter.undraw()
                        count = count + 1
                    specter.undraw()

            #FLEE
            elif 3.8 <= x <= 4.8 and  0.3 <= y <= 0.7:
                quit()

            #DEFEND
            elif 1.4 <= x <= 2.4 and 0.3 <= y <= 0.7:
                defend = True
                dialogue.undraw()
                dialogue = Text(Point(1.3, 4.7), "* You braced yourself..")
                dialogue.setFace("courier")
                dialogue.setTextColor("white")
                dialogue.draw(win)
                time.sleep(2)

            #HEAL
            elif 2.6 <= x <= 3.6 and 0.3 <= y <= 0.7:
                count = 3
                specter.undraw()
                while count != 0:
                    gif1 = Image(Point(1, 2), "specter1.png")
                    gif1.draw(win)
                    # time.sleep(1)
                    time.sleep(0.08)
                    gif1.undraw()
                    gif2 = Image(Point(1, 2), "specter2.png")
                    gif2.draw(win)

                    # time.sleep(1)
                    time.sleep(0.08)
                    gif2.undraw()
                    gif3 = Image(Point(1, 2), "specter3.png")
                    gif3.draw(win)
                    # time.sleep(1)
                    time.sleep(0.08)
                    gif3.undraw()
                    gif4 = Image(Point(1, 2), "specter4.png")
                    gif4.draw(win)
                    time.sleep(0.08)
                    gif4.undraw()
                    count = count - 1

                specter = Image(Point(1.2, 2.2), "specterheal1.png")
                specter.draw(win)
                time.sleep(0.08)
                specter.undraw()
                specter = Image(Point(1.2, 2.2), "specterheal2.png")
                specter.draw(win)
                time.sleep(0.08)
                specter.undraw()
                specter = Image(Point(1.2, 2.2), "specterheal3.png")
                specter.draw(win)
                time.sleep(0.08)
                specter.undraw()
                specter = Image(Point(1.2, 2.2), "specterheal4.png")
                specter.draw(win)
                time.sleep(0.08)
                specter.undraw()
                specter = Image(Point(1.2, 2.2), "specterheal5.png")
                specter.draw(win)
                time.sleep(0.08)
                specter.undraw()
                specter = Image(Point(1.2, 2.2), "specterheal6.png")
                specter.draw(win)
                time.sleep(0.08)
                specter.undraw()
                specter = Image(Point(1.2, 2.2), "specterheal7.png")
                specter.draw(win)
                time.sleep(0.08)
                specter.undraw()
                specter = Image(Point(1.2, 2.2), "specterheal8.png")
                specter.draw(win)
                time.sleep(0.08)
                specter.undraw()
                specter = Image(Point(1.2, 2.2), "specterheal9.png")
                specter.draw(win)
                time.sleep(0.08)
                specter.undraw()
                specter = Image(Point(1.2, 2.2), "specterheal10.png")
                specter.draw(win)
                time.sleep(0.08)
                specter.undraw()
                specter = Image(Point(1.2, 2.2), "specterheal11.png")
                specter.draw(win)
                time.sleep(1)
                specter.undraw()
                specter = Image(Point(1, 2), "specter1.png")
                specter.draw(win)
                dialogue.undraw()
                dialogue = Text(Point(1.3, 4.7), "* You recovered 20 HP!")
                dialogue.setFace("courier")
                dialogue.setTextColor("white")
                dialogue.draw(win)
                time.sleep(2)
                playerhp = playerhp + 20
                playerhpdisplay.undraw()
                playerhpdisplay.draw(win)


            #ENEMY TURN
            dialogue.undraw()
            dialogue = Text(Point(1.4, 4.7), "* SLIME's turn...")
            dialogue.setFace("courier")
            dialogue.setTextColor("white")
            dialogue.draw(win)
            time.sleep(1)

            enemychoice = random.randint(1,2)

            if enemychoice == 1:
                dialogue.undraw()
                dialogue = Text(Point(1.4, 4.7), "* Slime used POUND")
                dialogue.setFace("courier")
                dialogue.setTextColor("white")
                dialogue.draw(win)

                #SLIME ATTACK ANIMATION
                count = 5
                while count != 0:
                    slime.undraw()
                    slime = Image(Point(4.1, 1.5), "slime1.png")
                    slime.draw(win)
                    time.sleep(0.08)
                    slime.undraw()
                    slime = Image(Point(4, 1.5), "slime1.png")
                    slime.draw(win)
                    time.sleep(0.08)
                    slime.undraw()
                    slime = Image(Point(3.9, 1.5), "slime1.png")
                    slime.draw(win)
                    time.sleep(0.08)
                    slime.undraw()
                    slime = Image(Point(4, 1.5), "slime1.png")
                    slime.draw(win)
                    time.sleep(0.08)
                    count = count - 1

                accuracy = random.randint(1, 5)
                #accuracy = 2
                if accuracy == 3 or vanish == True:
                    dialogue.undraw()
                    dialogue = Text(Point(1.2, 4.7), "* SLIME MISSED!!")
                    dialogue.setFace("courier")
                    dialogue.setTextColor("white")
                    dialogue.draw(win)
                    count = 5
                    while count != 0:
                        miss = Image(Point(1.2, 2), "miss.png")
                        miss.draw(win)
                        time.sleep(0.09)
                        miss.undraw()
                        time.sleep(0.09)
                        count = count - 1
                    dmg = 0
                else:
                    count = 0
                    specter.undraw()
                    while count != 3:
                        specter.undraw()
                        specter = Image(Point(1, 2), "specterdamage.png")
                        specter.draw(win)
                        time.sleep(0.06)
                        specter.undraw()
                        specter = Image(Point(1.2, 2), "specterdamage.png")
                        specter.draw(win)
                        time.sleep(0.06)
                        specter.undraw()
                        specter = Image(Point(1, 2), "specterdamage.png")
                        specter.draw(win)
                        time.sleep(0.06)
                        specter.undraw()
                        specter = Image(Point(0.9, 2), "specterdamage.png")
                        specter.draw(win)
                        count = count + 1
                    dmg = 20
                    crit = random.randint(1, 5)
                    #crit = 1
                    if crit == 1:
                        dmg = 40
                        dialogue.undraw()
                        dialogue = Text(Point(1.4, 4.7), "* CRITICAL HIT! " + str(dmg) + " DMG!")
                        dialogue.setFace("courier")
                        dialogue.setTextColor("white")
                        dialogue.draw(win)
                        time.sleep(2)
                    if defend == True:
                        dmg = dmg - 20
                    dialogue.undraw()
                    dialogue = Text(Point(1.4, 4.7), "* You took " + str(dmg) + " DMG!")
                    dialogue.setFace("courier")
                    dialogue.setTextColor("white")
                    dialogue.draw(win)
                    time.sleep(2)
                    
                    playerhp = playerhp - dmg
                    playerhpdisplay.undraw()
                    playerhpdisplay.draw(win)
                    specter.undraw()

            elif enemychoice == 2:
                dialogue.undraw()
                dialogue = Text(Point(1.4, 4.7), "* Slime used RESTORE")
                dialogue.setFace("courier")
                dialogue.setTextColor("white")
                dialogue.draw(win)

                # SLIME ANIMATION
                count = 3
                while count != 0:
                    slime.undraw()
                    slime = Image(Point(4.1, 1.5), "slime1.png")
                    slime.draw(win)
                    time.sleep(0.08)
                    slime.undraw()
                    slime = Image(Point(4, 1.5), "slime1.png")
                    slime.draw(win)
                    time.sleep(0.08)
                    slime.undraw()
                    slime = Image(Point(3.9, 1.5), "slime1.png")
                    slime.draw(win)
                    time.sleep(0.08)
                    slime.undraw()
                    slime = Image(Point(4, 1.5), "slime1.png")
                    slime.draw(win)
                    time.sleep(0.08)
                    count = count - 1

                    time.sleep(0.5)

                dialogue.undraw()
                dialogue = Text(Point(1.4, 4.7), "* Slime RESTORED 20HP!")
                dialogue.setFace("courier")
                dialogue.setTextColor("white")
                dialogue.draw(win)
                time.sleep(2)

                enemyhp = enemyhp + 20

            #playerhp = 0
            if playerhp <= 0:
                dialogue.undraw()
                dialogue = Text(Point(1.4, 4.7), "* YOU DIED!!!")
                dialogue.setFace("courier")
                dialogue.setTextColor("red")
                dialogue.draw(win)
                time.sleep(2)
                attack.undraw()
                attackbox.undraw()
                defend.undraw()
                defendbox.undraw()
                heal.undraw()
                healbox.undraw()
                flee.undraw()
                fleebox.undraw()
                dialogue.undraw()
                dialoguebox.undraw()
                playerhpdisplay.undraw()
                enemyhpdisplay.undraw()
                slime.undraw()
                specter.undraw()
                self.gameover(win)



            #redo the loop
            specter.undraw()
            slime.undraw()
            playerhpdisplay.undraw()
            enemyhpdisplay.undraw()


    #CHALLENGING DIFFICULTY
    def challengingbattle(self,win,calcium):
        PlaySound("rude buster.wav", SND_ALIAS | SND_ASYNC)
        time.sleep(1)
        Image(Point(2.5, 2.5), "background.png").draw(win)

        # PLAYER
        specter = Image(Point(1, 2), "specter1.png")
        specter.draw(win)
        playerhp = 100

        # ENEMY
        enemyhp = 200
        specter.undraw()

        # BATTLE
        while enemyhp >= 0 or playerhp >= 0:
            vanish = False
            defend = False
            specter = Image(Point(1, 2), "specter1.png")
            specter.draw(win)
            vanish = ""

            skeleton = Image(Point(4, 2), "skeleton.png")
            skeleton.draw(win)

            GUI = Rectangle(Point(0, 1), Point(5, 0))
            GUI.setFill("black")
            GUI.draw(win)

            dialoguebox = Rectangle(Point(0, 5), Point(5, 4.5))
            dialoguebox.setFill("black")
            dialoguebox.draw(win)
            dialogue = Text(Point(1.5, 4.7), "* A spooky skeleton appears!!")
            dialogue.setFace("courier")
            dialogue.setTextColor("white")
            dialogue.draw(win)

            playerhpdisplay = Text(Point(1.3, 3), "HP: " + str(playerhp))
            playerhpdisplay.setTextColor("white")
            playerhpdisplay.draw(win)

            enemyhpdisplay = Text(Point(4, 3), "HP: " + str(enemyhp))
            enemyhpdisplay.setTextColor("white")
            enemyhpdisplay.draw(win)

            attackbox = Rectangle(Point(0.2, 0.7), Point(1.2, 0.3))
            attackbox.setOutline("white")
            attackbox.draw(win)
            attack = Text(Point(0.7, 0.5), "ATTACK")
            attack.setFace("courier")
            attack.setTextColor("red")
            attack.draw(win)

            defendbox = Rectangle(Point(1.4, 0.7), Point(2.4, 0.3))
            defendbox.setOutline("white")
            defendbox.draw(win)
            defend = Text(Point(1.9, 0.5), "DEFEND")
            defend.setFace("courier")
            defend.setTextColor("light blue")
            defend.draw(win)

            healbox = Rectangle(Point(2.6, 0.7), Point(3.6, 0.3))
            healbox.setOutline("white")
            healbox.draw(win)
            heal = Text(Point(3.1, 0.5), "HEAL")
            heal.setFace("courier")
            heal.setTextColor("lime")
            heal.draw(win)

            fleebox = Rectangle(Point(3.8, 0.7), Point(4.8, 0.3))
            fleebox.setOutline("white")
            fleebox.draw(win)
            flee = Text(Point(4.3, 0.5), "FLEE")
            flee.setFace("courier")
            flee.setTextColor("yellow")
            flee.draw(win)

            action = win.getMouse()
            x = action.getX()
            y = action.getY()

            # ATTACK
            if 0.2 <= x <= 1.2 and 0.3 <= y <= 0.7:
                dialogue.undraw()

                fleebox.undraw()
                flee.undraw()
                healbox.undraw()
                heal.undraw()
                defendbox.undraw()
                defend.undraw()
                attackbox.undraw()
                attack.undraw()

                dialogue = Text(Point(1.3, 4.7), "* Choose an attack!")
                dialogue.setFace("courier")
                dialogue.setTextColor("white")
                dialogue.draw(win)

                grimslashbox = Rectangle(Point(0.5, 0.7), Point(2, 0.3))
                grimslashbox.setOutline("white")
                grimslashtext = Text(Point(1.25, 0.5), "GRIM SLASH")
                grimslashtext.setFace("courier")
                grimslashtext.setTextColor("white")
                grimslashtext.draw(win)
                grimslashbox.draw(win)

                vanishbox = Rectangle(Point(4.5, 0.7), Point(3, 0.3))
                vanishbox.setOutline("white")
                vanishtext = Text(Point(3.7, 0.5), "VANISH")
                vanishtext.setFace("courier")
                vanishtext.setTextColor("white")
                vanishtext.draw(win)
                vanishbox.draw(win)

                action = win.getMouse()
                x = action.getX()
                y = action.getY()

                # GRIM SLASH
                if 0.5 <= x <= 2 and 0.3 <= y <= 0.7:
                    vanishbox.undraw()
                    vanishtext.undraw()
                    dialogue.undraw()

                    dialogue = Text(Point(1.5, 4.7), "* You used GRIM SLASH...")
                    dialogue.setFace("courier")
                    dialogue.setTextColor("white")
                    dialogue.draw(win)

                    count = 4
                    dmg = 50
                    specter.undraw()
                    while count != 0:
                        gif1 = Image(Point(1, 2), "specter1.png")
                        gif1.draw(win)
                        # time.sleep(1)
                        time.sleep(0.08)
                        gif1.undraw()
                        gif2 = Image(Point(1, 2), "specter2.png")
                        gif2.draw(win)

                        # time.sleep(1)
                        time.sleep(0.08)
                        gif2.undraw()
                        gif3 = Image(Point(1, 2), "specter3.png")
                        gif3.draw(win)
                        # time.sleep(1)
                        time.sleep(0.08)
                        gif3.undraw()
                        gif4 = Image(Point(1, 2), "specter4.png")
                        gif4.draw(win)
                        time.sleep(0.08)
                        gif4.undraw()
                        count = count - 1

                    specterattack = Image(Point(1.5, 2), "specterattack1.png")
                    specterattack.draw(win)
                    time.sleep(0.08)
                    specterattack.undraw()
                    specterattack = Image(Point(1.5, 2), "specterattack2.png")
                    specterattack.draw(win)
                    time.sleep(0.08)
                    specterattack.undraw()
                    specterattack = Image(Point(1.5, 2), "specterattack3.png")
                    specterattack.draw(win)
                    time.sleep(0.08)

                    accuracy = random.randint(1, 5)
                    # accuracy = 3
                    if accuracy == 3:
                        count = 5
                        while count != 0:
                            miss = Image(Point(4, 2), "miss.png")
                            miss.draw(win)
                            time.sleep(0.09)
                            miss.undraw()
                            time.sleep(0.09)
                            count = count - 1
                        dmg = 0


                    else:

                        count = 2
                        while count != 0:
                            skeleton.undraw()
                            skeleton = Image(Point(4.1, 2), "skeleton.png")
                            skeleton.draw(win)
                            time.sleep(0.08)
                            skeleton.undraw()
                            skeleton = Image(Point(4, 2), "skeleton.png")
                            skeleton.draw(win)
                            time.sleep(0.08)
                            skeleton.undraw()
                            skeleton = Image(Point(3.9, 2), "skeleton.png")
                            skeleton.draw(win)
                            time.sleep(0.08)
                            skeleton.undraw()
                            skeleton = Image(Point(4, 2), "skeleton.png")
                            skeleton.draw(win)
                            time.sleep(0.08)
                            count = count - 1

                        count = 4
                        while count != 0:
                            specterattack.undraw()

                            if dmg == 0:
                                dialogue.undraw()
                                dialogue = Text(Point(1.2, 4.7), "* You MISSED!!")
                                dialogue.setFace("courier")
                                dialogue.setTextColor("white")
                                dialogue.draw(win)
                            else:
                                dialogue.undraw()

                                crit = random.randint(1, 5)
                                # crit = 1
                                if crit == 1:
                                    dmg = 75
                                    dialogue = Text(Point(1.4, 4.7), "* CRITICAL HIT! " + str(dmg) + " DMG!")
                                    dialogue.setFace("courier")
                                    dialogue.setTextColor("white")
                                    dialogue.draw(win)
                                    # time.sleep(2)

                                else:
                                    dialogue = Text(Point(1.4, 4.7), "* You hit it for " + str(dmg) + " DMG!")
                                    dialogue.setFace("courier")
                                    dialogue.setTextColor("white")
                                    dialogue.draw(win)
                            gif1 = Image(Point(1, 2), "specter1.png")
                            gif1.draw(win)
                            # time.sleep(1)
                            time.sleep(0.08)
                            gif1.undraw()
                            gif2 = Image(Point(1, 2), "specter2.png")
                            gif2.draw(win)

                            # time.sleep(1)
                            time.sleep(0.08)
                            gif2.undraw()
                            gif3 = Image(Point(1, 2), "specter3.png")
                            gif3.draw(win)
                            # time.sleep(1)
                            time.sleep(0.08)
                            gif3.undraw()
                            gif4 = Image(Point(1, 2), "specter4.png")
                            gif4.draw(win)
                            time.sleep(0.08)
                            gif4.undraw()
                            count = count - 1

                    specterattack.undraw()

                    specter = Image(Point(1, 2), "specter1.png")
                    specter.draw(win)
                    time.sleep(1)
                    if calcium == True:
                        dmg = dmg - 10
                        dialogue.undraw()
                        dialogue = Text(Point(1.8, 4.7), "*CALCIUM bones made it take " + str(dmg) + " DMG!")
                        dialogue.setFace("courier")
                        dialogue.setTextColor("white")
                        dialogue.draw(win)
                        calcium = False
                        time.sleep(2)

                    else:
                        time.sleep(1)
                    enemyhp = enemyhp - dmg
                    enemyhpdisplay.undraw()
                    enemyhpdisplay.draw(win)
                    if enemyhp <= 0:
                        dialogue.undraw()
                        dialogue = Text(Point(1.4, 4.7), "* YOU WIN!!!")
                        dialogue.setFace("courier")
                        dialogue.setTextColor("lime")
                        dialogue.draw(win)
                        time.sleep(2)
                        attack.undraw()
                        attackbox.undraw()
                        defend.undraw()
                        defendbox.undraw()
                        heal.undraw()
                        healbox.undraw()
                        flee.undraw()
                        fleebox.undraw()
                        dialogue.undraw()
                        dialoguebox.undraw()
                        playerhpdisplay.undraw()
                        enemyhpdisplay.undraw()
                        skeleton.undraw()
                        specter.undraw()
                        self.victory(win)


                # VANISH

                if 3 <= x <= 4.5 and 0.3 <= y <= 0.7:
                    vanish = True
                    grimslashtext.undraw()
                    grimslashbox.undraw()
                    dialogue.undraw()

                    dialogue = Text(Point(1.5, 4.7), "* You used VANISH...")
                    dialogue.setFace("courier")
                    dialogue.setTextColor("white")
                    dialogue.draw(win)

                    # SPECTER VANISH ANIMATION
                    count = 3
                    specter.undraw()
                    while count != 0:
                        gif1 = Image(Point(1, 2), "specter1.png")
                        gif1.draw(win)
                        # time.sleep(1)
                        time.sleep(0.08)
                        gif1.undraw()
                        gif2 = Image(Point(1, 2), "specter2.png")
                        gif2.draw(win)

                        # time.sleep(1)
                        time.sleep(0.08)
                        gif2.undraw()
                        gif3 = Image(Point(1, 2), "specter3.png")
                        gif3.draw(win)
                        # time.sleep(1)
                        time.sleep(0.08)
                        gif3.undraw()
                        gif4 = Image(Point(1, 2), "specter4.png")
                        gif4.draw(win)
                        time.sleep(0.08)
                        gif4.undraw()
                        count = count - 1
                    count = 0
                    while count != 5:
                        specter = Image(Point(1, 2), "specter1.png")
                        specter.draw(win)
                        time.sleep(0.04)
                        specter.undraw()
                        specter = Image(Point(1.2, 2), "specter1.png")
                        specter.draw(win)
                        time.sleep(0.04)
                        specter.undraw()
                        specter = Image(Point(1, 2), "specter1.png")
                        specter.draw(win)
                        time.sleep(0.04)
                        specter.undraw()
                        specter = Image(Point(0.9, 2), "specter1.png")
                        specter.draw(win)
                        time.sleep(0.04)
                        specter.undraw()
                        count = count + 1
                    specter.undraw()

            # FLEE
            elif 3.8 <= x <= 4.8 and 0.3 <= y <= 0.7:
                quit()

            # DEFEND
            elif 1.4 <= x <= 2.4 and 0.3 <= y <= 0.7:
                defend = True
                dialogue.undraw()
                dialogue = Text(Point(1.3, 4.7), "* You braced yourself..")
                dialogue.setFace("courier")
                dialogue.setTextColor("white")
                dialogue.draw(win)
                time.sleep(2)

            # HEAL
            elif 2.6 <= x <= 3.6 and 0.3 <= y <= 0.7:
                count = 3
                specter.undraw()
                while count != 0:
                    gif1 = Image(Point(1, 2), "specter1.png")
                    gif1.draw(win)
                    # time.sleep(1)
                    time.sleep(0.08)
                    gif1.undraw()
                    gif2 = Image(Point(1, 2), "specter2.png")
                    gif2.draw(win)

                    # time.sleep(1)
                    time.sleep(0.08)
                    gif2.undraw()
                    gif3 = Image(Point(1, 2), "specter3.png")
                    gif3.draw(win)
                    # time.sleep(1)
                    time.sleep(0.08)
                    gif3.undraw()
                    gif4 = Image(Point(1, 2), "specter4.png")
                    gif4.draw(win)
                    time.sleep(0.08)
                    gif4.undraw()
                    count = count - 1

                specter = Image(Point(1.2, 2.2), "specterheal1.png")
                specter.draw(win)
                time.sleep(0.08)
                specter.undraw()
                specter = Image(Point(1.2, 2.2), "specterheal2.png")
                specter.draw(win)
                time.sleep(0.08)
                specter.undraw()
                specter = Image(Point(1.2, 2.2), "specterheal3.png")
                specter.draw(win)
                time.sleep(0.08)
                specter.undraw()
                specter = Image(Point(1.2, 2.2), "specterheal4.png")
                specter.draw(win)
                time.sleep(0.08)
                specter.undraw()
                specter = Image(Point(1.2, 2.2), "specterheal5.png")
                specter.draw(win)
                time.sleep(0.08)
                specter.undraw()
                specter = Image(Point(1.2, 2.2), "specterheal6.png")
                specter.draw(win)
                time.sleep(0.08)
                specter.undraw()
                specter = Image(Point(1.2, 2.2), "specterheal7.png")
                specter.draw(win)
                time.sleep(0.08)
                specter.undraw()
                specter = Image(Point(1.2, 2.2), "specterheal8.png")
                specter.draw(win)
                time.sleep(0.08)
                specter.undraw()
                specter = Image(Point(1.2, 2.2), "specterheal9.png")
                specter.draw(win)
                time.sleep(0.08)
                specter.undraw()
                specter = Image(Point(1.2, 2.2), "specterheal10.png")
                specter.draw(win)
                time.sleep(0.08)
                specter.undraw()
                specter = Image(Point(1.2, 2.2), "specterheal11.png")
                specter.draw(win)
                time.sleep(1)
                specter.undraw()
                specter = Image(Point(1, 2), "specter1.png")
                specter.draw(win)
                dialogue.undraw()
                dialogue = Text(Point(1.3, 4.7), "* You recovered 20 HP!")
                dialogue.setFace("courier")
                dialogue.setTextColor("white")
                dialogue.draw(win)
                time.sleep(2)
                playerhp = playerhp + 20
                playerhpdisplay.undraw()
                playerhpdisplay.draw(win)

            # ENEMY TURN
            dialogue.undraw()
            dialogue = Text(Point(1.4, 4.7), "* SKELETON's turn...")
            dialogue.setFace("courier")
            dialogue.setTextColor("white")
            dialogue.draw(win)
            time.sleep(1)

            enemychoice = random.randint(1, 3)
            # print(enemychoice)
            # enemychoice = 1


            #SKELETON ATTACK
            if enemychoice == 1:
                dialogue.undraw()
                dialogue = Text(Point(1.5, 4.7), "* Skeleton used BONE THROW")
                dialogue.setFace("courier")
                dialogue.setTextColor("white")
                dialogue.draw(win)

                count = 5
                while count != 0:
                    skeleton.undraw()
                    skeleton = Image(Point(4,2.2),"skeletonattack1.png")
                    skeleton.draw(win)
                    time.sleep(0.08)
                    skeleton.undraw()
                    skeleton = Image(Point(4, 2.2), "skeletonattack2.png")
                    skeleton.draw(win)
                    time.sleep(0.08)
                    count = count -1


                bone = Image(Point(3.5,2),"bone.png")
                bone.draw(win)
                time.sleep(0.08)
                bone.undraw()
                bone = Image(Point(3, 2), "bone.png")
                bone.draw(win)
                time.sleep(0.08)
                bone.undraw()
                bone = Image(Point(2.5, 2), "bone.png")
                bone.draw(win)
                time.sleep(0.08)
                bone.undraw()
                bone = Image(Point(2, 2), "bone.png")
                bone.draw(win)
                time.sleep(0.08)
                bone.undraw()
                bone = Image(Point(1.5, 2), "bone.png")
                bone.draw(win)
                time.sleep(0.08)
                bone.undraw()

                accuracy = random.randint(1, 5)
                # accuracy = 2
                if accuracy == 3 or vanish == True:
                    dialogue.undraw()
                    dialogue = Text(Point(1.2, 4.7), "* SKELETON MISSED!!")
                    dialogue.setFace("courier")
                    dialogue.setTextColor("white")
                    dialogue.draw(win)
                    count = 5
                    while count != 0:
                        miss = Image(Point(1.2, 2), "miss.png")
                        miss.draw(win)
                        time.sleep(0.09)
                        miss.undraw()
                        time.sleep(0.09)
                        count = count - 1
                    dmg = 0
                else:
                    count = 0
                    specter.undraw()
                    while count != 3:
                        specter.undraw()
                        specter = Image(Point(1, 2), "specterdamage.png")
                        specter.draw(win)
                        time.sleep(0.06)
                        specter.undraw()
                        specter = Image(Point(1.2, 2), "specterdamage.png")
                        specter.draw(win)
                        time.sleep(0.06)
                        specter.undraw()
                        specter = Image(Point(1, 2), "specterdamage.png")
                        specter.draw(win)
                        time.sleep(0.06)
                        specter.undraw()
                        specter = Image(Point(0.9, 2), "specterdamage.png")
                        specter.draw(win)
                        count = count + 1

                    dmg = 25
                    crit = random.randint(1, 5)
                    # crit = 1
                    if crit == 1:
                        dmg = 40
                        dialogue.undraw()
                        dialogue = Text(Point(1.4, 4.7), "* CRITICAL HIT! " + str(dmg) + " DMG!")
                        dialogue.setFace("courier")
                        dialogue.setTextColor("white")
                        dialogue.draw(win)
                        time.sleep(2)
                    if defend == True:
                        dmg = dmg - 20
                    dialogue.undraw()
                    dialogue = Text(Point(1.4, 4.7), "* You took " + str(dmg) + " DMG!")
                    dialogue.setFace("courier")
                    dialogue.setTextColor("white")
                    dialogue.draw(win)
                    time.sleep(2)

                    playerhp = playerhp - dmg
                    playerhpdisplay.undraw()
                    playerhpdisplay.draw(win)
                    specter.undraw()

            #SKELETON DEFEND
            elif enemychoice == 2:
                count = 2
                while count != 0:
                    skeleton.undraw()
                    skeleton = Image(Point(4.1, 2), "skeleton.png")
                    skeleton.draw(win)
                    time.sleep(0.08)
                    skeleton.undraw()
                    skeleton = Image(Point(4, 2), "skeleton.png")
                    skeleton.draw(win)
                    time.sleep(0.08)
                    skeleton.undraw()
                    skeleton = Image(Point(3.9, 2), "skeleton.png")
                    skeleton.draw(win)
                    time.sleep(0.08)
                    skeleton.undraw()
                    skeleton = Image(Point(4, 2), "skeleton.png")
                    skeleton.draw(win)
                    time.sleep(0.08)
                    count = count - 1
                dialogue.undraw()
                dialogue = Text(Point(1.4, 4.7), "* Skeleton used CALCIUM")
                dialogue.setFace("courier")
                dialogue.setTextColor("white")
                dialogue.draw(win)
                calcium = True
                time.sleep(2)


            #SKELETON HEALS
            elif enemychoice == 3:
                dialogue.undraw()
                dialogue = Text(Point(1.4, 4.7), "* Skeleton used MEND")
                dialogue.setFace("courier")
                dialogue.setTextColor("white")
                dialogue.draw(win)
                count = 2
                while count != 0:
                    skeleton.undraw()
                    skeleton = Image(Point(4.1, 2), "skeleton.png")
                    skeleton.draw(win)
                    time.sleep(0.08)
                    skeleton.undraw()
                    skeleton = Image(Point(4, 2), "skeleton.png")
                    skeleton.draw(win)
                    time.sleep(0.08)
                    skeleton.undraw()
                    skeleton = Image(Point(3.9, 2), "skeleton.png")
                    skeleton.draw(win)
                    time.sleep(0.08)
                    skeleton.undraw()
                    skeleton = Image(Point(4, 2), "skeleton.png")
                    skeleton.draw(win)
                    time.sleep(0.08)
                    count = count - 1

                dialogue.undraw()
                dialogue = Text(Point(1.4, 4.7), "* Skeleton HEALED 20HP!")
                dialogue.setFace("courier")
                dialogue.setTextColor("white")
                dialogue.draw(win)

                time.sleep(2)
                enemyhp = enemyhp + 20






            # playerhp = 0
            if playerhp <= 0:
                dialogue.undraw()
                dialogue = Text(Point(1.4, 4.7), "* YOU DIED!!!")
                dialogue.setFace("courier")
                dialogue.setTextColor("red")
                dialogue.draw(win)
                time.sleep(2)
                attack.undraw()
                attackbox.undraw()
                defend.undraw()
                defendbox.undraw()
                heal.undraw()
                healbox.undraw()
                flee.undraw()
                fleebox.undraw()
                dialogue.undraw()
                dialoguebox.undraw()
                playerhpdisplay.undraw()
                enemyhpdisplay.undraw()
                skeleton.undraw()
                specter.undraw()
                self.gameover(win)

            # redo the loop
            # print(str(playerhp))
            specter.undraw()
            skeleton.undraw()
            playerhpdisplay.undraw()
            enemyhpdisplay.undraw()



    def gameover(self,win):

        PlaySound("Death Theme", SND_ALIAS | SND_ASYNC)
        rectangle = Rectangle(Point(0,0),Point(5,5))
        rectangle.setFill("black")
        rectangle.draw(win)


        specter = Image(Point(2.5,2.5),"specterdeath.png")
        specter.draw(win)

        gameovertext = Text(Point(2.5,3.5),"GAME OVER")
        gameovertext.setFace("courier")
        gameovertext.setTextColor("red")
        gameovertext.setSize(30)
        gameovertext.draw(win)

        time.sleep(70)
        quit()

    def victory(self, win):
        PlaySound("Victory", SND_ALIAS | SND_ASYNC)
        rectangle = Rectangle(Point(0, 0), Point(5, 5))
        rectangle.setFill("black")
        rectangle.draw(win)

        specter = Image(Point(2.4, 2.4), "specter1.png")
        specter.draw(win)

        gameovertext = Text(Point(2.5, 3.5), "VICTORY!!")
        gameovertext.setFace("courier")
        gameovertext.setTextColor("lime")
        gameovertext.setSize(30)
        gameovertext.draw(win)

        time.sleep(54)
        quit()

            #gif1.undraw()
            #slime.undraw()



a = Win()
a.mainmenu()

