This study aimed to assess how widely candidate vaccine epitopes were conserved across HPV protein sequences collected from NCBI. This repository provides the HPV L1 analysis. For each candidate epitope, the Python script reports how many L1 protein records contain an exact match.
This repository contains a Python script that counts how many protein records in a FASTA file contain each query sequence as an exact match. Each matching record is counted once per query, even if the query occurs multiple times in that record.

## Files

- `count_epitope_matches.py` — Python script
- `L1.fasta` — HPV L1 protein records in FASTA format
- `epitope_file.txt` — Query sequences, one per line
- `results.txt` — Match counts for the L1 dataset
