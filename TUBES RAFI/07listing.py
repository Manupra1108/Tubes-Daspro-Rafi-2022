
data_game = [['id', 'nama', 'kategori', 'tahun_rilis', 'harga', 'stok'], 
            ['GAME001', 'Journey', 'Adventure', 2020, 120000, 3], 
            ['GAME002', 'Hitman 3', 'Action', 2021, 370000, 5], 
            ['GAME003', 'Skyrim', 'RPG', 2011, 200000, 1], 
            ['GAME004', 'Forza Horizon 5', 'Racing', 2021, 550000, 9], 
            ['GAME005', 'Sekiro', 'Action', 2019, 250000, 0]]

def length(list):
    index = 0

    for i in list :
        index += 1 
    return index 

def swap(x,y):
    return (y,x)

def listing(data):
    cek = True
    skemasorting = input("Skema sorting : ")
    urutan = skemasorting[-1:]
    atribut = skemasorting[0:-1]

    if atribut=='tahun':
        if urutan=='+':
            for i in range(1, length(data)):
                for j in range(i,length(data)):
                    if data[i][3]>data[j][3]:
                        (data[i], data[j]) = swap(data[i], data[j])
        elif urutan=='-':
            for i in range(1, length(data)):
                for j in range(i,length(data)):
                    if data[i][3]<data[j][3]:
                        (data[i], data[j]) = swap(data[i], data[j])
 
    elif atribut=='harga':
        if urutan=='+':
            for i in range(1, length(data)):
                for j in range(i,length(data)):
                    if data[i][4]>data[j][4]:
                        (data[i], data[j]) = swap(data[i], data[j])
        elif urutan=='-':
            for i in range(1, length(data)):
                for j in range(i,length(data)):
                    if data[i][3]<data[j][3]:
                        (data[i], data[j]) = swap(data[i], data[j])
    elif atribut=='':
        for i in range(1, length(data)):
            for j in range(i,length(data)):
                if data[i][0]>data[j][0]:
                    (data[i], data[j]) = swap(data[i], data[j])
    else:
        print('Skema sorting tidak valid!')
        cek = False
    
    if cek == True:
        return data
    
  

print(listing(data_game))
    
