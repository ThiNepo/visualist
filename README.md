# Visualist

This is a very simple lilbrary to visualize lists in Python. 

It was created mainly to support the creation of tutoriais for [Neps Academy](https://neps.academy/) (amazing website :D).

### Usage

The minimal example is shown below. 

```python
from visualist import draw_list

img = draw_list([1, 2, -4, 2], [2])
img.show()
```

The result of this code would be

![example](https://neps.academy/image/374.png)

Showing a list [1, 2, -4, 2] and highlighting the index 2.

#### Building the library

To build the library you need the **wheel** module:

```
pip install wheel
```

and run the following command:

```
python setup.py sdist bdist_wheel
```
