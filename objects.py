from matrix import *
from math import radians, pi
import pygame as pg


class Object:
    def __init__(self, render, vert, face, sc = 1):
        self.vert, self.faces = vert @ scale(sc), face
        self.render = render

        # self.vert = self.vert @ rotate_x(-radians(2))

    def movement(self):
        self.vert = self.vert @ rotate_y(radians(2))

    def draw(self):
        vert = self.vert
        vert = vert @ self.render.camera.camera_matrix()
        vert = vert @ self.render.projection.projection_matrix
        vert = vert @ self.render.projection.to_screen_matrix

        for f in self.faces:
            polygon = []
            for v in f:
                vertex = vert[v]

                p = (vertex[0] + self.render.w / 2, vertex[1] + self.render.h / 2)
                
                polygon.append(p)

                # pg.draw.circle(self.render.screen, (255, 255, 255), p, 3)

            pg.draw.polygon(self.render.screen, (200, 200, 0), polygon, 1)
