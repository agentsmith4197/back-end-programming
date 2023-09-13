storage = [{
    'name': "EnGentech",
    'sex': "male",
    'mobile': '08039678842'
}]

def new_user(name, sex, mobile):
    new_user_data = {
        'name': name,
        'sex': sex,
        'mobile': mobile
    }
    
    storage.append(new_user_data)
    
    print(storage)
userName = input("please enter your name$ ")
userSex = input("please enter your sex$ ")
userMobile = input("please enter your mobile number$ ")
new_user(userName, userSex, userMobile)
