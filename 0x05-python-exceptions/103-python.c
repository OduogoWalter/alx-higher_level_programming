#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - prints some basic info about Python lists
 * @p: pointer to PyObject
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;
	Py_ssize_t size, i;
	PyObject *element;

	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = var->ob_size;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
		if (strcmp(Py_TYPE(element)->tp_name, "bytes") == 0)
			print_python_bytes(element);
		else if (strcmp(Py_TYPE(element)->tp_name, "float") == 0)
			print_python_float(element);
	}
}

/**
 * print_python_bytes - prints some basic info about Python bytes
 * @p: pointer to PyObject
 */
void print_python_bytes(PyObject *p)
{
	PyVarObject *var = (PyVarObject *)p;
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = var->ob_size;
	str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	printf("  first 10 bytes: ");
	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02x", (unsigned char)str[i]);
		if (i < 9)
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_float - prints some basic info about Python float
 * @p: pointer to PyObject
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *float_obj = (PyFloatObject *)p;

	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	printf("  value: %f\n", float_obj->ob_fval);
}
