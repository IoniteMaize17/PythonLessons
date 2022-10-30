print("Main level code!")

def subfucntion():
    print("Subfunction code!")

def main():
    print("Main function code!")

print(__name__)
if __name__ == "__main__":
    main()
else:
    print(__name__)