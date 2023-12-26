class DividerContext:
    def __init__(self, divider):
        self.divider = divider

    def __enter__(self):
        print(f"Before executing code using a separator{self.divider}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"After executing code using a separator{self.divider} ")

divider = "==="
with DividerContext(divider):
    print("This is a code that the using a separator.")