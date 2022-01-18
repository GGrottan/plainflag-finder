import argparse
import subprocess 
import os.path
from genericpath import isfile
import sys

# Create arguments and sort them according to requirements
# Return the arguments passed in order to process them later
def define_arguments():
    parser = argparse.ArgumentParser()
    required = parser.add_argument_group('Required arguments')
    required.add_argument('-f', '--file', dest='file', help='file to find strings in', required=True)

    parser.add_argument('-w', '--wordlist', dest='wordlist', 
    help='wordlist to use. If none is specified, a default list is used. If a custom list is to be used, make sure to only have one keyword on each line.')

    parser.add_argument('-o', '--output', dest='output', help='Text file to write output to. If none is specified, output will be printed to the console.')

    parser.add_argument('-c', '--case', dest='case_sensitive', 
    help='Set this flag to enable case sensitive search. If not set, case sensitivity is ignored. This option will be most effective when using a custom wordlist.',
    action='store_true', default=False)

    parser.add_argument('-l','--length', dest='length', help='Set the minimum length of the flag in order to limit the amount of results', type=int)

    options = parser.parse_args()

    return options

def search_file(filename, wordlist, output_type, case_sensitive, length):

    # Hold result for processing later
    finds = []

    # Each word in the wordlist is given on a new line
    wl = open(wordlist)
    for word in wl:
        
        # Determine which command to execute
        # Default ignores case sensitivity
        command = 'strings ' + filename + ' | grep -i ' + word

        if case_sensitive:
            command = 'strings ' + filename + ' | grep ' + word

        process = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
        result = process.stdout

        if result.decode() == '':
            pass
        else:
            finds.append(result.decode().splitlines())

    return finds

if __name__ == '__main__':

    # Retrieve arguments
    argument = define_arguments()
    file = argument.file
    wordlist = argument.wordlist
    output_type = argument.output
    case_sensitive = argument.case_sensitive
    length = argument.length

    if not os.path.isfile('./' + file):
        sys.exit('\n[-] File to search not found!')

    if wordlist == None:
        wordlist = 'plainflag-wordlist.txt'

    if length == None:
        length = 0 # Default is to show everything

    # Store all of the returned results for easier access
    results = search_file(file, wordlist, output_type, case_sensitive, length)

    # We just want to check if output is set, since default is to print to console
    if output_type != None:
        
        try:
            # Need to account for nested list
            with open(output_type + '.txt', 'x') as output_file: 
                for i in range(0, len(results[0])):
                    output_file.write(str(results[0][i]) + '\n') 
        except:
            print('[-] Either a file with the same name already exists, or the directory specified does not exist.')
    else:
        # Print results to console
        if len(results) == 0:
            print('\n[-] No strings found...')
        else:
            for i in range(0, len(results[0])):
                if len(results[0][i]) >= length:
                    print('\n[+]' + results[0][i])
