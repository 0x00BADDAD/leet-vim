import zmq



def main():
    ctx = zmq.Context()
    sock1 = ctx.socket(zmq.ROUTER) ## This is the socket where we receive the requests from the client
    sock1.bind("tcp://*:6666")

    # Initialize poll set
    poller = zmq.Poller()
    poller.register(sock1, zmq.POLLIN)

    while True:
        print(f'poller checked after 2 secs!')
        socks = dict(poller.poll(timeout=2000))

        if socks.get(sock1) == zmq.POLLIN:
            msg = sock1.recv_multipart(copy=False)
            print(f'client-id: {msg[0].bytes}  -- middle frame: {msg[1].bytes.decode()} -- msg-contents: {msg[2].bytes.decode()}')
            break




if __name__ == '__main__':
    main()
