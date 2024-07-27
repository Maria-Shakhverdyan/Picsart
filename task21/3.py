def user_info(name, surname, *, age, city):
    profile = (
        f"User Profile\n"
        f"Name: {name}\n"
        f"Surname: {surname}\n"
        f"Age: {age}\n"
        f"City: {city}\n"
    )

    return profile

profile_info = user_info("Maria", "Shakhverdyan", age = 20, city = "Yerevan")
print(profile_info)