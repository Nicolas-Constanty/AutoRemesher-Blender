#include <thread>
#include <Python.h>

#include "autoremesher/quadmeshgenerator.h"
#include "geogram/basic/common.h"

#if DEBUG
#include <udan/debug/ULogger.h>
#endif

void run_generate(QuadMeshGenerator *generator)
{
    generator->generate();
}

static PyObject* generate_quadmesh(PyObject* self, PyObject *args)
{
    GEO::initialize();
#if DEBUG
    udan::debug::ULogger::Init();
#endif
	//Parse python arguments
    PyObject* pyOriginalVertices;
    PyObject* pyOriginalTriangles;
    double targetDensity;
    double targetScaling;
    int modelType;

	if (!PyArg_ParseTuple(args, "OOddi", &pyOriginalVertices, &pyOriginalTriangles, &targetDensity, &targetScaling, &modelType))
	{
        return nullptr;
	}

	//Convert list from python lists to std::vector
    std::vector<AutoRemesher::Vector3> originalVertices;
    std::vector<std::vector<std::size_t>> originalTriangles;
	for (Py_ssize_t i = 0; i < PyList_Size(pyOriginalVertices); i++)
	{
        PyObject *item = PyObject_GetAttrString(PyList_GetItem(pyOriginalVertices, i), "co");
        if (item == nullptr)
            return nullptr;
        originalVertices.emplace_back(
            PyFloat_AsDouble(PyObject_GetAttrString(item, "x")),
            PyFloat_AsDouble(PyObject_GetAttrString(item, "y")),
            PyFloat_AsDouble(PyObject_GetAttrString(item, "z"))
        );
	}

    for (Py_ssize_t i = 0; i < PyList_Size(pyOriginalTriangles); i++)
    {
        PyObject* face = PyObject_GetAttrString(PyList_GetItem(pyOriginalTriangles, i), "vertices");
        Py_ssize_t vCount = PyObject_Length(face);
        std::vector<std::size_t> tmp(vCount);
    	for (Py_ssize_t j = 0; j < vCount; j++)
    	{
            PyObject *vertice = PyObject_GetItem(face, PyLong_FromSize_t(j));
            std::size_t index = PyLong_AsSize_t(vertice);
            tmp[j] = index;
    	}
        originalTriangles.push_back(tmp);
    }

	//Generate new mesh
    QuadMeshGenerator quadMeshGenerator(originalVertices, originalTriangles);
    QuadMeshGenerator::Parameters parameters;
    {
        const int base = 100000;
        const int range = 500000;
        parameters.targetTriangleCount = base + range * targetDensity;
    }
    {
        parameters.scaling = targetScaling;
    }
    parameters.modelType = static_cast<AutoRemesher::ModelType>(modelType);

    quadMeshGenerator.setParameters(parameters);
    std::thread generateTask(run_generate, &quadMeshGenerator);
    generateTask.join();

    auto remeshedVertices = quadMeshGenerator.takeRemeshedVertices();
    auto remeshedQuad = quadMeshGenerator.takeRemeshedQuads();

	if (remeshedQuad == nullptr || remeshedVertices == nullptr)
        return nullptr;
    //Create and initialize python containers
    PyObject* quadMeshVertices = PyList_New(remeshedVertices->size());
    PyObject* quadMeshTriangles = PyList_New(remeshedQuad->size());
    PyObject* convertedMeshData = PyTuple_New(2);


    auto vertices = *remeshedVertices;
	for (Py_ssize_t i = 0; i < vertices.size(); ++i)
	{
        AutoRemesher::Vector3 v = vertices[i];
        PyObject* pyVertice = PyTuple_New(3);
        PyTuple_SetItem(pyVertice, 0, PyFloat_FromDouble(v.x()));
        PyTuple_SetItem(pyVertice, 1, PyFloat_FromDouble(v.y()));
        PyTuple_SetItem(pyVertice, 2, PyFloat_FromDouble(v.z()));
        PyList_SetItem(quadMeshVertices, i, pyVertice);
	}

    auto quad = *remeshedQuad;
    for (Py_ssize_t i = 0; i < quad.size(); ++i)
    {
		//Should be 4 everytime ??
        auto face = quad[i];
        auto size = face.size();
        PyObject* pyQuad = PyList_New(size);
	    for (Py_ssize_t j = 0; j < size; j++)
	    {
            PyList_SetItem(pyQuad, j, PyLong_FromSize_t(face[j]));
	    }
        PyList_SetItem(quadMeshTriangles, i, pyQuad);
    }
	
    PyTuple_SetItem(convertedMeshData, 0, quadMeshVertices);
    PyTuple_SetItem(convertedMeshData, 1, quadMeshTriangles);
    delete remeshedVertices;
    delete remeshedQuad;
	return convertedMeshData;
}

static struct PyMethodDef methods[] = {
	{ "generate_quad_mesh", generate_quadmesh, METH_VARARGS, "Returns a quad mesh from an input mesh"},
	{ NULL, NULL, 0, NULL }
};

static struct PyModuleDef modDef = {
	PyModuleDef_HEAD_INIT, "autoremesher", NULL, -1, methods,
	NULL, NULL, NULL, NULL
};

PyMODINIT_FUNC PyInit_autoremesher(void)
{
    PyObject *m;

    m = PyModule_Create(&modDef);
    if (m == NULL)
        return NULL;

    return m;
}