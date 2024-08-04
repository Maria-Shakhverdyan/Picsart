def make_config(key, value):
    def config():
        return {key: value}
    return config

config_func = make_config("Ann", "31")
config_dict = config_func()

print(config_dict)
