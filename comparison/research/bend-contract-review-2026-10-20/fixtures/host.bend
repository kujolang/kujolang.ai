import Base

def identity(n: Nat) -> Nat:
  n

def inc(n: Nat) -> Nat:
  Nat.add(n, 1n)

def add(a: Nat, b: Nat) -> Nat:
  Nat.add(a, b)

def word(x: U32) -> U32:
  x
