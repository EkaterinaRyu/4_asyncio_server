import asyncio
import nest_asyncio
nest_asyncio.apply()

HOST = 'localhost'
PORT = 9095


async def tcp_echo_client(host, port):
    reader, writer = await asyncio.open_connection(host, port)
    
    while True:
        message = input()

        writer.write(message.encode())
        await writer.drain()

        data = await reader.read(100)
        print(data.decode())
        if message == 'exit':
            break
    writer.close()
    # await writer.wait_closed()

# asyncio.run(tcp_echo_client(HOST, PORT))

loop = asyncio.get_event_loop()
task = loop.create_task(tcp_echo_client(HOST, PORT))
loop.run_until_complete(task)
