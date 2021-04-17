import pygame as pg

class Utilisateur:
    nom = "PAJON"
    prenom = "Quentin"
    age = 21
    licences = []

    def __init__(self):
        pass

    def ajoutLicence(self, idx, droits):
        self.licences.append({idx: idx, droits: droits})

    def droitsLicence(self, idx):
        for licence in self.licences:
            if licence.idx == idx:
                return licence.droits
        return 0


class Club:
    nom = None
    description = None

    def __init__(self, nom, description):
        self.nom = nom
        self.description = description


class Button:
    content = None
    bg_color = None
    bg_color_Pressed = None
    size = [200, 50]
    pos = [0, 0]
    isPressed = 0

    def __init__(self, button_size, button_position, text="", background=[128, 128, 128],
                 backgroundWhenPressed=[64, 64, 64]):
        self.size = button_size
        self.pos = button_position
        if text != "":
            self.content = text
        self.bg_color = background
        self.bg_color_Pressed = backgroundWhenPressed

    def mouseInButton(self, pressed):
        x, y = pg.mouse.get_pos()
        if self.pos[0] < x < self.pos[0] + self.size[0] and self.pos[1] < y < self.pos[1] + self.size[1]:
            wasPressed = self.isPressed
            self.isPressed = pressed
            return wasPressed
        self.isPressed = False
        return False

    def afficher(self, screen, font):
        if (self.pos[0] < screen.get_width() or self.pos[0] + self.size[0] > 0) and (
                self.pos[1] < screen.get_height() or self.pos[1] + self.size[1] > 0):
            if self.isPressed:
                pg.draw.rect(screen, self.bg_color_Pressed, pg.Rect(self.pos, self.size))
            else:
                pg.draw.rect(screen, self.bg_color, pg.Rect(self.pos, self.size))
            if self.content:
                img = font.render(self.content, True, [0, 0, 0])
                rect = img.get_rect()
                rect.topleft = [self.pos[0] + self.size[0] / 2 - rect.width / 2,
                                self.pos[1] + self.size[1] / 2 - rect.height / 2]
                screen.blit(img, rect)

