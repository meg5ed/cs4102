# Mary Graham (meg5ed)
# CS 4102 - Algorithms- S'18- Nate Brunelle
# HW5 Due Monday April 2, 2018 at 11PM Via Collab 
# Sources: Introduction to Algorithms 3rd edition Cormen et al. 
# Dynamic Programming CLRS Chapter 15 and memoized matrix (the grid) chain pg. 388
# Finding the longest path in grid aka drainage basin in a city. 
# Return size of list aka the count of the longest path in a city. 



def longest_drainage_run(grid):

    # memoize is taught in chapter 15 of he recommended textbook at 
    def memoize(i, j):


        # cuts out having to look at base case by using double negative
        # the memoize function maintains an entry in my list and recurses through until you find the longest path
        if loc[i][j] != None:

            curLoc = grid[i][j]

            #looking at the locations around current location
            aboveLoc = 0
            if(i - 1 >= 0):
                if(curLoc < grid[i-1][j]):
                    aboveLoc = memoize(i-1, j)

            belowLoc = 0
            if(i + 1 < len(grid)):
                if(curLoc < grid[i+1][j]):
                    belowLoc = memoize(i+1, j)
            
            leftOfLoc = 0
            if( j-1 >= 0):
                if(curLoc < grid[i][j-1]):
                    leftOfLoc = memoize(i, j-1)


            rightofLoc = 0
            if( j+1 < len(grid[i])):
                if(curLoc < grid[i][j+1]):
                    rightofLoc = memoize(i, j+1)

            loc[i][j] = max(aboveLoc, belowLoc, leftOfLoc, rightofLoc)+1

        return loc[i][j]

    loc=[] 

    # looking through columns to look at location and where the next smallest difference int is to make a path
    for i in range(0, len(grid)):
        loc.append([0 for x in range(0, len(grid[0]))])
        

    # looking through again by using the memoize function as described above
    for i in range(0,len(loc[i])):
        for j in range(0,len(loc[i])):
            memoize(i,j)

    # returns the max num of the longest path in grid
    return max(loc[x][y] for x in range(len(grid)) for y in range(len(grid[0])))



def main():

    f = open('map.txt', 'r')
    outputList = []
    for i in range(int(f.readline())):
        lsstInput = f.readline().split()
        stCity = lsstInput[0]  # city list index begins
        numRows = int(lsstInput[1]) # rows index begins
        numCols = int(lsstInput[2]) # cols index begins
        grid = []  
        for row in range(numRows):
            grid.append(list(map(lambda st: int(st), f.readline().split())))
        var = longest_drainage_run(grid)
        outputList.append([stCity, var])
    for row in range(0, len(outputList)):
        print(outputList[row][0] + ": " + str(outputList[row][1]))


if __name__=="__main__":
    main()
