# 1
a = [1, 2, 3, 4]
res = 0

for i in a:
  res += i
print('result:',res)

# 2
a = [5,6,7,8]

for i in a:
  if (i%2 == 0):

    print(i)

# 3
fruit = ['apple', 'mango', 'cheery', 'orange', 'banana']
for i in fruit:
  print('i love' , i)

# 4
names = []
i=1

while i <= 5:
    name1 = input(f'enter {i} name: ')
    names.append(name1)
    i += 1
#reverse the names list
names.reverse()
print(names)

# 5
num = int(input('enter number: '))

if num == 0:
  print('num is zero')
elif num > 0:
  print('num is positive')
else:
  [print('num is negative')]

# 6
def even_odd_check(num):
  if num%2 == 0:
    print('num is even')
  else:
    print('num is odd')

even_odd_check(1)

# 7
def average(num):
  res=0
  #calculate sum
  for i in num:
    res += i

  #avg = sum of list/ length of list
  avg = res/len(num)
  return avg

average([1,2,3,4])

# 8
from collections import Counter

num = [10,20 ,20,10]

#counter count how many times each value appears in a list
count = Counter(num)

print(dict(count))



# 9
keys = ['name', 'age', 'gender']
values = ['Ali', 25, 'Male']

#zip() combine two lists into key-value pairs
dictionary = zip(keys,values)

print(dict(dictionary))

# 10
a=10
b=30
c=50

if a>b and a>c:
    print("a is greater than b and c")
elif b>a and b>c:
    print("b is greater than a and c")
else:
    print("c is greater than a and b")


# 11
def is_palindrome(s):
  reverse_str = s[::-1]
  return s == reverse_str

# Example usage
print(is_palindrome("madam"))

# 12
words = ['ali' , 'uzair','ahmad' , 'umar','mooji']

long_string = []

for i in words:
  if len(i) > 4:
    long_string.append(i)

print(long_string)

# 13
def calculator(n1 , n2):

  print(n1 + n2)
  print(n1- n2)
  print(n1 * n2)
  print(n1 / n2)

calculator(9,4)


# 14
students = {
    "Ahmad": 85,
    "Uzair": 78,
    "Umar": 92,
    "Shehzaib": 66,
    "Bilal": 81
}

for names  in students.keys():
  print(names)

for names,marks in students.items():
  if marks > 80:
    print('\n' ,names , marks)


# 15
def login_system():
  uName = 'ahmad'
  uPassword = '1234'
  attempt = 0

  while attempt < 3:
    user_name = input('User Name: ')
    user_pass = input('User Password: ')

    if user_name == uName and user_pass == uPassword:
      print('Access Granted') 
      return
    else:
      print('Try Again')
      attempt += 1

  print('Account Locked')

login_system()


# 16
def group_names(names):
    result = {}   

    for name in names:
        letter = name[0]  

        if letter not in result: 
            result[letter] = [] 

        result[letter].append(name) 

    return result
 
print(group_names(['Ali', 'Asad', 'Bela']))


# 17
def word_frequency(text):
 
    text = text.lower()

    # Split text into words
    spl_words = text.split()

    #  Count word frequency
    return dict(Counter(spl_words)) 

 
paragraph = "Hello world Hello Python world"
print(word_frequency(paragraph))


# 18
def atm():
    balance = 0

    while True:  # loop until exit
        print("\n1. Check balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        option = input("Choose option from 1-4: ")

        if option == '1':
            print(f"Your balance is: {balance}")

        elif option == '2':
            amount = int(input("Deposit amount: "))
            balance += amount
            print(f"{amount} deposited.")

        elif option == '3':
            amount = int(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"{amount} withdrawn.")
            else:
                print("Insufficient balance.")

        elif option == '4':
            print("Thank you for using the ATM.")
            # for stop the while loop
            break  

        else:
            print("Invalid choice, please try again.")

 
atm()


# 19
def quiz():
    score = 0 

    print("Welcome to the Mini Quiz!")
 

    # Question 1
    print("\n1) How many days are there in a week?")
    print("1) 5")
    print("2) 7")
    print("3) 10")
    answer = input("Your answer: ")

    if answer == "2":
        score += 1
        print("Correct")
    else:
        print("Wrong! answer is 7.")



    # Question 2
    print("\n2) Which animal is known as the 'King of the Jungle'?")
    print("1) Elephant")
    print("2) Lion")
    print("3) Tiger")
    answer = input("Your answer: ")

    if answer == "2":
        score += 1
        print("Correct")
    else:
        print("Wrong! answer is Lion.")



    # Question 3
    print("\n3) What is the largest planet in our solar system?")
    print("1) Earth")
    print("2) Jupiter")
    print("3) Saturn")

    answer = input("Your answer: ")

    if answer == "2":
        score += 1
        print("Correct")
    else:
        print("Wrong! answer is Jupiter.")

 
    print("\nfinal score is:", score, "out of 3")

 
quiz()

