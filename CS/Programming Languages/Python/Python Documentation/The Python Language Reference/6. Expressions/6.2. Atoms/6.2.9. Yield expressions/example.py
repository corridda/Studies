def gen():  # defines a generator function
    yield 123


async def agen():  # defines an asynchronous generator function (PEP 525)
    yield 123


gen = gen()
agen = agen()
print(f"type(gen): {type(gen)}")
print(f"type(agen): {type(agen)}\n")



def echo(value=None):
    print("Execution starts when 'next()' is called for the first time.")
    try:
        while True:
            try:
                value = (yield value)
            except Exception as e:
                value = e
    finally:
        print("Don't forget to clean up when 'close()' is called.")


generator = echo(1)
print(next(generator))
print(next(generator))
print(generator.send(2))
print(generator.throw(TypeError, "spam"))
generator.close()