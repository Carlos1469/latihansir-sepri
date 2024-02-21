print("<<<      LATIHAN 1     >>>")
print("Berikut akan tampil list dengan kondisi:")
print("1. range(1,100)")
print("Hanya value/item : genap (i >=10 dan i <=20)")
print("Hanya value/item : ganjil (i >=90 dan i <=100)\n")

data_list = [
i for i in range(1, 100) 
if (i >= 10 and i <= 20 and i % 2 == 0) or (i >= 90 and i <= 100 and i % 2 != 0)
]
print(data_list)

print("-"*10, "Latihan 2", "-"*10)

data_list = ["Do", "Re", "Mi", "Fa", "Sol", "La", "Ti"]
new_list = data_list[2:3] + data_list[:1] + data_list[3:] + data_list[1:2]

print(new_list)

print("-"*10, "Latihan 3", "-"*10)
data = "IgNatIus"
result = [char for char in data if char.isupper()]
print(result)