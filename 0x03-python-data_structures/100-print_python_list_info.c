#include <Python.h>

/**
 * print_python_list_info - Prints some basic info about Python lists.
 * @p: A pointer to a Python object.
 */
void print_python_list_info(PyObject *p)
{
int size, alloc, i;
PyObject *item;

size = Py_SIZE(p);
alloc = ((PyListObject *)p)->allocated;

printf("[*] Size of the Python List = %d\n", size);
printf("[*] Allocated = %d\n", alloc);

for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
}
}
