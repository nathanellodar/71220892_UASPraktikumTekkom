print("="*59)
print("*"*21, " Justice League", "*"*21)
print("="*59)

anggota=[]
masukan=str(input("Masukan username anda:"))
while True:
    if masukan == ('victorstone'):
        print("="*4, "WELCOME", masukan, "="*4)
        print("1. Tambah Anggota Justice League")
        print("2. Hapus Anggota Justice League")
        print("3. Tampilkan Anggota justice League")
        print("4. Exit")
        pilihan=int(input("Masukan pilihan anda:"))
        if pilihan == 1:
            nama=(input("Nama Anggota baru:"))
            anggota.append(nama)
            print("data", "'", nama, "'", "berhasil ditambahkan")
        elif pilihan ==2:
            nama=(input("Anggota yang akan dihapus:"))
            if nama not in anggota:
                print("data", "'",nama,"'", "tidak ditemukan")
            else:
                anggota.remove(nama)
                print("data", "'", nama, "'", "berhasil dihapus")
        elif pilihan == 3:
            print(anggota)
        elif pilihan == 4:
            print("see u next time Mr. ",masukan, "GLHF")
            break
    elif masukan == ('brucewyne'):
        print ("="*4, "WELCOME", masukan, "="*4)
        print("1. Tambah Anggota Justice League")
        print("2. Hapus Anggota Justice League")
        print("3. Tampilkan Anggota justice League")
        print("4. Exit")
        pilihan=int(input("Masukan pilihan anda:"))
        if pilihan == 1:
            nama=(input("Nama Anggota baru:"))
            anggota.append(nama)
            print("data", "'", nama, "'", "berhasil ditambahkan")
        elif pilihan ==2:
            nama=(input("Anggota yang akan dihapus:"))
            if nama not in anggota:
                print("data", "'",nama,"'", "tidak ditemukan")
            else:
                anggota.remove(nama)
                print("data", "'", nama, "'", "berhasil dihapus")
        elif pilihan == 3:
            print(anggota)
        elif pilihan == 4:
            print("see u next time Mr. ",masukan, "GLHF")
            break
    elif masukan == ('ciscoramon'):
        print("="*4, "WELCOME", masukan, "="*4)
        print("1. Tambah Anggota Justice League")
        print("2. Hapus Anggota Justice League")
        print("3. Tampilkan Anggota justice League")
        print("4. Exit")
        pilihan=int(input("Masukan pilihan anda:"))
        if pilihan == 1:
            nama=(input("Nama Anggota baru:"))
            anggota.append(nama)
            print("data", "'", nama, "'", "berhasil ditambahkan")
        elif pilihan ==2:
            nama=(input("Anggota yang akan dihapus:"))
            if nama not in anggota:
                print("data", "'",nama,"'", "tidak ditemukan")
            else:
                anggota.remove(nama)
                print("data", "'", nama, "'", "berhasil dihapus")
        elif pilihan == 3:
            print(anggota)
        elif pilihan == 4:
            print("see u next time Mr. ",masukan, "GLHF")
            break
    else:
        print("Access Denied")
        break
