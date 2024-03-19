#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, i;
    PyListObject *list;

    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    list = (PyListObject *)p;
    size = PyList_Size(p);

    for (i = 0; i < size; ++i)
    {
        printf("Element %ld: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
    }
}
