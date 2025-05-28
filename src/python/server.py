import asyncio
import json


async def client_cb(reader, writer):
    print(f'Client connected!')
    print(f'Trying to read off the socket...')
    data = await reader.readline()
    data = data.decode()
    data += 'some modification from server'
    print(f'Data read is: {data} and type is: {type(data)}')
    print('writing response...')
    writer.write(bytes(data, encoding='utf-8'))
    await writer.drain()
    print('response sent!')
    writer.close()
    await writer.wait_closed()



async def main():
    print(f'Starting server at localhost:6666')
    server = await asyncio.start_server(client_cb, '127.0.0.1', 6666)

    async with server:
        await server.serve_forever()




if __name__ == '__main__':
    asyncio.run(main())
