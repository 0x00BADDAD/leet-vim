import zmq
import time


def main():
    ctx = zmq.Context()
    sock = ctx.socket(zmq.REQ)
    sock.setsockopt_string(option= zmq.IDENTITY, optval='cli1_uwu')
    sock.connect('tcp://localhost:6666')

    for i in range(3):
        print(f'sending Hello! {i}')
        sock.send(data= b'Hello from client!')




if __name__ == '__main__':
    main()
