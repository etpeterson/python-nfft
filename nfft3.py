'''Wrapper for nfft3.h

Generated with:
/usr/local/bin/ctypesgen.py nfft3.h -o nfft3.py --all-errors

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError,e:
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname

        else:
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        directories.extend(['/lib', '/usr/lib', '/lib64', '/usr/lib64'])

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs([])

# No libraries

# No modules

enum_fftw_r2r_kind_do_not_use_me = c_int # /usr/include/fftw3.h: 88

fftw_complex = c_double * 2 # /usr/include/fftw3.h: 341

# /usr/include/fftw3.h: 341
class struct_fftw_plan_s(Structure):
    pass

fftw_plan = POINTER(struct_fftw_plan_s) # /usr/include/fftw3.h: 341

fftw_r2r_kind = enum_fftw_r2r_kind_do_not_use_me # /usr/include/fftw3.h: 341

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 39
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfft_malloc'):
        continue
    nfft_malloc = _lib.nfft_malloc
    nfft_malloc.argtypes = [c_size_t]
    nfft_malloc.restype = POINTER(None)
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 40
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfft_free'):
        continue
    nfft_free = _lib.nfft_free
    nfft_free.argtypes = [POINTER(None)]
    nfft_free.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 41
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfft_die'):
        continue
    nfft_die = _lib.nfft_die
    nfft_die.argtypes = [String]
    nfft_die.restype = None
    break

nfft_malloc_type_function = CFUNCTYPE(UNCHECKED(POINTER(None)), c_size_t) # /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 44

nfft_free_type_function = CFUNCTYPE(UNCHECKED(None), POINTER(None)) # /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 45

nfft_die_type_function = CFUNCTYPE(UNCHECKED(None), String) # /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 46

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 47
for _lib in _libs.values():
    try:
        nfft_malloc_hook = (nfft_malloc_type_function).in_dll(_lib, 'nfft_malloc_hook')
        break
    except:
        pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 48
for _lib in _libs.values():
    try:
        nfft_free_hook = (nfft_free_type_function).in_dll(_lib, 'nfft_free_hook')
        break
    except:
        pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 49
for _lib in _libs.values():
    try:
        nfft_die_hook = (nfft_die_type_function).in_dll(_lib, 'nfft_die_hook')
        break
    except:
        pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 67
class struct_anon_8(Structure):
    pass

struct_anon_8.__slots__ = [
    'N_total',
    'M_total',
    'f_hat',
    'f',
    'mv_trafo',
    'mv_adjoint',
]
struct_anon_8._fields_ = [
    ('N_total', c_int),
    ('M_total', c_int),
    ('f_hat', POINTER(fftw_complex)),
    ('f', POINTER(fftw_complex)),
    ('mv_trafo', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('mv_adjoint', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
]

mv_plan_complex = struct_anon_8 # /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 67

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 72
class struct_anon_9(Structure):
    pass

struct_anon_9.__slots__ = [
    'N_total',
    'M_total',
    'f_hat',
    'f',
    'mv_trafo',
    'mv_adjoint',
]
struct_anon_9._fields_ = [
    ('N_total', c_int),
    ('M_total', c_int),
    ('f_hat', POINTER(c_double)),
    ('f', POINTER(c_double)),
    ('mv_trafo', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('mv_adjoint', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
]

mv_plan_double = struct_anon_9 # /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 72

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 347
class struct_anon_10(Structure):
    pass

struct_anon_10.__slots__ = [
    'N_total',
    'M_total',
    'f_hat',
    'f',
    'mv_trafo',
    'mv_adjoint',
    'd',
    'N',
    'sigma',
    'n',
    'n_total',
    'm',
    'b',
    'K',
    'nfft_flags',
    'fftw_flags',
    'x',
    'MEASURE_TIME_t',
    'my_fftw_plan1',
    'my_fftw_plan2',
    'c_phi_inv',
    'psi',
    'psi_index_g',
    'psi_index_f',
    'g',
    'g_hat',
    'g1',
    'g2',
    'spline_coeffs',
]
struct_anon_10._fields_ = [
    ('N_total', c_int),
    ('M_total', c_int),
    ('f_hat', POINTER(fftw_complex)),
    ('f', POINTER(fftw_complex)),
    ('mv_trafo', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('mv_adjoint', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('d', c_int),
    ('N', POINTER(c_int)),
    ('sigma', POINTER(c_double)),
    ('n', POINTER(c_int)),
    ('n_total', c_int),
    ('m', c_int),
    ('b', POINTER(c_double)),
    ('K', c_int),
    ('nfft_flags', c_uint),
    ('fftw_flags', c_uint),
    ('x', POINTER(c_double)),
    ('MEASURE_TIME_t', c_double * 3),
    ('my_fftw_plan1', fftw_plan),
    ('my_fftw_plan2', fftw_plan),
    ('c_phi_inv', POINTER(POINTER(c_double))),
    ('psi', POINTER(c_double)),
    ('psi_index_g', POINTER(c_int)),
    ('psi_index_f', POINTER(c_int)),
    ('g', POINTER(fftw_complex)),
    ('g_hat', POINTER(fftw_complex)),
    ('g1', POINTER(fftw_complex)),
    ('g2', POINTER(fftw_complex)),
    ('spline_coeffs', POINTER(c_double)),
]

nfft_plan = struct_anon_10 # /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 347

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 357
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndft_trafo'):
        continue
    ndft_trafo = _lib.ndft_trafo
    ndft_trafo.argtypes = [POINTER(nfft_plan)]
    ndft_trafo.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 366
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndft_adjoint'):
        continue
    ndft_adjoint = _lib.ndft_adjoint
    ndft_adjoint.argtypes = [POINTER(nfft_plan)]
    ndft_adjoint.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 375
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfft_trafo'):
        continue
    nfft_trafo = _lib.nfft_trafo
    nfft_trafo.argtypes = [POINTER(nfft_plan)]
    nfft_trafo.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 376
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfft_trafo_1d'):
        continue
    nfft_trafo_1d = _lib.nfft_trafo_1d
    nfft_trafo_1d.argtypes = [POINTER(nfft_plan)]
    nfft_trafo_1d.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 377
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfft_trafo_2d'):
        continue
    nfft_trafo_2d = _lib.nfft_trafo_2d
    nfft_trafo_2d.argtypes = [POINTER(nfft_plan)]
    nfft_trafo_2d.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 378
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfft_trafo_3d'):
        continue
    nfft_trafo_3d = _lib.nfft_trafo_3d
    nfft_trafo_3d.argtypes = [POINTER(nfft_plan)]
    nfft_trafo_3d.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 387
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfft_adjoint'):
        continue
    nfft_adjoint = _lib.nfft_adjoint
    nfft_adjoint.argtypes = [POINTER(nfft_plan)]
    nfft_adjoint.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 388
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfft_adjoint_1d'):
        continue
    nfft_adjoint_1d = _lib.nfft_adjoint_1d
    nfft_adjoint_1d.argtypes = [POINTER(nfft_plan)]
    nfft_adjoint_1d.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 389
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfft_adjoint_2d'):
        continue
    nfft_adjoint_2d = _lib.nfft_adjoint_2d
    nfft_adjoint_2d.argtypes = [POINTER(nfft_plan)]
    nfft_adjoint_2d.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 390
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfft_adjoint_3d'):
        continue
    nfft_adjoint_3d = _lib.nfft_adjoint_3d
    nfft_adjoint_3d.argtypes = [POINTER(nfft_plan)]
    nfft_adjoint_3d.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 401
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfft_init_1d'):
        continue
    nfft_init_1d = _lib.nfft_init_1d
    nfft_init_1d.argtypes = [POINTER(nfft_plan), c_int, c_int]
    nfft_init_1d.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 413
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfft_init_2d'):
        continue
    nfft_init_2d = _lib.nfft_init_2d
    nfft_init_2d.argtypes = [POINTER(nfft_plan), c_int, c_int, c_int]
    nfft_init_2d.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 426
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfft_init_3d'):
        continue
    nfft_init_3d = _lib.nfft_init_3d
    nfft_init_3d.argtypes = [POINTER(nfft_plan), c_int, c_int, c_int, c_int]
    nfft_init_3d.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 438
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfft_init'):
        continue
    nfft_init = _lib.nfft_init
    nfft_init.argtypes = [POINTER(nfft_plan), c_int, POINTER(c_int), c_int]
    nfft_init.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 453
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfft_init_advanced'):
        continue
    nfft_init_advanced = _lib.nfft_init_advanced
    nfft_init_advanced.argtypes = [POINTER(nfft_plan), c_int, POINTER(c_int), c_int, c_uint, c_uint]
    nfft_init_advanced.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 470
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfft_init_guru'):
        continue
    nfft_init_guru = _lib.nfft_init_guru
    nfft_init_guru.argtypes = [POINTER(nfft_plan), c_int, POINTER(c_int), c_int, POINTER(c_int), c_int, c_uint, c_uint]
    nfft_init_guru.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 486
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfft_precompute_one_psi'):
        continue
    nfft_precompute_one_psi = _lib.nfft_precompute_one_psi
    nfft_precompute_one_psi.argtypes = [POINTER(nfft_plan)]
    nfft_precompute_one_psi.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 492
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfft_precompute_full_psi'):
        continue
    nfft_precompute_full_psi = _lib.nfft_precompute_full_psi
    nfft_precompute_full_psi.argtypes = [POINTER(nfft_plan)]
    nfft_precompute_full_psi.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 498
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfft_precompute_psi'):
        continue
    nfft_precompute_psi = _lib.nfft_precompute_psi
    nfft_precompute_psi.argtypes = [POINTER(nfft_plan)]
    nfft_precompute_psi.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 504
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfft_precompute_lin_psi'):
        continue
    nfft_precompute_lin_psi = _lib.nfft_precompute_lin_psi
    nfft_precompute_lin_psi.argtypes = [POINTER(nfft_plan)]
    nfft_precompute_lin_psi.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 513
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfft_check'):
        continue
    nfft_check = _lib.nfft_check
    nfft_check.argtypes = [POINTER(nfft_plan)]
    nfft_check.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 522
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfft_finalize'):
        continue
    nfft_finalize = _lib.nfft_finalize
    nfft_finalize.argtypes = [POINTER(nfft_plan)]
    nfft_finalize.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 578
class struct_anon_11(Structure):
    pass

struct_anon_11.__slots__ = [
    'N_total',
    'M_total',
    'f_hat',
    'f',
    'mv_trafo',
    'mv_adjoint',
    'd',
    'N',
    'n',
    'sigma',
    'm',
    'nfct_full_psi_eps',
    'b',
    'nfct_flags',
    'fftw_flags',
    'x',
    'MEASURE_TIME_t',
    'my_fftw_r2r_plan',
    'r2r_kind',
    'c_phi_inv',
    'psi',
    'size_psi',
    'psi_index_g',
    'psi_index_f',
    'g',
    'g_hat',
    'g1',
    'g2',
    'spline_coeffs',
]
struct_anon_11._fields_ = [
    ('N_total', c_int),
    ('M_total', c_int),
    ('f_hat', POINTER(c_double)),
    ('f', POINTER(c_double)),
    ('mv_trafo', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('mv_adjoint', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('d', c_int),
    ('N', POINTER(c_int)),
    ('n', POINTER(c_int)),
    ('sigma', POINTER(c_double)),
    ('m', c_int),
    ('nfct_full_psi_eps', c_double),
    ('b', POINTER(c_double)),
    ('nfct_flags', c_uint),
    ('fftw_flags', c_uint),
    ('x', POINTER(c_double)),
    ('MEASURE_TIME_t', c_double * 3),
    ('my_fftw_r2r_plan', fftw_plan),
    ('r2r_kind', POINTER(fftw_r2r_kind)),
    ('c_phi_inv', POINTER(POINTER(c_double))),
    ('psi', POINTER(c_double)),
    ('size_psi', c_int),
    ('psi_index_g', POINTER(c_int)),
    ('psi_index_f', POINTER(c_int)),
    ('g', POINTER(c_double)),
    ('g_hat', POINTER(c_double)),
    ('g1', POINTER(c_double)),
    ('g2', POINTER(c_double)),
    ('spline_coeffs', POINTER(c_double)),
]

nfct_plan = struct_anon_11 # /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 578

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 590
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfct_init_1d'):
        continue
    nfct_init_1d = _lib.nfct_init_1d
    nfct_init_1d.argtypes = [POINTER(nfct_plan), c_int, c_int]
    nfct_init_1d.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 602
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfct_init_2d'):
        continue
    nfct_init_2d = _lib.nfct_init_2d
    nfct_init_2d.argtypes = [POINTER(nfct_plan), c_int, c_int, c_int]
    nfct_init_2d.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 615
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfct_init_3d'):
        continue
    nfct_init_3d = _lib.nfct_init_3d
    nfct_init_3d.argtypes = [POINTER(nfct_plan), c_int, c_int, c_int, c_int]
    nfct_init_3d.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 627
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfct_init'):
        continue
    nfct_init = _lib.nfct_init
    nfct_init.argtypes = [POINTER(nfct_plan), c_int, POINTER(c_int), c_int]
    nfct_init.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 643
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfct_init_guru'):
        continue
    nfct_init_guru = _lib.nfct_init_guru
    nfct_init_guru.argtypes = [POINTER(nfct_plan), c_int, POINTER(c_int), c_int, POINTER(c_int), c_int, c_uint, c_uint]
    nfct_init_guru.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 655
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfct_precompute_psi'):
        continue
    nfct_precompute_psi = _lib.nfct_precompute_psi
    nfct_precompute_psi.argtypes = [POINTER(nfct_plan)]
    nfct_precompute_psi.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 666
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfct_trafo'):
        continue
    nfct_trafo = _lib.nfct_trafo
    nfct_trafo.argtypes = [POINTER(nfct_plan)]
    nfct_trafo.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 676
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndct_trafo'):
        continue
    ndct_trafo = _lib.ndct_trafo
    ndct_trafo.argtypes = [POINTER(nfct_plan)]
    ndct_trafo.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 686
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfct_adjoint'):
        continue
    nfct_adjoint = _lib.nfct_adjoint
    nfct_adjoint.argtypes = [POINTER(nfct_plan)]
    nfct_adjoint.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 696
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndct_adjoint'):
        continue
    ndct_adjoint = _lib.ndct_adjoint
    ndct_adjoint.argtypes = [POINTER(nfct_plan)]
    ndct_adjoint.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 705
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfct_finalize'):
        continue
    nfct_finalize = _lib.nfct_finalize
    nfct_finalize.argtypes = [POINTER(nfct_plan)]
    nfct_finalize.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 716
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfct_phi_hut'):
        continue
    nfct_phi_hut = _lib.nfct_phi_hut
    nfct_phi_hut.argtypes = [POINTER(nfct_plan), c_int, c_int]
    nfct_phi_hut.restype = c_double
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 727
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfct_phi'):
        continue
    nfct_phi = _lib.nfct_phi
    nfct_phi.argtypes = [POINTER(nfct_plan), c_double, c_int]
    nfct_phi.restype = c_double
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 736
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfct_fftw_2N'):
        continue
    nfct_fftw_2N = _lib.nfct_fftw_2N
    nfct_fftw_2N.argtypes = [c_int]
    nfct_fftw_2N.restype = c_int
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 745
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfct_fftw_2N_rev'):
        continue
    nfct_fftw_2N_rev = _lib.nfct_fftw_2N_rev
    nfct_fftw_2N_rev.argtypes = [c_int]
    nfct_fftw_2N_rev.restype = c_int
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 793
class struct_anon_12(Structure):
    pass

struct_anon_12.__slots__ = [
    'N_total',
    'M_total',
    'f_hat',
    'f',
    'mv_trafo',
    'mv_adjoint',
    'd',
    'N',
    'n',
    'sigma',
    'm',
    'nfst_full_psi_eps',
    'b',
    'nfst_flags',
    'fftw_flags',
    'x',
    'MEASURE_TIME_t',
    'my_fftw_r2r_plan',
    'r2r_kind',
    'c_phi_inv',
    'psi',
    'size_psi',
    'psi_index_g',
    'psi_index_f',
    'g',
    'g_hat',
    'g1',
    'g2',
    'spline_coeffs',
]
struct_anon_12._fields_ = [
    ('N_total', c_int),
    ('M_total', c_int),
    ('f_hat', POINTER(c_double)),
    ('f', POINTER(c_double)),
    ('mv_trafo', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('mv_adjoint', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('d', c_int),
    ('N', POINTER(c_int)),
    ('n', POINTER(c_int)),
    ('sigma', POINTER(c_double)),
    ('m', c_int),
    ('nfst_full_psi_eps', c_double),
    ('b', POINTER(c_double)),
    ('nfst_flags', c_uint),
    ('fftw_flags', c_uint),
    ('x', POINTER(c_double)),
    ('MEASURE_TIME_t', c_double * 3),
    ('my_fftw_r2r_plan', fftw_plan),
    ('r2r_kind', POINTER(fftw_r2r_kind)),
    ('c_phi_inv', POINTER(POINTER(c_double))),
    ('psi', POINTER(c_double)),
    ('size_psi', c_int),
    ('psi_index_g', POINTER(c_int)),
    ('psi_index_f', POINTER(c_int)),
    ('g', POINTER(c_double)),
    ('g_hat', POINTER(c_double)),
    ('g1', POINTER(c_double)),
    ('g2', POINTER(c_double)),
    ('spline_coeffs', POINTER(c_double)),
]

nfst_plan = struct_anon_12 # /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 793

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 805
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfst_init_1d'):
        continue
    nfst_init_1d = _lib.nfst_init_1d
    nfst_init_1d.argtypes = [POINTER(nfst_plan), c_int, c_int]
    nfst_init_1d.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 817
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfst_init_2d'):
        continue
    nfst_init_2d = _lib.nfst_init_2d
    nfst_init_2d.argtypes = [POINTER(nfst_plan), c_int, c_int, c_int]
    nfst_init_2d.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 830
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfst_init_3d'):
        continue
    nfst_init_3d = _lib.nfst_init_3d
    nfst_init_3d.argtypes = [POINTER(nfst_plan), c_int, c_int, c_int, c_int]
    nfst_init_3d.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 842
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfst_init'):
        continue
    nfst_init = _lib.nfst_init
    nfst_init.argtypes = [POINTER(nfst_plan), c_int, POINTER(c_int), c_int]
    nfst_init.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 856
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfst_init_m'):
        continue
    nfst_init_m = _lib.nfst_init_m
    nfst_init_m.argtypes = [POINTER(nfst_plan), c_int, POINTER(c_int), c_int, c_int]
    nfst_init_m.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 872
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfst_init_guru'):
        continue
    nfst_init_guru = _lib.nfst_init_guru
    nfst_init_guru.argtypes = [POINTER(nfst_plan), c_int, POINTER(c_int), c_int, POINTER(c_int), c_int, c_uint, c_uint]
    nfst_init_guru.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 884
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfst_precompute_psi'):
        continue
    nfst_precompute_psi = _lib.nfst_precompute_psi
    nfst_precompute_psi.argtypes = [POINTER(nfst_plan)]
    nfst_precompute_psi.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 894
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfst_trafo'):
        continue
    nfst_trafo = _lib.nfst_trafo
    nfst_trafo.argtypes = [POINTER(nfst_plan)]
    nfst_trafo.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 904
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndst_trafo'):
        continue
    ndst_trafo = _lib.ndst_trafo
    ndst_trafo.argtypes = [POINTER(nfst_plan)]
    ndst_trafo.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 916
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfst_adjoint'):
        continue
    nfst_adjoint = _lib.nfst_adjoint
    nfst_adjoint.argtypes = [POINTER(nfst_plan)]
    nfst_adjoint.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 926
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndst_adjoint'):
        continue
    ndst_adjoint = _lib.ndst_adjoint
    ndst_adjoint.argtypes = [POINTER(nfst_plan)]
    ndst_adjoint.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 935
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfst_finalize'):
        continue
    nfst_finalize = _lib.nfst_finalize
    nfst_finalize.argtypes = [POINTER(nfst_plan)]
    nfst_finalize.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 943
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfst_full_psi'):
        continue
    nfst_full_psi = _lib.nfst_full_psi
    nfst_full_psi.argtypes = [POINTER(nfst_plan), c_double]
    nfst_full_psi.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 954
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfst_phi_hut'):
        continue
    nfst_phi_hut = _lib.nfst_phi_hut
    nfst_phi_hut.argtypes = [POINTER(nfst_plan), c_int, c_int]
    nfst_phi_hut.restype = c_double
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 965
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfst_phi'):
        continue
    nfst_phi = _lib.nfst_phi
    nfst_phi.argtypes = [POINTER(nfst_plan), c_double, c_int]
    nfst_phi.restype = c_double
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 974
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfst_fftw_2N'):
        continue
    nfst_fftw_2N = _lib.nfst_fftw_2N
    nfst_fftw_2N.argtypes = [c_int]
    nfst_fftw_2N.restype = c_int
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 983
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfst_fftw_2N_rev'):
        continue
    nfst_fftw_2N_rev = _lib.nfst_fftw_2N_rev
    nfst_fftw_2N_rev.argtypes = [c_int]
    nfst_fftw_2N_rev.restype = c_int
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1046
class struct_anon_13(Structure):
    pass

struct_anon_13.__slots__ = [
    'N_total',
    'M_total',
    'f_hat',
    'f',
    'mv_trafo',
    'mv_adjoint',
    'd',
    'sigma',
    'a',
    'N',
    'N1',
    'aN1',
    'm',
    'b',
    'K',
    'aN1_total',
    'direct_plan',
    'nnfft_flags',
    'n',
    'x',
    'v',
    'c_phi_inv',
    'psi',
    'size_psi',
    'psi_index_g',
    'psi_index_f',
    'F',
    'spline_coeffs',
]
struct_anon_13._fields_ = [
    ('N_total', c_int),
    ('M_total', c_int),
    ('f_hat', POINTER(fftw_complex)),
    ('f', POINTER(fftw_complex)),
    ('mv_trafo', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('mv_adjoint', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('d', c_int),
    ('sigma', POINTER(c_double)),
    ('a', POINTER(c_double)),
    ('N', POINTER(c_int)),
    ('N1', POINTER(c_int)),
    ('aN1', POINTER(c_int)),
    ('m', c_int),
    ('b', POINTER(c_double)),
    ('K', c_int),
    ('aN1_total', c_int),
    ('direct_plan', POINTER(nfft_plan)),
    ('nnfft_flags', c_uint),
    ('n', POINTER(c_int)),
    ('x', POINTER(c_double)),
    ('v', POINTER(c_double)),
    ('c_phi_inv', POINTER(c_double)),
    ('psi', POINTER(c_double)),
    ('size_psi', c_int),
    ('psi_index_g', POINTER(c_int)),
    ('psi_index_f', POINTER(c_int)),
    ('F', POINTER(fftw_complex)),
    ('spline_coeffs', POINTER(c_double)),
]

nnfft_plan = struct_anon_13 # /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1046

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1060
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nnfft_init'):
        continue
    nnfft_init = _lib.nnfft_init
    nnfft_init.argtypes = [POINTER(nnfft_plan), c_int, c_int, c_int, POINTER(c_int)]
    nnfft_init.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1076
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nnfft_init_guru'):
        continue
    nnfft_init_guru = _lib.nnfft_init_guru
    nnfft_init_guru.argtypes = [POINTER(nnfft_plan), c_int, c_int, c_int, POINTER(c_int), POINTER(c_int), c_int, c_uint]
    nnfft_init_guru.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1090
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nndft_trafo'):
        continue
    nndft_trafo = _lib.nndft_trafo
    nndft_trafo.argtypes = [POINTER(nnfft_plan)]
    nndft_trafo.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1103
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nndft_adjoint'):
        continue
    nndft_adjoint = _lib.nndft_adjoint
    nndft_adjoint.argtypes = [POINTER(nnfft_plan)]
    nndft_adjoint.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1116
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nnfft_trafo'):
        continue
    nnfft_trafo = _lib.nnfft_trafo
    nnfft_trafo.argtypes = [POINTER(nnfft_plan)]
    nnfft_trafo.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1129
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nnfft_adjoint'):
        continue
    nnfft_adjoint = _lib.nnfft_adjoint
    nnfft_adjoint.argtypes = [POINTER(nnfft_plan)]
    nnfft_adjoint.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1142
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nnfft_precompute_lin_psi'):
        continue
    nnfft_precompute_lin_psi = _lib.nnfft_precompute_lin_psi
    nnfft_precompute_lin_psi.argtypes = [POINTER(nnfft_plan)]
    nnfft_precompute_lin_psi.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1156
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nnfft_precompute_psi'):
        continue
    nnfft_precompute_psi = _lib.nnfft_precompute_psi
    nnfft_precompute_psi.argtypes = [POINTER(nnfft_plan)]
    nnfft_precompute_psi.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1171
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nnfft_precompute_full_psi'):
        continue
    nnfft_precompute_full_psi = _lib.nnfft_precompute_full_psi
    nnfft_precompute_full_psi.argtypes = [POINTER(nnfft_plan)]
    nnfft_precompute_full_psi.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1185
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nnfft_precompute_phi_hut'):
        continue
    nnfft_precompute_phi_hut = _lib.nnfft_precompute_phi_hut
    nnfft_precompute_phi_hut.argtypes = [POINTER(nnfft_plan)]
    nnfft_precompute_phi_hut.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1194
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nnfft_finalize'):
        continue
    nnfft_finalize = _lib.nnfft_finalize
    nnfft_finalize.argtypes = [POINTER(nnfft_plan)]
    nnfft_finalize.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1253
class struct_anon_14(Structure):
    pass

struct_anon_14.__slots__ = [
    'N_total',
    'M_total',
    'f_hat',
    'f',
    'mv_trafo',
    'mv_adjoint',
    'd',
    'J',
    'sigma',
    'flags',
    'index_sparse_to_full',
    'r_act_nfft_plan',
    'act_nfft_plan',
    'center_nfft_plan',
    'set_fftw_plan1',
    'set_fftw_plan2',
    'set_nfft_plan_1d',
    'set_nfft_plan_2d',
    'x_transposed',
    'x_102',
    'x_201',
    'x_120',
    'x_021',
]
struct_anon_14._fields_ = [
    ('N_total', c_int),
    ('M_total', c_int),
    ('f_hat', POINTER(fftw_complex)),
    ('f', POINTER(fftw_complex)),
    ('mv_trafo', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('mv_adjoint', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('d', c_int),
    ('J', c_int),
    ('sigma', c_int),
    ('flags', c_uint),
    ('index_sparse_to_full', POINTER(c_int)),
    ('r_act_nfft_plan', c_int),
    ('act_nfft_plan', POINTER(nfft_plan)),
    ('center_nfft_plan', POINTER(nfft_plan)),
    ('set_fftw_plan1', POINTER(fftw_plan)),
    ('set_fftw_plan2', POINTER(fftw_plan)),
    ('set_nfft_plan_1d', POINTER(nfft_plan)),
    ('set_nfft_plan_2d', POINTER(nfft_plan)),
    ('x_transposed', POINTER(c_double)),
    ('x_102', POINTER(c_double)),
    ('x_201', POINTER(c_double)),
    ('x_120', POINTER(c_double)),
    ('x_021', POINTER(c_double)),
]

nsfft_plan = struct_anon_14 # /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1253

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1265
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nsdft_trafo'):
        continue
    nsdft_trafo = _lib.nsdft_trafo
    nsdft_trafo.argtypes = [POINTER(nsfft_plan)]
    nsdft_trafo.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1277
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nsdft_adjoint'):
        continue
    nsdft_adjoint = _lib.nsdft_adjoint
    nsdft_adjoint.argtypes = [POINTER(nsfft_plan)]
    nsdft_adjoint.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1290
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nsfft_trafo'):
        continue
    nsfft_trafo = _lib.nsfft_trafo
    nsfft_trafo.argtypes = [POINTER(nsfft_plan)]
    nsfft_trafo.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1303
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nsfft_adjoint'):
        continue
    nsfft_adjoint = _lib.nsfft_adjoint
    nsfft_adjoint.argtypes = [POINTER(nsfft_plan)]
    nsfft_adjoint.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1312
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nsfft_cp'):
        continue
    nsfft_cp = _lib.nsfft_cp
    nsfft_cp.argtypes = [POINTER(nsfft_plan), POINTER(nfft_plan)]
    nsfft_cp.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1321
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nsfft_init_random_nodes_coeffs'):
        continue
    nsfft_init_random_nodes_coeffs = _lib.nsfft_init_random_nodes_coeffs
    nsfft_init_random_nodes_coeffs.argtypes = [POINTER(nsfft_plan)]
    nsfft_init_random_nodes_coeffs.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1335
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nsfft_init'):
        continue
    nsfft_init = _lib.nsfft_init
    nsfft_init.argtypes = [POINTER(nsfft_plan), c_int, c_int, c_int, c_int, c_uint]
    nsfft_init.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1344
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nsfft_finalize'):
        continue
    nsfft_finalize = _lib.nsfft_finalize
    nsfft_finalize.argtypes = [POINTER(nsfft_plan)]
    nsfft_finalize.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1375
class struct_anon_15(Structure):
    pass

struct_anon_15.__slots__ = [
    'N_total',
    'M_total',
    'f_hat',
    'f',
    'mv_trafo',
    'mv_adjoint',
    'plan',
    'N3',
    'sigma3',
    't',
    'w',
]
struct_anon_15._fields_ = [
    ('N_total', c_int),
    ('M_total', c_int),
    ('f_hat', POINTER(fftw_complex)),
    ('f', POINTER(fftw_complex)),
    ('mv_trafo', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('mv_adjoint', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('plan', nfft_plan),
    ('N3', c_int),
    ('sigma3', c_double),
    ('t', POINTER(c_double)),
    ('w', POINTER(c_double)),
]

mri_inh_2d1d_plan = struct_anon_15 # /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1375

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1391
class struct_anon_16(Structure):
    pass

struct_anon_16.__slots__ = [
    'N_total',
    'M_total',
    'f_hat',
    'f',
    'mv_trafo',
    'mv_adjoint',
    'plan',
    'N3',
    'sigma3',
    't',
    'w',
]
struct_anon_16._fields_ = [
    ('N_total', c_int),
    ('M_total', c_int),
    ('f_hat', POINTER(fftw_complex)),
    ('f', POINTER(fftw_complex)),
    ('mv_trafo', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('mv_adjoint', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('plan', nfft_plan),
    ('N3', c_int),
    ('sigma3', c_double),
    ('t', POINTER(c_double)),
    ('w', POINTER(c_double)),
]

mri_inh_3d_plan = struct_anon_16 # /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1391

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1406
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'mri_inh_2d1d_trafo'):
        continue
    mri_inh_2d1d_trafo = _lib.mri_inh_2d1d_trafo
    mri_inh_2d1d_trafo.argtypes = [POINTER(mri_inh_2d1d_plan)]
    mri_inh_2d1d_trafo.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1420
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'mri_inh_2d1d_adjoint'):
        continue
    mri_inh_2d1d_adjoint = _lib.mri_inh_2d1d_adjoint
    mri_inh_2d1d_adjoint.argtypes = [POINTER(mri_inh_2d1d_plan)]
    mri_inh_2d1d_adjoint.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1435
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'mri_inh_2d1d_init_guru'):
        continue
    mri_inh_2d1d_init_guru = _lib.mri_inh_2d1d_init_guru
    mri_inh_2d1d_init_guru.argtypes = [POINTER(mri_inh_2d1d_plan), POINTER(c_int), c_int, POINTER(c_int), c_int, c_double, c_uint, c_uint]
    mri_inh_2d1d_init_guru.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1445
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'mri_inh_2d1d_finalize'):
        continue
    mri_inh_2d1d_finalize = _lib.mri_inh_2d1d_finalize
    mri_inh_2d1d_finalize.argtypes = [POINTER(mri_inh_2d1d_plan)]
    mri_inh_2d1d_finalize.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1459
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'mri_inh_3d_trafo'):
        continue
    mri_inh_3d_trafo = _lib.mri_inh_3d_trafo
    mri_inh_3d_trafo.argtypes = [POINTER(mri_inh_3d_plan)]
    mri_inh_3d_trafo.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1473
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'mri_inh_3d_adjoint'):
        continue
    mri_inh_3d_adjoint = _lib.mri_inh_3d_adjoint
    mri_inh_3d_adjoint.argtypes = [POINTER(mri_inh_3d_plan)]
    mri_inh_3d_adjoint.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1475
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'mri_inh_3d_init_guru'):
        continue
    mri_inh_3d_init_guru = _lib.mri_inh_3d_init_guru
    mri_inh_3d_init_guru.argtypes = [POINTER(mri_inh_3d_plan), POINTER(c_int), c_int, POINTER(c_int), c_int, c_double, c_uint, c_uint]
    mri_inh_3d_init_guru.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1485
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'mri_inh_3d_finalize'):
        continue
    mri_inh_3d_finalize = _lib.mri_inh_3d_finalize
    mri_inh_3d_finalize.argtypes = [POINTER(mri_inh_3d_plan)]
    mri_inh_3d_finalize.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1988
class struct_anon_17(Structure):
    pass

struct_anon_17.__slots__ = [
    'N_total',
    'M_total',
    'f_hat',
    'f',
    'mv_trafo',
    'mv_adjoint',
    'N',
    'x',
    't',
    'flags',
    'plan_nfft',
    'f_hat_intern',
]
struct_anon_17._fields_ = [
    ('N_total', c_int),
    ('M_total', c_int),
    ('f_hat', POINTER(fftw_complex)),
    ('f', POINTER(fftw_complex)),
    ('mv_trafo', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('mv_adjoint', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('N', c_int),
    ('x', POINTER(c_double)),
    ('t', c_int),
    ('flags', c_uint),
    ('plan_nfft', nfft_plan),
    ('f_hat_intern', POINTER(fftw_complex)),
]

nfsft_plan = struct_anon_17 # /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1988

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1999
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfsft_init'):
        continue
    nfsft_init = _lib.nfsft_init
    nfsft_init.argtypes = [POINTER(nfsft_plan), c_int, c_int]
    nfsft_init.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2011
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfsft_init_advanced'):
        continue
    nfsft_init_advanced = _lib.nfsft_init_advanced
    nfsft_init_advanced.argtypes = [POINTER(nfsft_plan), c_int, c_int, c_uint]
    nfsft_init_advanced.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2025
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfsft_init_guru'):
        continue
    nfsft_init_guru = _lib.nfsft_init_guru
    nfsft_init_guru.argtypes = [POINTER(nfsft_plan), c_int, c_int, c_uint, c_uint, c_int]
    nfsft_init_guru.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2041
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfsft_precompute'):
        continue
    nfsft_precompute = _lib.nfsft_precompute
    nfsft_precompute.argtypes = [c_int, c_double, c_uint, c_uint]
    nfsft_precompute.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2049
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfsft_forget'):
        continue
    nfsft_forget = _lib.nfsft_forget
    nfsft_forget.argtypes = []
    nfsft_forget.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2062
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndsft_trafo'):
        continue
    ndsft_trafo = _lib.ndsft_trafo
    ndsft_trafo.argtypes = [POINTER(nfsft_plan)]
    ndsft_trafo.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2076
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'ndsft_adjoint'):
        continue
    ndsft_adjoint = _lib.ndsft_adjoint
    ndsft_adjoint.argtypes = [POINTER(nfsft_plan)]
    ndsft_adjoint.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2089
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfsft_trafo'):
        continue
    nfsft_trafo = _lib.nfsft_trafo
    nfsft_trafo.argtypes = [POINTER(nfsft_plan)]
    nfsft_trafo.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2103
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfsft_adjoint'):
        continue
    nfsft_adjoint = _lib.nfsft_adjoint
    nfsft_adjoint.argtypes = [POINTER(nfsft_plan)]
    nfsft_adjoint.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2112
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfsft_finalize'):
        continue
    nfsft_finalize = _lib.nfsft_finalize
    nfsft_finalize.argtypes = [POINTER(nfsft_plan)]
    nfsft_finalize.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2114
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfsft_precompute_x'):
        continue
    nfsft_precompute_x = _lib.nfsft_precompute_x
    nfsft_precompute_x.argtypes = [POINTER(nfsft_plan)]
    nfsft_precompute_x.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2150
class struct_fpt_set_s_(Structure):
    pass

fpt_set = POINTER(struct_fpt_set_s_) # /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2150

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2167
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fpt_init'):
        continue
    fpt_init = _lib.fpt_init
    fpt_init.argtypes = [c_int, c_int, c_uint]
    fpt_init.restype = fpt_set
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2189
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fpt_precompute'):
        continue
    fpt_precompute = _lib.fpt_precompute
    fpt_precompute.argtypes = [fpt_set, c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int, c_double]
    fpt_precompute.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2202
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'dpt_trafo'):
        continue
    dpt_trafo = _lib.dpt_trafo
    dpt_trafo.argtypes = [fpt_set, c_int, POINTER(fftw_complex), POINTER(fftw_complex), c_int, c_uint]
    dpt_trafo.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2215
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fpt_trafo'):
        continue
    fpt_trafo = _lib.fpt_trafo
    fpt_trafo.argtypes = [fpt_set, c_int, POINTER(fftw_complex), POINTER(fftw_complex), c_int, c_uint]
    fpt_trafo.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2228
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'dpt_transposed'):
        continue
    dpt_transposed = _lib.dpt_transposed
    dpt_transposed.argtypes = [fpt_set, c_int, POINTER(fftw_complex), POINTER(fftw_complex), c_int, c_uint]
    dpt_transposed.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2241
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fpt_transposed'):
        continue
    fpt_transposed = _lib.fpt_transposed
    fpt_transposed.argtypes = [fpt_set, c_int, POINTER(fftw_complex), POINTER(fftw_complex), c_int, c_uint]
    fpt_transposed.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2244
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fpt_finalize'):
        continue
    fpt_finalize = _lib.fpt_finalize
    fpt_finalize.argtypes = [fpt_set]
    fpt_finalize.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2491
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'posN'):
        continue
    posN = _lib.posN
    posN.argtypes = [c_int, c_int, c_int]
    posN.restype = c_int
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2523
class struct_nfsoft_plan_(Structure):
    pass

struct_nfsoft_plan_.__slots__ = [
    'N_total',
    'M_total',
    'f_hat',
    'f',
    'mv_trafo',
    'mv_adjoint',
    'x',
    'wig_coeffs',
    'cheby',
    'aux',
    't',
    'flags',
    'p_nfft',
    'fpt_kappa',
]
struct_nfsoft_plan_._fields_ = [
    ('N_total', c_int),
    ('M_total', c_int),
    ('f_hat', POINTER(fftw_complex)),
    ('f', POINTER(fftw_complex)),
    ('mv_trafo', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('mv_adjoint', CFUNCTYPE(UNCHECKED(None), POINTER(None))),
    ('x', POINTER(c_double)),
    ('wig_coeffs', POINTER(fftw_complex)),
    ('cheby', POINTER(fftw_complex)),
    ('aux', POINTER(fftw_complex)),
    ('t', c_int),
    ('flags', c_uint),
    ('p_nfft', nfft_plan),
    ('fpt_kappa', c_int),
]

nfsoft_plan = struct_nfsoft_plan_ # /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2523

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2534
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfsoft_precompute'):
        continue
    nfsoft_precompute = _lib.nfsoft_precompute
    nfsoft_precompute.argtypes = [POINTER(nfsoft_plan)]
    nfsoft_precompute.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2546
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SO3_single_fpt_init'):
        continue
    SO3_single_fpt_init = _lib.SO3_single_fpt_init
    SO3_single_fpt_init.argtypes = [c_int, c_int, c_int, c_uint, c_int]
    SO3_single_fpt_init.restype = fpt_set
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2547
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SO3_fpt'):
        continue
    SO3_fpt = _lib.SO3_fpt
    SO3_fpt.argtypes = [POINTER(fftw_complex), fpt_set, c_int, c_int, c_int, c_uint]
    SO3_fpt.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2548
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'SO3_fpt_transposed'):
        continue
    SO3_fpt_transposed = _lib.SO3_fpt_transposed
    SO3_fpt_transposed.argtypes = [POINTER(fftw_complex), fpt_set, c_int, c_int, c_int, c_uint]
    SO3_fpt_transposed.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2560
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfsoft_init'):
        continue
    nfsoft_init = _lib.nfsoft_init
    nfsoft_init.argtypes = [POINTER(nfsoft_plan), c_int, c_int]
    nfsoft_init.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2571
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfsoft_init_advanced'):
        continue
    nfsoft_init_advanced = _lib.nfsoft_init_advanced
    nfsoft_init_advanced.argtypes = [POINTER(nfsoft_plan), c_int, c_int, c_uint]
    nfsoft_init_advanced.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2585
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfsoft_init_guru'):
        continue
    nfsoft_init_guru = _lib.nfsoft_init_guru
    nfsoft_init_guru.argtypes = [POINTER(nfsoft_plan), c_int, c_int, c_uint, c_uint, c_int, c_int]
    nfsoft_init_guru.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2598
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfsoft_trafo'):
        continue
    nfsoft_trafo = _lib.nfsoft_trafo
    nfsoft_trafo.argtypes = [POINTER(nfsoft_plan)]
    nfsoft_trafo.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2611
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfsoft_adjoint'):
        continue
    nfsoft_adjoint = _lib.nfsoft_adjoint
    nfsoft_adjoint.argtypes = [POINTER(nfsoft_plan)]
    nfsoft_adjoint.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2619
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'nfsoft_finalize'):
        continue
    nfsoft_finalize = _lib.nfsoft_finalize
    nfsoft_finalize.argtypes = [POINTER(nfsoft_plan)]
    nfsoft_finalize.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2726
class struct_anon_18(Structure):
    pass

struct_anon_18.__slots__ = [
    'mv',
    'flags',
    'w',
    'w_hat',
    'y',
    'f_hat_iter',
    'r_iter',
    'z_hat_iter',
    'p_hat_iter',
    'v_iter',
    'alpha_iter',
    'beta_iter',
    'dot_r_iter',
    'dot_r_iter_old',
    'dot_z_hat_iter',
    'dot_z_hat_iter_old',
    'dot_p_hat_iter',
    'dot_v_iter',
]
struct_anon_18._fields_ = [
    ('mv', POINTER(mv_plan_complex)),
    ('flags', c_uint),
    ('w', POINTER(c_double)),
    ('w_hat', POINTER(c_double)),
    ('y', POINTER(fftw_complex)),
    ('f_hat_iter', POINTER(fftw_complex)),
    ('r_iter', POINTER(fftw_complex)),
    ('z_hat_iter', POINTER(fftw_complex)),
    ('p_hat_iter', POINTER(fftw_complex)),
    ('v_iter', POINTER(fftw_complex)),
    ('alpha_iter', c_double),
    ('beta_iter', c_double),
    ('dot_r_iter', c_double),
    ('dot_r_iter_old', c_double),
    ('dot_z_hat_iter', c_double),
    ('dot_z_hat_iter_old', c_double),
    ('dot_p_hat_iter', c_double),
    ('dot_v_iter', c_double),
]

solver_plan_complex = struct_anon_18 # /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2726

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2728
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'solver_init_advanced_complex'):
        continue
    solver_init_advanced_complex = _lib.solver_init_advanced_complex
    solver_init_advanced_complex.argtypes = [POINTER(solver_plan_complex), POINTER(mv_plan_complex), c_uint]
    solver_init_advanced_complex.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2729
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'solver_init_complex'):
        continue
    solver_init_complex = _lib.solver_init_complex
    solver_init_complex.argtypes = [POINTER(solver_plan_complex), POINTER(mv_plan_complex)]
    solver_init_complex.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2730
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'solver_before_loop_complex'):
        continue
    solver_before_loop_complex = _lib.solver_before_loop_complex
    solver_before_loop_complex.argtypes = [POINTER(solver_plan_complex)]
    solver_before_loop_complex.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2731
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'solver_loop_one_step_complex'):
        continue
    solver_loop_one_step_complex = _lib.solver_loop_one_step_complex
    solver_loop_one_step_complex.argtypes = [POINTER(solver_plan_complex)]
    solver_loop_one_step_complex.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2732
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'solver_finalize_complex'):
        continue
    solver_finalize_complex = _lib.solver_finalize_complex
    solver_finalize_complex.argtypes = [POINTER(solver_plan_complex)]
    solver_finalize_complex.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2763
class struct_anon_19(Structure):
    pass

struct_anon_19.__slots__ = [
    'mv',
    'flags',
    'w',
    'w_hat',
    'y',
    'f_hat_iter',
    'r_iter',
    'z_hat_iter',
    'p_hat_iter',
    'v_iter',
    'alpha_iter',
    'beta_iter',
    'dot_r_iter',
    'dot_r_iter_old',
    'dot_z_hat_iter',
    'dot_z_hat_iter_old',
    'dot_p_hat_iter',
    'dot_v_iter',
]
struct_anon_19._fields_ = [
    ('mv', POINTER(mv_plan_double)),
    ('flags', c_uint),
    ('w', POINTER(c_double)),
    ('w_hat', POINTER(c_double)),
    ('y', POINTER(c_double)),
    ('f_hat_iter', POINTER(c_double)),
    ('r_iter', POINTER(c_double)),
    ('z_hat_iter', POINTER(c_double)),
    ('p_hat_iter', POINTER(c_double)),
    ('v_iter', POINTER(c_double)),
    ('alpha_iter', c_double),
    ('beta_iter', c_double),
    ('dot_r_iter', c_double),
    ('dot_r_iter_old', c_double),
    ('dot_z_hat_iter', c_double),
    ('dot_z_hat_iter_old', c_double),
    ('dot_p_hat_iter', c_double),
    ('dot_v_iter', c_double),
]

solver_plan_double = struct_anon_19 # /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2763

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2765
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'solver_init_advanced_double'):
        continue
    solver_init_advanced_double = _lib.solver_init_advanced_double
    solver_init_advanced_double.argtypes = [POINTER(solver_plan_double), POINTER(mv_plan_double), c_uint]
    solver_init_advanced_double.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2766
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'solver_init_double'):
        continue
    solver_init_double = _lib.solver_init_double
    solver_init_double.argtypes = [POINTER(solver_plan_double), POINTER(mv_plan_double)]
    solver_init_double.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2767
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'solver_before_loop_double'):
        continue
    solver_before_loop_double = _lib.solver_before_loop_double
    solver_before_loop_double.argtypes = [POINTER(solver_plan_double)]
    solver_before_loop_double.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2768
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'solver_loop_one_step_double'):
        continue
    solver_loop_one_step_double = _lib.solver_loop_one_step_double
    solver_loop_one_step_double.argtypes = [POINTER(solver_plan_double)]
    solver_loop_one_step_double.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2769
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'solver_finalize_double'):
        continue
    solver_finalize_double = _lib.solver_finalize_double
    solver_finalize_double.argtypes = [POINTER(solver_plan_double)]
    solver_finalize_double.restype = None
    break

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 137
try:
    PRE_PHI_HUT = (1 << 0)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 150
try:
    FG_PSI = (1 << 1)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 167
try:
    PRE_LIN_PSI = (1 << 2)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 180
try:
    PRE_FG_PSI = (1 << 3)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 192
try:
    PRE_PSI = (1 << 4)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 205
try:
    PRE_FULL_PSI = (1 << 5)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 216
try:
    MALLOC_X = (1 << 6)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 228
try:
    MALLOC_F_HAT = (1 << 7)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 239
try:
    MALLOC_F = (1 << 8)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 250
try:
    FFT_OUT_OF_PLACE = (1 << 9)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 261
try:
    FFTW_INIT = (1 << 10)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 276
try:
    PRE_ONE_PSI = (((PRE_LIN_PSI | PRE_FG_PSI) | PRE_PSI) | PRE_FULL_PSI)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1010
try:
    MALLOC_V = (1 << 11)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1221
try:
    NSDFT = (1 << 12)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1770
try:
    NFSFT_NORMALIZED = (1 << 0)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1782
try:
    NFSFT_USE_NDFT = (1 << 1)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1795
try:
    NFSFT_USE_DPT = (1 << 2)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1810
try:
    NFSFT_MALLOC_X = (1 << 3)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1825
try:
    NFSFT_MALLOC_F_HAT = (1 << 5)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1840
try:
    NFSFT_MALLOC_F = (1 << 6)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1852
try:
    NFSFT_PRESERVE_F_HAT = (1 << 7)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1865
try:
    NFSFT_PRESERVE_X = (1 << 8)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1877
try:
    NFSFT_PRESERVE_F = (1 << 9)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1888
try:
    NFSFT_DESTROY_F_HAT = (1 << 10)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1900
try:
    NFSFT_DESTROY_X = (1 << 11)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1911
try:
    NFSFT_DESTROY_F = (1 << 12)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1924
try:
    NFSFT_NO_DIRECT_ALGORITHM = (1 << 13)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1935
try:
    NFSFT_NO_FAST_ALGORITHM = (1 << 14)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1944
try:
    NFSFT_ZERO_F_HAT = (1 << 16)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1956
def NFSFT_INDEX(k, n, plan):
    return ((((((2 * ((plan.contents.N).value)) + 2) * ((((plan.contents.N).value) - n) + 1)) + ((plan.contents.N).value)) + k) + 1)

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 1962
def NFSFT_F_HAT_SIZE(N):
    return (((2 * N) + 2) * ((2 * N) + 2))

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2136
try:
    FPT_NO_FAST_ALGORITHM = (1 << 2)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2137
try:
    FPT_NO_DIRECT_ALGORITHM = (1 << 3)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2138
try:
    FPT_NO_STABILIZATION = (1 << 0)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2141
try:
    FPT_PERSISTENT_DATA = (1 << 4)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2144
try:
    FPT_FUNCTION_VALUES = (1 << 5)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2147
try:
    FPT_AL_SYMMETRY = (1 << 6)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2287
try:
    NFSOFT_NORMALIZED = (1 << 0)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2299
try:
    NFSOFT_USE_NDFT = (1 << 1)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2311
try:
    NFSOFT_USE_DPT = (1 << 2)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2326
try:
    NFSOFT_MALLOC_X = (1 << 3)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2335
try:
    NFSOFT_REPRESENT = (1 << 4)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2351
try:
    NFSOFT_MALLOC_F_HAT = (1 << 5)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2366
try:
    NFSOFT_MALLOC_F = (1 << 6)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2378
try:
    NFSOFT_PRESERVE_F_HAT = (1 << 7)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2391
try:
    NFSOFT_PRESERVE_X = (1 << 8)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2403
try:
    NFSOFT_PRESERVE_F = (1 << 9)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2414
try:
    NFSOFT_DESTROY_F_HAT = (1 << 10)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2426
try:
    NFSOFT_DESTROY_X = (1 << 11)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2437
try:
    NFSOFT_DESTROY_F = (1 << 12)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2447
try:
    NFSOFT_NO_STABILIZATION = (1 << 13)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2458
try:
    NFSOFT_CHOOSE_DPT = (1 << 14)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2470
try:
    NFSOFT_SOFT = (1 << 15)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2480
try:
    NFSOFT_ZERO_F_HAT = (1 << 16)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2489
def NFSOFT_INDEX(m, n, l, B):
    return ((l + (B + 1)) + (((2 * B) + 2) * ((n + (B + 1)) + (((2 * B) + 2) * (m + (B + 1))))))

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2497
def NFSOFT_F_HAT_SIZE(B):
    return (((B + 1) * (((4 * (B + 1)) * (B + 1)) - 1)) / 3)

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2644
try:
    LANDWEBER = (1 << 0)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2652
try:
    STEEPEST_DESCENT = (1 << 1)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2661
try:
    CGNR = (1 << 2)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2670
try:
    CGNE = (1 << 3)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2678
try:
    NORMS_FOR_LANDWEBER = (1 << 4)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2686
try:
    PRECOMPUTE_WEIGHT = (1 << 5)
except:
    pass

# /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2694
try:
    PRECOMPUTE_DAMP = (1 << 6)
except:
    pass

fpt_set_s_ = struct_fpt_set_s_ # /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2150

nfsoft_plan_ = struct_nfsoft_plan_ # /home/eric/Downloads/nfft-3.1.3/include/nfft3.h: 2523

# No inserted files

