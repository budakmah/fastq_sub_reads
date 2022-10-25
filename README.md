# fastq_sub_reads
A python script that creates sub-reads from fastq file based on desired probality.

A python script that you can use whenever you want to create subdatasets from short reads.
It takes forward and reverse fastq files as input and creates files according to the specified probability.
example usage

python3 sub_reads.py [forward.fastq] [reverse.fastq] [@] [50 100] path/to/output
