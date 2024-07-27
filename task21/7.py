def log_messages(level, *messages, **metadata):
    timestamp = metadata.get('timestamp', 'ne ukazano')
    user = metadata.get('user', 'ne znayem')

    for message in messages:
        print(f"[{timestamp}] [{level}] [User: {user}] - {message}")

result = log_messages(
    'INFO',
    'The application has been launched',
    'Status check complete.',
    timestamp = '2024-07-27 12:00:00',
    user = 'Maria'
)

result = log_messages(
    'ERROR',
    'Server connecting error.',
    "Cant't find the file.",
    user='Bob'
)