import pickle, shelve
print("Консервация списков.")
variety = ["огурцы", "помидоры", "капуста"]
shape = ["целые", "кубиками", "соломкой"]
brand = ["Главпродукт", "Чумак", "Бондюэль"]
f = open("pickles.dat", "wb")

pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

print("\nРасконсервация списков.")
f = open("pickles.dat", "rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)
print(variety)
print(shape)
print(brand)
f.close()

print("\nПомещение списков на полку.")
s = shelve.open("pickles2.dat")
s["variety"] = ["огурцы", "помидоры", "капуста"]
s["shape"] = ["целые", "кубиками", "соломкой"]
s["brand"] = ["Главпрдукт", "Чумак", "Бондюэль"]
s.sync()

print("\nИзвлечение списков из файла полки: ")
print(f"торговые марки - {s["brand"]}")
print(f"формы - {s["shape"]}")
print(f"виды овощей - {s["variety"]}")
s.close()


input("\n\nPress Enter to exit")