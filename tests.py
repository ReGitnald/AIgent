from functions.get_files_info import get_files_info
from functions.get_file_content import *
from functions.run_python_file import run_python_file
def main():
    # default = get_files_info("calculator", ".")
    # calc = get_files_info("calculator", "pkg")
    # bin = get_files_info("calculator", "/bin")
    # calcwrong = get_files_info("calculator", "../")
    # # print("what is going on?")
    # print(f"Result for current directory:\n{default}")
    # print(f"Result for 'pkg' directory:\n{calc}")
    # print(f"Result for '/bin' directory:\n{bin}")
    # print(f"Result for '../' directory:\n{calcwrong}")
    # print(get_file_content("calculator", "lorem.txt"))
    # thing = get_file_content("calculator", "main.py")
    # print(thing)
    # thing = get_file_content("calculator", "pkg/calculator.py")
    # print(thing)
    # thing = get_file_content("calculator", "/bin/cat")
    # print(thing)
    # thing = get_file_content("calculator", "pkg/does_not_exist.py")
    # print(thing)

    # print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    # print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    # print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    print(run_python_file("calculator", "main.py")) #(should print the calculator's usage instructions)
    print(run_python_file("calculator", "main.py", ["3 + 5"])) #(should run the calculator... which gives a kinda nasty rendered result)
    print(run_python_file("calculator", "tests.py"))
    print(run_python_file("calculator", "../main.py") )#(this should return an error)
    print(run_python_file("calculator", "nonexistent.py"))



if __name__ == "__main__":
    main()