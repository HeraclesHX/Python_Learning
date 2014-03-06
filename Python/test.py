#!/usr/bin/python
def repeater(value):
	while True:
		new = (yield value)
		if value is not None: value = new

r = repeater(42)
print list(r)
print r.next()
print r.send("Hello, world")


