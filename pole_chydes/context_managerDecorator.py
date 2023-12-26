from contextlib import contextmanager
@contextmanager
def DividerContext(divider):
    print(f"Before executing code using a separator: {divider}")
    yield
    print(f"After executing code using a separator: {divider}:")

divider = "==="

with DividerContext(divider):
    print("This is a code that the using separator. ")