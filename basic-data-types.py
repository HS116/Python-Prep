#Octal
print(0o10)
#Hex
print(0x10)
#Binary
print(0b10)
#Decimal
print(10)

print(type(3))
#Float
print(type(4.3))
#Scientific Notation
print(4.2e-4)
print(1.7e308)
#Too large to be represented as float, remem Python uses 64 bit double precision for floats
print(1.8e308)
print(5e-324)
#Too small to be represented, hence it will be represented as simply 0
print(1e-325)

#Complex Numbers
print(type(2+3j))

#Strings, escape characters
print("Here is a speech mark \"")
print("Here is a\
      \"fake\" multiline string\
      haha")
print("Here is a backslash \\")
print("Here is a new line \n xD")

#Raw strings, aka escape sequences are not translated
print(r"foo\nbar")

print("""   Actual
multiline
string
xD 
""")

print(type(True))
print(type(False))

#Built-In Functions
print(abs(-5))
print(max(1,2,3,4))
print(min(1,2,-3,4))
print(pow(5, 3))
print(round(5.3))
print(sum([1,2,3,4,5]))

print(bin(33))
print(bool(31))
print(bool(0))
print(chr(88))
print(type(int("5")))
print(type(str(5)))

for count, item in enumerate([4,2,5,5,2,2,]):
    print(f"i:{count}, j:{item}")
