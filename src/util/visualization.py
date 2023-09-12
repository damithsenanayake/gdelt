import matplotlib.pyplot as plt
from umap import UMAP


def visualize_graph(adj_matrix, node_list, nodelist_order):
    dist_mat = adj_matrix

    # coo_mat = coo_matrix(adj_matrix)

    nonzero_coords = adj_matrix.nonzero()

    layout = UMAP(metric='precomputed').fit_transform(1-dist_mat.toarray())

    plt.scatter(layout.T[0], layout.T[1], s = 1)

    for i in range(len(node_list)):
        fd = {'fontsize':18 if node_list[i] == 'Anthony Albanese' else 10}
        plt.text(layout[nodelist_order[i]][0], layout[nodelist_order[i]][1], node_list[i], fontdict= fd)

    for k in range(len(nonzero_coords[0])):
        plt.plot([layout[nonzero_coords[0][k]][0],layout[nonzero_coords[1][k]][0]], [layout[nonzero_coords[0][k]][1], layout[nonzero_coords[1][k]][1]], c = 'black', linewidth=adj_matrix[nonzero_coords[0][k], nonzero_coords[1][k]])
    plt.show()
