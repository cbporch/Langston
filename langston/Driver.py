# from OpenGL.GLU import *
import numpy as np
from OpenGL import GL as gl, GLUT as glut

from langston.ant import Ant

window = 0  # glut window number
tile_size = 10
tile_grid = 70  # grid is a square: tile_grid x tile_grid
tile_spacing = 1
width = (tile_size * tile_grid) + (tile_spacing * tile_grid) + 1
height = (tile_size * tile_grid) + (tile_spacing * tile_grid) + 1

tiles = [[0 for x in range(tile_grid)] for y in range(tile_grid)]
ant = Ant(int(np.floor(tile_grid / 2)), int(np.floor(tile_grid / 2)), 'white', 'N')


def draw_rect(x, y, w, h):
    gl.glBegin(gl.GL_QUADS)  # start drawing a rectangle
    gl.glVertex2f(x, y)  # bottom left point
    gl.glVertex2f(x + w, y)  # bottom right point
    gl.glVertex2f(x + w, y + h)  # top right point
    gl.glVertex2f(x, y + h)  # top left point
    gl.glEnd()  # done drawing a rectangle


def refresh2d(w, h):
    gl.glViewport(0, 0, width, height)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    gl.glOrtho(0.0, w, 0.0, h, 0.0, 1.0)
    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()


def update_ant():
    global ant, tiles
    if 0 <= ant.x < tile_grid and 0 <= ant.y < tile_grid:
        curr_tile = tiles[ant.x][ant.y]
        next_color = ant.next_step(curr_tile.get('color', -1))
        curr_tile['color'] = next_color
    else:
        pass


def build_board():
    global tiles
    gl.glColor3f(1.0, 1.0, 1.0)  # set color to white
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
    global tiles
    for i in range(tile_grid):
        for j in range(tile_grid):
            curr_tile = tiles[i][j]
            if curr_tile['color'] == 'white':
                gl.glColor3f(1.0, 1.0, 1.0)  # set color to white
            elif curr_tile['color'] == 'black':
                gl.glColor3f(0.0, 0.0, 0.0)  # set color to black
            draw_rect(curr_tile.get('x', -1),
                      curr_tile.get('y', -1),
                      tile_size,
                      tile_size)


def draw():  # draw is called all the time
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)  # clear the screen
    gl.glLoadIdentity()  # reset position
    refresh2d(width, height)  # set mode to 2d

    draw_board()
    update_ant()

    glut.glutSwapBuffers()  # important for double buffering


# initialization
glut.glutInit()  # initialize glut
glut.glutInitDisplayMode(glut.GLUT_RGBA | glut.GLUT_DOUBLE | glut.GLUT_ALPHA | glut.GLUT_DEPTH)
glut.glutInitWindowSize(width, height)  # set window size
glut.glutInitWindowPosition(0, 0)  # set window position
window = glut.glutCreateWindow(title=b'Ant')  # create window with title
glut.glutDisplayFunc(draw)  # set draw function callback
glut.glutIdleFunc(draw)  # draw all the time
build_board()

glut.glutMainLoop()  # start everything
