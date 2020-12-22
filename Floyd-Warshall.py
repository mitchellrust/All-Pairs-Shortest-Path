from tabulate import tabulate

inf = float('inf') # represents infinity as an integer

# W is weight matrix for a graph G<V,E>
W = [
    [0, 2.2, inf, inf, 3.2, inf, inf, inf, inf, inf, inf],
    [2.2, 0, 1.1, inf, inf, inf, inf, inf, inf, inf, inf],
    [inf, 1.1, 0, 4.1, inf, inf, inf, inf, inf, inf, inf],
    [inf, inf, 4.1, 0, 6.0, inf, inf, inf, inf, inf, inf],
    [3.2, inf, inf, 6.0, 0, 4.1, 1.4, inf, inf, inf, inf],
    [inf, inf, inf, inf, 4.1, 0, 3.1, 2.3, inf, inf, inf],
    [inf, inf, inf, inf, 1.4, 4.1, 0, inf, 3.4, inf, inf],
    [inf, inf, inf, inf, inf, 2.3, inf, 0, 3.4, inf, inf],
    [inf, inf, inf, inf, inf, inf, 3.4, 4.4, 0, 2.3, 6.3],
    [inf, inf, inf, inf, inf, inf, inf, inf, 2.3, 0, 4.3],
    [inf, inf, inf, inf, inf, inf, inf, inf, 6.3, 4.3, 0]
]

# Map node names to indexes for printing
name_mapping = [
    "Altair IV",
    "Londinium",
    "Remulak",
    "Omicron Persei 8",
    "Thermia",
    "Vulcan",
    "Irk",
    "Endor",
    "Minbar",
    "Druidia",
    "Gallifrey"
]


# Create a new n by n matrix
def new_matrix(n):
    d = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(None)
        d.append(row)
    return d


# Print a matrix to stdout
def print_matrix(matrix):
    new_matrix = []
    for index, row in enumerate(matrix):
        copy = row.copy()
        copy.insert(0, name_mapping[index])
        new_matrix.append(copy)
    print(tabulate(new_matrix, headers=name_mapping))


def floyd_warshall(weight_matrix):
    n = len(weight_matrix)  # number of vertices in graph
    D = []                  # initialize empty array that will hold all new matricies
    d = weight_matrix       # Setup initial matrix
    D.append(d)

    print("Initial Setup - d0:")
    print_matrix(d)

    prev_d = d
    for k in range(n):
        d = new_matrix(n)
        for i in range(n):
            for j in range (n):
                try:
                    if i == j:
                        d[i][j] = 0
                    else:
                        if prev_d[i][j] <= prev_d[i][k] + prev_d[k][j]:
                            d[i][j] = prev_d[i][j]
                        else:
                            d[i][j] = prev_d[i][k] + prev_d[k][j]
                except Exception as e:
                    print(f"ERROR: {e}")
                    print(f"prev_d[i][k]: {prev_d[i][k]}")
                    print(f"prev_d[k][j]: {prev_d[k][j]}")
                    exit(-1)
        D.append(d)
        prev_d = d   # Get previous matrix for comparisons
        print("\nd" + str(k + 1) + ":")
        print_matrix(d)
    return D[n]

### MAIN
final_matrix = floyd_warshall(W)

print("\n\nSHORTEST PATHS:")
print_matrix(final_matrix)