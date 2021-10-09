from threading import Lock

class Singleton():
    _instance_lock = Lock()

    def __init__(self):
        print("this is init")

    @classmethod
    def get_instance(cls,*args,**kwargs):
        if not hasattr(Singleton,"_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = Singleton(*args,**kwargs)
        return Singleton._instance



print(Singleton.__dict__)
a = Singleton().get_instance()
print(Singleton.__dict__)
b = Singleton().get_instance()
print(Singleton.__dict__)
print(id(a),id(b))


class A():
    def __init__(self,a,b=[]):
        self.a = a
        self.b = b

    def add(self,par):
        self.b.append(par)


group1 = A(1)
group2 = A(2)

group1.add("a")
group1.add("b")

group2.add("c")
group2.add("d")


print(id(group1.b))
print(id(group2.b))