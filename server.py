import argparse
import asyncio

import h11

import keyvaluedb


class HTTPProtocol(asyncio.Protocol):
    # Asyncio protocol to serve barebones GET request
    # TODO: Deal with timeouts and add drain
    def __init__(self) -> None:
        self.connection = h11.Connection(h11.SERVER)
        self.db = db

    def connection_made(self, transport) -> None:
        peername = transport.get_extra_info("peername")
        print(f"Connection from {peername}")
        self.transport = transport

    def data_received(self, data) -> None:
        self.connection.receive_data(data)
        while True:
            event = self.connection.next_event()
            if isinstance(event, h11.Request):
                self.send_response(event)
            elif (
                isinstance(event, h11.ConnectionClosed)
                or event is h11.NEED_DATA
                or event is h11.PAUSED
            ):
                break
        if self.connection.our_state is h11.MUST_CLOSE:
            self.transport.close()

    def send_response(self, event) -> None:
        # Lookup from key-value DB
        body = db.get(event.target[1:])
        headers = [
            ("content-type", "text/plain"),
            ("content-length", str(len(body))),
        ]
        response = h11.Response(status_code=200, headers=headers)
        self.send(response)
        self.send(h11.Data(data=body))
        self.send(h11.EndOfMessage())

    def send(self, event) -> None:
        data = self.connection.send(event)
        self.transport.write(data)


async def main(host, port) -> None:
    loop = asyncio.get_running_loop()
    server = await loop.create_server(HTTPProtocol, host, port)
    print(f"Serving on {host}:{port}")
    await server.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="data file location")
    parser.add_argument("--location", type=str)
    parser.add_argument("--address", type=str, default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8889)
    args = parser.parse_args()
    db = keyvaluedb.load(args.location)

    asyncio.run(main(args.address, args.port))
