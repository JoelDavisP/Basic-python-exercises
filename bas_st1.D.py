def mix_up(a,b):
 if len(a) <= 2 or len(b) <= 2:
   return ''
 else:
   asl = a[0:2]
   bsl = b[0:2]
   arem = a[2:]
   brem = b[2:]
   newst = bsl + arem  + ' ' + asl + brem
   return newst

def main():

 print mix_up('good', 'morning')
 print mix_up('df','h')
 print mix_up('mix', 'pod')
 print mix_up('dog', 'dinner')

if __name__ == '__main__':
  main()

