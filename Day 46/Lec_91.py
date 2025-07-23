def simple_gen():
    yield "Hello"
    yield "World"

g = simple_gen()
print(next(g))  # Hello
print(next(g))  # World
