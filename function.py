# function = A block of reusable code
# Place () after the function name to invoke it.


# def bday_func(name, msg):
#     print(f"Happy Birthday {name}!")
#     print(f"Good to see you {msg}!")
#     print()


# bday_func("Brother", "Buddy")
# bday_func("Steve", "My Frined")


def display_invoice(invoive_no, username, amount):
    print(f"Your invoive_no is : {invoive_no:02d}")
    print(f"Username : {username}")
    print(f"Total amount : ${amount}")


display_invoice(1, "Anam", 25.00)
display_invoice(2, "David", 50.00)
display_invoice(3, "Archar", 10.50)
