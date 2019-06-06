
import socket
import struct
import typevalue
import time
from threading import Thread


incoming = []
initialized = False


class socketClass():

    def listen(self, conn):
        global initialized
        print('listening...')
        while True:
            data = conn.recv(16)
            if not data:
                continue
            data = struct.unpack('hl', data)
            if data[0] == 0x04:
                initialized = True
            print(data)

    def talk(self, sockIn, sockOut):
        while True:
            global initialized
            if initialized:
                for name, tag in typevalue.typeValue.items():
                    value = typevalue.defaults[name]
                    data = struct.pack('hl', tag, value)
                    sockOut.send(data)
            else:
                for name, tag in typevalue.sendOnce.items():
                    value = typevalue.defaults[name]
                    data = struct.pack('hl', tag, value)
                    sockOut.send(data)



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
    listener.start()
    talker.start()
