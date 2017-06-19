def match_ends(l):
 count = 0
 for x in l:
  if len(x) > 2 and x[:1] == x[-1:]:
   count += 1
 return count


def main():
 print match_ends(['bubble','sdfd','ammana','dadaad','sd'])
 print match_ends(['c','fsd','aaaa','ewewwe','a','klk'])

if __name__ == '__main__':
  main()
