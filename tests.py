from functions.get_files_info import get_files_info

def main():
    default = get_files_info("calculator", ".")
    calc = get_files_info("calculator", "pkg")
    bin = get_files_info("calculator", "/bin")
    calcwrong = get_files_info("calculator", "../")
    # print("what is going on?")
    print(f"Result for current directory:\n{default}")
    print(f"Result for 'pkg' directory:\n{calc}")
    print(f"Result for '/bin' directory:\n{bin}")
    print(f"Result for '../' directory:\n{calcwrong}")


if __name__ == "__main__":
    main()