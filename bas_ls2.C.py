def remove_adjacent(l):
 s= len(l)
 while s == 0:
  index = 0
  if l[index] == l[index + 1]:
    del l[index]
  index += 1
  s = s-1
   
 return l

def main():
 print remove_adjacent([1,2,1,2,2,2,1,3,1,1])
 print remove_adjacent([1,1,1,1,2,2,2,2,3,3,3,4,4,45,5])

if __name__ == '__main__':
  main()

