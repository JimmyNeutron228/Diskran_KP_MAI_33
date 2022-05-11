INF_CONST = 10000000007


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
    S_matrix = [[0 for i in range(node_quantity)] for i in range(node_quantity)]
    for i in range(edge_quantity):
        out_node, in_node, cost = map(int, input().split())
        out_node -= 1
        in_node -= 1
        adjacency_matrix[out_node][in_node] = cost
        S_matrix[out_node][in_node] = 0 if cost == 0 else 1
    L_matrix = subtraction(adjacency_matrix, transposition(adjacency_matrix))
    C_matrix = [[0] * node_quantity for i in range(node_quantity)]
    for i in range(node_quantity):
        for j in range(node_quantity):
            C_matrix[i][j] = L_matrix[i][j]
            if C_matrix[i][j] <= 0:
                C_matrix[i][j] = INF_CONST

    t, s = find_t_and_s(S_matrix, len(S_matrix))
    v = [i for i in range(len(S_matrix))]
    spis_g = []
    while s != []:
        s, g, ans, v = find_s_P(S_matrix, s, v)
        spis_g += [[g, ans]]
    for i in range(len(spis_g)):
        print(i + 1, "-я компонента сильной связанности:", sep="")
        for j in spis_g[i][1]:
            print(j + 1, end=" ")
        print()
        for j in spis_g[i][0]:
            print(*j)


def disjunction(a, b):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1 or b[i][j] == 1:
                a[i][j] = 1
    return a


def conjunction(a, b):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i][j] == 0 or b[i][j] == 0:
                a[i][j] = 0
    return a


def transposition(a):
    n = len(a)
    c = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = a[j][i]
    return c


def multiplication(a, b):
    n = len(a)
    c = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            fl = 0
            for k in range(n):
                if a[i][k] == 1 and b[k][j] == 1:
                    fl = 1
                    break
            c[i][j] = fl
    return c


def find_t_and_s(r, n):
    e = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        e[i][i] = 1
    r_n = r
    t = disjunction(e, r)
    for i in range(2, n):
        r_n = multiplication(r, r_n)
        t = disjunction(t, r_n)
    s = conjunction(t, transposition(t))
    return t, s


def find_s_P(a, s, v):
    n = len(s)
    ans = []
    for i in range(n):
        if s[0][i] == 1:
            ans += [v[i]]
    k = len(ans)
    g = [[0 for i in range(k)] for j in range(k)]
    for i in range(k):
        for j in range(k):
            g[i][j] = a[ans[i]][ans[j]]
    for i in ans[::-1]:
        ind = -1
        for j in range(len(v) - 1, -1, -1):
            if v[j] == i:
                ind = j
                break
        if ind == 0:
            v = v[ind + 1:] if ind != len(v) - 1 else []
            s = s[ind + 1:] if ind != len(v) else []
            for j in range(len(s)):
                s[j] = s[j][ind + 1:] if ind != len(v) else []
        else:
            v = v[:ind] + (v[ind + 1:] if ind != len(v) - 1 else [])
            s = s[:ind] + (s[ind + 1:] if ind != len(v) else [])
            for j in range(len(s)):
                s[j] = s[j][:ind] + (s[j][ind + 1:] if ind != len(v) else [])
    return s, g, ans, v


if __name__ == "__main__":
    main()
