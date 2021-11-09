
n=5

#* * * * *
#* * * * *
#* * * * *
#* * * * *
#* * * * *
def rectangl(n):
    for row in range(n):
        for col in range(n):
            print("*",end=" ")

        print()

#--->column
#|   *
#|   * *
#|   * * *
#|   * * * *
#row * * * * *
def Etriangle(n):
    for row in range(n+1):
        for col in range(row):
            print("*",end=" ")
        #when the one row is printed newline
        print()

#* * * * * *
#* * * * *
#* * * *
#* * *
#* *
#*
def updowntriangle(n):
    for row in range(n):
        for col in range(n-row): #(row,n)
            print("*",end=" ")

        print()




def diamond(n):
    for row in range(1, 2*n):
        total_column_in_row = 2*n-row if row > n else row

        for space in range(n-total_column_in_row):
            print(end=" ")
        for col in range(total_column_in_row):
            print("*",end=" ")

        print()


#diamond(5)

def triangle(n):
    for row in range(1, 2*n):
        total_column_in_row = 2*n-row if row > n else row

        for space in range(n-total_column_in_row):
            print(end="")
        for col in range(total_column_in_row):
            print("*", end=" ")

        print()

#triangle(5)

def equilaterealtriangle(n):
    for row in range(n):
        for space in range(n-row+1):
            print(end=" ")
        for col in range(row+1):
            print("*", end=" ")

        print()

#equilaterealtriangle(5)

def spacetriangle(n):
    for row in range(n):
        for space in range(n-row):
            print(end="  ")
        for col in range(row+1):
            print("*", end=" ")
        print()

spacetriangle(5)