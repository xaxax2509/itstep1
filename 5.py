
    try:
        print("Hello")
        print("No error")
    except NameError as error:
        print(error)
    else:
        print("No problems")
    finally:
        print("Finally code")

