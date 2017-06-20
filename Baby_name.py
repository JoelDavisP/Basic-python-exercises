import re
import sys
def extract_names(fname):
 ls = []
 name_list = []
 name_rank = {}
 inf = open(fname,'rU')
 lines = inf.read()
 year = re.search(r'\w\w\w\w\w\w\w\w\w\w\s\w\w\s(\d\d\d\d)',lines)
 if year:
  year_new = year.group(1)
  ls.append(year_new)
 else:
  print ''
 name_ls = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)',lines)
 if name_ls:
  for i in name_ls[:]: 
   name_list.append(i)
 else:
  return ''
 for tup in name_list:
  (rank,mname,fname) = tup  #This is taken from the solution
  if mname not in name_rank:
   name_rank[mname] = rank
  if fname not in name_rank:
   name_rank[fname] = rank
 namelist1 = sorted(name_rank.keys())
 for i in namelist1:
  ls.append(i)
  ls.append( name_rank[i])
 return ls
 inf.close()
def main():
  nameout = []
  if len(sys.argv) != 3: #Command line first argument is file name, next argument is 'w' if usr want to write the result to another file, 'n' if not to write to another file.
    print 'usage: ./babyname.py {file name} file'
    sys.exit(1)
  filename = sys.argv[1]
  s = sys.argv[2]
  nameout = extract_names(filename)
  disp_out = '\n'.join(nameout)  #This is taken from solution
  print disp_out
  if s == 'w':
   namenew = extract_names(filename) 
   text = '\n'.join(namenew)
   outf = open('output_file.txt','w')  #This is taken from solution
   outf.write(text)
   outf.close() 
if __name__ == '__main__':
  main()
