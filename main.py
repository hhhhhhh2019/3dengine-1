import pygame as pg
from objects import *
import numpy as np
from matrix import *
from camera import Camera
from projection import Projection
from math import radians


class Renderer:
    def __init__(self, w, h):
        self.res = self.w, self.h = w, h

        self.screen = pg.display.set_mode((w, h))
        self.clock = pg.time.Clock()

        self.fps = 60

        self.objects = []

        self.camera = Camera(self, (0, 0, 0))
        self.camera.camera_yaw(radians(190))
        self.projection = Projection(self)

    def get_object_from_file(self, filename, scale=1):
        vertex, faces = [], []
        with open(filename) as f:
            for line in f:
                if line.startswith('v '):
                    vertex.append([float(i) for i in line.split()[1:]] + [1])
                elif line.startswith('f'):
                    faces_ = line.split()[1:]
                    faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
        return Object(self, vertex, faces, scale)

    def create_object(self, file, scale):
        self.objects.append(self.get_object_from_file(file, scale))

    def draw(self):
        for i in self.objects:
            i.movement()
            i.draw()

    def run(self):
        while True:
            self.clock.tick(self.fps)
            self.screen.fill(pg.Color('darkslategray'))

            for e in pg.event.get():
                if e.type == pg.QUIT:
                    exit()

                if e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
                    exit()

            self.draw()

            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()

app = Renderer(1024, 720)
app.create_object('people.obj', 0.02)
app.run()
