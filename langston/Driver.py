import numpy as np
from OpenGL import GL, GLUT

from langston.ant import Ant

# window = 0  # glut window number
tile_size = 5
tile_grid = 120  # grid is a square: tile_grid x tile_grid
tile_spacing = 1
width = (tile_size * tile_grid) + (tile_spacing * tile_grid) + 1
height = (tile_size * tile_grid) + (tile_spacing * tile_grid) + 1
speed = 1  # ms
tiles = [[0 for x in range(tile_grid)] for y in range(tile_grid)]
ant = Ant(int(np.floor(tile_grid / 2)), int(np.floor(tile_grid / 2)), 'white', 'W')


def draw_rect(x, y, w, h):
    GL.glBegin(GL.GL_QUADS)  # start drawing a rectangle
    GL.glVertex2f(x, y)  # bottom left point
    GL.glVertex2f(x + w, y)  # bottom right point
    GL.glVertex2f(x + w, y + h)  # top right point
    GL.glVertex2f(x, y + h)  # top left point
    GL.glEnd()  # done drawing a rectangle


def refresh2d(w, h):
    GL.glViewport(0, 0, width, height)
    GL.glMatrixMode(GL.GL_PROJECTION)
    GL.glLoadIdentity()
    GL.glOrtho(0.0, w, 0.0, h, 0.0, 1.0)
    GL.glMatrixMode(GL.GL_MODELVIEW)
    GL.glLoadIdentity()


def update_ant(arg=None):
    global ant, tiles
    # print('ant')
    # if 0 <= ant.x < tile_grid and 0 <= ant.y < tile_grid:
    curr_tile = tiles[ant.x % tile_grid][ant.y % tile_grid]
    next_color = ant.next_step(curr_tile.get('color', -1))
    curr_tile['color'] = next_color
    # if curr_tile['color'] == 'white':
    #     gl.glColor3f(1.0, 1.0, 1.0)  # set color to white
    # elif curr_tile['color'] == 'black':
    #     gl.glColor3f(0.0, 0.0, 0.0)  # set color to black
    # draw_rect(curr_tile.get('x', -1),
    #           curr_tile.get('y', -1),
    #           tile_size,
    #           tile_size)
    GLUT.glutTimerFunc(speed, update_ant, None)
    GLUT.glutPostRedisplay(window)
    # else:
    #     pass


def build_board():
    global tiles
    GL.glColor3f(1.0, 1.0, 1.0)  # set color to white
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
                GL.glColor3f(1.0, 1.0, 1.0)  # set color to white
            elif curr_tile['color'] == 'black':
                GL.glColor3f(0.0, 0.0, 0.0)  # set color to black
            draw_rect(curr_tile.get('x', -1),
                      curr_tile.get('y', -1),
                      tile_size,
                      tile_size)
    curr_tile = tiles[ant.x % tile_grid][ant.y % tile_grid]
    GL.glColor3f(1.0, 0.0, 0.0)
    draw_rect(curr_tile.get('x', -1),
              curr_tile.get('y', -1),
              tile_size,
              tile_size)

def draw():  # draw is called all the time
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)  # clear the screen
    GL.glLoadIdentity()  # reset position
    refresh2d(width, height)  # set mode to 2d

    draw_board()
    # update_ant()

    GLUT.glutSwapBuffers()  # important for double buffering


# initialization
GLUT.glutInit()  # initialize glut
GLUT.glutInitDisplayMode(GLUT.GLUT_RGBA | GLUT.GLUT_DOUBLE | GLUT.GLUT_ALPHA | GLUT.GLUT_DEPTH)
GLUT.glutInitWindowSize(width, height)  # set window size
GLUT.glutInitWindowPosition(0, 0)  # set window position
window = GLUT.glutCreateWindow(b'Ant')  # create window with title
GLUT.glutDisplayFunc(draw)  # set draw function callback
GLUT.glutTimerFunc(speed, update_ant, None)
GLUT.glutPostRedisplay(window)
# glut.glutIdleFunc()  # draw all the time

build_board()

GLUT.glutMainLoop()  # start everything
