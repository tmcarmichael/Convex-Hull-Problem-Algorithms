import random
import time
import timeit

class Solution:
# Use: Find all interesting points in r records and d dimensions
# Methods: 
#   NaiveAlg1           Initial brute force approach
#   NaiveAlg2           Minor optimization
#   RandomizedAlg3      Randomized Approach
#   RandomizedAlg4      Randomized Approach with speedup filter

    def __init__(self, records, dimensions, point):
    # Constructor for loading records, dimensions, and points
    # NOTE: Each new file used requires recalling solution constructor with new records/dimensions
        self.records = records
        self.dimensions = dimensions
        self.point = point

    """

    NaiveAlg1 and NaiveAlg2 below are ported from C++ instructions

    """

    # The following function is analogous to C++ SimpleAlgo1
    def NaiveAlg1(self):
        # Initialize records array
        pareto = [True]*(records + 1)
        for i in range(records):
            for j in range(records):
                lower = False
                for k in range(dimensions):
                    if point[i][k] < point[j][k]:
                        lower = True
                higher = False
                for k in range(dimensions):
                    if point[i][k] > point[j][k]:
                        higher = True
                if lower and not higher:
                    pareto[i] = False

        # Count the number of points in pareto frontier
        count = 0
        for i in range(records):
            if pareto[i]:
                count += 1
        return count

    # The following function is analogous to C++ SimpleAlgo2
    def NaiveAlg2(self):
        # Initialize records array
        pareto = [True]*(records + 1)
        for i in range(records):
            for j in range(records):
                if pareto[i]:
                    lower = False
                    for k in range(dimensions):
                        if point[i][k] < point[j][k]:
                            lower = True
                    higher = False
                    for k in range(dimensions):
                        if point[i][k] > point[j][k]:
                            higher = True
                    if lower and not higher:
                        pareto[i] = False

        # Count the number of points in pareto frontier
        count = 0
        for i in range(records):
            if pareto[i]:
                count += 1
        return count

    """

    RandomizedAlg3 and RandomizedAlg4 below are two functions with improvements

    """

    # The following function utilizes randomization and minor improvements to speedup pareto search
    def RandomizedAlg3(self):

        # RANDOMIZE: record order, dimensions order
        # 1) Randomize order of records
        random.shuffle(point)
        # 2) Randomize dimensions order
        dims = list(range(dimensions))
        random.shuffle(dims)

        # Solve pareto frontier in randomzied order
        pareto = [True]*(records + 1)
        for i in range(records):
            for j in range(records):
                lower, other_lower = False, True
                # dims is selecting in randomized order with each fx call
                # this handles some specific worst-case test cases
                for k in dims:
                    # point is also in randomized order to handle worst-case test cases
                    if point[i][k] < point[j][k]:
                        lower = True
                    elif point[i][k] > point[j][k]:
                        other_lower = False
                if lower and other_lower:
                    pareto[i] = False
        # Count the number of points in pareto frontier
        return sum([1 if pareto[i] else 0 for i in range(records)])

    # This approach with utilize randomization demonstrated above and enhancements
    def RandomizedAlg4(self):
        # accumulator for number of valid points found
        count = 0

        # RANDOMIZE: record order, dimensions order
        # 1) Randomize order of records
        random.shuffle(point)
        # 2) Randomize dimensions order
        dims = list(range(dimensions))
        random.shuffle(dims)

        # while there is at least 2 points
        while len(point) > 0:
            row_index, higher = 1, 1
            current_point = point[0]
            # compare current_point 'point' to 'compare_point'
            while len(point) > 0 and row_index < len(point):
                compare_point = point[row_index]
                # check if compare_point is dominated by current_point
                # Note: dims holds shuffled order of dimensions to process checking against worst case
                if all([current_point[x] >= compare_point[x] for x in dims]):
                    point.remove(compare_point)
                    continue
                # check if current_point is dominated by compare_point
                # Note: dims holds shuffled order of dimensions to process checking against worst case
                elif all([compare_point[x] >= current_point[x] for x in dims]):
                    higher = 0
                row_index += 1
            # increment counter if current_point is not dominated by another point
            count += higher
            point.remove(current_point)
        return count


if __name__ == "__main__":
    """

    Read Input

    """

    # Replace "TGen_Out.txt" with any testfile
    file = open("TGen_Out.txt", "r")
    header = file.readline().split()
    records, dimensions = int(header[0]), int(header[1])
    point = [None]*records
    #data_hash = dict()
    row = 0
    with file as f:
        for line in f:
            point[row] = map(int,line.split())
            #data_hash[row] = data[row]
            row += 1
    file.close()

    """

    Find Pareto Points

    """

    s = Solution(records, dimensions, point)
    # Method 1: Testing NaiveAlg1
    # print(s.NaiveAlg1())

    # timeit.timeit(s.NaiveAlg1())
    # timeit.timeit('s.NaiveAlg1()', setup='from __main__ import s', number=500)

    # Method 2: Testing NaiveAlg2
    # print(s.NaiveAlg2())

    # Method 3: Testing RandomizedAlg3
    # print(s.RandomizedAlg3())

    # Method 4: Testing RandomizedAlg3
    # print(s.RandomizedAlg4())







