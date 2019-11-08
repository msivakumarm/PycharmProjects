import inspect

# functions
def whoami():
    return inspect.stack()[1][3]

def myfunc():
    x=whoami()
    print(x)


myfunc()