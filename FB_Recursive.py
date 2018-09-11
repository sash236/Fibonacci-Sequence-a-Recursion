"""
This code was written to help Data Science students 
The Fibonacci Sequence is generated recursively
One can terminate the code by entering "exit"
Python 3.6.5
"""
import sys

# This function takes the length of the Fibonacci Sequence from user
def get_FS_length():
# While loop ensures a valid entry from the user
# and takes user input of "quit" to exit out
  while True:
    try:
      # Checking if the user entered an integer
      value = input('What is the length of the ' +
         ' Fibonacci Sequence needs to be displayed? ' +
         ' Please limit it to 20:\n ')
      if (value.casefold() in ["exit", "quit", "q"] )  :
        print ('OK - I am quiting')
        break

      FS_length = int(value)  
      if FS_length < 1:
        print("Value needs to be " + 
          "larger than 0 ")
        continue
      elif FS_length > 20:
        print ("Please enter a number less than 20!")    
        continue

    except ValueError:
      # User entered non-integer value hence asking for another entry
      print ("Please enter an integer!")
      continue
    else:   
      # Checking if the entry is a positive value
      return(FS_length)

#Recursive function prints Fibonacci sequence   
def gen_seq(n):
  if n <= 1:
    return n
  else:
    return(gen_seq(n-1) + gen_seq(n-2))
  
  
def main():
  length = get_FS_length()
  if (length is not None):
#    seq = gen_FS(length)
    print("\nHere is the Python generated Fibonacci Sequence:")
    for i in range(length):
      print(gen_seq(i))
  else:
    sys.exit()
  
main() 
