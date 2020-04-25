# Visualist

This is a very simple library to visualize lists in Python. 

It was created mainly to support the creation of tutorials for [Neps Academy](https://neps.academy/) (amazing website :D).

### Install

```
pip install visualist
```

### Usage

The minimal example is shown below. It supposes that we want to create an image 640x180 pixels from the list [1, 2, -4, 2, -2, 5] and highlight the indexes [2, 4].

```python
from visualist import Visualist

visualist = Visualist((640, 180))

img = visualist.img_from_list([1, 2, -4, 2, -2, 5], [2, 4])

img.show()
```

The result of this code would be

![example](https://neps.academy/image/375.png)

If you want to save the image change `img.show()` to `img.save('my_dear_list.png')`.

#### Building the library

To build the library you need the **wheel** module:

```
pip install wheel
```

and run the following command:

```
python setup.py sdist bdist_wheel
```
