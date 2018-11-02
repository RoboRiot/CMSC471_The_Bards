new_dict = dict()

keys = [1001]
movies = [1001]

for i in range(0, 1000):
    keys.append(i)
    movies.append(chr(i%256) + "")


for i in range(0,1000):
    new_dict[keys[i]] = movies[i]

print(new_dict)
