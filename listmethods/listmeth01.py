#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
print(proto)
print(proto[1])
proto.extend("dns") # this lined will add d, n, and s
print(proto)
