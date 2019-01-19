import sys

# reads input from stdin and dumps the contents into memory
def read_input(args):
    '''
    args: commandline arguments from sys (a list of strings)

    Attempts to read the file specified at index 1, ensures it is in the
    correct format, and alerts the user and closes if any issues are found.

    returns: the opened file
    '''

    # try to open the file, alert the user and exit if that fails
    try:
        file_info = open(args[1], "r")
        return(file_info)
    except FileNotFoundError:
        print("File not found")
        sys.exit(-1)

def format_file(file_info, mode):
    stripped_lines = []
    formatted_line = []
    lines = file_info.readlines()
    file_info.close()
    n = 0

    # remove new line characters from the text and strip blankspace
    for line in lines:
        if line == "\n":   # Ignore blank new lines
            pass
        elif len(line) <= 2: # ignore lines that are length 2 or less
            pass
        else:
            stripped_lines.append(line.strip())    # strip new lines

    # Pass 2, checks file again after whitespace is removed
    for line in stripped_lines:
        if line == "\n":   # Ignore blank new lines
            pass
        elif len(line) <= 2: # ignore lines that are length 2 or less
            pass
        else:
            formatted_line.append(line.strip())




# Modes:
# -1: We will not parse this
# 0: python
def pick_mode(file_name):
    if file_name[-3:] == ".py": # the mode is python
        return 0
    else:
        return -1


if __name__ == "__main__":
    file_info = read_input(sys.argv) # read the file
    mode = pick_mode(sys.argv[1]) # Arg 1 is the file name of target file
    if mode == -1: # if mode is -1 we will not parse this file
        print("File Ignored")
        exit()
    else:
        formatted_file = format_file(file_info, mode) # format the file
        #line_count = count_lines(file_info, mode)
        #comment_count = count_comments(formatted_info, mode)
