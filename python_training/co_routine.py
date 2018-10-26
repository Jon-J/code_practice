
def co_routine():
    print("inside co-routine")
    while True:
        value = yield
        print("this is value = ", value)

gen1 = co_routine()
next(gen1)
gen1.send(20)
gen1.send(30)
gen1.send(40)
gen1.send(50)
gen1.send(60)
