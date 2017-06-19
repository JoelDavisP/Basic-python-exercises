def linear_merge(l1,l2):
 lnew = l1 + l2
 ls = sorted(lnew)
 return ls
def main():
 print linear_merge([1,3,5,7,9], [2,4,6,8,10])
 print linear_merge([2,3,4,5,9], [3,5,7,9,11,13])
 print linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
 print linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
 print linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
if __name__ == '__main__':
  main()
