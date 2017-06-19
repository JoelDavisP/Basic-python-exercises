def my_fn(s):
 return s[-1]

def sort_last(t):
 l = sorted(t, key=my_fn)
 return l


def main():
 print sort_last([(1,7),(4,6,5),(1,21,3,5,56,87),(7,8,96,6,52,3,5)])
 print sort_last([('c','fsd'),('aaaa','ewewwe'),('a','klk')])

if __name__ == '__main__':
  main()

