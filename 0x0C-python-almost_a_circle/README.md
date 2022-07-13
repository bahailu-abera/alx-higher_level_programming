# python-almost_a_circle
## unit testing, serialization, deserialization, JSON, args and kwargs in Python.

Technologies<br>
Python Scripts are written with Python 3.4.3<br>
Tested on Ubuntu 20.04 LTS<br>

## Files
Inside models folder:

|Filename	        | Description                 |
------------------ | ------------------------------------------ |
|__init__.py	    | Script that converts the directory as a package |
| base.py	        | Base class of geometrical instances              |
|rectangle.py     |	Class that inherits attributes references from Base class
|square.py	      | Class that inherits attributes references from Square class

Each class contains public/private attibutes, class and static methods. Also, these class raise exceptions when is required.

### Inside tests/test_models folder:

|Filename     |	Description |
----------------- | --------------- |
| __init__.py	| Script that converts the directory as a package
| test_base.py |	Module that contains unittests to Base class
| test_rectangle.py | 	Module that contains unittests to Rectangle class
| test_square.py	  | Module that contains unittests to Square class
