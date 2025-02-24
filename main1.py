import fee_pending
import no_fee
import otp

while True:
    admin_username=input("Enter username: ")
    if admin_username == "admin":
        otp=otp.send_otp("kodudhulapoojitha19@gmail.com")
        x=int(input("Enter otp: "))
        if x == otp:
            print("Login success")
            break
        else:
            print("Login failed")
    else:
        print("Invalid Username")
        
userdetails={
    101:["Poojitha","poojithakodudhula19@gmail.com","false"],
    102:["user1","user1@gmail.com","false"],
    103:["user2","poojithakodudhula19@gmail.com","true"],
    104:["user3","user3@gmail.com","false"]
    }

res=[]
for user in userdetails:
    x=input("Enter status:")
    if x == "false":
        res.append([userdetails[user][0],userdetails[user][1]])
        fee_pending.feepending(res)
        print("All mails sent to fee pending users")
        break
    else:
        res.append([userdetails[user][0],userdetails[user][1]])
        no_fee.feepaid(res)
        print("All mails sent to fee cleared users")
        break

