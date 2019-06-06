import pygame
import socket
import struct
import typevalue
from threading import Thread
from time import sleep, time
from multiprocessing.dummy import Pool as ThreadPool

#TODO: get info from server
initialized = False
defaults = []
# create a listener socket, and get information from server

class SocketClass:

    def listen(self, conn):
        global defaults
        global initialized
        while True:
            sleep(0.2)
            data = conn.recv(16)
            if not data:
                continue
            data = struct.unpack('hl', data)
            if data not in defaults and len(defaults) < 7:
                defaults.append(data)
            if len(defaults) == 7:
                temp = [None, None, None, None, None, None, None]
                for i in defaults:
                    temp[i[0]] = i[1]
                defaults = temp
                defaults.append(1)  # Makes the length 8 so client wont continually send "initialized" packets
                data = struct.pack('hl', 0x04, 1)
                initialized = True
                sockOut.send(data)
        conn.close()

    def talk(self, sockIn, sockOut):
        game_exit = False
        while not game_exit:
            tags = []
            values = []
            try:
                for event in pygame.event.get():
                    tags = []
                    values = []
                    if event.type == pygame.QUIT:
                        tags.append(typevalue.QUIT)
                        values.append(1)
                        game_exit = True  # This allows the X in the corner to close the window.
                    elif event.type == pygame.KEYDOWN:  # Everything in this elif statement has key input handling
                        if event.key == pygame.K_UP:
                            tags.append(typevalue.UP)
                            values.append(1)
                        elif event.key == pygame.K_DOWN:
                            tags.append(typevalue.DOWN)
                            values.append(1)
                    elif event.type == pygame.KEYUP:  # Event handling when key is lifted.
                        if event.key == pygame.K_UP:
                            tags.append(typevalue.UP)
                            values.append(0)
                        elif event.key == pygame.K_DOWN:
                            tags.append(typevalue.DOWN)
                            values.append(0)
                for ind in range(len(tags)):
                    data = struct.pack('hl', tags[ind], values[ind])
                    sockOut.send(data)
            except:
                pass
        pygame.quit()
        quit()

def pygameInitialize():
    DISPLAY_WIDTH = defaults[0]
    DISPLAY_HEIGHT = defaults[1]
    pygame.init()
    pygame.mouse.set_visible(False)
    gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    clock = pygame.time.Clock()
    score_font = pygame.font.SysFont(None, DISPLAY_WIDTH // 20)
    alert_font = pygame.font.SysFont(None, 24)
    #pygame.quit()
    #quit()



if __name__ == '__main__':
    server = ('127.0.0.1', 2000)
    client = ('localhost', 1500)
    sockOut = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockOut.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sockIn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockIn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sockIn.bind(client)
    sockIn.listen(5)
    sockOut.connect(server)
    socks = SocketClass()
    conn, addr = sockIn.accept()
    pool = ThreadPool(2)
    listener = Thread(target=socks.listen, args=(conn,))
    talker = Thread(target=socks.talk, args=(sockIn, sockOut,))
    listener.start()
    while not initialized:
        sleep(0.2)
    pygameInitialize()
    talker.start()
