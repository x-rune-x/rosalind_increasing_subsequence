def longest_subsequence(permutation, subsequences):
    if len(permutation) == 1:
        return permutation
    else:
        for i in range(len(permutation)):
            current_subsequence = [permutation[i]]
            for j in range(i+1, len(permutation)):
                if permutation[j] > current_subsequence[-1]:
                    current_subsequence.append(permutation[j])
                    longest_subsequence(permutation[j:], subsequences)
            subsequences.append(current_subsequence)
        return subsequences


print(longest_subsequence([8, 2, 1, 6, 5, 7, 4, 3, 9], []))
