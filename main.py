INF_CONST = int(10e9 + 7)

def subtraction(a_matrix, b_matrix):
    if (len(b_matrix) != len(a_matrix) or len(a_matrix[0]) != len(b_matrix[0]) or len(a_matrix) != len(a_matrix[0])):
        print("Разные размерности у матриц. Исправьте ввод")
        return [[0]]
    n = len(a_matrix)
    for i in range(n):
        # Для того чтобы не использовать лишнюю память, результирующей матрицей будет a_matrix
        for j in range(n):
            a_matrix[i][j] = a_matrix[i][j] - b_matrix[i][j]
    return a_matrix


def transposition(a_matrix):
    if (len(a_matrix) != len(a_matrix[0])):
        print("Разные размерности у матриц. Исправьте ввод")
        return [[0]]
    trans_matrix = a_matrix
    n = len(a_matrix)
    for i in range(n):
        for j in range(n):
            trans_matrix[j][i] = a_matrix[i][j]
    return trans_matrix


def main():
    print("Введите количество вершин графа: ", end="")
    node_quantity = int(input())
    print("Введите количество ребер в графе: ", end="")
    edge_quantity = int(input())
    adjacency_matrix = [[0] * node_quantity for i in range(node_quantity)]
    print("Введите {} ребер в формате: <исходящая вершина> <входящая вершина> <вес вершины>."
          "(Без скобок. Номера вершин начинаются с 1)".format(edge_quantity))
    for i in range(edge_quantity):
        out_node, in_node, cost = int(input()), int(input()), int(input())
        out_node -= 1
        in_node -= 1
        adjacency_matrix[out_node][in_node] = cost
    L_matrix = subtraction(adjacency_matrix, transposition(adjacency_matrix))
    C_matrix = [[0] * node_quantity for i in range(node_quantity)]
    for i in range(edge_quantity):
        for j in range(node_quantity):
            C_matrix[i][j] = L_matrix[i][j]
            if C_matrix[i][j] <= 0:
                C_matrix[i][j] = INF_CONST



if __name__ == "__main__":
    main()
