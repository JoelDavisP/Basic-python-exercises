import sys

def help_fun(fname):
 wc = {}
 f = open(fname, 'r')
 for l in f:
  words = l.split()
  for w in words:
   word = w.lower()
   if word in wc:
    wc[word] += 1
   else: 
    wc[word] = 1
 f.close()
 return wc
def print_words(flname):
 word_count = help_fun(flname)
 words = sorted(word_count.keys())  #Create the list sorted under the keys
 for i in words:
  print i, word_count[i]

def my_fn(w):
 return w[1]


def print_top(fname):   #Referred solution list forcreating this function
 word_count = help_fun(fname)
 count_srt = sorted(word_count.items(), key = my_fn, reverse = True)  #Create the list sorted under the keys
 for i in count_srt[:20]:
  print i[0] ,i[1]

def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
