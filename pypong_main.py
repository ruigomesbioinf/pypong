# IMPORTS
import pygame
import random
import os

# SET DISPLAY
pygame.init()
display_width = 640
display_height = 480
display = pygame.display.set_mode( (display_width, display_height) )
pygame.display.set_caption( "PyPong" )
clock = pygame.time.Clock()

# CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRASS = (0, 154, 23)


def gameloop():
    
    score1 = 0
    score2 = 0

    # UNIVERSAL PLAYER STRIBUTES
    SPEED = 12
    BLOCK_WIDTH = 20
    BLOCK_HEIGHT = 100

    # PLAYER 1 ATRIBUTES
    X1 = 0
    Y1 = 0
    Y1_CHANGE = 0

    # PLAYER 2 ATRIBUTES
    X2 = display_width - BLOCK_WIDTH
    Y2 = 0
    Y2_CHANGE = 0

    # BALL ATRIBUTES
    XBALL = display_width // 2
    YBALL = display_height // 2
    '''
    XBALL_CHANGE = random.randint(8, 16) # horizontal change
    YBALL_CHANGE = random.randint(4, 12) # vertical change
    '''
    XBALL_CHANGE = -5
    YBALL_CHANGE = 0
    BALL_RADIUS = 25


    # MAIN LOGIC
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Y1_CHANGE = -SPEED
                elif event.key == pygame.K_DOWN:
                    Y1_CHANGE = SPEED

        Y1 += Y1_CHANGE
        XBALL += XBALL_CHANGE
        YBALL += YBALL_CHANGE
        # DRAW THE SCREEN WITH LINES AND PLAYERS AND BALL
        display.fill(GRASS)
        pygame.draw.rect(display, WHITE, [X1, Y1, BLOCK_WIDTH, BLOCK_HEIGHT])
        pygame.draw.rect(display, WHITE, [X2, Y2, BLOCK_WIDTH, BLOCK_HEIGHT])
        pygame.draw.circle(display, WHITE, ( display_width // 2, display_height // 2), 30)
        pygame.draw.circle(display, GRASS, ( display_width // 2, display_height // 2), 20)
        pygame.draw.line(display, WHITE,(display_width // 2, 0), (display_width // 2, display_height), 10)
        ball = pygame.image.load(os.path.join("assets", "ball.png"))
        ball = pygame.transform.scale(ball, (BALL_RADIUS, BALL_RADIUS))
        display.blit(ball, (XBALL, YBALL))
        
        # PLAYER BOUNDARIES
        # PLAYER 1
        if Y1 > display_height - BLOCK_HEIGHT:
            Y1 = display_height - BLOCK_HEIGHT
        elif Y1 < 0:
            Y1 = 0
        # PLAYER 2
        if Y2 > display_height - BLOCK_HEIGHT:
            Y2 = display_height - BLOCK_HEIGHT
        elif Y2 < 0:
            Y2 = 0

        # BALL TOP AND BOTTOM BOUNDARIES
        if YBALL <= 0:
            YBALL_CHANGE = -YBALL_CHANGE
        if YBALL >= display_height + 1 - BALL_RADIUS:
            YBALL_CHANGE = -YBALL_CHANGE
        
        # GOAL LOGIC
        if XBALL >= display_width:
            XBALL = display_width // 2
            YBALL = display_height // 2
            XBALL_CHANGE = -XBALL_CHANGE
            score1 += 1
        elif XBALL < 0:
            XBALL = display_width // 2
            YBALL = display_height // 2
            XBALL_CHANGE = -XBALL_CHANGE
            score2 += 1
        
        # PADDLES LOGIC
        # PLAYER1
        if XBALL == BLOCK_WIDTH and YBALL in range(Y1 - BLOCK_HEIGHT // 2, Y1 + BLOCK_HEIGHT // 2, 1):
            XBALL_CHANGE = -XBALL_CHANGE
            YBALL_CHANGE = random.randint(1, 10)
        
        # PLAYER2
        # movement (""" automatic movement simulation """)
        if YBALL > Y2:
            Y2 += SPEED
        elif YBALL < Y2:
            Y2 -= SPEED

        # boundaries player 2 paddle
        if XBALL >= display_width + 1 - BALL_RADIUS - BLOCK_WIDTH and YBALL in range(Y2 - BLOCK_HEIGHT // 2, Y2 + BLOCK_HEIGHT // 2, 1):
            XBALL_CHANGE = -XBALL_CHANGE
            YBALL_CHANGE = random.randint(1, 10)
        
        # SCORES
        myfont1 = pygame.font.SysFont("Comic Sans MS", 20)
        label1 = myfont1.render("Score "+str(score1), 1, (255,255,0))
        display.blit(label1, (50,20))

        myfont2 = pygame.font.SysFont("Comic Sans MS", 20)
        label2 = myfont2.render("Score "+str(score2), 1, (255,255,0))
        display.blit(label2, (470, 20)) 

        pygame.display.update()
        clock.tick(SPEED)
    
gameloop()
