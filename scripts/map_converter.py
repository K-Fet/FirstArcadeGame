liste = ((275,0),(1810,0),(1840,200),(1725,340),(1660,750),(1640,860),(1650,1050),(1480,1050),(1480,800),(1390,800),(1390,900),(1235,900),(1230,800),(240,830))

print('(', end='', flush=True)
for couple in liste:
  couple = list(couple)
  couple[0] = str(int(couple[0] * 1280 / 1920))
  couple[1] = str(abs(int(couple[1] * 1280 / 1920 - 720)))
  print('(' + couple[0] + ',' + couple[1] + ')' + ',', end='', flush=True)

print(')', end='', flush=True)
