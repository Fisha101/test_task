

# Bioinformatics Test Tasks

Solutions for three bioinformatics test tasks.

## Task 1 — BAM filtering with pysam

**Task:**  
Write a Python function that:
1. Finds alignments where soft-clipped nucleotides follow hard-clipped nucleotides or hard-clipped nucleotides follow soft-clipped nucleotides, producing CIGAR strings such as `4H10S100M`, `3S103M9S6H`, and similar.
2. Writes the selected alignments to a BAM file.

**Module:** `pysam`  
**Solution:** [task1_bam_filter.py](task1_bam_filter.py)

## Task 2 — FASTQ trimming with Biopython

**Task:**  
Write a Python function that:
1. Reads reads from a FASTQ file.
2. Trims reads from both ends if the average sequencing quality in a sliding window of 5 nucleotides with a step of 2 nucleotides is below 25.
3. Writes the reverse-complement sequence of the trimmed read to a FASTQ file.

**Module:** `Biopython`  
**Solution:** [task2_fastq_trim.py](task2_fastq_trim.py)

## Task 3 — BED interval merging with pandas

**Task:**  
Write a Python function that:
1. Reads a BED file.
2. Merges intervals that overlap or are directly adjacent without a gap.
3. Writes the resulting intervals to a BED file.

## Test Data

Example input files are provided in the `test_data/` folder:
- `test.bed`
- `test.fastq`
- `test_small.bam`
**Module:** `pandas`  
**Solution:** [task3_bed_merge.py](task3_bed_merge.py)
