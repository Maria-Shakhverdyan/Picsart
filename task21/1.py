def greeting(first_name, last_name, message = "Hello"):
    full_name = f"{first_name} {last_name}"
    greet = f"{message}, {full_name}!"
    return greet

print(greeting("John", "Asatryan"))
print(greeting("Maria", "Shakhverdyan", message = "Welcome"))