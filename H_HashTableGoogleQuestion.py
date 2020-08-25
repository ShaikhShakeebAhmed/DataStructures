#Given a array find the first repeted element
#Given an array  = [1,2,3,2,4,5,6,7,8,9,0] it should return 2

inputArray = [1,2,3,2,4,5,6,7,8,9,0]

def returnFirstMatch(inputarr):
  count = -1
  inputarr.sort(reverse = True)
  checking = dict()
  print(inputarr)
#>> range([start], stop[, step])
  for i in range(len(inputarr) - 1 , -1 , -1):
    if inputarr[i] in checking.keys(): 
      count = i   
    else:
      checking[inputarr[i]] = 1
  # Print the result 
    if (count != -1): 
        print("The first repeating element is", inputarr[count]) 
        break
    

returnFirstMatch([1,2,3,2,4,5,6,7,8,9,0])