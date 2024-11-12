from codecarbon import track_emissions

@track_emissions()
# Penjumlahan matriks
def add(m1, m2):
    Nrow = len(m1)  # Jumlah baris
    Ncol = len(m1[0])  # Jumlah kolom
    m3 = [[0 for i in range(Ncol)] for j in range(Nrow)]
    # Matriks hasil jumlah
    for i in range(Nrow):
        for j in range(Ncol):
            m3[i][j] = m1[i][j] + m2[i][j]
    return m3

# Pengurangan matriks
def subs(m1, m2):
    Nrow = len(m1)  # Jumlah baris
    Ncol = len(m1[0])  # Jumlah kolom
    m3 = [[0 for i in range(Ncol)] for j in range(Nrow)]
    # Matriks hasil pengurangan
    for i in range(Nrow):
        for j in range(Ncol):
            m3[i][j] = m1[i][j] - m2[i][j]
    return m3

# Perkalian matriks dengan matriks
def matProd(m1, m2):
    Nrow_1 = len(m1)
    Ncol_1 = len(m1[0])
    Nrow_2 = len(m2)
    Ncol_2 = len(m2[0])
    # Pastikan Ncol_1 == Nrow_2 dahulu
    if Ncol_1 != Nrow_2:
        raise ValueError("Jumlah kolom matriks pertama harus sama dengan jumlah baris matriks kedua")
    m3 = [[0 for i in range(Ncol_2)] for j in range(Nrow_1)]
    for i in range(Nrow_1):
        for j in range(Ncol_2):
            for k in range(Ncol_1):
                m3[i][j] += m1[i][k] * m2[k][j]
    return m3

# Perkalian titik (dot product)
def dotProd(v1, v2):
    Ndim = len(v1)
    return sum(v1[i] * v2[i] for i in range(Ndim))

# Perkalian silang (cross product)
def croProd(v1, v2):
    if len(v1) != 3 or len(v2) != 3:
        raise ValueError("Cross product hanya bisa untuk vektor 3 dimensi")
    v3 = [0, 0, 0]
    v3[0] = v1[1] * v2[2] - v1[2] * v2[1]
    v3[1] = v1[2] * v2[0] - v1[0] * v2[2]
    v3[2] = v1[0] * v2[1] - v1[1] * v2[0]
    return v3

# Contoh penggunaan fungsi
if __name__ == "__main__":
    # Contoh matriks
    m1 = [[1, 2], [3, 4]]
    m2 = [[5, 6], [7, 8]]
    print("Penjumlahan Matriks:", add(m1, m2))
    print("Pengurangan Matriks:", subs(m1, m2))
    
    # Contoh perkalian matriks
    m3 = [[1, 2, 3], [4, 5, 6]]
    m4 = [[7, 8], [9, 10], [11, 12]]
    print("Perkalian Matriks:", matProd(m3, m4))
    
    # Contoh dot product
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    print("Dot Product:", dotProd(v1, v2))
    
    # Contoh cross product
    print("Cross Product:", croProd(v1, v2))