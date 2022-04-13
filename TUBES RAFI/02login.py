data_user = [["id","username","nama","password","role","saldo"],
[0,"rafi","rafi","rafi","admin",0],
[1,"bat_man","batman","kelelawar","user",0],
[2,"baim","ibrahim","baimsipsip","user",0],
[3,"ard_studios","ardhan","dandan123","user",0]
[4,"super_man","superman","kuat","user",0]]

def length(list):
    index = 0

    for i in list :
        index += 1 
    return index 
    
def login(data):
    username = input("Masukan username: ")
    password = input("Masukan password: ")

    index = 0
    cek = False
    for i in range(1, length(data)):
        if data[i][1]==username and data[i][3]==password:
            cek = True
            index = i
    
    if cek == True:
        print(f"Halo {data[index][2]}! Selamat datang di “Binomo”.")
    else:
        print("Password atau username salah atau tidak ditemukan.")

    return data[index][4]


print(login(data_user))
        

