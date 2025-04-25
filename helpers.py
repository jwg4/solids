from stl import mesh
import numpy as np

def make_mesh(data):
    co_mesh = mesh.Mesh(np.zeros(data.shape[0], dtype=mesh.Mesh.dtype))
    for i, v in enumerate(data):
        for j in range(3):
            co_mesh.vectors[i][j] = v[j]
    return co_mesh


def write_mesh(shape, scale, filename):
    data = np.array(shape)
    make_mesh(data * scale).save(filename)
