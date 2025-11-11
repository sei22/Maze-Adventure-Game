import pyxel
import random
 
 
class Jeu:
   def __init__(self):
       """
       initialisation
       """
       # ecran 128x128 pixels
       #pyxel.init(248, 248)
       # position initial du joueur et variable qui montre si il est en vie ou pas
       self.p_x = 124
       self.p_y = 193.75

       # liste qui contient l'ensemble des bullets
       self.blt = []
       # liste qui contient l'ensemble des ennemis
       self.enmy_txt = ["CREDITS:","UTA BAYON DE NOYER","ELYES JEMEL","TEO FUJISAKI BRILLAUD","SEI BAYLE"]
       self.enmy = []
       # liste qui contient l'ensemble des explosions
       self.explose = []
       # score du joueur
       self.score = 0
       self.merci = 0
       self.timer = 0
       self.phase = "goal"
       
   
       pyxel.run(self.update, self.draw)

   def collision(self, x1, y1, w1, h1, x2, y2, w2, h2):
       if x1-w2<x2<x1+w1 and y1-h2<y2<y1+h1:
           return True
       return False  
   
   
   def shoot(self):
       """
       creation d'un bullet en haut du joueur
       """
       # premier element, x de bullet et le second, y de bullet
       new_blt = [self.p_x + 5.8, self.p_y - 7.75]
       self.blt.append(new_blt)
 
   def update_blt(self):
       """
       met a jour l'ensembles des bullets contenu dans la liste blt
       """
       for b in self.blt:
           # fait monter chaque bullet vers le haut de l'ecran, 3 pixels par frame
           b[1] += -5.8
           # lorsque le bullet est en dehors des limites de l'ecran, alors le supprimer
           if b[1] < -19.375:
               self.blt.remove(b)
           # quand bullet en collision avec ennemi
           # supprimer bullet et enlever une vie a ennemi
           for e in self.enmy:
               if self.collision(e[0], e[1], len(e[3])*4, 5, b[0], b[1], 2, 8):
                   self.blt.remove(b)
                   e[2] -= 1
                   break
 
   def spawn(self):
       """
       apparition d'un ennemi en haut de l'ecran
       """
       # premier element, x de l'ennemi et le second, y de l'ennemi
       # troisieme element est le nombre de vie
       #random.shuffle(self.enmy_txt)
       self.timer += 1
       if self.timer == 20:
        new_enmy = [100, 20, 3, self.enmy_txt[0]]
        self.enmy.append(new_enmy)
       if self.timer == 60:
        new_enmy = [90, 20, 3, self.enmy_txt[1]]
        self.enmy.append(new_enmy)
       if self.timer == 100:
        new_enmy = [90, 20, 3, self.enmy_txt[2]]
        self.enmy.append(new_enmy)  
       if self.timer == 140:
        new_enmy = [90, 20, 3, self.enmy_txt[3]]
        self.enmy.append(new_enmy)
       if self.timer == 180:
        new_enmy = [100, 20, 3, self.enmy_txt[4]]
        self.enmy.append(new_enmy)
 
   def update_enmy(self):
       """
       met a jour l'ensemble des ennemis contenu dans la liste enmy
       """
       for e in self.enmy:
           # fait descendre chaque ennemi vers le bas de l'ecran, 1 pixels par frame
           e[1] += 1
           # lorsque l'ennemi est en dehors des limites de l'ecran,
           # ou lorsque l'ennemi n'a plus de vie
           # alors le supprimer + explosion
           if e[1] > 232.5 or e[2] == 0:
               self.enmy.remove(e)
               self.explosion(e[0], e[1])
               # ajouter un point au score lors de la destruction d'un ennemi
               if e[2] == 0:
                   self.score += 1
               
               

 
   def explosion(self, x, y):
       """
       apparition d'une explosion aux coordonnees x,y
       le troisieme element des listes des explosions correspondent a la progression des
       explosions
       """
       new_explose = [x, y, 0]
       self.explose.append(new_explose)
 
   def update_explosion(self):
       """
       met a jour l'ensemble des explosions
       """
       for ex in self.explose:
           ex[2] += 1
           # l'explosion se fait en 12 etapes
           if ex[2] == 12:
               self.explose.remove(ex)
 
   def update_play(self):
       """
       methode update qui met a jour l'etat du jeu
       """
       # deplacement du joueur dans les quatres directions, vitesse de 4 pixels par frame
       # utilisation des touches fleches en fonction de la direction
       if pyxel.btn(pyxel.KEY_RIGHT) and self.p_x < 232.5:
           self.p_x += 4
       if pyxel.btn(pyxel.KEY_LEFT) and self.p_x > 0:
           self.p_x += -4
       if pyxel.btn(pyxel.KEY_DOWN) and self.p_y < 232.5:
           self.p_y += 4
       if pyxel.btn(pyxel.KEY_UP) and self.p_y > 0:
           self.p_y += -4
       # lorsque touche espace pressee et joueur en vie, creation d'un bullet
       if pyxel.btnp(pyxel.KEY_SPACE, 5, 5):
           self.shoot()
       # apparition aleatoire d'un ennemi
       #if random.random() < 0.04 and self.score < 10:
       self.spawn()
       # mettre a jour les bullets
       self.update_blt()
       # mettre a jour les ennemis
       self.update_enmy()
       # mettre a jour les explosions
       self.update_explosion()
       if self.timer >= 250:
           self.merci +=2
       if self.timer >=340:
           pyxel.quit()
 

   def update_goal(self):
       if self.timer >= 60:
           self.phase = "play"
           self.timer = 0
       self.timer +=1

   def update(self):
       if self.phase == "goal":
           self.update_goal()
       elif self.phase == "play":
           self.update_play()


   def draw_play(self):
       """
       methode draw qui gere l'affichage
       """
       # afficher un ecran noir qui sera le fond d'ecran
       pyxel.cls(0)
       # affichage du joueur (rectange 8x8 bleu) si joueur en vie
       # sinon afficher game over
       pyxel.rect(self.p_x, self.p_y, 15.5, 15.5, 1)
       
       # affichage de l'ensemble des bullets contenus dans la liste blt, rectangle 1x4 jaune
       for b in self.blt:
           pyxel.rect(b[0], b[1], 1.9, 7.7, 10)
       # affichage de l'ensemble des ennemis contenus dans la liste blt, rectangle 8x8 rouge
       for e in self.enmy:
           pyxel.text(e[0], e[1], e[3], 7)
       # affichage de l'ensemble des explosions contenus dans la liste explose
       # disque qui change de rayon, couleur en fonction de la progression de l'explosion
       for ex in self.explose:
           pyxel.circb(ex[0] + 7.75, ex[1] + 7.75, 1.9375*2 * (ex[2] // 4), 8 + ex[2] % 3)
       # afficher le score
       if self.timer >= 250:
           pyxel.text(110, self.merci, "MERCI!!!", 9)

   def draw_goal(self):
       pyxel.text(110, 130, "GOAL!!", 7)    
        
        
   def draw(self):
       if self.phase == "goal":
           self.draw_goal()
       elif self.phase == "play":
           self.draw_play()
