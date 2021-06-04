import pygame as pg


class Button:
    content = None
    bg_color = [128, 128, 255]
    bg_color_Pressed = [255, 128, 0]
    size = [200, 50]
    pos = [0, 0]
    isPressed = 0

    def __init__(self, button_size, button_position, text="", background=None, backgroundWhenPressed=None):
        self.size = button_size
        self.pos = button_position
        if text != "":
            self.content = text
        if background:
            self.bg_color = background
        if backgroundWhenPressed:
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
        if (self.pos[0] < screen.get_width() or self.pos[0] + self.size[0] > 0) and (self.pos[1] < screen.get_height() or self.pos[1] + self.size[1] > 30):
            if self.isPressed:
                pg.draw.rect(screen, self.bg_color_Pressed, pg.Rect(self.pos, self.size))
            else:
                pg.draw.rect(screen, self.bg_color, pg.Rect(self.pos, self.size))
            if self.content:
                img = font.render(self.content, True, [0, 0, 0])
                rect = img.get_rect()
                rect.topleft = [self.pos[0] + self.size[0] / 2 - rect.width / 2, self.pos[1] + self.size[1] / 2 - rect.height / 2]
                screen.blit(img, rect)


class ZoneText:
    title = ""
    content = ""
    posCursor = 0
    size = [320, 50]
    pos = [0, 0]
    isIn = False
    sizeLimit = 22

    def __init__(self, title=None, text=None, textSize=None, textPos=None):
        if title:
            self.title = title
            self.sizeLimit -= len(self.title)
        if text:
            self.content = text[:self.sizeLimit]
            self.posCursor = len(self.content)
        if textPos:
            self.pos = textPos
        if textSize:
            self.size = textSize

    def clickIn(self):
        x, y = pg.mouse.get_pos()
        if self.pos[0] < x < self.pos[0] + self.size[0] and self.pos[1] < y < self.pos[1] + self.size[1]:
            self.isIn = True
        else:
            self.isIn = False

    def handleKeyDown(self, event):
        if event.key == pg.K_BACKSPACE:
            self.content = self.content[:max(self.posCursor - 1, 0)] + self.content[self.posCursor:]
            self.posCursor = max(self.posCursor - 1, 0)
        elif event.key == pg.K_DELETE:
            self.content = self.content[:self.posCursor] + self.content[self.posCursor + 1:]
            self.posCursor = min(len(self.content), self.posCursor)
        elif event.key == pg.K_RIGHT:
            self.posCursor = min(len(self.content), self.posCursor + 1)
        elif event.key == pg.K_LEFT:
            self.posCursor = max(0, self.posCursor - 1)
        elif self.posCursor < self.sizeLimit:
            self.content = self.content[:self.posCursor] + event.unicode + self.content[self.posCursor:]
            self.posCursor += 1

    def afficher(self, screen, font):
        if (self.pos[0] < screen.get_width() or self.pos[0] + self.size[0] > 0) and (self.pos[1] < screen.get_height() or self.pos[1] + self.size[1] > 30):
            pg.draw.rect(screen, [52, 189, 52], pg.Rect(self.pos, self.size))

            img_title = font.render(self.title + " :", True, [0, 0, 0])
            rect_title = img_title.get_rect()
            rect_title.topleft = [self.pos[0], self.pos[1] + self.size[1] / 2 - rect_title.height / 2]
            screen.blit(img_title, rect_title)

            img = font.render(self.content, True, [0, 0, 0])
            if self.isIn:
                curseur = pg.Surface((int(font.get_height() / 20 + 1), font.get_height()))
                img.blit(curseur, (font.render(self.content[:self.posCursor], True, [0, 0, 0]).get_width() - 0.5, 0))
            rect = img.get_rect()
            rect.topleft = [self.pos[0] + rect_title.width + (self.size[0] - rect_title.width) / 2 - rect.width / 2, self.pos[1] + self.size[1] / 2 - rect.height / 2]
            screen.blit(img, rect)


class Text:
    text = ""
    size = [320, 50]
    pos = [0, 0]

    def __init__(self, content="", textSize=None, textPos=None):
        self.text = content
        if textSize:
            self.size = textSize
        if textPos:
            self.pos = textPos

    def afficher(self, screen, font):
        if (self.pos[0] < screen.get_width() or self.pos[0] + self.size[0] > 0) and (self.pos[1] < screen.get_height() or self.pos[1] + self.size[1] > 30):
            img = font.render(self.text, True, [0, 0, 0])
            rect = img.get_rect()
            rect.topleft = [self.pos[0] + self.size[0] / 2 - rect.width / 2, self.pos[1] + self.size[1] / 2 - rect.height / 2]
            screen.blit(img, rect)


class Page:
    def __init__(self, title):
        self.title = title
        self.buttons = []
        self.zoneTexts = []
        self.texts = []
        self.links = {}

    def addButton(self, button):
        self.buttons.append(button)

    def addZoneText(self, zonetext):
        self.zoneTexts.append(zonetext)

    def addText(self, text):
        self.texts.append(text)

    def ScrollUp(self):
        canScroll = False
        for button in self.buttons:
            if button.pos[1] - 30 < 0:
                canScroll = True
                break
        if not canScroll:
            for zone in self.zoneTexts:
                if zone.pos[1] - 30 < 0:
                    canScroll = True
                    break
        if not canScroll:
            return

        for button in self.buttons:
            button.pos[1] += 10
        for zone in self.zoneTexts:
            zone.pos[1] += 10

    def ScrollDown(self, screenHeight):
        canScroll = False
        for button in self.buttons:
            if button.pos[1] + button.size[1] + 10 > screenHeight:
                canScroll = True
                break
        if not canScroll:
            for zone in self.zoneTexts:
                if zone.pos[1] + zone.size[1] + 10 > screenHeight:
                    canScroll = True
                    break
        if not canScroll:
            return

        for button in self.buttons:
            button.pos[1] -= 10
        for zone in self.zoneTexts:
            zone.pos[1] -= 10

    def GetZone(self, name):
        for zone in self.zoneTexts:
            if zone.title == name:
                return zone.content
        return None

    def afficher(self, screen, font):
        screen.fill([255, 255, 255])

        for zone in self.zoneTexts:
            zone.afficher(screen, font)
        for boutton in self.buttons:
            boutton.afficher(screen, font)
        for text in self.texts:
            text.afficher(screen, font)

        pg.draw.rect(screen, [128, 64, 255], pg.Rect(0, 0, screen.get_width(), 20))
        img = font.render(self.title, True, [0, 0, 0])
        rect = img.get_rect()
        rect.topleft = [screen.get_width() / 2 - rect.width / 2, 10 - rect.height / 2]
        screen.blit(img, rect)

