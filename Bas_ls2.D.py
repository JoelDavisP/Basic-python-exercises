def remove_adjacent(lst):
 new_ls = []
 for i in lst:
    if len(new_ls) == 0 or i != new_ls[-1]:
      new_ls.append(i)
 return new_ls


def main():
 print remove_adjacent([1,2,1,2,2,2,1,1,3,3,3,3,1,1,2])
 print remove_adjacent([5,5,66,7,7,8,7,8,8,8,9,9,9,10,10,1,2])
 print remove_adjacent([5,3,0,0,7,5,4,6,6,5,2,0,3,3,0,1,2])
if __name__ == '__main__':
  main()
