#----------------------*CREATE FUNCTION TO RANDOM_ROW POINT*---------------#
# def randomPointRow():
#     global storeRowPoint
#     storeRowPoint = []
#     while len(storeRowPoint) != 3:
#         randomRowPoint = randrange(0, 4)
#         if randomRowPoint not in storeRowPoint:
#             storeRowPoint.append(randomRowPoint)
#     randomPointCol()
#----------------------*CREATE FUNCTION TO RANDOM_COL POINT*---------------#
# def randomPointCol():
#     global storeNumPoint
#     storeNumPoint = []
#     while len(storeNumPoint) !=3:
#         randNumPoint = randrange(1, 8)
#         if randNumPoint not in storeNumPoint:
#             storeNum.append(randNumPoint)
#     pointReplace()

#----------------------*CREATE FUNCTION TO INPUT POINT*--------------------#
# def pointReplace():
#     global Grid
#     for num in range(len(storeRowPoint)):
#         Grid[storeRowPoint[num]][storeNumPoint[num]] = 4
#     displayGrid()