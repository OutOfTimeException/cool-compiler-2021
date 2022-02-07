import sys
import os
import ast_print
from lexer import tokenize
from parser import parse
from testers import test_parser

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
        test_parser(program_directory)
    else:
        raise Exception('Not implemented Test Mode for %s' % module_to_execute)

# RUN
programs_files = [file for file in os.listdir(program_directory) if file.endswith('.cl')]
for program_file in programs_files:
    input('Press enter to analyze ' + program_file)
    program_route = program_directory + '/' + program_file

    # To run lexer
    if module_to_execute == 'lexer':
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
    elif module_to_execute == 'parser':
        with open(program_route, 'r', encoding='UTF-8') as f:
            ast, errors = parse(f.read())
            if len(errors):
                print(errors)
            else:
                # print ast
                formatter = ast_print.FormatVisitor()
                tree = formatter.visit(ast)
                print(str(tree))

    else:
        print('Invalid section to execute: ' + module_to_execute)
