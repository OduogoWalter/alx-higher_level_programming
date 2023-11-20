#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <floatobject.h>
#include <listobject.h>
#include <bytesobject.h>

/**
 * print_python_list - Print information about a Python list
 * @p: Pointer to a Python object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	printf("[*] Python list info\n[*] Size of the Python List = %ld\n"
			"[*] Allocated = %ld\n", size, ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Print information about a Python bytes object
 * @p: Pointer to a Python object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("[.] bytes object info\n  size: %ld\n  trying string: %s\n",
			size, str);
	printf("  first %ld bytes: ", (size < 10) ? size : 10);

	 for (i = 0; i < 10 && i < size; i++)
		 printf("%02hhx ", str[i]);

	 printf("\n");
}

/**
 * print_python_float - Print information about a Python float object
 * @p: Pointer to a Python object
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
		return;
	}

	printf("[.] float object info\n  value: %f\n",
			((PyFloatObject *)p)->ob_fval);
}
