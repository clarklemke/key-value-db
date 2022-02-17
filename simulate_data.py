import uuid
import random
import string


# Used to simulate data (problem expects up to 1m key-values)


n = 1000000
letters = string.ascii_lowercase + " "

with open("data", "w") as file:
    for _ in range(n):
        random_length = random.randint(1, 80)
        random_string = "".join(random.choice(letters) for i in range(random_length))
        file.write(str(uuid.uuid4()) + " " + random_string + "\n")
