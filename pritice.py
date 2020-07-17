class A:
    pass


class B(A):

    def __init__(self):
        print("__init__方法被执行")
    def __new__(cls):
        print("__new__方法被执行")
        return super().__new__(cls)



b = B()