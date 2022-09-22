from doctest import FAIL_FAST
import math
import sys

def hello():
  val = float(sys.argv[1])
  print(math.radians(val))
  print("HelloWorld")

def cat():
  print("NYAHAHAHA!!!")

def isint(s):
  try:
    int(s,10)
  except ValueError:
    return False
  else:
    return True

if __name__ == "__main__":
  args = sys.argv
  if len(args) == 2:
    if isint(sys.argv[1]) == True:
      hello()
    else:
      cat()
  else:
    cat()
