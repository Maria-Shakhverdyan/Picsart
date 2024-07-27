def generate_report(title, content, *, author = None, date = None, **extra_info):
    report = (f"Title is: {title}\n")
    report += (f"Content is: {content}\n")

    if author:
        report += (f"Author is: {author}\n")
    if date:
        report += (f"Date is: {date}\n")

    for key, value in extra_info.items():
        report += (f"{key.capitalize()}: {value}")

    return report

report = generate_report(
    title = 'To do list',
    content = "'1. Date with Ann', '2. Help mom', '3. Practice Python'",
    author = 'Dave',
    date = '27 July, 2024',
    additionally = 'Watch the movie if I have time'
)

print(report)