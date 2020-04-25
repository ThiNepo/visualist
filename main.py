from visualist import Visualist

visualist = Visualist((640, 180))

img = visualist.img_from_list([1, 2, -4, 2, -2, 5], [2, 4])

img.show()