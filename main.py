def longest_subsequence(start_position, permutation):
    subsequences = []
    if start_position == len(permutation):
        return subsequences
    else:
        for i in permutation:
            current_subsequence = [i]
            for j in range(start_position, len(permutation)):
                if permutation[j] > current_subsequence[-1]:
                    current_subsequence.append(permutation[j])
                    longest_subsequence(i, permutation)
            subsequences.append(current_subsequence)


print(longest_subsequence(0, [8, 2, 1, 6, 5, 7, 4, 3, 9]))
