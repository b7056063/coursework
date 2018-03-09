import sys
from Bio import SeqIO
from Bio.Alphabet import generic_dna,generic_protein
import csv
import os

#convert fasta files to genbank files
def fasta2genbank(test_fasta,test_gb):
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
class Curve():

    def __init__(self,*items):
        self.items=[]
        for i in items:
            self.append(i)

    def append(self,item):
        if not isinstance(item,Curve2):
             raise TypeError("Curves can only take Curve2")
        self.items.append(item)
    def __str__(self):
        return "{}".format(self.items)
    def __repr__(self):
        s=","
        s=s.join([repr(x) for x in self.items])
        return "{}".format(s)

class Curve2():
        
    def __init__(self,*items):
        self.items=list(items);

    def __str__(self):    
        return "{}".format(self.items)

    def __repr__(self):
        return "{}".format(self.items)
    
def fasta2csv(fastafile,csvfile):

    #the csv title
    columns=['seq_id','sequence']

    #get current path
    root_path=os.getcwd()

    #the whole path of this csv file
    tmp_path=root_path+"/temp.csv"

    f=open(tmp_path,"w")
    writer=csv.writer(f)

    #write csv title
    writer.writerow(columns)
        
    for record in SeqIO.parse(fastafile,"fasta"):
        m=record.id
        n=record.seq
        
        li=Curve(Curve2(m,n))
        
        for l in li.items:
            writer.writerow(l.items)

    return f
        
#user input
if sys.argv[2]=='gbk':
    fasta2genbank(sys.argv[1],"test_gb")
elif sys.argv[2]=='csv':
    fasta2csv(sys.argv[1],"test_csv")
elif sys.argv[2]=='gbk and csv':
    fasta2genbank(sys.argv[1],"test_gb")
    fasta2csv(sys.argv[1],"test_csv")


