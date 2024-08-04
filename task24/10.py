def make_config(key, value):
    def config():
        return {key: value}
    return config

# person_info = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York",
#     "email": "alice@example.com",
#     "is_employee": True,
# }

config_func = make_config("Ann", "31")
config_dict = config_func()

print(config_dict)