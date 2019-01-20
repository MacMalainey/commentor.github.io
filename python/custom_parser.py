import sys
import re

multi_comment_flag = 0
multi_comment_char_sum = 0
comment_sym = ["#", "//"] # Legal comment symbols
comment_sym_multi = ['"""', "/*"] # Legal multiline comment symbols

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
    global comment_sym, comment_sym_multi
    stripped_lines = []
    formatted_lines = []
    lines = file_info.readlines()
    file_info.close()

    # remove new line characters from the text and strip blankspace
    for line in lines:
        if line == "\n":   # Ignore blank new lines
            pass
        elif len(line) <= 2 and (not comment_sym_multi[mode] in line) and (not comment_sym_multi[mode][::-1] in line): # ignore lines that are length 2 for languages and does not contain their multiline comment delimiter
            pass
        else:
            stripped_lines.append(line.strip())    # strip blank space

    # Pass 2, checks file again after whitespace is removed
    for line in stripped_lines:
        if line == "\n":   # Ignore blank new lines
            pass
        elif len(line) <= 2 and (not comment_sym_multi[mode] in line) and (not comment_sym_multi[mode][::-1] in line):
            # ignore lines that are length 2 for languages and does not contain their multiline comment delimiter
            pass
        else:
            formatted_lines.append(line.strip())    # strip blank space

    return formatted_lines

# Counts the number of total lines
def count_lines(formatted_info, mode):
    counter = 0
    for lines in formatted_info:
        counter+=1

    return counter

# Counts number of lines with comments
def count_comments_and_code(formatted_info, mode):
    global comment_sym, comment_sym_multi
    comment_counter = 0
    code_counter = 0

    for line in formatted_info:
        if (line == formatted_info[-1]):
            print(line)
            temp_comment_counter, temp_code_counter = find_comment(line, comment_sym[mode], comment_sym_multi[mode], 1)
        else:
            temp_comment_counter, temp_code_counter = find_comment(line, comment_sym[mode], comment_sym_multi[mode], 0)

        if temp_comment_counter == -1: # Edge case for files that don't end their multiline comments
            comment_counter = len(formatted_info) - code_counter
            return comment_counter, code_counter

        comment_counter += temp_comment_counter
        code_counter += temp_code_counter

    return comment_counter, code_counter

# Determine number of comments based off of defined length of "single" comment
def determine_number_of_comments(comment_length):
    comment_length_constant = 80 # The length of a comment that we will consider 1 comment
    if comment_length <= comment_length_constant:
        return 1
    else:
        return round(comment_length / comment_length_constant)

def find_comment(line, comment_sym, comment_sym_multi, last_line):
    global multi_comment_flag, multi_comment_char_sum

    # If we are in the middle of a multiline comment, add the characters to the sum and return 0
    if (multi_comment_flag == 1) and (comment_sym_multi not in line) and (not last_line):
        multi_comment_char_sum += len(line)
        return 0, 0

    # multiline comments
    elif (comment_sym_multi in line) or (multi_comment_flag and last_line):
        # if the flag is not set, set it and start counting
        if multi_comment_flag == 0:
            multi_comment_char_sum += len(line)
            multi_comment_flag = 1
            return 0, 0
        elif(multi_comment_flag and last_line):
            return -1, 0
        else:
            multi_comment_char_sum += len(line) - len(comment_sym_multi) * 2 #subtract off the length of the symbols
            multi_comment_flag = 0

            comment_len = determine_number_of_comments(multi_comment_char_sum)

            multi_comment_char_sum = 0
            return comment_len, 0

    # single line comments
    elif line[0:len(comment_sym)] == comment_sym:  # If we detect a comment at the beginning of a line
        return determine_number_of_comments(len(line)), 0

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
            return determine_number_of_comments(len(line)), 1

    else:
        return 0, 1

# Modes:
# -1: We will not parse this
# 0: python
# 1: c++
def pick_mode(file_name):
    if file_name[-3:] == ".py": # the mode is python
        return 0
    if file_name[-4:] == ".cpp": # the mode is c++
        return 1
    else:
        return -1

# Returns in this order: line count, comment count, code count
# -1, -1, -1 is returned if it is not a valid file
def parse_code(file_name, file_contents):
    mode = pick_mode(file_name)
    if mode == -1: # if mode is -1 we will not parse this file
        return -1, -1, -1
    else:
        formatted_info = format_file(file_contents, mode) # format the file
        line_count = count_lines(formatted_info, mode)
        comment_count, code_count = count_comments_and_code(formatted_info, mode)
        return line_count, comment_count, code_count


if __name__ == "__main__":
    file_info = read_input(sys.argv) # read the file
    mode = pick_mode(sys.argv[1]) # Arg 1 is the file name of target file
    if mode == -1: # if mode is -1 we will not parse this file
        print("File Ignored")
        exit()
    else:
        formatted_info = format_file(file_info, mode) # format the file
        line_count = count_lines(formatted_info, mode)
        comment_count, code_count = count_comments_and_code(formatted_info, mode)
        print("lines: " + str(line_count))
        print("Comment: " + str(comment_count))
        print("Code: " + str(code_count))
