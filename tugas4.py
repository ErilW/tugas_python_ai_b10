# List – akses & manipulasi
mixed_list = ["apel", 10, 3.5, "pisang", 42, "badak"]

print("Elemen pertama:", mixed_list[0])
print("Elemen akhir:", mixed_list[-1])
print("Slicing [1:5:2]:", mixed_list[1:5:2])

print( mixed_list) # sebelum append insert extend

mixed_list.append("anj")
mixed_list.insert(2, "pir")
mixed_list.extend([100, "melon"])

print(mixed_list) # setelah append insert extend


mixed_list.pop()
mixed_list.remove("pisang")

print(mixed_list) # setelah pop remove


# Tuple – immutability & unpacking
tuple_data = ("red", "green", "blue", "yellow", "black")

print(f"lenght: {len(tuple_data)}")
print("indeks 2:", tuple_data[2])

a, b, c, *sisanya = tuple_data

print("a:", a)
print("b:", b)
print("c:", c)
print("sisanya:", sisanya)


# Set – keunikan & operasi himpunan
set_a = {1, 2, 3, 4, 5, 5, 5}
set_b = {4, 5, 6, 7, 8}

print("Set A:", set_a)
print("Set B:", set_b)

print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference A-B:", set_a - set_b)
print("Symmetric Difference:", set_a ^ set_b)


# Dictionary – key/value dasar
mahasiswa = {
    "nama": "Budi",
    "nim": "22001",
    "angkatan": 2022,
    "kota": "Batam"
}

print("Data awal:", mahasiswa)

mahasiswa["prodi"] = "Informatika"
mahasiswa["kota"] = "Jakarta"
del mahasiswa["angkatan"]

print(mahasiswa) # data setelah perubahan

print("Keys:", mahasiswa.keys())
print("Values:", mahasiswa.values())
print("Items:", mahasiswa.items())

for k, v in mahasiswa.items():
    print(k, ":", v)


# Nested structures
books = [
    {"judul": "Data Science Handbook", "penulis": "Dewi", "tahun": 2020},
    {"judul": "Python for Everyone", "penulis": "Andi", "tahun": 2019},
    {"judul": "Machine Learning 101", "penulis": "Sari", "tahun": 2021}
]

print("Semua judul buku:")

for book in books:
    print(book["judul"])

tahun_filter = 2020
filtered_books = [b for b in books if b["tahun"] >= tahun_filter]

print("Buku tahun >=", tahun_filter, ":", filtered_books)


# Comprehension & utilitas
numbers = list(range(1, 21))

even_numbers = [n for n in numbers if n % 2 == 0]
square_numbers = [n**2 for n in numbers]

print("List genap:", even_numbers)
print("List kuadrat:", square_numbers)

dict_even_odd = {n: "genap" if n % 2 == 0 else "ganjil" for n in range(1, 11)}

print("Dict genap ganjil:", dict_even_odd)

sentence = "python gampang banget"
unique_letters = {c.lower() for c in sentence if c.isalpha()}

print("Huruf unik:", unique_letters)


# Keanggotaan & pencarian sederhana
search_list = ["python", "java", "c++", "golang"]
search_set = {"apple", "banana", "orange"}

print("python in list:", "python" in search_list)
print("mango in set:", "mango" in search_set)

if "java" in search_list:
    print("Posisi java:", search_list.index("java"))
else:
    print("java tidak ditemukan")