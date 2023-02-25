values = ["a", "b", "c"]
for count, value in enumerate(values):
  print(count, value)

print('---------')
first = ["a", "b", "c"]
second = ["d", "e", "f"]
third = ["g", "h", "i"]
for one, two, three in zip(first, second, third):
  print(one, two, three)

print('------')
for count, (one, two, three) in enumerate(zip(first, second, third)):
  print(count, one, two, three)
