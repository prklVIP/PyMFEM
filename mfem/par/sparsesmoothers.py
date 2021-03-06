# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_sparsesmoothers', [dirname(__file__)])
        except ImportError:
            import _sparsesmoothers
            return _sparsesmoothers
        if fp is not None:
            try:
                _mod = imp.load_module('_sparsesmoothers', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _sparsesmoothers = swig_import_helper()
    del swig_import_helper
else:
    import _sparsesmoothers
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


try:
    import weakref
    weakref_proxy = weakref.proxy
except Exception:
    weakref_proxy = lambda x: x


import vector
import array
import operators
import sparsemat
import matrix
import densemat
class SparseSmoother(matrix.MatrixInverse):
    __swig_setmethods__ = {}
    for _s in [matrix.MatrixInverse]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SparseSmoother, name, value)
    __swig_getmethods__ = {}
    for _s in [matrix.MatrixInverse]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SparseSmoother, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def SetOperator(self, a):
        return _sparsesmoothers.SparseSmoother_SetOperator(self, a)
    __swig_destroy__ = _sparsesmoothers.delete_SparseSmoother
    __del__ = lambda self: None
SparseSmoother_swigregister = _sparsesmoothers.SparseSmoother_swigregister
SparseSmoother_swigregister(SparseSmoother)

class GSSmoother(SparseSmoother):
    __swig_setmethods__ = {}
    for _s in [SparseSmoother]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, GSSmoother, name, value)
    __swig_getmethods__ = {}
    for _s in [SparseSmoother]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, GSSmoother, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _sparsesmoothers.new_GSSmoother(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def Mult(self, x, y):
        return _sparsesmoothers.GSSmoother_Mult(self, x, y)
    __swig_destroy__ = _sparsesmoothers.delete_GSSmoother
    __del__ = lambda self: None
GSSmoother_swigregister = _sparsesmoothers.GSSmoother_swigregister
GSSmoother_swigregister(GSSmoother)

class DSmoother(SparseSmoother):
    __swig_setmethods__ = {}
    for _s in [SparseSmoother]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, DSmoother, name, value)
    __swig_getmethods__ = {}
    for _s in [SparseSmoother]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, DSmoother, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _sparsesmoothers.new_DSmoother(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def Mult(self, x, y):
        return _sparsesmoothers.DSmoother_Mult(self, x, y)
    __swig_destroy__ = _sparsesmoothers.delete_DSmoother
    __del__ = lambda self: None
DSmoother_swigregister = _sparsesmoothers.DSmoother_swigregister
DSmoother_swigregister(DSmoother)

# This file is compatible with both classic and new-style classes.


