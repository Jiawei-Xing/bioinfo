k = 12
string = 'GGAGCGGAGCACCCCTTCACTTCTTATATCCATTAGAATTCGGCGGCTAGGCGTGAAGAGGTCCGGCTTAATACCTTGGGTACGATCCAATACTCCAATGTACTTGCTTGGGGCTACGATGTGCGGCAAGGTTTCTCACAGTATAACTAACTCGTTAAATTAATGCCCGGTTTTCCTTATGCTCAGTTGTGCTTGTTGTCTTCCGGGTTGTATGGAGACGGCTTTCCCTTTGTATCCTGGGCTAACCTTCTAGGACTACGTGCGCCGCCGCATTCTGAGGCTACCTGTTTGTCAACGATCCTGGGTCGCGGTGTGTTACTTTTCTTAAATACAAACCTGCGTGGGATTTAATACAGAGCATACCCCCAAGCGTAGACAGGTTTGGTCCATCAAAAATCTAATCCGCCTCGGGAATACGAGTTCGTATTAGTTCTCCCCCTGCTCGTAGGTTACGTTCCAGACTATTACCTAAAATGTACTACACCGTGTAATTACGTCTCCTAGAGTGACTCGCATAAGTGTTCGGATCGGGCTATCTAGTTTTAACAATCGATGCGCAGATCCAGAAACGGCCTACAGGACCCATTATTTACACACGTGTCACGGCCCTTATAAATGCCGTCCCTCCTTACCAGAAGCTTTTGCTCAAAATATCGAAGACGGTAGATGCGCGCCCCGCGGCTCCATATCCTGCAAGCTTTCTTTGGGCAAATTATATGTGGTACTATGTTGACAATCACGTACGAAATTCTGAAAAATTTAATATTCCAATTGGCGTATTTCGGGTACACTGTCGCACTGTCTGTCTTCCCGCCATCTGCACATGCACAGATGTTATGACTACTTAGTTAATGATCGGAAGCGTCGGCGACCGAACTTCGCGCTTCTCGATGCCGTGTAGTTACTGATCACCCATGTTGGTGCGGCAGCGTGTAGTTATCGACTTGAGGCCCCACACGCATCCACCGGCTGGTTTATAATCAGAGAAACACCTTAGTGTGATATACTTCGCCCTAAATCAGGTGACGCCGCCCGCTTTCTTTCCATCGCATACGAGGTGTCTTGACCCGTTTTGGTGCTCCATAAGGGTTCCTGCCATTTGTCGCTCGATCTATGTATCACCAGCATAATCGATCGATTGAGATCTGAAATTTCCGGACACACGTTCCGGTGGCTACCCAATCGCTCCTCTTCCTACTGGTAACGTAATTCATAAGACGTAAGGGTCATGGGTCAGCCGGGGTACGTAGTTTGAAGTCCAAGCAACAAACACTGAGGAGCACGTTAAATCTTCGGTTCGCAATGCAAACGGGATATGGACCACGAAGACCTTACACTTCGATTAAGGTGTGCCAGGAGCGAAACTCTTGTCTGTTGAACAATCGTGTCCGTTTCTCCGTAATGTCGGAAGCGTAACACACGAGTTACTACAAGGGGAGAGAGTGTATGCCGGGAACCAACGATGCTTTGAGACGAGGATTACCTATAAGGGTTCCGTAGTATCATAGTTACCAGTGTTGAGTATGGGACGAATGATTGGCGCGGGCTTTATCGTAACACGGATGACCTTTAGCATCATGCGCCTAGCAAAGATAGGGTTACACACAGTAAACAGGGTAGATGCTTATCCCAGTAGAACGTTGTGACCGTCCACCTAGTCGCGGATGATTTCCTTCCGCTTCCTCAGCGAATAACGTTTGAGTGGGGCCGCAGGTATGCAGAGCTGGCCTGAGTCGCACACTGCAACTCTGCTCATACATCACCCCAGAACAGCTTAGAATGCAAGGATCTAGTAACTATTCACACGAAAACGTGCATGAACCCTGATCAGCCTATTCATACGTATAGGTAGCTGCTCGTCTCATCAGCGCGGCCCCGCTGTTACTCTGGCGATCTATATAGAGTCCAGGTTCTGGCTAGTCATTTACAGACGTCTTCTTGGATCTCTTTAAGTTCACAAGGTACAGAGGTGTATGACGGTGATTACGTTTACTTGTGGA'

graph={}
for i in range(len(string)-k+1):
    m = string[i:i+k-1]
    if m in graph:
        graph[m].append(string[i+1:i+k])
    else:
        graph[m] = [string[i+1:i+k]]

for key, value in graph.items():
    print(key + " -> " + ','.join(value))
