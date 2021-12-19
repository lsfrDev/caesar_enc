from time import sleep


def caesar_enc(
    shift: int = 4,
    ms="abcdefghijklmnopqrstuvwxyz",
    plain_text="hello world",
    print_it=True,
):
    c = ""
    for i in plain_text:

        i = i.lower()
        if i == " ":
            c += " "
            if print_it:
                print(" ", end="")

        if i != " ":
            where_is_it = ms.find(i) + shift

            while where_is_it > 25:
                where_is_it %= 26
            c += ms[where_is_it]
            if print_it:
                print(ms[where_is_it], end="")

    return c


sleep(1)
print("caesar enc bt lsfr @k0xxk")
sleep(1)
pt = input("text : ")
sleep(1)
shift = int(input("shift : "))
print("cipher : ", end="")
print(caesar_enc(shift=shift, plain_text=pt))
