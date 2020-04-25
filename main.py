from visualist import Visualist

visualist = Visualist()

# 1 List
img = visualist.img_from_list([1, 2, -4, 2, -2, 5], [2, 4])
img.show()

# N Lists
img = visualist.img_from_lists([[1, 2, -4, 2, -2, 5], [1, 2, 3, 4]], [[2, 4], [1]])
img.show()