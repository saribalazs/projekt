import pygame, sys, socket
from paddle import Paddle
from labda import Labda


pygame.init()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1250))


fekete = (0,0,0)
feher = (255,255,255)

meret = (700,500)
ablak = pygame.display.set_mode(meret)
hatterkep = pygame.image.load('hatter.jpg')
hatterkep = pygame.transform.scale(hatterkep, meret)

paddleA = Paddle(feher, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
 
paddleB = Paddle(feher, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

labda = Labda(feher,10,10)
labda.rect.x = 345
labda.rect.y = 195

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(labda)

ora = pygame.time.Clock()

pont = 0
pont2 = 0

while True:
    ablak.blit(hatterkep,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    uzenet = s.recv(1024)
    adatok = uzenet.decode("utf-8").replace('(','').replace(')','').replace(' ', '').strip().split(',')

    igaz = False
    if adatok[0] != '':
        cyb = int(adatok[0])
        cyj = int(adatok[1])
        igaz = True
    
    if igaz:
        paddleA.rect.y = cyj
        paddleB.rect.y = cyb


    

    all_sprites_list.update()
    
    if labda.rect.x>=690:
        labda.velocity[0] = -labda.velocity[0]
        pont += 1
        labda.rect.x = 345
        labda.rect.y = 195
        if pont == 10:
            labda.velocity = 0
            print("A nyertes: 1. Játékos")
            sys.exit()
    if labda.rect.x<=0:
        labda.velocity[0] = -labda.velocity[0]
        pont2 += 1
        labda.rect.x = 345
        labda.rect.y = 195
        if pont2 == 10:
            labda.velocity = 0
            print("A nyertes: 2. Játékos")
            sys.exit()
    if labda.rect.y>490:
        labda.velocity[1] = -labda.velocity[1]
    if labda.rect.y<0:
        labda.velocity[1] = -labda.velocity[1] 

    if pygame.sprite.collide_mask(labda, paddleA) or pygame.sprite.collide_mask(labda, paddleB):
      labda.bounce()


    pygame.draw.line(ablak, feher, [349,0], [349,500], 5)

    font = pygame.font.Font(None, 74)
    text = font.render(str(pont), 1, feher)
    ablak.blit(text, (250,10))
    text = font.render(str(pont2), 1, feher)
    ablak.blit(text, (420,10))

    all_sprites_list.draw(ablak)
    
    
    pygame.display.flip()
    
    ora.tick(60)
    
pygame.quit()