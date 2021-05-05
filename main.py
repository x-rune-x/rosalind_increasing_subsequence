def increasing_subsequence(permutation, subsequences):
    if len(permutation) == 1:
        return permutation
    else:
        for i in range(len(permutation)):
            larger_numbers = []
            for j in range(i+1, len(permutation)):
                if j > i:
                    larger_numbers.append(j)
                increasing_subsequence(larger_numbers, subsequences)
            subsequences.append(larger_numbers)
    return max(subsequences, key=len)


print(increasing_subsequence([9, 1, 6, 2, 5, 7, 4, 8, 3], []))
