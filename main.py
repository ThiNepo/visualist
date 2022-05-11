from pygments import highlight
from visualist import Visualist

visualist = Visualist()

# 1 List
img = visualist.img_from_list([1, 2, -4, 2, -2, 5], highlight_indexes=[2, 4])
img.show()

# N Lists
img = visualist.img_from_lists([[1, 2, -4, 2, -2, 5], [1, 2, 3, 4]], highlight_indexes=[[2, 4], [1]], show_indexes=False)
img.show()

# Matrix
matrix=[".o...", ".#...", ".....", ".....", ".....", "..#..", "....."]

img = visualist.img_from_matrix(matrix, [[] for i in range(len(matrix))], show_indexes=False)
img.show()
