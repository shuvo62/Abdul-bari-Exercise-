emailid = input("Enter your email id: ")
atrate = emailid.find("@")
print("User name: ", emailid[:atrate])
print("Domain name: ", emailid[atrate + 1 :])
