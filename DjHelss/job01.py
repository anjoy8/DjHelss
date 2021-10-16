def printpolicy_job001():
    a = 0
    b = 1/a


if __name__ == "__main__":
    try:
     printpolicy_job001()
    except IOError as e:
        print("Error" + e.__str__())
     

