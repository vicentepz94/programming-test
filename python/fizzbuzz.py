for x in range(1,101):
  output=''
  if x % 3 == 0:
    output = 'Fizz'
  if x % 5 == 0:
    output += 'Buzz'
  print(output or x)
