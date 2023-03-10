usuarios = {1,5,76,34,52,13,17}
print(len(usuarios))


usuarios.add(13)
print(len(usuarios))


usuarios = frozenset(usuarios)
print(usuarios)

print(type(usuarios))