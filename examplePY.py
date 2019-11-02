"""

Algo 1 python translation

"""

def SimpleAlgo1(records, dimensions, point):
    isBest = [True]*(records+1)
    for i in range(records):
        for j in range(records):
            worse_somewhere = False
            for k in range(dimensions):
                if point[i][k] < point[j][k]:
                    worse_somewhere = True
            not_better = True
            for k in range(dimensions):
                if point[i][k] > point[j][k]:
                    not_better = False
            if worse_somewhere and not_better:
                isBest[i] = False

    # Count the number of points in pareto frontier
    count = 0
    for i in range(records):
        if isBest[i]:
            count += 1

    return count

"""

# Algo 2 python translation

"""

def SimpleAlgo2(records, dimensions, point):
    isBest = [True]*(records + 10)
    for i in range(records):
        for j in range(records):
            if isBest[i]:
                worse_somewhere = False
                for k in range(dimensions):
                    if point[i][k] < point[j][k]:
                            worse_somewhere = True
                not_better = True
                for k in range(dimensions):
                    if point[i][k] > point[j][k]:
                        not_better = False
                if worse_somewhere and not_better:
                    isBest[i] = False

        # Count the number of points in pareto frontier
        count = 0
        for i in range(records):
            if isBest[i]:
                count += 1

        return count