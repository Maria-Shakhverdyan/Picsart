def make_greeting(greeting):
    def give_greeting(name):
        print(f"{greeting}! {name}")
    return give_greeting

hello_greet = make_greeting("Hello")
hello_greet("Maria")