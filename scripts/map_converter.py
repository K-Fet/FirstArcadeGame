liste = ((183,720),(1206,720),(1226,586),(1150,493),(1106,220),(1093,146),(1100,20),(986,20),(986,186),(926,186),(926,120),(823,120),(820,186),(160,166))

print('(', end='', flush=True)
for couple in liste:
  couple = list(couple)
  couple[0] = str(int(couple[0]))
  couple[1] = str(abs(int(couple[1])))
  print('(' + couple[0] + ',' + couple[1] + ')' + ',', end='', flush=True)

print(')', end='', flush=True)
