# # handles 'ValueError' exception
# while True:
#     try:
#         x = int(input("Please enter a number:\n"))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...\n")
#
# # handles any kind of exception
# while True:
#     try:
#         x = int(input("Please enter a number:\n"))
#         break
#     except Exception:
#         pass

# handles ValueError, RuntimeError, TypeError, NameError exceptions
while True:
    try:
        x = int(input("Please enter a number:\n"))
        break
    except (ValueError, RuntimeError, TypeError, NameError):
        print("Oops!  Something went wrong...\n")

