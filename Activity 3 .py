# take marks as input from user
print("Enter Marka Obtained in 4 Subjects: ")
maths = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
hindi = int(input("hindi :"))

sum = maths+english+science+hindi
print("sun of maths,english,science and hindi")

perc =(sum/400)*100

print(end="Percentage Mark = ")
print(perc)