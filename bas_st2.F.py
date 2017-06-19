def proc(a):
 x = len(a)
 t = [] 
 if x%2 == 0:
  front = a[0: (x/2)]
  back = a[(x/2):]
 else:
  front = a[0: (x/2)+1]
  back = a[(x/2)+1:]
 t.append(front)
 t.append(back)
 return t

def front_back(a,b):
  
 x  = proc(a)
 y = proc(b)
 return x[0] + ' ' + y[0] + ' ' + x[1] + ' ' + y[1]

def main():

 print front_back('good','morn')
 print front_back('good', 'day')
 print front_back('hai','joel')
 print front_back('hai', 'angel')
 print front_back('abcd', 'xy')
 print front_back('abcde', 'xyz')
 print front_back('Kitten', 'Donut') 
if __name__ == '__main__':
 main()

