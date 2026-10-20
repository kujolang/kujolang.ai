import Base

def host_value() -> IO(U32):
  import "./host_value.js"

def main() -> IO(Unit):
  do IO<Unit>:
    value : U32 <- host_value()
    IO.print(U32.show(value))
