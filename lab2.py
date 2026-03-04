import glfw 
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

vertices_cubo = ((1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1), 
                 (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1))


faces_cubo = ((0, 1, 2, 3), (3, 2, 7, 6), (6, 7, 5, 4), 
              (4, 5, 1, 0), (1, 5, 7, 2), (4, 0, 3, 6))

cores_cubo = ((1, 0, 0), (0, 1, 0), (0, 0, 1), 
              (1, 1, 0), (1, 0, 1), (0, 1, 1))

def desenhar_cubo():
    glBegin(GL_QUADS)
    for i, face in enumerate(faces_cubo):
        glColor3f(*cores_cubo[i])
        for vertice in face: 
            glVertex3f(*vertices_cubo[vertice])
    glEnd()


glfw.init()

window = glfw.create_window(640, 480, "Lab 3D", None, None)

glfw.make_context_current(window)
glfw.swap_interval(1)

glEnable(GL_DEPTH_TEST)
glClearColor(0.0, 0.0, 0.0, 1.0)


glMatrixMode(GL_PROJECTION)
gluPerspective(45, (640/480), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)

while not glfw.window_should_close(window): 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()

    glTranslatef(0, 0, -5)
    glRotatef(45, 0, 1, 0)
    desenhar_cubo()

    glfw.window_buffers(window)
    glfw.poll_events()

glfw.terminate()
