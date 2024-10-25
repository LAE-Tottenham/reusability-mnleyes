def get_adjacent():

    amountcalled = 0

    if amountcalled == 0:
        string = "first"
    elif amountcalled == 1:
        string = "second"

    adj = float(input(f"Enter your {string} triangle's adjacent side length: "))

    amountcalled = amountcalled + 1

    return adj