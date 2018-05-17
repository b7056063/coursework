import sys
from Bio import SeqIO
from Bio.Alphabet import generic_dna,generic_protein
import csv
import os
import click

#convert fasta files to genbank files
def fasta2genbank(test_fasta,test_gb):
    '''This is a function for converting fasta files to genbank files,

    open terminal and type: python3 coursework.py filename.fasta gbk,
    then you will get a file named test_gb. enjoy it.'''
    input_handle=open(test_fasta,"rU")
    output_handle=open(test_gb,"w")

    sequences=list(SeqIO.parse(input_handle,"fasta"))
    for seq in sequences:
        seq.name = seq.name[:9]

        seq.seq.alphabet=generic_dna
    
    count=SeqIO.write(sequences,output_handle,"genbank")
    output_handle.close()
    input_handle.close()
    print("Converted %i records" % count)
    
#convert fasta files to csv files
#creat a list which can contain all information
class Csv():

    def __init__(self,*items):
        self.items=[]
        for i in items:
            self.append(i)

    def append(self,item):
        if not isinstance(item,Csv2):
             raise TypeError("Csv can only take Csv2")
        self.items.append(item)
    def __str__(self):
        return "{}".format(self.items)
    def __repr__(self):
        s=","
        s=s.join([repr(x) for x in self.items])
        return "{}".format(s)

class Csv2():
        
    def __init__(self,*items):
        self.items=list(items);

    def __str__(self):    
        return "{}".format(self.items)

    def __repr__(self):
        return "{}".format(self.items)
    
def fasta2csv(fastafile,csvfile):
    
    '''This is a function for converting fasta files to csv files,

    open terminal and type: python3 coursework.py filename.fasta csv,
    then you will get a file named test_csv. enjoy it.'''
    #the csv title
    columns=['seq_id','sequence']

    #get current path
    root_path=os.getcwd()

    #the whole path of this csv file
    tmp_path=root_path+"/test_csv"

    f=open(tmp_path,"w")
    writer=csv.writer(f)

    #write csv title
    writer.writerow(columns)
        
    for record in SeqIO.parse(fastafile,"fasta"):
        m=record.id
        n=record.seq
        
        li=Csv(Csv2(m,n))
        
        for l in li.items:
            writer.writerow(l.items)

    return f

@click.command()
@click.option('-i', type=click.File('rb'), help='fasta file')
@click.option('-o', type=click.File('w'), help='txt file')

def fasta2txt(f, t):
    for line in f:
        if line.startswith(">"):
            lin = line.strip().split()[0][1:]
            t.writelines('\n' + lin + '\t')
        else:
            t.writelines(line.strip())
#user input
if sys.argv[2]=='gbk':
    fasta2genbank(sys.argv[1],"test_gb")
elif sys.argv[2]=='csv':
    fasta2csv(sys.argv[1],"test_csv")
elif sys.argv[2]=='txt':
    fasta2csv(sys.argv[1],"test.txt")    
elif sys.argv[2]=='gbk and csv':
    fasta2genbank(sys.argv[1],"test_gb")
    fasta2csv(sys.argv[1],"test_csv")


