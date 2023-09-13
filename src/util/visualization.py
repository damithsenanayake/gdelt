import matplotlib.pyplot as plt
from umap import UMAP
import numpy as np
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go
# from scipy.sparse import coo_matrix

def draw_curve(p1, p2, width):
    a = (p2[1] - p1[1]) / (np.sinh(p2[0]) - np.sinh(p1[0]))
    b = p1[1] - a * np.sinh(p1[0])
    x = np.linspace(p1[0], p2[0], 100)
    y = a * np.sinh(x) + b

    plt.plot(x, y, linewidth = width, c = 'black')

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



# def visualize_graph(adj_matrix, node_list, nodelist_order):
#     dist_mat = adj_matrix
#
#     layout = UMAP(metric='precomputed', min_dist=0.8).fit_transform(1 - dist_mat.toarray())
#
#     df = pd.DataFrame({
#         'x': layout[:, 0],
#         'y': layout[:, 1],
#         'node_list': node_list[nodelist_order],
#         # 'point_size': [0.0001]*len(layout)
#     })
#     noise_vectors = np.random.random((len(node_list), 2)) * 0.1
#     df['x'] += noise_vectors[:, 0]
#     df['y'] += noise_vectors[:, 1]
#
#     fig = px.scatter(df, x='x', y='y', text='node_list',   title='UMAP Visualization of the Connectivity Graph')
#
#     # fig.update_traces(marker=dict(size=0.05,
#     #                               alpha = 0.2),
#     #                  selector=dict(mode='markers'))
#     edge_traces = []
#     for i, j, width in zip(*adj_matrix.nonzero(), adj_matrix.data):
#         edge_traces.append(
#             go.Scatter(x=[layout[i, 0], layout[j, 0]], y=[layout[i, 1], layout[j, 1]],
#                        mode='lines', line=dict(width=width, color=f'rgba(0, 0, 255, {max(1., 0.1 +width)})'), showlegend=False, ))
#
#     # Add edge traces to the figure
#     for trace in edge_traces:
#         fig.add_trace(trace)
#     # fig.update_traces(marker=dict(size=1), line=dict( color='black', opacity=0.5))
#     # Update layout properties
#     fig.update_layout(
#         xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
#         yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
#     )
#
#     # Show the plot
#     fig.show()
