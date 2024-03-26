import pygame
from OpenGL.GL import *
import random

SCREEN_SIZE = (800, 600)

# planet parameters
sun_radius = 80
sun_pos = (0, 0)
sun_color = (1, 1, 0)
sun_rotation_speed = 0.2
mercury_radius = 10
mercury_pos = (130, 0)
mercury_color = (0.5, 0.5, 0.5)
mercury_rotation_speed = 3
venus_radius = 15
venus_pos = (190, 0)
venus_color = (1, 0.5, 0)
venus_rotation_speed = 2
earth_radius = 20
earth_pos = (260, 0)
earth_color = (0, 0, 1)
earth_rotation_speed = 1
mars_radius = 18
mars_pos = (330, 0)
mars_color = (1, 0, 0)
mars_rotation_speed = 0.5

#spaceship parameters
triangle_pos = [0, 0]
triangle_size = 5


def draw_circle(center, radius, color):
    glColor3f(*color)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(center[0], center[1])
    x, y = radius, 0
    d = 1 - radius
    while x >= y:
        glVertex2f(center[0] + x, center[1] + y)
        glVertex2f(center[0] + y, center[1] + x)
        glVertex2f(center[0] - y, center[1] + x)
        glVertex2f(center[0] - x, center[1] + y)
        glVertex2f(center[0] - x, center[1] - y)
        glVertex2f(center[0] - y, center[1] - x)
        glVertex2f(center[0] + y, center[1] - x)
        glVertex2f(center[0] + x, center[1] - y)
        if d < 0:
            d += 2 * y + 3
        else:
            d += 2 * (y - x) + 5
            x -= 1
        y += 1
    glEnd()


def draw_triangle(pos, size, color):
    glColor3f(*color)
    glBegin(GL_TRIANGLES)
    x, y = pos[0], pos[1] - size
    x1, y1 = x - size, y + size
    x2, y2 = x + size, y + size

    dx1, dy1 = x1 - x, y1 - y
    dx2, dy2 = x2 - x, y2 - y

    d1 = dx1 - dy1
    d2 = dx2 - dy2

    while y < pos[1]:
        glVertex2f(x, y + size)
        glVertex2f(x1, y1 + size)
        glVertex2f(x2, y2 + size)

        if d1 > 0:
            x += 1
            dx1 -= 2 * dy1
            d1 -= 2 * dy1
        if d1 <= 0:
            y += 1
            dy1 += 2 * dx1
            d1 += 2 * dx1

        if d2 > 0:
            x2 -= 1
            dx2 -= 2 * dy2
            d2 -= 2 * dy2
        if d2 <= 0:
            y2 += 1
            dy2 += 2 * dx2
            d2 += 2 * dx2

        x1 += 1
        dx1 += 2 * dy1
        d1 += 2 * dy1

        x2 -= 1
        dx2 -= 2 * dy2
        d2 -= 2 * dy2

    glEnd()


def main():
    pygame.init()
    pygame.display.set_mode(SCREEN_SIZE, pygame.DOUBLEBUF | pygame.OPENGL)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-400, 400, -300, 300, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    clock = pygame.time.Clock()

    # Generate star positions
    star_positions = [(random.uniform(-400, 400), random.uniform(-300, 300)) for _ in range(1000)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                triangle_pos[0] -= 5
            elif keys[pygame.K_RIGHT]:
                triangle_pos[0] += 5
            elif keys[pygame.K_UP]:
                triangle_pos[1] += 5
            elif keys[pygame.K_DOWN]:
                triangle_pos[1] -= 5

        glClearColor(51.0/255.0, 51.0/255.0, 52.0/255.0, 1.0);
        glClear(GL_COLOR_BUFFER_BIT)


        # Draw stars
        for pos in star_positions:
            draw_circle(pos, 1, (1, 1, 1))

        # Draw Sun
        draw_circle(sun_pos, sun_radius, sun_color)

        #draw triangle
        draw_triangle(triangle_pos, triangle_size, (1, 1, 1))

        # Draw Mercury and rotate it
        glPushMatrix()
        glRotatef(pygame.time.get_ticks() * mercury_rotation_speed / 1000, 0, 0, 1)
        draw_circle(mercury_pos, mercury_radius, mercury_color)
        glPopMatrix()

        # Draw Venus and rotate it
        glPushMatrix()
        glRotatef(pygame.time.get_ticks() * venus_rotation_speed / 1000, 0, 0, 1)
        draw_circle(venus_pos, venus_radius, venus_color)
        glPopMatrix()

        # Draw Earth and rotate it
        glPushMatrix()
        glRotatef(pygame.time.get_ticks() * earth_rotation_speed / 1000, 0, 0, 1)
        draw_circle(earth_pos, earth_radius, earth_color)
        glPopMatrix()

        # Draw Mars and rotate it
        glPushMatrix()
        glRotatef(pygame.time.get_ticks() * mars_rotation_speed / 1000, 0, 0, 1)
        draw_circle(mars_pos, mars_radius, mars_color)
        glPopMatrix()

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
