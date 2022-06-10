#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints information about python list object
 * @p: instance of python object type
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	long int length, count = 0;

	PyListObject *list;
	PyObject *item;

	length = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", length);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	while (count < length)
	{
		item = PyList_GetItem(p, count);
		printf("Element %ld: %s\n", count, Py_TYPE(item)->tp_name);
	        count += 1;
	}

}
