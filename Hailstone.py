#  File: Hailstone.py

#  Description: Calculates highest number of steps for number to reach 1 using Hailstone Sequence for number in a given range

#  Student Name: Christina Nerona

#  Student UT EID: cmn845

#  Course Name: CS 303E

#  Unique Number: 51630

#  Date Created: 2/25/15

#  Date Last Modified: 2/28/15


def main():
  #Prompt user to enter a starting & ending number
  st=eval(input('Enter starting number of the range: '))
  end=eval(input('Enter ending number of the range: '))

  #Convert to range and list
  a=list(range(st,end+1))
  
  #Set count and empty list
  count=0
  listo=[]
  for i in a:
    while(i!=1):
      #if even
      if(i%2==0):
        i=i//2
        count+=1

      #if odd
      else:
        i=(3*i)+1
        count+=1

    #Adding final count to list
    listo.append(count)

    #Reseting count before going through loop again
    count=0

  #Find max value
  high=max(listo)
  
  #Find index of max in list
  num_max=listo.count(high)

  #Copy List to make sure of maximum number
  copy=listo

  #Number of times we've seen max number
  seen_max=0
  
  #Setting step to count number of steps from beginning of the list
  step=0

  #Finding last number if maximum is seen twice
  if (num_max>1):

    #Peeling first number in list
    while(len(listo)>=1):
      first=listo.pop(0)
      step+=1

      #keeping count of how many times we've seen that number
      if(first==high):
        seen_max+=1
      
        #checking to see if we've seen the maximum number of the "max number"
        if(seen_max==num_max):
          #Adjusting for list that starts at number other than 0
          num=(st+step-1)

        
          #Returning output
          print('The number',num,'has the longest cycle length of',str(high)+'.')
          return
  else:
    #Adjusting for list that starts at number other than 0
    num=(listo.index(high)+1)+st-1

    #Finding max from list of number of steps
    max_list=max(copy)

    #Returning output
    print('The number',num,'has the longest cycle length of',str(high)+'.')
  
main()
