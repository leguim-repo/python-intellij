from rich import print
from rich import inspect
from rich.console import Console

console = Console()

test_data = [
    {"jsonrpc": "2.0", "method": "sum", "params": [None, 1, 2, 4, False, True], "id": "1", },
    {"jsonrpc": "2.0", "method": "notify_hello", "params": [7]},
    {"jsonrpc": "2.0", "method": "subtract", "params": [42, 23], "id": "2"},
]


def test_log():
    myvar = "content of my local var"
    enabled = True
    context = {
        "foo": "bar",
        }
    movies = ["Deadpool", "Rise of the Skywalker"]
    console.log("Hello from", console, "!")
    console.log("Another log")
    console.log(test_data, log_locals=False)


class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


if __name__ == "__main__":
    print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())
    inspect(Dog, methods=True)
    myDog = Dog('Brutus')
    myDog.add_trick('roll over')
    print(myDog.tricks)
    test_log()
