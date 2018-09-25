if __name__ == '__main__':
    print(int((lambda x: x % 400 == 0 or (not x % 100 == 0 and x % 4 == 0))(int(input()))))