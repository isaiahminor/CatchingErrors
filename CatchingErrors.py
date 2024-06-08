try:
  17/0

except ZeroDivisionError:
  print("You can't divide by zero")


try:
  zerodiverror = 17/2
  zerodiverror + "100"
except TypeError:
  print("You can't add a string to an integer")

try:
  zerodiverrorr = 17/0
  zerodiverrorr + "100"
except(ZeroDivisionError, TypeError):
  result = 4+3
  print(result)
