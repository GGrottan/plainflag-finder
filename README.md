# plainflag-finder

## About 🚩
The `plainflag-finder` is a small script that is made for finding specific types of strings in CTF challenges - typically those hidden in images or other various files.
The script runs through a small dictionary of words associated with a flag, and grabs every string that contains one of the given keywords. The keywords are given in
a separate text file, making it easier to modify the search.

## Usage 📝
| Flag           | Description                                                                                                                                              |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| -w, --wordlist | wordlist to use. If none is specified, a default list is used. If a custom list is to be used, make sure to only have one keyword on each line.          |
| -o, --output   | Text file to write output to. If none is specified, output will be printed to the console.                                                               |
| -c, --case     | Set this flag to enable case sensitive search. If not set, case sensitivity is ignored. This option will be most effective when using a custom wordlist. |
| -l, --length   | Set the minimum length of the flag in order to limit the amount of results.                                                                              |
| -f, --file     | File to find strings in (obligatory)                                                                                                                     |                                                                                                              |                                                                                                           |

The above information can also be viewed by calling setting the `-h, --help` flag.

## Details ⚙️
### wordlist
The wordlist is a small list of typically used strings in a file given in a CTF-challenge, such as `CTF` or `Password`.
The default list contains every English Caesar cipher permutation of the word `CTF`. Furthermore, both the binary and 
Base64 encoded representations of the word `CTF` is also added, as well as some various other variations and supplementary words. This is in no way a complete list,
but should make it easier to retrieve easy-to-catch flags, be it an easy challenge, or part of a bigger one. 

There is also an option to add your own wordlist in case you want to look for additional keywords, or narrow down your search (e.g. searching for every permuation
in a Caesar Cipher might produce a lot of garbage output, depending on the amount of strings). The only requirement for making a new list is that each word has to be on its own separate line in the text file.

### Output
By setting the `-o, --output` flag, the results of the search is written to a separate file in the same directory as the script is executed. The file will
be saved as a text file by default, so you need only supplement the name of the file as an option to the argument. If no output argument is given, the results will be 
printed to the console. 

### Case
The `-c, --case` flag indicates whether you want to search according to the case sensitivity given in the wordlist. By default, case sensitivity is not 
accounted for, and all words in the default wordlist is given in lowercase. Therefore, if you want to detail your search by case sensitivity, a custom
wordlist will give the best results when using this argument. No option is needed for this argument, simply appending the `-c, --case` flag to the command 
will suffice.

### Length
The length argument can be set in order to further limit the amount of results. If the length is not set, it defaults to a length of 0, meaning that 
all results will be shown.

### File
This is the only obligatory argument, and needs a filename to search. Executing the script using only this argument is possible, and will
search the given file with the following configuration:
  - Grab every string that contains the words given in the default wordlist, regardless of uppercase or lowercase results
  - Print every result to the console

