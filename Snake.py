# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 09:26:59 2024

@author: xMiku
"""

import pyxel
import random

longueur = 128
hauteur = 128
taille_carre = 8  

class JeuSnake:
    def __init__(self):
        pyxel.init(longueur, hauteur)
        self.rejouer_game()
        pyxel.run(self.update, self.draw)

    def rejouer_game(self):
        self.snake = [(longueur // 2, hauteur // 2)]  
        self.direction = (taille_carre, 0) 
        self.taille_serpent = False  
        self.fruit = self.placer_fruit() 
        self.score = 0 
        self.game_over = False  

    def placer_fruit(self):
        while True:
            x = random.randint(0, (longueur - taille_carre) // taille_carre) * taille_carre
            y = random.randint(0, (hauteur - taille_carre) // taille_carre) * taille_carre
            if (x, y) not in self.snake:
                return (x, y)

    def update(self):
        if self.game_over:
            if pyxel.btnp(pyxel.KEY_R): 
                self.rejouer_game()
            elif pyxel.btnp(pyxel.KEY_Q):  
                pyxel.quit()
            return

        if pyxel.btn(pyxel.KEY_RIGHT) and self.direction != (-taille_carre, 0):
            self.direction = (taille_carre, 0)
        elif pyxel.btn(pyxel.KEY_LEFT) and self.direction != (taille_carre, 0):
            self.direction = (-taille_carre, 0)
        elif pyxel.btn(pyxel.KEY_UP) and self.direction != (0, taille_carre):
            self.direction = (0, -taille_carre)
        elif pyxel.btn(pyxel.KEY_DOWN) and self.direction != (0, -taille_carre):
            self.direction = (0, taille_carre)

        if pyxel.frame_count % 5 == 0:
            new_head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])

            if (new_head in self.snake or 
                new_head[0] < 0 or new_head[0] >= longueur or 
                new_head[1] < 0 or new_head[1] >= hauteur):
                self.game_over = True  
                return

            self.snake = [new_head] + self.snake
            
            if new_head == self.fruit:
                self.score += 1
                self.fruit = self.placer_fruit()
                self.taille_serpent = True
            else:
                if not self.taille_serpent:
                    self.snake.pop()
                self.taille_serpent = False

    def draw(self):
        pyxel.cls(0)  

        if self.game_over:
            pyxel.text(40, 50, "Game Over!", pyxel.frame_count % 16)
            pyxel.text(30, 60, f"Score: {self.score}", 7)
            pyxel.text(20, 80, "cliquez R pour rejouer", 8)
            pyxel.text(20, 90, "cliquez Q pour quitter", 8)
        else:
            for (x, y) in self.snake:
                pyxel.rect(x, y, taille_carre, taille_carre, 11)

            pyxel.rect(self.fruit[0], self.fruit[1], taille_carre, taille_carre, 8)

            pyxel.text(5, 5, f"Score: {self.score}", 7)

JeuSnake()