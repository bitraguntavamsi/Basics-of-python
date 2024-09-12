# operation=input("select the operation\n+\t-\t*\t/\noption:")
# match operation:
#     case "+":
#         a=int(input("a:"))
#         b=int(input("b:"))
#         print(a+b)
#     case "-":
#         a=int(input("a:"))
#         b=int(input("b:"))
#         print(a-b)
#     case "*":
#         a=int(input("a:"))
#         b=int(input("b:"))
#         print(a*b)
#     case "/":
#         a=int(input("a:"))
#         b=int(input("b:"))
#         print(a/b)
#     case _:
#         print("invalid integer")

while True:
    operation=input("select the operation\n+\t-\t*\t/\noption:")
    match operation:
        case "+":
            a=int(input("a:"))
            b=int(input("b:"))
            print(a+b)
        case "-":
            a=int(input("a:"))
            b=int(input("b:"))
            print(a-b)
        case "*":
            a=int(input("a:"))
            b=int(input("b:"))
            print(a*b)
        case "/":
            a=int(input("a:"))
            b=int(input("b:"))
            print(a/b)
        case'8':
            print("invalid integer")
        case 'cancel':
            break
