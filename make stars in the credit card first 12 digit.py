cardno = input("Enter Card Number: ")
lastdigit = cardno[15::]
fourstar = "*" * 4 + " "

disno = fourstar * 3 + lastdigit
print(disno)
