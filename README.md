# BibTeX Journal Name Abbreviator

## Update (2025-7-31)
- Current version: 1.2
The code has been rewriten in C++ for more elegant usage and better performance (with the help of Claude Sonnet 4). The old Python version is still available and will be removed in the future.

## Usage

```bash
git clone https://github.com/xu-shi-jie/bib-journal-abbreviator
cd bib-journal-abbreviator
make all
mv refabbr /usr/local/bin
```

## Deprecated
- Current version: 1.1
- journalList.txt: A list of journal names and their abbreviations. You can add more journal names and abbreviations to this file by appending them to the end of the file. The format is "Journal Name = Abbreviation". For example, "Journal of the American Chemical Society = JACS".
- run `python3 main.py ref.bib` to abbreviate the journal names in the BibTeX file `ref.bib`. The output will be saved in `ref-abbr.bib`.

