from OpenGL.GL import *
from OpenGL.GLUT import *
# from OpenGL.GLU import *
import numpy as np

from ant import Ant

window = 0  # glut window number
tile_size = 25
tile_grid = 30  # grid is a square: tile_grid x tile_grid
tile_spacing = 1
width = (tile_size * tile_grid) + (tile_spacing * tile_grid) + 1
height = (tile_size * tile_grid) + (tile_spacing * tile_grid) + 1

tiles = [[0 for x in range(tile_grid)] for y in range(tile_grid)]
ant = Ant(int(np.floor(tile_grid / 2)), int(np.floor(tile_grid / 2)), 'white', 'N')


def draw_rect(x, y, w, h):
    glBegin(GL_QUADS)  # start drawing a rectangle
    glVertex2f(x, y)  # bottom left point
    glVertex2f(x + w, y)  # bottom right point
    glVertex2f(x + w, y + h)  # top right point
    glVertex2f(x, y + h)  # top left point
    glEnd()  # done drawing a rectangle


def refresh2d(w, h):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, w, 0.0, h, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def update_ant():
    global ant
    if 0 <= ant.x < tile_grid and 0 <= ant.y < tile_grid:
        try:
            curr_tile = tiles[ant.x][ant.y]
            next_color = ant.next_step(curr_tile.get('color', -1))
            if next_color == 'white':
                glColor3f(1.0, 1.0, 1.0)  # set color to white
            elif next_color == 'black':
                glColor3f(0.0, 0.0, 0.0)  # set color to black
            draw_rect(curr_tile.get('x', -1),
                      curr_tile.get('y', -1),
                      tile_size,
                      tile_size)
            curr_tile['color'] = next_color
        except:
            pass
    else:
        pass


def build_board():
    glColor3f(1.0, 1.0, 1.0)  # set color to white
    for i in range(tile_grid):
        for j in range(tile_grid):
            tile = (i * tile_size, j * tile_size)
            tiles[i][j] = {'x': tile[0] + tile_spacing * i + 1,
                           'y': tile[1] + tile_spacing * j + 1,
                           'color': "white"}
            draw_rect(tile[0] + tile_spacing * i + 1,
                      tile[1] + tile_spacing * j + 1,
                      tile_size,
                      tile_size)


def draw_board():
    for i in range(tile_grid):
        for j in range(tile_grid):
            curr_tile = tiles[i][j]
            if curr_tile['color'] == 'white':
                glColor3f(1.0, 1.0, 1.0)  # set color to white
            elif curr_tile['color'] == 'black':
                glColor3f(0.0, 0.0, 0.0)  # set color to black
            draw_rect(curr_tile.get('x', -1),
                      curr_tile.get('y', -1),
                      tile_size,
                      tile_size)


def draw():  # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen
    glLoadIdentity()  # reset position
    refresh2d(width, height)  # set mode to 2d

    draw_board()
    update_ant()

    glutSwapBuffers()  # important for double buffering


# initialization
glutInit()  # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)  # set window size
glutInitWindowPosition(0, 0)  # set window position
window = glutCreateWindow(title=b'Ant')  # create window with title
glutDisplayFunc(draw)  # set draw function callback
glutIdleFunc(draw)  # draw all the time

build_board()

glutMainLoop()  # start everything
