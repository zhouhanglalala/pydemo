from random import choice

my_tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
              "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
while True:
    num_1 = choice(my_tickets)

    num_2 = choice(my_tickets)

    num_3 = choice(my_tickets)

    num_4 = choice(my_tickets)

    my_num = f"{num_1}{num_2}{num_3}{num_4}"
    print(my_num)
    if my_num == "r6h4":
        break
