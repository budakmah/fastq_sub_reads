from random import choices
import sys
"""
f1 for forward reads
f2 for reverse reads
m for header of reads (eg. @SRR12345)
o for a number between 1 and 1000. eg. If a value of 1 is entered, the data will decrease by 1 in 1000.
d output folder
usage:
python sub_read.py forward_read.fasq reverse_read.fastq @SRR12345 10 20 500 path/to/output/

"""
f1=sys.argv[1]
f2=sys.argv[2]
m=sys.argv[3]
o=sys.argv[4:-1]
d=sys.argv[-1]


def dump(f1,f2,m,o,d):
    fq1=open(f1,"rt")
    fq2=open(f2,"rt")
    fq1=fq1.read()
    fq2=fq2.read()
    fq1=fq1.split(m)
    fq2=fq2.split(m)
    fq1=fq1[1:]
    fq2=fq2[1:]
    a_list = [0, 1]

    for n in range(len(fq1)):
        fq1[n]=m+fq1[n]
        fq2[n]=m+fq2[n]
    for i in o:
        p=int(i)/1000
        distribution = [1-p, p]
        fastq1=str(p*1000)+"_"+f1.split("/")[-1]
        fastq2=str(p*1000)+"_"+f2.split("/")[-1]
        out1=open(d+"/"+fastq1,"wt")
        out2=open(d+"/"+fastq2,"wt")
        for l1,l2 in zip(fq1,fq2):
            r_n=choices(a_list, distribution)
            if r_n[0]==1:
                out1.write(l1.split("\n")[0]+"\n"+l1.split("\n")[1]+"\n"+l1.split("\n")[2]+"\n"+l1.split("\n")[3]+"\n")
                out2.write(l2.split("\n")[0]+"\n"+l2.split("\n")[1]+"\n"+l2.split("\n")[2]+"\n"+l2.split("\n")[3]+"\n")
dump(f1,f2,m,o,d)
