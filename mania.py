import pygame, random, sys 

pygame.init()
pygame.font.init()

SIZE = [800,600]
screen = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)

clock = pygame.time.Clock()

FPS = 60
SPEED = 10

font = pygame.font.Font("./Fonts/bit5x3.ttf", 50)

score = 1

total = 1

lanepos = []

for i in range(4):
    x = (SIZE[0]/5)*(i+1)
    lanepos.append(int(x))

class Tile(pygame.sprite.Sprite):

    def __init__(self, x, c):
        super().__init__()
        self.width = 50
        self.height = 50
        self.img = pygame.Surface([self.width, self.height])
        self.img.fill(c)
        self.rect = self.img.get_rect()
        self.rect.centerx = x
        self.rect.centery = (3/4)*SIZE[1]

    def collide(self, obj):
        if pygame.sprite.collide_rect(self, obj):
            return True
        else:
            return False

    def render(self):
        screen.blit(self.img, self.rect)

    def update(self):
        self.render()

class Block(pygame.sprite.Sprite):

    def __init__(self, x, c):
        super().__init__()
        self.width = 25
        self.height = 25
        self.img = pygame.Surface([self.width, self.height])
        self.img.fill(c)
        self.rect = self.img.get_rect()
        self.rect.centerx = x
        self.rect.centery = random.randint(-SIZE[1], -self.height)

        self.default_color = c

    def move(self):
        if self.rect.centery < -self.height:
            self.rect.centery = self.rect.centery + random.randint(SPEED/10,SPEED)
        else:
            self.rect.centery = self.rect.centery + SPEED

    def render(self):
        screen.blit(self.img, self.rect)
    
    def update(self):
        global score, total
        self.render()
        if self.rect.centery > SIZE[1]+self.height:
            self.img.fill(self.default_color)
            self.rect.centery = random.randint(-SIZE[1], -self.height)
            total = total + 1

tiles = []
tile = Tile(lanepos[0], [255,0,0])
tiles.append(tile)
tile = Tile(lanepos[1], [0,0,255])
tiles.append(tile)
tile = Tile(lanepos[2], [255,0,0])
tiles.append(tile)
tile = Tile(lanepos[3], [0,0,255])
tiles.append(tile)

blocks = []

block = Block(lanepos[0],[255,0,0])
blocks.append(block)
block = Block(lanepos[1],[0,0,255])
blocks.append(block)
block = Block(lanepos[2],[255,0,0])
blocks.append(block)
block = Block(lanepos[3],[0,0,255])
blocks.append(block)

while True:

    event_list = pygame.event.get()
    screen.fill([0,0,0])

    for event in event_list:
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if tiles[0].collide(blocks[0]):
                    score = score + 1
                    blocks[0].img.fill([0,0,0])

            if event.key == pygame.K_f:
                if tiles[1].collide(blocks[1]):
                    score = score + 1
                    blocks[1].img.fill([0,0,0])

            if event.key == pygame.K_j:
                if tiles[2].collide(blocks[2]):
                    score = score + 1
                    blocks[2].img.fill([0,0,0])

            if event.key == pygame.K_k:
                if tiles[3].collide(blocks[3]):
                    score = score + 1
                    blocks[3].img.fill([0,0,0])

    for tile in tiles:
        tile.update()

    for block in blocks:
        block.update()
        block.move()

    score_surface = font.render(str(round((score/total)*100)) + "%", True, [255,255,255], [100,100])
    screen.blit(score_surface, (10,10))

    clock.tick(FPS)
    pygame.display.update()