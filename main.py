class Element:
    # Create objects that keep track of each element in the permutation and the position in should be in a subsequence.
    def __init__(self, value, position):
        self.value = value
        self.position = position


def longest_increasing_subsequence(lis_permutation):
    # First, go through the permutation and assign each element a number that describes its order in an increasing
    # subsequence.
    for i in range(len(lis_permutation)):
        for j in range(i):  # For each element in the list (i), check it against all preceding elements in the list (j).
            # Every time i is greater than j, increase its position value if its position value is also equal to or
            # smaller than j.
            # All elements start with the position value 1.
            if lis_permutation[i].value > lis_permutation[j].value and \
                    lis_permutation[i].position <= lis_permutation[j].position:
                lis_permutation[i].position = lis_permutation[j].position + 1

    max_position = 0  # Find the largest position value in the list. We can set this as the start of our lis, and also
    # use it to restrict our searching through the list since we know all the numbers we need must be downstream of it.
    lis = []
    for pos in lis_permutation:
        if pos.position > max_position:
            max_position = pos.position
            lis = [pos]
    final = lis[0]

    for position in lis_permutation[lis_permutation.index(final)::-1]:
        # Starting from the largest identified position, traverse back down the list and whenever the next position
        # value is encounter, add the item to the lis.
        if position.position == (lis[0].position - 1) and position.value < lis[0].value:
            lis.insert(0, position)

    string_list = []
    for item in lis:
        string_list.append(str(item.value))

    return string_list


def longest_decreasing_subsequence(dis_permutation):
    # The same as the LIS function but sorts elements in decreasing order.
    for i in range(len(dis_permutation)):
        for j in range(i):
            if dis_permutation[i].value < dis_permutation[j].value and \
                    dis_permutation[i].position <= dis_permutation[j].position:
                dis_permutation[i].position = dis_permutation[j].position + 1

    for x in dis_permutation:
        print(x.position)

    max_position = 0
    dis = []
    for pos in dis_permutation:
        if pos.position > max_position:
            max_position = pos.position
            dis = [pos]

    final = dis[0]

    for position in dis_permutation[dis_permutation.index(final)::-1]:
        if position.position == (dis[0].position - 1) and position.value > dis[0].value:
            dis.insert(0, position)

    string_list = []
    for item in dis:
        string_list.append(str(item.value))

    return string_list


def process_file(file_name):
    file = open(file_name, 'r')
    file.readline()  # The file provided by Rosalind has the length of the permutation (n) on the first line but this is
    # not necessary to solve the problem so I ignore it.
    permutation = file.read()
    file.close()

    permutation_list = permutation.split()  # Take string read from file and make a list.
    permutation_list_lis = []
    permutation_list_dis = []
    for i in range(len(permutation_list)):
        # Populate a list for LIS and DIS with each element of our permutation list and give each element a position
        # of 1.
        permutation_list_lis.append(Element(int(permutation_list[i]), 1))
        permutation_list_dis.append(Element(int(permutation_list[i]), 1))

    lis = longest_increasing_subsequence(permutation_list_lis)
    dis = longest_decreasing_subsequence(permutation_list_dis)

    # Convert lists back to string to make Rosalind happy.
    string_increasing = ' '.join(lis)
    string_decreasing = ' '.join(dis)
    print(string_increasing)
    print(string_decreasing)

    output_file = open('solution.txt', 'w')
    output_file.write(string_increasing)
    output_file.write('\n')
    output_file.write(string_decreasing)
    output_file.write('\n')
    output_file.close()


process_file('rosalind_lgis.txt')
