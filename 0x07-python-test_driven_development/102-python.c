#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints Python string info
 * @p: PyObject string pointer
 */
void print_python_string(PyObject *p)
{
    const char *type;
    Py_ssize_t length;
    wchar_t *value;

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    if (PyUnicode_IS_COMPACT_ASCII(p))
        type = "compact ascii";
    else if (PyUnicode_IS_COMPACT(p))
        type = "compact unicode object";
    else
        type = "legacy string object";

    length = PyUnicode_GET_LENGTH(p);
    value = PyUnicode_AsWideCharString(p, &length);

    printf("  type: %s\n", type);
    printf("  length: %ld\n", length);
    printf("  value: %ls\n", value);

    PyMem_Free(value);
}
