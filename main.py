import os
import re
import sys

try:
    bibtexdb = open(sys.argv[1]).read()
except:
    print("Error: specify the file to be processed!")

# get the direction of current script
this_dir = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(this_dir, "journalList.txt")
# url = "https://gist.githubusercontent.com/FilipDominec/6df14b3424e335c4a47a96640f7f0df9/raw/74876d2d5df9ed60492ef3a14dc3599a6a6a9cfc/journalList.txt"

rulesfile = open(FILE_NAME)

# reversed alphabetical order matches extended journal names first
for rule in rulesfile.readlines()[::-1]:
    pattern1, pattern2 = rule.strip().split(" = ")
    if len(sys.argv) >= 3 and sys.argv[2] == 'nodot':
        pattern2 = pattern2.replace('.', '')
    # find "journal={<pattern1>}" or "journal = {<pattern1>}" and replace ... with pattern2
    repl = re.compile(
        r'journal\s*=\s*{\s*' + pattern1.strip() + '\s*}', re.IGNORECASE)
    (bibtexdb, num_subs) = repl.subn(
        lambda m: 'journal = {' + pattern2 + '}', bibtexdb)
    if num_subs > 0:
        print(
            "Replaced (%ix) '%s' FOR '%s'" %
            (num_subs, pattern1, pattern2))


out_file = sys.argv[1].replace('.bib', '-abbr.bib')
with open(out_file, 'w') as outfile:
    outfile.write(bibtexdb)
    print("Bibtex database with abbreviated files saved into %s" % out_file)
