# Python example to check if a class is subclass of another
class Base:
    pass
class Derived(Base):
    pass

print(issubclass(Derived,Base))
print(issubclass(Base,Derived))

d = Derived()
b = Base()

# b is not an instance of Derived
print(isinstance(b, Derived))

# But d is an instance of Base
print(isinstance(d, Base))
