def luDecomposition(mat, n):
 
    lower = [[0 for x in range(n)]
             for y in range(n)]
    upper = [[0 for x in range(n)]
             for y in range(n)]
    
    # Dekomposisi Matriks LU (Bawah dan Atas)
    for i in range(n):
 
        # Upper (Atas)
        for k in range(i, n):
 
            # Penjumlahan dari L(i, j) * U(j, k)
            sum = 0
            for j in range(i):
                sum += (lower[i][j] * upper[j][k])
 
            # Mengevaluasi U(i, k)
            upper[i][k] = float(mat[i][k] - sum)
 
        # Lower (Bawah)
        for k in range(i, n):
            if (i == k):
                lower[i][i] = 1  # Diagonal = 1
            else:
 
                # Penjumlahan of L(k, j) * U(j, i)
                sum = 0
                for j in range(i):
                    sum += (lower[k][j] * upper[j][i])
 
                # Mengevaluasi L(k, i)
                lower[k][i] = float((mat[k][i] - sum) /
                                  upper[i][i])
 
    
    print("Lower\t\t\t\tUpper")
 
    # Hasil :
    for i in range(n):
        
        # Lower
        for j in range(n):
            print("%.2f" %  lower[i][j], end="\t")
        print("", end="\t")
 
        # Upper
        for j in range(n):
            print("%.2f" %  upper[i][j], end="\t")
        print("")


mat = [[1, 2, 3],
       [3, -1, 2],
       [4, -6, -4]]



luDecomposition(mat, 3) 
#luDecomposition(mat, 4)