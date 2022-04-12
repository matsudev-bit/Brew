from operator import iconcat
import brew
import os

while True:
    text = input(os.path.abspath(__file__) + "$ brew > ")
    result, error = brew.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)