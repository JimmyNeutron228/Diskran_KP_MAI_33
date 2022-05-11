def main():
    print("Введите количество вершин графа: ", end="")
    node_quantity = int(input())
    print("Введите количество ребер в графе: ", end="")
    edge_quantity = int(input())
    adjacency_matrix = [[0] * node_quantity for i in range(node_quantity)]
    print("Введите {} ребер в формате: <исходящая вершина> <входящая вершина>. "
          "(Без скобок. Номера вершин начинаются с 1)".format(edge_quantity))
    for i in range(edge_quantity):
        out_node, in_node = int(input()), int(input())
        out_node -= 1
        in_node -= 1
        adjacency_matrix[out_node][in_node] = 1


print("hello, git")

if __name__ == "__main__":
    main()
