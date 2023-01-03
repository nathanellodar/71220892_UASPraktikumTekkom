def action():
    print(" ")
    print("="*2, "Berikut pilihan film action yang sedang tayang", 2*"=")
    print("1. Black Panther: Wakanda Forever")
    print("2. Avatar: The Way of Water")
    film=int(input("Silahkan pilih mau nonton film apa:"))
    if film <= 2:

        tiket=int(input("Mau pesan tiket sebanyak:"))
        harga= tiket*25000
        print("Total yang harus dibayar adalah Rp. ", harga)
    else:
        print("Pilihan yang anda pilih tidak tersedia di bioskop ini")


def horror():
    print(" ")
    print("="*2, "Berikut pilihan film horor yang sedang tayang", 2*"=")
    print("1. The Devil's Light")
    print("2. Pengabdi Setan")
    film=int(input("Silahkan pilih mau nonton film apa:"))
    if film <= 2:

        tiket=int(input("Mau pesan tiket sebanyak:"))
        harga= tiket*25000
        print("Total yang harus dibayar adalah Rp. ", harga)
    else:
        print("Pilihan yang anda pilih tidak tersedia di bioskop ini")

def genre():
    print(" ")
    print("="*2, "Berikut genre film yang tersedia", 2*"=")
    print("1. Horror")
    print("2. Action")
    print(" ")
    genre=int(input("Silahkan pilih mau nonton film bergenre apa:"))
    if genre == 1:
        horror()
    elif genre ==2 :
        action()
    else:
        print("pilihan yang anda pilih tidak tersedia di bioskop ini")

print (4*"=", "Selamat datang di XXV", 4*"=")
tanggal=int(input("Masukkan tanggal hari ini:"))
if tanggal % 2 == 0:
    genre()
else:
    genre()
