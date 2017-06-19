def fix_start(s):
 if len(s) <= 1:
  return ''
 else:
  first = s[0]
  rep = '*'
  new = s[1:]
  new1 = new.replace( first, rep)
  return first + new1

def main():
 print fix_start('bubble')
 print fix_start('c')

if __name__ == '__main__':
  main()
