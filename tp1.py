def say_hello(chain):
    return f"Hello, {chain}!"


mon_nom = input("Enter your name: ")

message = say_hello(mon_nom)

print(message)  