with open("0067_triangle.txt", "r") as f:
    data = f.readlines()
data = [[int(x) for x in d.split()] for d in data]

for i in range(len(data)-2, 0, -1):
    for j in range(len(data[i])):
        data[i][j] += max(data[i+1][j], data[i+1][j+1])

print(data[0][0] + max(data[1][0], data[1][1]))
