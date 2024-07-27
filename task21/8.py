def update_settings(**kwargs):
    process_settings(**kwargs)

def process_settings(**settings):
    print("Settings update:")
    for key, value in settings.items():
        print(f"{key}: {value}")

update_settings(
    theme = 'dark',
    notifications = True,
    language='English',
    timezone='GMT+4'
)
