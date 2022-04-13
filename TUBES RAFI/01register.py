data_user = [["id","username","nama","password","role","saldo"],
[0,"rafi","rafi","rafi","admin",0],
[1,"bat_man","batman","kelelawar","user",0],
[2,"baim","ibrahim","baimsipsip","user",0],
[3,"ard_studios","ardhan","dandan123","user",0]
[4,"super_man","superman","kuat","user",0]]

def isUserValid(username):
    isvalid = True
    for i in username:
        if not((i>='a' and i<='z') or (i>='A' and i<='Z') or (i>='0' and i<='9') or (i=='_' or i=='-')):
            isvalid=False
        
    return isvalid

def length(list):
    index = 0

    for i in list :
        index += 1 
    return index 

def isUnique(username):
    len = length(data_user)

    issame = True
    for i in range(1,len):
        if data_user[i][1] == username:
            issame = False

    return issame

def register(data):
    
    cek_regis=True
    while(cek_regis):
        nama = input("Masukan nama: ")
        username = input("Masukan username: ")
        password = input("Masukan password: ")
        
        if isUserValid(username) == False:
            print("Username Anda tidak valid. Silakan buat Username lagi.")
        else:
            if isUnique(username) == False:
                print(f"Username {username} sudah terpakai, silakan menggunakan username lain.")
            else:
                print(f'Username {username} telah berhasil register ke dalam "Binomo".')
                data+=[[length(data)-1,username,nama,password,"user",0]]
                cek_regis=False
    return data
    

print(register(data_user))
