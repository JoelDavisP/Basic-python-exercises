def front_x(s):
 l1 = [] 
 l2 = [] 
 for a in s:
  if a[0] == 'x':
   l1.append(a)
   l1.sort()
  else: 
   l2.append(a)
   l2.sort()
 return l1 + l2

def main():
 print front_x(['xubble','sdfd','ammana','xadaad','xd'])
 print front_x(['c','fsd','xaaa','ewewwe','a','xlk'])
 print front_x(['sddf','erdds','fdxfd','raesx'])
if __name__ == '__main__':
  main()
