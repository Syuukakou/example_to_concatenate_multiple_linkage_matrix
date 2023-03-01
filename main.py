from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
import matplotlib.pyplot as plt

# Create samples and linkage matrix
x1 = [[i] for i in range(5)]
x1z = linkage(x1, method="ward")
x1_merged_ids = [i[:2].tolist() for i in x1z]
x1_merged_ids = [item for sublist in x1_merged_ids for item in sublist]
x1_merged_ids = list(set(x1_merged_ids) - set(list(range(20))))

x2 = [[i] for i in range(0, 5)]
x2z = linkage(x2, method="ward")
x2_merged_ids = [i[:2] for i in x2z]
x2_merged_ids = [item for sublist in x2_merged_ids for item in sublist]
x2_merged_ids = list(set(x2_merged_ids) - set(list(range(75))))

x3 = [[i] for i in range(0, 10)]
x3z = linkage(x3, method="ward")
x3_merged_ids = [i[:2] for i in x3z]
x3_merged_ids = [item for sublist in x3_merged_ids for item in sublist]
x3_merged_ids = list(set(x3_merged_ids) - set(list(range(40))))

# Get count of all samples
total_samples = len(x1) + len(x2) + len(x3)


for row in x1z:
    if row[0] >= len(x1):
        row[0] = row[0] - len(x1) + total_samples
        # row[0] += total_samples
    if row[1] >= len(x1):
        row[1] = row[1] - len(x1) + total_samples
print(x1z)
x1z_max_id = np.amax(np.asarray([i[:2] for i in x1z])) + 1
print(x1z_max_id)
x1z_max_dist = np.amax(np.asarray([i[2] for i in x1z])) + 1
print(x1z_max_dist)

# print(x2z)

for row in x2z:
    if row[0] < len(x2):
        row[0] += len(x1)
    else:
        row[0] = row[0] - len(x2) + total_samples + len(x1) - 1

    if row[1] < len(x2):
        row[1] += len(x1)
    else:
        row[1] = row[1] - len(x2) + total_samples + len(x1) - 1
print(x2z)
x2z_max_id = np.amax(np.asarray([i[:2] for i in x2z])) + 1
print(x2z_max_id)
x2z_max_dist = np.amax(np.asarray([i[2] for i in x2z])) + 1

# print(x3z)
for row in x3z:
    if row[0] < len(x3):
        row[0] = row[0] + len(x1) + len(x2)
    else:
        row[0] = row[0] - len(x3) + total_samples + len(x1) - 1 + len(x2) - 1
    if row[1] < len(x3):
        row[1] = row[1] + len(x1) + len(x2)
    else:
        row[1] = row[1] - len(x3) + total_samples + len(x1) - 1 + len(x2) - 1
print(x3z)
x3z_max_id = np.amax(np.asarray([i[:2] for i in x3z])) + 1
print(x3z_max_id)
x3z_max_dist = np.amax(np.asarray([i[2] for i in x3z])) + 1

x1_x2 = [x1z_max_id, x2z_max_id, max(x1z_max_dist, x2z_max_dist, x3z_max_dist) + 10, len(x1) + len(x2)]
x1_x2_x3 = [x3z_max_id, x3z_max_id + 1, max(x1z_max_dist, x2z_max_dist, x3z_max_dist) + 20, len(x1) + len(x2) + len(x3)]
combine = np.asarray([x1_x2, x1_x2_x3])

final_linkage_matrix = np.concatenate([x1z, x2z, x3z, combine])
print(final_linkage_matrix)

fig, ax = plt.subplots(figsize=(10, 8))

dendrogram(
    final_linkage_matrix,
    ax=ax
)
plt.show()


