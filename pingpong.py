from pygame import*

okno = display.set_mode((600,400))
fon = transform.scale(image.load('exture.jpg'),(600,400))
gm = True
clock = time.Clock()
FPS = 60

class sprit(sprite.Sprite):
    def __init__(self, imimage, x, y, sspeed):
        super().__init__()
        self.image = transform.scale(image.load(imimage),(65,65))
        self.speed = sspeed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def selff (self):
        okno.blit(self.image,(self.rect.x, self.rect.y))

class mach(sprit):
    def __init__(self,  x, y, imimage, sspeed):
        super().__init__()
        keys_pressed = key.get_pressed()
        self.image = transform.scale(image.load(imimage),(65,65))
        self.speed = sspeed
        self.rect.x = x
        self.rect.y = y
        

tennis = mach('tennis.png',60,2)

while gm:
    mach.self()
    okno.blit(fon,(0,0))
    for i in event.get():
        if i.type == QUIT:
            gm = False
    display.update()