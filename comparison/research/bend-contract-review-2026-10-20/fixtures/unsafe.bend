import Base

@unsafe
def raw(x: U32) -> U32:
  x

def wrapper(x: U32) -> U32:
  raw(x)

def main() -> U32:
  wrapper(42)
