# Data Tags

DISPLAY_WIDTH = 0X01
DISPLAY_HEIGHT = 0x02
PADDLE_GAP = 0x03
PADDLE_GIRTH = 0x04
BALL_RADIUS = 0x05
FPS = 0x06
SCORE_TO_WIN = 0x07
BALL_POS = 0x08
P1_POS = 0x09
P2_POS = 0x0A
NEW_ROUND = 0X0B


# Client events
UP = 0x01
DOWN = 0x02
QUIT = 0x03
INITIALIZED = 0x04


sendOnce = {
    'DISPLAY_WIDTH': 0X00,
    'DISPLAY_HEIGHT': 0x01,
    'PADDLE_GAP': 0x02,
    'PADDLE_GIRTH': 0x03,
    'BALL_RADIUS': 0x04,
    'FPS': 0x05,
    'SCORE_TO_WIN': 0x06,
}


typeValue = {
    'BALL_POS': 0x08,
    'P1_POS': 0x09,
    'P2_POS': 0x0A,
    'NEW_ROUND': 0x0B
}

defaults = {
    'DISPLAY_WIDTH': 400,
    'DISPLAY_HEIGHT': 400,
    'PADDLE_GAP': 60,
    'PADDLE_GIRTH': 20,
    'BALL_RADIUS': 25,
    'FPS': 30,
    'SCORE_TO_WIN': 5,
    'BALL_POS': 1000,  #FIXME
    'BALL_VEL': 0,
    'P1_POS': 400,
    'P1_VEL': 0,
    'P2_POS': 400,
    'P2_VEL': 0,
    'NEW_ROUND': 0
}

