def not_bad(s):
 a = s.find('not')
 b = s.find('bad')
 if a!= -1 and b != -1 and a < b :
   newst = s.replace(s[a:(b+3)], 'good')
 else:
   newst = ''
 return newst

def main():

 print not_bad('sd')
 print not_bad('gdcy  i think food is not so convinently bad')
 print not_bad('not too bad food')

if __name__ == '__main__':
 main()
