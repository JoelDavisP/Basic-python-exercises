
def donuts(count):
  if count <= 10:
    x = ' Number of Donuts:',  count
  else:
    x = ' Number of Donuts : Many'
  return x

def main():

 print donuts(6)
 print donuts(20)
 print donuts(8)


if __name__ == '__main__':
   main()
