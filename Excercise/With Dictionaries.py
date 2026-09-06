#To delete the sensitive info password and phone number

name=input("Enter your name:")
password=input("Enter your password:")
email=input("Enter your email:")
country=input("Enter your country:")
phone=int(input("Enter your Phone number:"))

user={"user_name":name,"user_Password":password,
      "user_email":email,"user_country":country,
      "user_number":phone}
sensitive_info=["user_Password","user_number"]
for i in sensitive_info:
        user.pop(i)

print(user)