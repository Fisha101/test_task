from Bio import SeqIO

input_file = "test.fastq"
output_file = "output.fastq"

with open(output_file, "w") as output_file_handle:
    for read in SeqIO.parse(input_file, "fastq"):

        #left trim
        quality = read.letter_annotations["phred_quality"]
        left_trim = 0

        for i in range(0, len(quality) - 5 + 1, 2):
            window = quality[i:i+5]
            average = sum(window) / len(window)

            if average < 25:
                left_trim = i + 5
            else:
                break

        new_seq = read.seq[left_trim:]
        new_quality = quality[left_trim:]

        read.letter_annotations = {}
        read.seq = new_seq
        read.letter_annotations["phred_quality"] = new_quality

        #right trim
        quality = read.letter_annotations["phred_quality"]
        right_trim = len(quality)

        for i in range(-1, -len(quality) + 5 - 1, -2):
            window = quality[i-4:i+1]

            if len(window) < 5:
                break

            average = sum(window) / len(window)

            if average < 25:
                right_trim = i - 4
            else:
                break

        new_seq = read.seq[:right_trim]
        new_quality = quality[:right_trim]

        read.letter_annotations = {}
        read.seq = new_seq
        read.letter_annotations["phred_quality"] = new_quality

     
        read.seq = read.seq.reverse_complement()
        read.letter_annotations["phred_quality"] = read.letter_annotations["phred_quality"][::-1]


        SeqIO.write(read, output_file_handle, "fastq")
