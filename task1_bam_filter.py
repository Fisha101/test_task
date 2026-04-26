import pysam

input_file = "input.bam" 
output_file = "output.bam" 

bam = pysam.AlignmentFile(input_file, "rb")
output_bam = pysam.AlignmentFile(output_file, "wb", template=bam)
for read in bam:
    cigar = read.cigartuples
    for i in range(len(cigar) - 1):
        current_op = cigar[i][0]
        next_op = cigar[i + 1][0]
        if (current_op == 4 and next_op == 5) or (current_op == 5 and next_op == 4):
            output_bam.write(read)
            break

bam.close()
output_bam.close()


