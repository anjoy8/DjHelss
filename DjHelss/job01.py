
def printpolicy_job001():
    f = open('D:\\Code\\Test\\Python\\DjCodeTest\\DjHelss\\DjHelss\\test.json')
    data = f.read()
    print(data)
    f.close
   


if __name__ == "__main__":
    try:
     printpolicy_job001()
    except IOError as e:
        print("Error" + e.__str__())
     

