# key-value-db

### Dead simple python implementation of a key-value server. 
Uses [asyncio](https://docs.python.org/3/library/asyncio.html) to manage IO between client and server, and [h11](https://github.com/python-hyper/h11) for HTTP parsing. Data is stored in python dictionary (in bytes).

* Server startup via command-line with single argument: `python server.py --location {location}`

Defaults to serving on `localhost:8889` but can be changed via command line: `python server.py --location example.data --address=123.123.123 --port=80`

Requests to the server are made with curl. For example from the example data:
 `curl localhost:8889/3f47dc34-c2e9-4f00-98f1-337d16423934` will return `zyalpvvu`
