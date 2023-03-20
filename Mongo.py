# oH91fGU4LWMahHZv

import pymongo
from bson import ObjectId

client = pymongo.MongoClient("mongodb+srv://TusharVerma:oH91fGU4LWMahHZv@cluster0.qavskrj.mongodb.net/?retryWrites=true&w=majority")
db=client["FoodieFriends"]
userData=db["UserData"]

def signup(user):
    if(user["pass"]!= user["cpass"]):
        res={"message":"Password and confirm password is not same","id":None}
        return res
    userinfo=userData.find_one({"email":user["email"]})
    if(userinfo !=None):
        res={"message":"Email already exists","id":None}
        return res
    userinfo=userData.find_one({"phone":user["phone"]})
    if(userinfo !=None):
        res={"message":"Email already exists","id":None}
        return res
    else:
        del user["cpass"]
        print(user)
        userData.insert_one(user)
        userinfo=userData.find_one(user)
        userid=str(userinfo["_id"])
        res={"message":"Sign up successful","id":userid}
        return res
def login(user):
    userinfo=userData.find_one({"email":user["email"]})
    if(userinfo==None):
        res={"message":"User does'exists","id":None}
    elif(user["pass"]!=userinfo["pass"]):
        res={"message":"Wrong password","id":None}
    elif(user["pass"]==userinfo["pass"]):
        res={"message":"Login successful","id":str(userinfo["_id"])}
    else:
        res={"message":"somthing went wrong plz try again","id":None}
    
    return res

user={
    "fName":"Tushar S Verma",
    "email":"abc@gmail.com",
    "phone":"8003591244",
    "pass":"Tushar@0402",
    "cpass":"Tushar@0402"
}

print(login(user))