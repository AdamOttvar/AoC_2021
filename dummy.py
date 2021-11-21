
def first_part(input_file):
    result = 1

    print(result)

def second_part(input_file):
    result = 2

    print(result)


if __name__ == '__main__':
    # Read the input file.
    with open("inputs/dummy.txt", "r") as myfile:
        input_file = [i.rstrip("\n") for i in myfile.readlines()]
    
    first_part(input_file)
    second_part(input_file)
