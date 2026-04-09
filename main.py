#!/usr/bin/env python

#Resolución de una matriz de coeficientes por factorización QR

def main():
    from qr import qr
    from gram_schmidt import matrix_to_str

#Matriz ejemplo
    A = [[1, 1], [1, 0], [0, 1]]
    b = [2, 1, 1]

    Q, R = qr(A)

    print("Q:")
    print(matrix_to_str(Q))
    print("\nR:")
    print(matrix_to_str(R))

if __name__ == "__main__":
    main()
