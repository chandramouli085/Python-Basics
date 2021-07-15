class SlowMatrix:

    ## The constructor
    # @param matrix A 2d Python list containing data
    def __init__(self, matrix):
        self.a=matrix

    ## Matrix multiplication
    # @param self SlowMatrix1
    # @param mat2 SlowMatrix2
    def __matmul__(self, mat2):
        arr=[]
        for i in range(len(self.a)):
            col=[]
            for j in range(len(mat2[0])):
                sum=0
                for x in range(len(mat2)):
                    sum=sum+(self.a[i][x] * mat2[x][j])
                    #print(self.a[i][x], mat2[x][j])
                col.append(sum)
            arr.append(col)
        return arr

    ## Element wise multiplication
    # @param self SlowMatrix1
    # @param mat2 SlowMatrix2
    def __mul__(self, mat2):
        arr=[]
        for i in range(len(mat2)):
            col=[]
            for j in range(len(mat2[0])):
                mult=self.a[i][j]*mat2[i][j]
                col.append(mult)
            arr.append(col)
        return arr

    ## Element wise addition
    # @param self SlowMatrix1
    # @param mat2 SlowMatrix2
    def __add__(self, mat2):
        arr=[]
        for i in range(len(mat2)):
            col=[]
            for j in range(len(mat2[0])):
                ad=self.a[i][j]+mat2[i][j]
                col.append(ad)
            arr.append(col)
        return arr

    ## Element wise subtraction
    # @param self SlowMatrix1
    # @param mat2 SlowMatrix2
    def __sub__(self, mat2):
        arr=[]
        for i in range(len(mat2)):
            col=[]
            for j in range(len(mat2[0])):
                ad=self.a[i][j]-mat2[i][j]
                col.append(ad)
            arr.append(col)
        return arr

    ## Equality operator
    # @param self SlowMatrix1
    # @param mat2 SlowMatrix2
    def __eq__(self, mat2):
        if self.a==mat2:
            return True
        else :
            return False

    ## Calculate transpose
    def transpose(self):
        arr=[]
        for i in range(len(self.a[0])):
            col=[]
            for j in range(len(self.a)):
                col.append(self.a[j][i])
            arr.append(col)
        return arr

    ## Creates a SlowMatrix of 1s
    # @param shape A python pair (row, col)
    def ones(shape):
        row,col=shape
        arr=[[1]*col]*row
        return arr[:]                

    ## Creates a SlowMatrix of 0s
    # @param shape A python pair (row, col)
    def zeros(shape):
        row,col=shape
        arr=[[0]*col]*row
        return arr[:]

    ## Returns i,jth element
    # @param key A python pair (i,j)
    def __getitem__(self, key):
        i,j=key
        return self.a[i][j]

    ## Sets i,jth element
    # @param key A python pair (i,j)
    # #param value Value to set
    def __setitem__(self, key, value):
        i,j=key
        self.a[i][j]=value

    ## Converts SlowMatrix to a Python string
    def __str__(self):
        res=str(self.a)
        return res
