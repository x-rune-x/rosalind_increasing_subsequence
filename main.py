def increasing_subsequence(permutation):
    subsequences = []
    for x in range(len(permutation)):
        subsequences.append([[permutation[x]]])
    for i in range(len(permutation)):
        for j in range(i):
            for sub in subsequences[j]:
                if permutation[i] > sub[-1]:
                    subsequences[j].append(sub + [permutation[i]])
    increasing_subs = []
    for long_sub in subsequences:
        increasing_subs.append(max(long_sub, key=len))
    return max(increasing_subs, key=len)


def decreasing_subsequence(permutation):
    subsequences = []
    for x in range(len(permutation)):
        subsequences.append([[permutation[x]]])
    for i in range(len(permutation)):
        for j in range(i):
            for sub in subsequences[j]:
                if permutation[i] < sub[-1]:
                    subsequences[j].append(sub + [permutation[i]])
    decreasing_subs = []
    for long_sub in subsequences:
        decreasing_subs.append(max(long_sub, key=len))
    return max(decreasing_subs, key=len)


def process_file(file_name):
    file = open(file_name, 'r')
    file.readline()
    permutation = file.read()
    file.close()

    permutation_list = permutation.split()

    print(permutation_list)

    increasing_sub = increasing_subsequence(permutation_list)
    decreasing_sub = decreasing_subsequence(permutation_list)

    string_increasing = ' '.join(increasing_sub)
    string_decreasing = ' '.join(decreasing_sub)

    output_file = open('solution.txt', 'w')
    output_file.write(string_increasing + '\n')
    output_file.write(string_decreasing)
    output_file.close()


process_file('rosalind_lgis.txt')
