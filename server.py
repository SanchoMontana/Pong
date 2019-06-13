
import socket
import struct
import typevalue
from time import sleep
from threading import Thread, Lock


lock = Lock()
incoming = []
initialized = False
transfer_data = []
movement_vars = typevalue.defaults
translate_obj = []


class socketClass():

    def listen(self, conn):
        print('listening...')
        global initialized, transfer_data
        while True:
            data = conn.recv(16)
            if not data:
                continue
            data = struct.unpack('hl', data)
            if data[0] == 0x04:
                lock.acquire()
                initialized = True
                lock.release()
            lock.acquire()
            transfer_data.append(data)
            lock.release()
            print(data)

    def talk(self, sockIn, sockOut):
        while True:
            sleep(0.20)
            global initialized
            if initialized:
                for name, tag in typevalue.typeValue.items():
                    value = movement_vars[name]
                    data = struct.pack('hl', tag, value)
                    sockOut.send(data)
            else:
                for name, tag in typevalue.sendOnce.items():
                    value = typevalue.defaults[name]
                    data = struct.pack('hl', tag, value)
                    sockOut.send(data)


def game_loop():
    while True:
        for packet in transfer_data:
            for obj in translate_obj:
                if packet[0] == obj.event_num:
                    lock.acquire()
                    obj.value = packet[1]
                    lock.release()
        for obj in translate_obj:
            obj.change_variables()
        sleep(0.1)


class Compute:
    def __init__(self, event_num, variable, increment):
        self.event_num = event_num
        self.variable = variable
        self.increment = increment
        self.value = 0

    def change_variables(self):
        global movement_vars
        lock.acquire()
        print("Before: " + str(movement_vars['P1_POS']))
        movement_vars['P1_POS'] += self.value * self.increment
        print("After: " + str(movement_vars['P1_POS']))
        lock.release()


translate_obj.append(Compute(typevalue.clientEvent['UP'], movement_vars['P1_POS'], 5))
translate_obj.append(Compute(typevalue.clientEvent['DOWN'], movement_vars['P1_POS'], -5))

if __name__ == '__main__':
    server = ('localhost', 2000)
    sockIn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockIn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sockIn.bind(server)
    sockIn.listen(5)
    conn, addr = sockIn.accept()
    client = (addr[0], 1500)

    sockOut = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockOut.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sockOut.connect(('localhost', 1500))

    socks = socketClass()
    listener = Thread(target=socks.listen, args=(conn,))
    talker = Thread(target=socks.talk, args=(sockIn, sockOut,))
    game = Thread(target=game_loop, args=())
    listener.start()
    talker.start()
    game.start()
