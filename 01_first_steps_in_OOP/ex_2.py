x = "global"


def outer():
    x = "local"

    def inner():
        nonlocal x #promenqme stojnosta na x v gornata funkciq s tazi koqto e na dolniqt red(9red)
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()


print(x)
outer()
print(x)
print(x)