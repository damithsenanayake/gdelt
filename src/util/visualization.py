import matplotlib.pyplot as plt
from umap import UMAP
import numpy as np

def draw_curve(p1, p2, width):
    a = (p2[1] - p1[1]) / (np.sinh(p2[0]) - np.sinh(p1[0]))
    b = p1[1] - a * np.sinh(p1[0])
    x = np.linspace(p1[0], p2[0], 100)
    y = a * np.sinh(x) + b

    plt.plot(x, y, linewidth = width, c = 'black')


def visualize_graph(adj_matrix, node_list, nodelist_order):
    dist_mat = adj_matrix

    # coo_mat = coo_matrix(adj_matrix)

    nonzero_coords = adj_matrix.nonzero()

    layout = UMAP(metric='precomputed', min_dist=0.8).fit_transform(1-dist_mat.toarray())

    plt.scatter(layout.T[0], layout.T[1], s = 0.001)

    for i in range(len(node_list)):
        noise_vector = np.random.random(2)*0.1
        fd = {'fontsize':18 if node_list[i] == 'Anthony Albanese' else 8}
        plt.text(layout[nodelist_order[i]][0] + noise_vector[0], layout[nodelist_order[i]][1]+noise_vector[1], node_list[i],
                 horizontalalignment = 'center', verticalalignment = 'center', fontdict= fd,  color = 'red' if node_list[i] == 'Anthony Albanese' else 'black')

    for k in range(len(nonzero_coords[0])):
        draw_curve(layout[nonzero_coords[0][k]], layout[nonzero_coords[1][k]], width = adj_matrix[nonzero_coords[0][k], nonzero_coords[1][k]])
        # plt.plot([layout[nonzero_coords[0][k]][0],layout[nonzero_coords[1][k]][0]], [layout[nonzero_coords[0][k]][1], layout[nonzero_coords[1][k]][1]], c = 'black', linewidth=adj_matrix[nonzero_coords[0][k], nonzero_coords[1][k]])
    plt.show()
