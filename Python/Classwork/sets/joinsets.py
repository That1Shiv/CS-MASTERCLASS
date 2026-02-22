laptops = {"Dell", "HP", "Lenovo"}
phones = {"Apple", "Samsung", "Google"}  
furniture = {'chair', 'table', 'sofa'}

electronics = laptops.union(phones)
# print(electronics)
devices = phones|laptops 
# print(devices)

# you can use the " | " operator or the union method to join sets 

all_devices = laptops.union(phones,electronics,furniture) 
# print(all_devices) 

laptops.update(phones)
print(laptops)