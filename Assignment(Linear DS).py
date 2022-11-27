# Linear-DS-Assgnmt
# Question-1::
def findPair(nums, target):
 
    # consider each element except the last
    for i in range(len(nums) - 1):
 
        # start from the i'th element until the last element
        for j in range(i + 1, len(nums)):
 
            # if the desired sum is found, print it
            if nums[i] + nums[j] == target:
                print('Pair found', (nums[i], nums[j]))
                return
 
    # No pair with the given sum exists in the list
    print('Pair not found')
 
 
if __name__ == '__main__':
 
    nums = [8, 7, 2, 5, 3, 1]
    target = 10
 
    findPair(nums, target)
 
 
 Question-2::
 #The original array
arr = [11, 22, 33, 44, 55]
print("Array is :",arr)
 
res = arr[::-1] #reversing using list slicing
print("Resultant new reversed array:",res)

Question-3::
# Python program to check if strings are rotations of
# each other or not
  
# Function checks if passed strings (str1 and str2)
# are rotations of each other
def areRotations(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = ''
  
    # Check if sizes of two strings are same
    if size1 != size2:
        return 0
  
    # Create a temp string with value str1.str1
    temp = string1 + string1
  
    # Now check if str2 is a substring of temp
    # string.count returns the number of occurrences of
    # the second string in temp
    if (temp.count(string2)> 0):
        return 1
    else:
        return 0
  
# Driver program to test the above function
string1 = "AACD"
string2 = "ACDA"
  
if areRotations(string1, string2):
    print "Strings are rotations of each other"
else:
    print "Strings are not rotations of each other"
    


Question-4::
def getCharCountArray(string):
    count = [0] * NO_OF_CHARS
    for i in string:
        count[ord(i)]+= 1
    return count
 
# The function returns index of first non-repeating
# character in a string. If all characters are repeating
# then returns -1
def firstNonRepeating(string):
    count = getCharCountArray(string)
    index = -1
    k = 0
 
    for i in string:
        if count[ord(i)] == 1:
            index = k
            break
        k += 1
 
    return index
 
# Driver program to test above function
string = "geeksforgeeks"
index = firstNonRepeating(string)
if index == 1:
    print ("Either all characters are repeating or string is empty")
else:
    print ("First non-repeating character is" , string[index])
    
    

Question-5::
def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
         
# Driver code
n = 4
TowerOfHanoi(n,'A','B','C')
# A, C, B are the name of rods



Question-6::
# Example Input
s = "*-A/BC-/AKL"
 
# Stack for storing operands
stack = []
 
operators = set(['+', '-', '*', '/', '^'])
 
# Reversing the order
s = s[::-1]
 
# iterating through individual tokens
for i in s:
 
    # if token is operator
    if i in operators:
 
        # pop 2 elements from stack
        a = stack.pop()
        b = stack.pop()
 
        # concatenate them as operand1 +
        # operand2 + operator
        temp = a+b+i
        stack.append(temp)
 
    # else if operand
    else:
        stack.append(i)
 
# printing final output
print(*stack)



Question-7::
def prefixToInfix(prefix):
    stack = []
     
    # read prefix in reverse order
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
             
            # symbol is operand
            stack.append(prefix[i])
            i -= 1
        else:
           
            # symbol is operator
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
     
    return stack.pop()
 
def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False
 
# Driver code
if __name__=="__main__":
    str = "*-A/BC-/AKL"
    print(prefixToInfix(str))
    
    
    
Question-8::
def areBracketsBalanced(expr):
    stack = []
 
    # Traversing the Expression
    for char in expr:
        if char in ["(", "{", "["]:
 
            # Push the element in the stack
            stack.append(char)
        else:
 
            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
 
    # Check Empty Stack
    if stack:
        return False
    return True
 
 
# Driver Code
if __name__ == "__main__":
    expr = "{()}[]"
 
    # Function call
    if areBracketsBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")
        
        
        
 Question-9::
 class Stack:
 
    # create empty list
    def __init__(self):
        self.Elements = []
         
    # push() for insert an element
    def push(self, value):
        self.Elements.append(value)
       
    # pop() for remove an element
    def pop(self):
        return self.Elements.pop()
     
    # empty() check the stack is empty of not
    def empty(self):
        return self.Elements == []
     
    # show() display stack
    def show(self):
        for value in reversed(self.Elements):
            print(value)
 
# Insert_Bottom() insert value at bottom
def BottomInsert(s, value):
   
    # check the stack is empty or not
    if s.empty():
         
        # if stack is empty then call
        # push() method.
        s.push(value)
         
    # if stack is not empty then execute
    # else block
    else:
        popped = s.pop()
        BottomInsert(s, value)
        s.push(popped)
 
# Reverse() reverse the stack
def Reverse(s):
    if s.empty():
        pass
    else:
        popped = s.pop()
        Reverse(s)
        BottomInsert(s, popped)
 
 
# create object of stack class
stk = Stack()
 
stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.push(5)
 
print("Original Stack")
stk.show()
 
print("\nStack after Reversing")
Reverse(stk)
stk.show()



Question-10::
class MinStack(object):
   min=float('inf')
   def __init__(self):
      self.min=float('inf')
      self.stack = []
   def push(self, x):
      if x<=self.min:
         self.stack.append(self.min)
         self.min = x
      self.stack.append(x)
   def pop(self):
      t = self.stack[-1]
      self.stack.pop()
      if self.min == t:
         self.min = self.stack[-1]
         self.stack.pop()
   def top(self):
      return self.stack[-1]
   def getMin(self):
      return self.min
m = MinStack()
m.push(-2)
m.push(0)
m.push(-3)
print(m.getMin())
m.pop()
print(m.top())
print(m.getMin())
