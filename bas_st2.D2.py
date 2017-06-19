def verbing(s):
 a = len(s)
 if a < 3:
  return s
 elif s[-3:] == 'ing':
  newstr = s.replace(s[-3:],'ly')
  return newstr
 else:
  s = s + 'ing'
  return s

def main():

 print verbing('sd')
 print verbing('gsygiysgsdy')
 print verbing('vdvying')

if __name__ == '__main__':
 main()
