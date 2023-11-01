from random import randint


def roll_d100():
    return randint(0, 99)


def check_doubles(n):
    if n < 10:
        d1, d2 = "0", str(n)
    else:
        d1, d2 = str(n)[0], str(n)[1]

    return d1 == d2


def doubles_value(n):
    if not check_doubles(n):
        raise ValueError(f'{n} is not a valid "double digits" result.')
    return n % 10


def roll_d10():
    return randint(0, 9)


def get_key(n, d):
    """gets the nearest valid key in a dict with integer keys"""
    if n > max(d.keys()):
        raise KeyError(f"{n} is higher than all the keys in {d}.")
    while n not in d:
        n += 1
    return n


def get_reaction():
    roll = roll_d100()
    double = check_doubles(roll)
    positives = ("Positive", "Friendly")
    negatives = ("Negative", "Hostile")
    if roll % 2 == 0:  # even case
        return positives[double]
    return negatives[double]


if __name__ == "__main__":
    print(check_doubles(99))
    print(check_doubles(87))
    print(doubles_value(78))
