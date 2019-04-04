# casesar cipher


a = [chr(x).lower() for x in range(65, 91)]
print("Original Alphabets are = > ", a)
shift = int(input("enter shift (encryption key) >> "))

lpart = a[:shift]
rpart = a[shift:]
print(lpart)
print(rpart)
print(rpart + lpart)
