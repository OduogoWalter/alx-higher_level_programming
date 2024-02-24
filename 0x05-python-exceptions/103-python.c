#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints Python list basic info
 * @p: Python object
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, alloc, i;
    PyObject *obj;

    size = PyList_Size(p);
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);

    for (i = 0; i < size; i++)
    {
        obj = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
        if (strcmp(Py_TYPE(obj)->tp_name, "bytes") == 0)
            print_python_bytes(obj);
        else if (strcmp(Py_TYPE(obj)->tp_name, "float") == 0)
            print_python_float(obj);
    }
}

/**
 * print_python_bytes - Prints Python bytes basic info
 * @p: Python object
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);

    printf("  first %ld bytes: ", size + 1 > 10 ? 10 : size + 1);
    for (i = 0; i < size + 1 && i < 10; i++)
    {
        printf("%02x ", str[i] & 0xff);
    }
    printf("\n");
}

/**
 * print_python_float - Prints Python float basic info
 * @p: Python object
 */
void print_python_float(PyObject *p)
{
    PyFloatObject *f = (PyFloatObject *)p;

    printf("[.] float object info\n");
    if (!PyFloat_Check(f))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    printf("  value: %f\n", f->ob_fval);
}
