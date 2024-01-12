#List is basically implemented as dynamic array behind the scenes, not a linked list
# It is mutable
#And it can hold arbitrary many different types


#Because they can hold arbitrary many types, the data is not so tightly packed
#Hence the data structure takes up more space. 

arr = ["one", "two", "three"]
del arr[1]
arr.append(4)
print(arr)


#Tuples
#Similar to Lists but they are immutable, hence they must be defined at creation time
arr = ("one", "two")

#This would throw an error, since tuples are immutable
#arr[1] = "four"

#Tuples can also hold arbitrary many different data types, 
# hence the data is not as tightly packed and thus not so efficient

#Btw "adding an element" for a tuple would involve making a copy of the old tuple with the new element in it
#Really bad for performance
arr + (23,)

#array.array offers a typed array, hence data more tightly packed i.e. more efficient!!!
#These arrays are also mutable btw
import array
arr = array.array("f", (1.0, 1.5, 3.2))
print(arr[1])

arr.append(42.0)

#Below would throw an error cuz the array is typed as floating point
#arr[1] = "hello"

#Str objects are also basically immutable arrays of unicode characters. 
#Remem they are immutable!!!
#So if are trying to "modify" it, u would have to make a copy, which is obv bad for performance
#If u want a mutable string, then u should create a list of characters instead
arr="abcd"

#Would throw an error cuz strings are immutable
#arr[1] = "z"

#"bytes" object is immutable sequence of single bytes
#Remem immutable!!!

#2 ways of creating a bytes object
arr = bytes((0,1,2,3))
print(arr)
arr = b"\x00\x01\x02\x03"
print(arr)

#This would throw an error cuz "bytes" is immutable
#arr[2] = 200


#But "bytearray" gives us a MUTABLE array of single bytes

arr=bytearray((0,1,2,3))
arr[2] = 210
print(arr)

