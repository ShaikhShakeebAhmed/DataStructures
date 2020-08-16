import time
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank'];

def findNemo(array):
  #start = time.time()
  count = 0
  for x in array:
    print(count)
    count += 1
    if x == 'hank':
      print('Found hank')
      break
  #end = time.time()
  #print(start - end)
  print("O(n) / Linear Time taken = %s " % count)
  
findNemo(everyone)
