#문자열처리함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

#문자열에 원하는 값이 없을때 
print(python.find("Java")) 
#print(python.index("Java")) #오류
print("hi") #오류 이후에 있을경우 실행 안 됨

print(python.count("n"))
