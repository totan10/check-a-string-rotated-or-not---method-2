def isRotated(s1, s2):
  if len(s1)!=len(s2):
    return False
  s=(s1+s1)
  return s.find(s2)!=-1


s1=input()
s2=input()
print(isRotated(s1, s2))