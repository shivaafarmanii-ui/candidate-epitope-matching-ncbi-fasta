def count_epitopes_in_proteins(epitope_file, fasta_file, count_file):
    epitopes = []
    with open(epitope_file, "r") as f:
        for line in f:
            epitopes.append(line.strip().upper())

    proteins = [""]
    with open(fasta_file, "r") as f:
        for line in f:
            line = line.strip()

            if line.startswith(">"):
                if proteins[-1]:
                    proteins.append("")
            else:
                proteins[-1] += line.upper()

    if proteins[-1] == "":
        proteins.pop()

    results = []
    for epitope in epitopes:
        if not epitope:
            continue

        matches = [protein for protein in proteins if epitope in protein]
        count = len(matches)
        results.append(f"The epitope '{epitope}' was found in {count} protein(s).")

    with open(count_file, "w") as f:
        f.write("\n".join(results))

    print(f"Results have been saved to {count_file}.")


count_epitopes_in_proteins("epitope_file.txt", "L1.fasta", "results.txt")