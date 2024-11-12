from codecarbon import track_emissions

@track_emissions()
# Penjumlahan matriks
def add(m1, m2):
    return [[x + y for x, y in zip(row1, row2)] for row1, row2 in zip(m1, m2)]

# Pengurangan matriks
def subs(m1, m2):
    return [[x - y for x, y in zip(row1, row2)] for row1, row2 in zip(m1, m2)]

# Perkalian matriks dengan matriks
def matProd(m1, m2):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*m2)] for row in m1]

# Perkalian titik (dot product)
def dotProd(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

# Perkalian silang (cross product)
def croProd(v1, v2):
    if len(v1) != 3 or len(v2) != 3:
        raise ValueError("Cross product hanya bisa untuk vektor 3 dimensi")
    return [
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    ]

# Contoh penggunaan fungsi
if __name__ == "__main__":
    # Contoh matriks
    m1, m2 = [[1, 2], [3, 4]], [[5, 6], [7, 8]]
    print("Penjumlahan Matriks:", add(m1, m2))
    print("Pengurangan Matriks:", subs(m1, m2))
    
    # Contoh perkalian matriks
    m3, m4 = [[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]]
    print("Perkalian Matriks:", matProd(m3, m4))
    
    # Contoh dot product
    v1, v2 = [1, 2, 3], [4, 5, 6]
    print("Dot Product:", dotProd(v1, v2))
    
    # Contoh cross product
    print("Cross Product:", croProd(v1, v2))