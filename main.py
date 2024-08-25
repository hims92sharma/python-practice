import module.test as t
import Himanshu
import math


myString = 3
testing = None
my2ndString = "S2tring"
print(str(myString)+my2ndString)
if my2ndString == "String":
    print("String")
elif myString == 2:
    print("tested")
else:
    print("rest is printing")

myList = ["Himanshu", "HImanshu", 3]

for x in myList:
    print(x)

oneNumber = 2**4
secondNumber = 3**2
print(oneNumber, secondNumber)

hello = "Hello" + " " + "world"
print(hello)

lotOfHello = "Hello" * 3
print(lotOfHello)

oddNumber = [2, 4, 6]
evenNumber = [1, 3, 5]
allNumber = oddNumber+evenNumber
print(allNumber)

test = [1, 2, 3] * 2
print(test)

hello = "Himanshu"
print("testing %s Sharma" % hello)

name = "John"
age = 23
print("%s is %s years old" % (name, age))

listing = [1, 2, 3]
print("my list is %s !!!" % listing)

testString = "Hello this is Himanshu Sharma"
print("Length == ", len(testString))

print("position of O character in above string is ", testString.index('o'))

print("To print how many H character are there is == ", testString.count('h'))
print(testString[3:7])
print(testString[3:7:])

print(testString.lower())
print(testString.upper())

print(testString.startswith("l"))
print(testString.endswith("a"))

splitArray = testString.split(" ")
print(splitArray)

x = 7
if x == 2:
    print("it's 2")
elif x == 5:
    print("it's 5")
else:
    print("Don't know")

name = "Himanshu"
age = 28
if name == "Himanshu" and age == 24:
    print("Yes, gotcha you are Himanshu")
elif name == "Himanshu" or name == "TEST":
    print("YOu are OR operator")
else:
    print("You are not Himanshu")


if name in ["Himanshu", "Test"]:
    print("you are in block")

testName = "Himanshu"
if name is testName:
    print("TRUE")

print(not False)


testArray = [1, 2, 3]
for x in testArray:
    print("value of x == ", x)

testArray = [3, 2, 1]
for x in testArray:
    print("value of x == ", x)

for x in range(3, 10):
    print("value  of range == ", x)

count = 0
while count < 5:
    print("count ==", count)
    count = count+1


count = 0
while count < 5:
    if count == 4:
        break
    else:
        print("testing == ", count)
    count = count+1



count = 0
while count < 5:
    if count == 4:
        break
    else:
        print("testing == ", count)
    count = count+1


def myfunction():
    print("This is my first method without argument function")


myfunction()


def myfunction(name1, age1):
    print("name == %s, age  == %s" % (name1, age1))


myfunction("Himanshu", 23)


def myfunction(a, b):
    return a+b


c = myfunction(1, 2)
print("value of c == ",  c)

test = "tetsing" + "test"


class Test:
    name = "testing"
    age = "0"

    def __init__(self, name3, age3):
        self.age = age3
        self.name = name3

    def testfunction(self):
        print("My first object function")


test1 = Test("hims", "23")
print(test1.name, test1.age)

test2 = Test("", "")
print("Testing test2 object == ", test2.name)


phonebook = {
    "hims": 87476784,
    "himanshu": 89798,
    "Main": 8909
}

phonebook.update({'rest': 8989})
phonebook.pop("hims")

for x in range(1, 5):
    phonebook["x"+str(x)] = x+5

for key, value in phonebook.items():
    print("key == %s, value == %d" % (key, value))

print(phonebook.get("Main"))

t.function()


object1 = Himanshu.TestHimanshu()
object1.test()

sqrt = math.sqrt(4)
print(sqrt)



