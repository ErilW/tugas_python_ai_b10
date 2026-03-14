# Deklarasi Variabel dan Tipe Data
str_var = "string"
int_var = 123
float_var = 3.14
bool_var = True
list_var = [1, 2, 3, 4, 5]

# Manupulasi String
print(str_var.upper())  # Output: STRING
print(str_var.lower())  # Output: string
print(str_var.replace("string", "text"))  # Output: text
print(f"length: {len(str_var)}") # Output: length: 6
print("String", str_var) # Output: String string

# Operasi Matematika Sederhana
print(int_var + 10)  # Output: 133
print(float_var * 2)  # Output: 6.28
print(int_var / 2)  # Output: 61.5
print(int_var - 23)  # Output: 100
print(int_var % 10)  # Output: 3
print(int_var // 2) # Output: 61  

#List dan Akses Elemen 
list_var_2 = ['a', 'b', 'c', 'd', 'e']
print(list_var_2[0])  # Output: a
print(list_var_2[2])  # Output: c
list_var_2.append('f') 
print(list_var_2)  # Output: ['a', 'b', 'c', 'd', 'e', 'f']
list_var_2.remove('b') 
print(list_var_2)  # Output: ['a', 'c', 'd', 'e', 'f']


# Penggunaan input dari user
user_input = input("Ketik sesuatu mas bro: ")
print(f"Kamu ketik ini bos: {user_input}")


user_input = input("Nama: ")
user_input = input("Umur: ")

print(f"Halo, nama saya {user_input} dan umur saya {user_input} tahun.")