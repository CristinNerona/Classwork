#  File: Goldbach.py

#  Description: Checks Goldbach's Conjecture: "Every even number >=4 can be expressed as sum of two primes" for all evens in a given range

#  Student Name: Christina Nerona

#  Date Created: 3/8/15

#  Date Last Modified: 3/14/12


def is_prime (n): #Function to determine if prime
    
  limit = int (n ** 0.5) + 1
  div = 2 #Set limit and diviser
  
  while (div < limit): #While loop to divide num by diviser
    if (n % div == 0):
      return False #Returns false if divisible by something other than 1 or itself

    div = div + 1 #Increment diviser
    
  return True #Return True if breaks out of while loop


def peel_factors(listo): #Function to peel prime numbers from list
    
  a=str(listo.pop(0))+' + '+str(listo.pop(0)) #Set first two numbers and separate with '+'

  while (len(listo)>0): #While more factors exist, peel and separate with '+' and '='
    a+=' = '+str(listo.pop(0))+' + '+str(listo.pop(0))
    
  return(a) #Returns numbers that add up to i

def main(): #Main function

  #Prompt user to input values
  #low_lim=eval(input('Enter lower limit: '))
  #up_lim=eval(input('Enter upper limit: '))

  print("Goldbach's conjecture: 'Every even number >=4 can be expressed as sum of two primes for all evens in a given range' ")
  print("Initializing range from 4 to 400")
  low_lim=4
  up_lim=400
  print('')

  #Make sure upper limit is greater than lower limit and lower limit is not 2
  while (up_lim<low_lim or low_lim<4):
      low_lim=eval(input('Enter lower limit: '))
      up_lim=eval(input('Enter upper limit: '))
      print('')

  #Create Range of values
  a=list(range(low_lim,up_lim+1))

  #Set first two numbers to find sum & the maximum number of pairs
  num_sum1=0
  num_sum2=0
  max_pairs=1

  #For i in given range, set initial value to begin peeling numbers that add to i
  #Set empty list of factors
  for i in a:
    peel=1
    factors=[]

    #Check if i is an even number & set number of pairs
    if (i%2==0):
      pairs=0

      #Set Limit to half of the even number to avoid repeats
      #Peel numbers that add to i one by one
      while(peel<=(i//2)):
        num_sum1=i-peel
        num_sum2=peel
        peel+=1

        #Check is the numbers that add up to i are prime and not 1
        #If so, add to list of numbers
        if (is_prime(num_sum1) and is_prime(num_sum2) and num_sum1!=1 and num_sum2!=1):
          factors.append(num_sum2)
          factors.append(num_sum1)
          
      #Uncomment code below to double check factors:
      #print(i,factors)

      #Count number of numbers that are prime and add up to i    
      pairs=(len(factors))

      #print equation of primes that add up to i
      print(i,'=',peel_factors(factors))

      #Compare number of pairs to current maximum
      if (pairs>max_pairs):
        max_pairs=pairs

      #Break out of loop and continue to next i in range a
      continue
    
  #Return the maximum number of pairs of primes that add up to i in given range
  print('')
  print('The maximum number of pairs =',(max_pairs)//2)
  
main()
    
