#Arrays also known as lists in Python
arrayOrList  = [1,2,3,4,5]

#>> Get Certain element on certain index
print(arrayOrList[3]) #O(n)

#>> Add new element
arrayOrList.append(6) #O(1) or 0(n)

print(arrayOrList)

#>> Append Left or Append right use insert Or splice

arrayOrList.insert(0 , 0) #O(n)

print(arrayOrList)

#>> pop
print(arrayOrList.pop(3)) #O(n)
print(arrayOrList)

# Reverse a string

def reverseAString(string):
  lengthofString = len(string)
  result = string[lengthofString::-1]
  print(result)


reverseAString("shakeeb")