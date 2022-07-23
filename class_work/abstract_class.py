import abc


class A(abc.ABC):

    @abc.abstractmethod
    def must_be_implemented(self):
        return


class B(A):

    def must_be_implemented(self):
        print("Hello")
