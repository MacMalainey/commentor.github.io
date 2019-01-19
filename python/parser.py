import sys
import re

multi_comment_flag = 0
multi_comment_char_sum = 0

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

# Removes garbage from the file
def format_file(file_info, mode):
    stripped_lines = []
    formatted_lines = []
    lines = file_info.readlines()
    file_info.close()

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
            formatted_lines.append(line.strip())

    return formatted_lines

# Counts the number of total lines
def count_lines(formatted_info, mode):
    counter = 0
    for lines in formatted_info:
        counter+=1

    return counter

# Counts number of lines with comments
def count_comments(formatted_info, mode):

    comment_sym = ["#"] # Legal comment symbols
    comment_sym_multi = ['"""'] # Legal multiline comment symbols
    counter = 0

    for line in formatted_info:
        counter += find_comment(line, comment_sym[mode], comment_sym_multi[mode])

    return counter

# Determine number of comments based off of defined length of "single" comment
def determine_number_of_comments(comment_length):
    comment_length_constant = 80 # The length of a comment that we will consider 1 comment
    if comment_length <= comment_length_constant:
        return 1
    else:
        return round(comment_length / comment_length_constant)

def find_comment(line, comment_sym, comment_sym_multi):
    global multi_comment_flag, multi_comment_char_sum

    # If we are in the middle of a multiline comment, add the characters to the sum and return 0
    if (multi_comment_flag == 1) and (comment_sym_multi not in line):
        multi_comment_char_sum += len(line)
        return 0

    # multiline comments
    elif comment_sym_multi in line:
        # if the flag is not set, set it and start counting
        if multi_comment_flag == 0:
            multi_comment_char_sum += len(line)
            multi_comment_flag = 1
            return 0
        else:
            multi_comment_char_sum += len(line) - len(comment_sym_multi) * 2 #subtract off the length of the symbols
            multi_comment_flag = 0

            comment_len = determine_number_of_comments(multi_comment_char_sum)

            multi_comment_char_sum = 0
            return comment_len

    # single line comments
    elif line[0:len(comment_sym)] == comment_sym:  # If we detect a comment at the beginning of a line
        return determine_number_of_comments(len(line))

    # inline comments
    elif comment_sym in line:
        phrase = re.search('(?<=\")(.*?' + comment_sym + '.*?)(?=\")', line)
        phrase2 = re.search('(?<=\')(.*?' + comment_sym + '.*?)(?=\')', line)
        if(phrase):
            # remove text from line
            line = line.replace('"' + phrase.group() + '"', '')
            return find_comment(line, comment_sym, comment_sym_multi) # Recurse with text removed
        elif(phrase2):
            # remove text from line
            line = line.replace("'" + phrase2.group() + "'", '')
            return find_comment(line, comment_sym, comment_sym_multi) # Recurse with text removed
        else:
            return determine_number_of_comments(len(line))

    else:
        return 0

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
        formatted_info = format_file(file_info, mode) # format the file
        line_count = count_lines(formatted_info, mode)
        comment_count = count_comments(formatted_info, mode)
        print(comment_count)
