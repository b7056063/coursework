# Function
This is a programming has 3 functions:
one is for converting a fasta file to a genbank file;
one is to extract the 'id' and 'sequence' of DNA or protein from a fasta file and then organize them into one csv file;
the last one is for converting a fasta file to a txt file.
# Direction
This app requires you to install python3 (https://www.python.org/downloads/) in advance, and if you want to use fasta2txt function, please ensure you installed 'click'. Then save 'coursework.py' please.
Open Terminal,
if you want to get a genbank file,
e.g. type: python3 coursework.py filename.fasta gbk,
then you will get a file named test_gb;
if you want to get a csv file,
e.g. type: python3 coursework.py filename.fasta csv,
then you will get a file named test_csv;
if you want to get both a genbank file and a csv file,
e.g. type: python3 coursework.py filename.fasta gbk and csv.
if you want to get a txt file,
e.g. type: python3 coursework.py filename.fasta txt.
There is a sample file in the document named 'sample.fasta' for testing.
# Warning
Sometimes this program will show a warning about some kind of information exceeds the length when it is running, this warning doesn't affect the result, don't worry about that.
