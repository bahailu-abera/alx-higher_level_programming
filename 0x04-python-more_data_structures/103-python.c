#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - print some basic info about Python lists
 * @p: PyObject
 *
 *Return: void
 */
void print_python_list(PyObject *p)
{
	long int length, count;
	PyListObject *list;
	PyObject *obj;

	length = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", length);

	list = (PyListObject *)p;
	print("[*] Allocated = %ld\n", list->allocated);

	for (count = 0; count < length; count++)
	{
		obj = ((PyListObject *)p)->ob_item[count];
		print("Element %ld: %s\n", count, ((obj)->ob_type)->tp_name);

		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}

/**
 * print_python_bytes - print some basic info about python lists
 * @P: PyObject
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
}
