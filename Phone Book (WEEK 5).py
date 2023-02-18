# set the name of the phone book file
phone_book_file = "BukuTelepon.txt"

# load phone book data from file
phone_book = {}
with open(phone_book_file, "r") as f:
    for line in f:
        line = line.strip()
        if ":" not in line:
            print(f"Lewati baris '{line}': format tidak valid")
            continue
        name, number = line.split(":")
        if name in phone_book:
            phone_book[name].append(number)
        else:
            phone_book[name] = [number]

while True:
    # print ASCII art
    print('''
______       _            _____    _                        
| ___ \     | |          |_   _|  | |                       
| |_/ /_   _| | ___   _    | | ___| | ___ _ __   ___  _ __  
| ___ \ | | | |/ / | | |   | |/ _ \ |/ _ \ '_ \ / _ \| '_ \ 
| |_/ / |_| |   <| |_| |   | |  __/ |  __/ |_) | (_) | | | |
\____/ \__,_|_|\_\\__,__|   \_/\___|_|\___| .__/ \___/|_| |_|
                                         | |                
                                         |_|                 ''')

    # print the current phone book
    if phone_book:
        print("Kontak:")
        for name, numbers in phone_book.items():
            print(f"{name}: {', '.join(numbers)}")
        print()

    # prompt the user for action
    print("Apa yang ingin dilakukan?")
    print("1. Tambah kontak baru")
    print("2. Ubah kontak yang sudah ada")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("5. Keluar")

    choice = input("Masukan pilihan (1-5): ")

    # add a new contact
    if choice == "1":
        name = input("Masukkan nama kontak: ")
        number = input("Masukkan nomor telepon kontak: ")
        if name in phone_book:
            phone_book[name].append(number)
        else:
            phone_book[name] = [number]
        print(f"{name} telah ditambahkan ke buku telepon.\n")

    # update an existing contact
    elif choice == "2":
        name = input("Masukkan nama kontak: ")
        if name in phone_book:
            numbers = phone_book[name]
            print(f"Nomor telepon yang tersedia untuk {name}: {', '.join(numbers)}")
            number = input("Masukkan nomor telepon baru untuk kontak: ")
            numbers.append(number)
            phone_book[name] = numbers
            print(f"Nomor telepon {name} telah diperbarui.\n")
        else:
            print(f"{name} tidak ada di dalam buku telepon.\n")

    elif choice == "3":
    name = input("Masukkan nama kontak: ")
    if name in phone_book:
        numbers = phone_book[name]
        print(f"Nomor telepon yang tersedia untuk {name}: {', '.join(numbers)}")
        if len(numbers) == 1:
            del phone_book[name]
            print(f"{name} telah dihapus dari buku telepon.\n")
        else:
            number = input("Masukkan nomor telepon yang akan dihapus: ")
            if number in numbers:
                numbers.remove(number)
                phone_book[name] = numbers
                print(f"Nomor telepon {number} telah dihapus dari kontak {name}.\n")
            else:
                print(f"{number} tidak ditemukan dalam kontak {name}.\n")
    else:
        print(f"{name} tidak ada di dalam buku telepon.\n")

    # search for a contact
    elif choice == "4":
        name = input("Masukkan nama kontak: ")
        if name in phone_book:
            print(f"{name}: {phone_book[name]}\n")
        else:
            print(f"{name} tidak ada di dalam buku telepon.\n")

    # quit the program
    elif choice == "5":
        # write the phone book data to the file
        with open(phone_book_file, "w") as f:
            for name, number in phone_book.items():
                f.write(f"{name}:{number}\n")

        print("Selamat Tinggal!")
        break

    # invalid choice
    else:
        print("Input salah!. Tolong masukan lagi\n")
        