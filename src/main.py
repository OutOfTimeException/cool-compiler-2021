import sys
import os
from lexer import tokenize
from parser import parse
from testers import parser_tester

#########################################################################
# To use this script execute in terminal:                               #
#   python3 main.py execute_mode module_to_execute program_directory    #
#                                                                       #
# execute_mode is to use the tester or just run the program(s), ex:     #
#   - test      - run                                                   #
# module_to_execute can be:                                             #
#   - lexer     - parser                                                #
# program_directory is the dir where program(s) is(are), ex:            #
#   ../tests/lexer                                                      #
#   ../tests/parser                                                     #
#########################################################################

execute_mode = sys.argv[1]
module_to_execute = sys.argv[2]
program_directory = sys.argv[3]

# TEST
if execute_mode == 'test':
    if module_to_execute == 'parser':
        parser_tester(program_directory)
    else:
        raise Exception('Not implemented Test Mode for %s' % module_to_execute)

# RUN
programs_files = [file for file in os.listdir(program_directory) if file.endswith('.cl')]
for program_file in programs_files:
    input('Press enter to analyze ' + program_file)
    program_route = program_directory + '/' + program_file

    # To run lexer
    if sys.argv[1] == 'lexer':
        with open(program_route, 'r', encoding='UTF-8') as f:
            tokens, errors = tokenize(f.read())

        for token in tokens:
            print(token)
        print()
        if len(errors):
            print('ERRORS:')
            for error in errors:
                print(error)

    # To run parser
    if sys.argv[1] == 'parser':
        with open(program_route, 'r', encoding='UTF-8') as f:
            tree, errors = parse(f.read())
            if len(errors):
                print(errors)
            else:
                pass
                # print ast

    else:
        print('Invalid section to test: ' + sys.argv[1])
