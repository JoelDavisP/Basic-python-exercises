def both_ends(s):
  i = len(s)
  if i <= 2:
    st = ''
  else:
    st = s[0:2] +  s[-2:]
  return st

def main():
  print both_ends('goodmorning')
  print both_ends('d')
if __name__ == '__main__':
 main()
