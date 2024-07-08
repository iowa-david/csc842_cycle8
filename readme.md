
PII is a common concern in my day job when dealing with data, I know different patterns and practices and tools to identify possible PII within data storage such as SQL databases but have not delved into looking for them within files. As I mentioned in my previous assignment, I wanted to find more opportunities to leverage the same scaffolding in other avenues.

# security_check.py
This script reviews files stored on the computer and runs checks to see if it can find in plain text files potential PII patterns.
The two main ones I am looking for on this example are Social Security Numbers and Birthdays.

## Installation
The program uses two libraries. The first is OS, which is included with the standard Python installation. The second is psutil, which can be added to your machine with pip install psutil.

## Description
The script starts with empty lists of files and then recursively goes through the folder structure and identifies potential PII infractions in each file based upon the specified type of PII in the regular expression.

## Three main points:
###Python allows for relatively easy processing across a folder structure to view and check through files.
###Setting up specific regular expressions and combining with the above lets one go across a large array of files to see what is available.
###Python's print formatting syntax helps streamline the combination of complex objects in a friendly, easy-to-read output without string concatenation or other string manipulation processes.
## Room for improvement:
I am focusing on files that are located on the machine where the application is hosted, going across and seeing what is available on common network shares would be my next step. 
Additionally, I have found a new library to levrage to read in more types of files besides standard file types that are handled automatically by python.
FullText,https://github.com/btimby/fulltext, looks to be a powerful text search that can convert docx, pdf, and doc files to text to be able to query.

