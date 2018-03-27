#!/usr/local/bin/python3

def fasta_summary(fasta):
    fasta = fasta.upper()
    g = fasta.count("G")
    c = fasta.count("C")
    a = fasta.count("A")
    t = fasta.count("T")
    total = sum([g,c,a,t])
    gc = int(sum([g,c])/float(total)*100)
    pur = int(sum([a,g])/float(total)*100)
    pyr = int(sum([c,t])/float(total)*100)
    
    return {"G":g,
            "C":c,
            "A":a,
            "T":t,
            "Purine":pur,
            "Pyrimidine":pyr,
            "GC Content":gc,
            "Length":total
        }
