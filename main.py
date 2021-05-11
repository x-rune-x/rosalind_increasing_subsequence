def increasing_subsequence(permutation):
    subsequences = []
    for i in range(len(permutation)):
        for j in range(len(permutation)-1, i, -1):
            subsequences.append([permutation[i]] + permutation[j:])
            for k in range(j-1, i, -1):
                subsequences.append([permutation[i]] + permutation[k:j])

    for x in range(len(subsequences)):
        print(x)
        sub = subsequences[x]
        print(sub)
        for pos in range(len(sub)-1):
            if sub[pos] > sub[pos+1]:
                subsequences[x] = ''

    return subsequences


f = increasing_subsequence([9, 1, 6, 2, 5, 7, 4, 8, 3])
print(f)
