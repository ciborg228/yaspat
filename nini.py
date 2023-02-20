import pygame


w, hue = [int(x) for x in input().split()]


def draw_cube():
    c1 = pygame.Color(255, 255, 255)
    hsv = color1.hsva
    color2 = pygame.Color(255, 255, 255)
    hsv2 = color2.hsva
    color3 = pygame.Color(255, 255, 255)
    hsv3 = color3.hsva
    wx = 130 - (w / 2)
    wy = 180 - (w / 2)
    ww = w / 2
    color1.hsva = (hue, hsv[1] + 100, hsv[2] - 25, hsv[3])
    color2.hsva = (hue, hsv2[1] + 100, hsv2[2], hsv[3])
    color3.hsva = (hue, hsv3[1] + 100, hsv3[2] - 50, hsv[3])
    pygame.draw.polygon(screen, color1, ((wx, wy), (wx + w, wy), (wx + w, wy + w), (wx, wy + w)))
    pygame.draw.polygon(screen, color2, ((wx + ww, wy - ww), (wx + ww + w, wy - ww), (wx + w, wy), (wx, wy)))
    pygame.draw.polygon(screen, color3, ((wx + w, wy), (wx + ww + w, wy - ww), (wx + ww + w, wy + ww),
                                    (wx + w, wy + w)))
if w % 4 == 0 and w <= 100 and 0 <= hue <= 360:
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    while pygame.event.wait().type != pygame.QUIT:
        draw_cube()
        pygame.display.flip()
    pygame.quit()
else:
    print('Неправильный формат ввода')