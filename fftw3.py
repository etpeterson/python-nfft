'''Wrapper for fftw3.h

Generated with:
/usr/local/bin/ctypesgen.py fftw3.h -o /home/eric/fftw3.py

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

# /usr/include/bits/types.h: 62
class struct_anon_1(Structure):
    pass

struct_anon_1.__slots__ = [
    '__val',
]
struct_anon_1._fields_ = [
    ('__val', c_long * 2),
]

__quad_t = struct_anon_1 # /usr/include/bits/types.h: 62

__off_t = c_long # /usr/include/bits/types.h: 141

__off64_t = __quad_t # /usr/include/bits/types.h: 142

# /usr/include/libio.h: 271
class struct__IO_FILE(Structure):
    pass

FILE = struct__IO_FILE # /usr/include/stdio.h: 49

_IO_lock_t = None # /usr/include/libio.h: 180

# /usr/include/libio.h: 186
class struct__IO_marker(Structure):
    pass

struct__IO_marker.__slots__ = [
    '_next',
    '_sbuf',
    '_pos',
]
struct__IO_marker._fields_ = [
    ('_next', POINTER(struct__IO_marker)),
    ('_sbuf', POINTER(struct__IO_FILE)),
    ('_pos', c_int),
]

struct__IO_FILE.__slots__ = [
    '_flags',
    '_IO_read_ptr',
    '_IO_read_end',
    '_IO_read_base',
    '_IO_write_base',
    '_IO_write_ptr',
    '_IO_write_end',
    '_IO_buf_base',
    '_IO_buf_end',
    '_IO_save_base',
    '_IO_backup_base',
    '_IO_save_end',
    '_markers',
    '_chain',
    '_fileno',
    '_flags2',
    '_old_offset',
    '_cur_column',
    '_vtable_offset',
    '_shortbuf',
    '_lock',
    '_offset',
    '__pad1',
    '__pad2',
    '__pad3',
    '__pad4',
    '__pad5',
    '_mode',
    '_unused2',
]
struct__IO_FILE._fields_ = [
    ('_flags', c_int),
    ('_IO_read_ptr', String),
    ('_IO_read_end', String),
    ('_IO_read_base', String),
    ('_IO_write_base', String),
    ('_IO_write_ptr', String),
    ('_IO_write_end', String),
    ('_IO_buf_base', String),
    ('_IO_buf_end', String),
    ('_IO_save_base', String),
    ('_IO_backup_base', String),
    ('_IO_save_end', String),
    ('_markers', POINTER(struct__IO_marker)),
    ('_chain', POINTER(struct__IO_FILE)),
    ('_fileno', c_int),
    ('_flags2', c_int),
    ('_old_offset', __off_t),
    ('_cur_column', c_ushort),
    ('_vtable_offset', c_char),
    ('_shortbuf', c_char * 1),
    ('_lock', POINTER(_IO_lock_t)),
    ('_offset', __off64_t),
    ('__pad1', POINTER(None)),
    ('__pad2', POINTER(None)),
    ('__pad3', POINTER(None)),
    ('__pad4', POINTER(None)),
    ('__pad5', c_size_t),
    ('_mode', c_int),
    ('_unused2', c_char * (((15 * sizeof(c_int)) - (4 * sizeof(POINTER(None)))) - sizeof(c_size_t))),
]

enum_fftw_r2r_kind_do_not_use_me = c_int # /usr/include/fftw3.h: 88

FFTW_R2HC = 0 # /usr/include/fftw3.h: 88

FFTW_HC2R = 1 # /usr/include/fftw3.h: 88

FFTW_DHT = 2 # /usr/include/fftw3.h: 88

FFTW_REDFT00 = 3 # /usr/include/fftw3.h: 88

FFTW_REDFT01 = 4 # /usr/include/fftw3.h: 88

FFTW_REDFT10 = 5 # /usr/include/fftw3.h: 88

FFTW_REDFT11 = 6 # /usr/include/fftw3.h: 88

FFTW_RODFT00 = 7 # /usr/include/fftw3.h: 88

FFTW_RODFT01 = 8 # /usr/include/fftw3.h: 88

FFTW_RODFT10 = 9 # /usr/include/fftw3.h: 88

FFTW_RODFT11 = 10 # /usr/include/fftw3.h: 88

# /usr/include/fftw3.h: 94
class struct_fftw_iodim_do_not_use_me(Structure):
    pass

struct_fftw_iodim_do_not_use_me.__slots__ = [
    'n',
    '_is',
    'os',
]
struct_fftw_iodim_do_not_use_me._fields_ = [
    ('n', c_int),
    ('_is', c_int),
    ('os', c_int),
]

# /usr/include/fftw3.h: 101
class struct_fftw_iodim64_do_not_use_me(Structure):
    pass

struct_fftw_iodim64_do_not_use_me.__slots__ = [
    'n',
    '_is',
    'os',
]
struct_fftw_iodim64_do_not_use_me._fields_ = [
    ('n', c_ptrdiff_t),
    ('_is', c_ptrdiff_t),
    ('os', c_ptrdiff_t),
]

fftw_complex = c_double * 2 # /usr/include/fftw3.h: 341

# /usr/include/fftw3.h: 341
class struct_fftw_plan_s(Structure):
    pass

fftw_plan = POINTER(struct_fftw_plan_s) # /usr/include/fftw3.h: 341

fftw_iodim = struct_fftw_iodim_do_not_use_me # /usr/include/fftw3.h: 341

fftw_iodim64 = struct_fftw_iodim64_do_not_use_me # /usr/include/fftw3.h: 341

fftw_r2r_kind = enum_fftw_r2r_kind_do_not_use_me # /usr/include/fftw3.h: 341

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_execute'):
        continue
    fftw_execute = _lib.fftw_execute
    fftw_execute.argtypes = [fftw_plan]
    fftw_execute.restype = None
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_dft'):
        continue
    fftw_plan_dft = _lib.fftw_plan_dft
    fftw_plan_dft.argtypes = [c_int, POINTER(c_int), POINTER(fftw_complex), POINTER(fftw_complex), c_int, c_uint]
    fftw_plan_dft.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_dft_1d'):
        continue
    fftw_plan_dft_1d = _lib.fftw_plan_dft_1d
    fftw_plan_dft_1d.argtypes = [c_int, POINTER(fftw_complex), POINTER(fftw_complex), c_int, c_uint]
    fftw_plan_dft_1d.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_dft_2d'):
        continue
    fftw_plan_dft_2d = _lib.fftw_plan_dft_2d
    fftw_plan_dft_2d.argtypes = [c_int, c_int, POINTER(fftw_complex), POINTER(fftw_complex), c_int, c_uint]
    fftw_plan_dft_2d.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_dft_3d'):
        continue
    fftw_plan_dft_3d = _lib.fftw_plan_dft_3d
    fftw_plan_dft_3d.argtypes = [c_int, c_int, c_int, POINTER(fftw_complex), POINTER(fftw_complex), c_int, c_uint]
    fftw_plan_dft_3d.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_many_dft'):
        continue
    fftw_plan_many_dft = _lib.fftw_plan_many_dft
    fftw_plan_many_dft.argtypes = [c_int, POINTER(c_int), c_int, POINTER(fftw_complex), POINTER(c_int), c_int, c_int, POINTER(fftw_complex), POINTER(c_int), c_int, c_int, c_int, c_uint]
    fftw_plan_many_dft.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_guru_dft'):
        continue
    fftw_plan_guru_dft = _lib.fftw_plan_guru_dft
    fftw_plan_guru_dft.argtypes = [c_int, POINTER(fftw_iodim), c_int, POINTER(fftw_iodim), POINTER(fftw_complex), POINTER(fftw_complex), c_int, c_uint]
    fftw_plan_guru_dft.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_guru_split_dft'):
        continue
    fftw_plan_guru_split_dft = _lib.fftw_plan_guru_split_dft
    fftw_plan_guru_split_dft.argtypes = [c_int, POINTER(fftw_iodim), c_int, POINTER(fftw_iodim), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), c_uint]
    fftw_plan_guru_split_dft.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_guru64_dft'):
        continue
    fftw_plan_guru64_dft = _lib.fftw_plan_guru64_dft
    fftw_plan_guru64_dft.argtypes = [c_int, POINTER(fftw_iodim64), c_int, POINTER(fftw_iodim64), POINTER(fftw_complex), POINTER(fftw_complex), c_int, c_uint]
    fftw_plan_guru64_dft.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_guru64_split_dft'):
        continue
    fftw_plan_guru64_split_dft = _lib.fftw_plan_guru64_split_dft
    fftw_plan_guru64_split_dft.argtypes = [c_int, POINTER(fftw_iodim64), c_int, POINTER(fftw_iodim64), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), c_uint]
    fftw_plan_guru64_split_dft.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_execute_dft'):
        continue
    fftw_execute_dft = _lib.fftw_execute_dft
    fftw_execute_dft.argtypes = [fftw_plan, POINTER(fftw_complex), POINTER(fftw_complex)]
    fftw_execute_dft.restype = None
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_execute_split_dft'):
        continue
    fftw_execute_split_dft = _lib.fftw_execute_split_dft
    fftw_execute_split_dft.argtypes = [fftw_plan, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    fftw_execute_split_dft.restype = None
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_many_dft_r2c'):
        continue
    fftw_plan_many_dft_r2c = _lib.fftw_plan_many_dft_r2c
    fftw_plan_many_dft_r2c.argtypes = [c_int, POINTER(c_int), c_int, POINTER(c_double), POINTER(c_int), c_int, c_int, POINTER(fftw_complex), POINTER(c_int), c_int, c_int, c_uint]
    fftw_plan_many_dft_r2c.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_dft_r2c'):
        continue
    fftw_plan_dft_r2c = _lib.fftw_plan_dft_r2c
    fftw_plan_dft_r2c.argtypes = [c_int, POINTER(c_int), POINTER(c_double), POINTER(fftw_complex), c_uint]
    fftw_plan_dft_r2c.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_dft_r2c_1d'):
        continue
    fftw_plan_dft_r2c_1d = _lib.fftw_plan_dft_r2c_1d
    fftw_plan_dft_r2c_1d.argtypes = [c_int, POINTER(c_double), POINTER(fftw_complex), c_uint]
    fftw_plan_dft_r2c_1d.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_dft_r2c_2d'):
        continue
    fftw_plan_dft_r2c_2d = _lib.fftw_plan_dft_r2c_2d
    fftw_plan_dft_r2c_2d.argtypes = [c_int, c_int, POINTER(c_double), POINTER(fftw_complex), c_uint]
    fftw_plan_dft_r2c_2d.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_dft_r2c_3d'):
        continue
    fftw_plan_dft_r2c_3d = _lib.fftw_plan_dft_r2c_3d
    fftw_plan_dft_r2c_3d.argtypes = [c_int, c_int, c_int, POINTER(c_double), POINTER(fftw_complex), c_uint]
    fftw_plan_dft_r2c_3d.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_many_dft_c2r'):
        continue
    fftw_plan_many_dft_c2r = _lib.fftw_plan_many_dft_c2r
    fftw_plan_many_dft_c2r.argtypes = [c_int, POINTER(c_int), c_int, POINTER(fftw_complex), POINTER(c_int), c_int, c_int, POINTER(c_double), POINTER(c_int), c_int, c_int, c_uint]
    fftw_plan_many_dft_c2r.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_dft_c2r'):
        continue
    fftw_plan_dft_c2r = _lib.fftw_plan_dft_c2r
    fftw_plan_dft_c2r.argtypes = [c_int, POINTER(c_int), POINTER(fftw_complex), POINTER(c_double), c_uint]
    fftw_plan_dft_c2r.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_dft_c2r_1d'):
        continue
    fftw_plan_dft_c2r_1d = _lib.fftw_plan_dft_c2r_1d
    fftw_plan_dft_c2r_1d.argtypes = [c_int, POINTER(fftw_complex), POINTER(c_double), c_uint]
    fftw_plan_dft_c2r_1d.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_dft_c2r_2d'):
        continue
    fftw_plan_dft_c2r_2d = _lib.fftw_plan_dft_c2r_2d
    fftw_plan_dft_c2r_2d.argtypes = [c_int, c_int, POINTER(fftw_complex), POINTER(c_double), c_uint]
    fftw_plan_dft_c2r_2d.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_dft_c2r_3d'):
        continue
    fftw_plan_dft_c2r_3d = _lib.fftw_plan_dft_c2r_3d
    fftw_plan_dft_c2r_3d.argtypes = [c_int, c_int, c_int, POINTER(fftw_complex), POINTER(c_double), c_uint]
    fftw_plan_dft_c2r_3d.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_guru_dft_r2c'):
        continue
    fftw_plan_guru_dft_r2c = _lib.fftw_plan_guru_dft_r2c
    fftw_plan_guru_dft_r2c.argtypes = [c_int, POINTER(fftw_iodim), c_int, POINTER(fftw_iodim), POINTER(c_double), POINTER(fftw_complex), c_uint]
    fftw_plan_guru_dft_r2c.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_guru_dft_c2r'):
        continue
    fftw_plan_guru_dft_c2r = _lib.fftw_plan_guru_dft_c2r
    fftw_plan_guru_dft_c2r.argtypes = [c_int, POINTER(fftw_iodim), c_int, POINTER(fftw_iodim), POINTER(fftw_complex), POINTER(c_double), c_uint]
    fftw_plan_guru_dft_c2r.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_guru_split_dft_r2c'):
        continue
    fftw_plan_guru_split_dft_r2c = _lib.fftw_plan_guru_split_dft_r2c
    fftw_plan_guru_split_dft_r2c.argtypes = [c_int, POINTER(fftw_iodim), c_int, POINTER(fftw_iodim), POINTER(c_double), POINTER(c_double), POINTER(c_double), c_uint]
    fftw_plan_guru_split_dft_r2c.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_guru_split_dft_c2r'):
        continue
    fftw_plan_guru_split_dft_c2r = _lib.fftw_plan_guru_split_dft_c2r
    fftw_plan_guru_split_dft_c2r.argtypes = [c_int, POINTER(fftw_iodim), c_int, POINTER(fftw_iodim), POINTER(c_double), POINTER(c_double), POINTER(c_double), c_uint]
    fftw_plan_guru_split_dft_c2r.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_guru64_dft_r2c'):
        continue
    fftw_plan_guru64_dft_r2c = _lib.fftw_plan_guru64_dft_r2c
    fftw_plan_guru64_dft_r2c.argtypes = [c_int, POINTER(fftw_iodim64), c_int, POINTER(fftw_iodim64), POINTER(c_double), POINTER(fftw_complex), c_uint]
    fftw_plan_guru64_dft_r2c.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_guru64_dft_c2r'):
        continue
    fftw_plan_guru64_dft_c2r = _lib.fftw_plan_guru64_dft_c2r
    fftw_plan_guru64_dft_c2r.argtypes = [c_int, POINTER(fftw_iodim64), c_int, POINTER(fftw_iodim64), POINTER(fftw_complex), POINTER(c_double), c_uint]
    fftw_plan_guru64_dft_c2r.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_guru64_split_dft_r2c'):
        continue
    fftw_plan_guru64_split_dft_r2c = _lib.fftw_plan_guru64_split_dft_r2c
    fftw_plan_guru64_split_dft_r2c.argtypes = [c_int, POINTER(fftw_iodim64), c_int, POINTER(fftw_iodim64), POINTER(c_double), POINTER(c_double), POINTER(c_double), c_uint]
    fftw_plan_guru64_split_dft_r2c.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_guru64_split_dft_c2r'):
        continue
    fftw_plan_guru64_split_dft_c2r = _lib.fftw_plan_guru64_split_dft_c2r
    fftw_plan_guru64_split_dft_c2r.argtypes = [c_int, POINTER(fftw_iodim64), c_int, POINTER(fftw_iodim64), POINTER(c_double), POINTER(c_double), POINTER(c_double), c_uint]
    fftw_plan_guru64_split_dft_c2r.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_execute_dft_r2c'):
        continue
    fftw_execute_dft_r2c = _lib.fftw_execute_dft_r2c
    fftw_execute_dft_r2c.argtypes = [fftw_plan, POINTER(c_double), POINTER(fftw_complex)]
    fftw_execute_dft_r2c.restype = None
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_execute_dft_c2r'):
        continue
    fftw_execute_dft_c2r = _lib.fftw_execute_dft_c2r
    fftw_execute_dft_c2r.argtypes = [fftw_plan, POINTER(fftw_complex), POINTER(c_double)]
    fftw_execute_dft_c2r.restype = None
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_execute_split_dft_r2c'):
        continue
    fftw_execute_split_dft_r2c = _lib.fftw_execute_split_dft_r2c
    fftw_execute_split_dft_r2c.argtypes = [fftw_plan, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    fftw_execute_split_dft_r2c.restype = None
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_execute_split_dft_c2r'):
        continue
    fftw_execute_split_dft_c2r = _lib.fftw_execute_split_dft_c2r
    fftw_execute_split_dft_c2r.argtypes = [fftw_plan, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    fftw_execute_split_dft_c2r.restype = None
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_many_r2r'):
        continue
    fftw_plan_many_r2r = _lib.fftw_plan_many_r2r
    fftw_plan_many_r2r.argtypes = [c_int, POINTER(c_int), c_int, POINTER(c_double), POINTER(c_int), c_int, c_int, POINTER(c_double), POINTER(c_int), c_int, c_int, POINTER(fftw_r2r_kind), c_uint]
    fftw_plan_many_r2r.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_r2r'):
        continue
    fftw_plan_r2r = _lib.fftw_plan_r2r
    fftw_plan_r2r.argtypes = [c_int, POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(fftw_r2r_kind), c_uint]
    fftw_plan_r2r.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_r2r_1d'):
        continue
    fftw_plan_r2r_1d = _lib.fftw_plan_r2r_1d
    fftw_plan_r2r_1d.argtypes = [c_int, POINTER(c_double), POINTER(c_double), fftw_r2r_kind, c_uint]
    fftw_plan_r2r_1d.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_r2r_2d'):
        continue
    fftw_plan_r2r_2d = _lib.fftw_plan_r2r_2d
    fftw_plan_r2r_2d.argtypes = [c_int, c_int, POINTER(c_double), POINTER(c_double), fftw_r2r_kind, fftw_r2r_kind, c_uint]
    fftw_plan_r2r_2d.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_r2r_3d'):
        continue
    fftw_plan_r2r_3d = _lib.fftw_plan_r2r_3d
    fftw_plan_r2r_3d.argtypes = [c_int, c_int, c_int, POINTER(c_double), POINTER(c_double), fftw_r2r_kind, fftw_r2r_kind, fftw_r2r_kind, c_uint]
    fftw_plan_r2r_3d.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_guru_r2r'):
        continue
    fftw_plan_guru_r2r = _lib.fftw_plan_guru_r2r
    fftw_plan_guru_r2r.argtypes = [c_int, POINTER(fftw_iodim), c_int, POINTER(fftw_iodim), POINTER(c_double), POINTER(c_double), POINTER(fftw_r2r_kind), c_uint]
    fftw_plan_guru_r2r.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_guru64_r2r'):
        continue
    fftw_plan_guru64_r2r = _lib.fftw_plan_guru64_r2r
    fftw_plan_guru64_r2r.argtypes = [c_int, POINTER(fftw_iodim64), c_int, POINTER(fftw_iodim64), POINTER(c_double), POINTER(c_double), POINTER(fftw_r2r_kind), c_uint]
    fftw_plan_guru64_r2r.restype = fftw_plan
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_execute_r2r'):
        continue
    fftw_execute_r2r = _lib.fftw_execute_r2r
    fftw_execute_r2r.argtypes = [fftw_plan, POINTER(c_double), POINTER(c_double)]
    fftw_execute_r2r.restype = None
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_destroy_plan'):
        continue
    fftw_destroy_plan = _lib.fftw_destroy_plan
    fftw_destroy_plan.argtypes = [fftw_plan]
    fftw_destroy_plan.restype = None
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_forget_wisdom'):
        continue
    fftw_forget_wisdom = _lib.fftw_forget_wisdom
    fftw_forget_wisdom.argtypes = []
    fftw_forget_wisdom.restype = None
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_cleanup'):
        continue
    fftw_cleanup = _lib.fftw_cleanup
    fftw_cleanup.argtypes = []
    fftw_cleanup.restype = None
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_set_timelimit'):
        continue
    fftw_set_timelimit = _lib.fftw_set_timelimit
    fftw_set_timelimit.argtypes = [c_double]
    fftw_set_timelimit.restype = None
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_plan_with_nthreads'):
        continue
    fftw_plan_with_nthreads = _lib.fftw_plan_with_nthreads
    fftw_plan_with_nthreads.argtypes = [c_int]
    fftw_plan_with_nthreads.restype = None
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_init_threads'):
        continue
    fftw_init_threads = _lib.fftw_init_threads
    fftw_init_threads.argtypes = []
    fftw_init_threads.restype = c_int
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_cleanup_threads'):
        continue
    fftw_cleanup_threads = _lib.fftw_cleanup_threads
    fftw_cleanup_threads.argtypes = []
    fftw_cleanup_threads.restype = None
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_export_wisdom_to_file'):
        continue
    fftw_export_wisdom_to_file = _lib.fftw_export_wisdom_to_file
    fftw_export_wisdom_to_file.argtypes = [POINTER(FILE)]
    fftw_export_wisdom_to_file.restype = None
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_export_wisdom_to_string'):
        continue
    fftw_export_wisdom_to_string = _lib.fftw_export_wisdom_to_string
    fftw_export_wisdom_to_string.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        fftw_export_wisdom_to_string.restype = ReturnString
    else:
        fftw_export_wisdom_to_string.restype = String
        fftw_export_wisdom_to_string.errcheck = ReturnString
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_export_wisdom'):
        continue
    fftw_export_wisdom = _lib.fftw_export_wisdom
    fftw_export_wisdom.argtypes = [CFUNCTYPE(UNCHECKED(None), c_char, POINTER(None)), POINTER(None)]
    fftw_export_wisdom.restype = None
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_import_system_wisdom'):
        continue
    fftw_import_system_wisdom = _lib.fftw_import_system_wisdom
    fftw_import_system_wisdom.argtypes = []
    fftw_import_system_wisdom.restype = c_int
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_import_wisdom_from_file'):
        continue
    fftw_import_wisdom_from_file = _lib.fftw_import_wisdom_from_file
    fftw_import_wisdom_from_file.argtypes = [POINTER(FILE)]
    fftw_import_wisdom_from_file.restype = c_int
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_import_wisdom_from_string'):
        continue
    fftw_import_wisdom_from_string = _lib.fftw_import_wisdom_from_string
    fftw_import_wisdom_from_string.argtypes = [String]
    fftw_import_wisdom_from_string.restype = c_int
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_import_wisdom'):
        continue
    fftw_import_wisdom = _lib.fftw_import_wisdom
    fftw_import_wisdom.argtypes = [CFUNCTYPE(UNCHECKED(c_int), POINTER(None)), POINTER(None)]
    fftw_import_wisdom.restype = c_int
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_fprint_plan'):
        continue
    fftw_fprint_plan = _lib.fftw_fprint_plan
    fftw_fprint_plan.argtypes = [fftw_plan, POINTER(FILE)]
    fftw_fprint_plan.restype = None
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_print_plan'):
        continue
    fftw_print_plan = _lib.fftw_print_plan
    fftw_print_plan.argtypes = [fftw_plan]
    fftw_print_plan.restype = None
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_malloc'):
        continue
    fftw_malloc = _lib.fftw_malloc
    fftw_malloc.argtypes = [c_size_t]
    fftw_malloc.restype = POINTER(None)
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_free'):
        continue
    fftw_free = _lib.fftw_free
    fftw_free.argtypes = [POINTER(None)]
    fftw_free.restype = None
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_flops'):
        continue
    fftw_flops = _lib.fftw_flops
    fftw_flops.argtypes = [fftw_plan, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    fftw_flops.restype = None
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftw_estimate_cost'):
        continue
    fftw_estimate_cost = _lib.fftw_estimate_cost
    fftw_estimate_cost.argtypes = [fftw_plan]
    fftw_estimate_cost.restype = c_double
    break

# /usr/include/fftw3.h: 341
for _lib in _libs.values():
    try:
        fftw_version = (POINTER(c_char)).in_dll(_lib, 'fftw_version')
        break
    except:
        pass

# /usr/include/fftw3.h: 341
for _lib in _libs.values():
    try:
        fftw_cc = (POINTER(c_char)).in_dll(_lib, 'fftw_cc')
        break
    except:
        pass

# /usr/include/fftw3.h: 341
for _lib in _libs.values():
    try:
        fftw_codelet_optim = (POINTER(c_char)).in_dll(_lib, 'fftw_codelet_optim')
        break
    except:
        pass

fftwf_complex = c_float * 2 # /usr/include/fftw3.h: 342

# /usr/include/fftw3.h: 342
class struct_fftwf_plan_s(Structure):
    pass

fftwf_plan = POINTER(struct_fftwf_plan_s) # /usr/include/fftw3.h: 342

fftwf_iodim = struct_fftw_iodim_do_not_use_me # /usr/include/fftw3.h: 342

fftwf_iodim64 = struct_fftw_iodim64_do_not_use_me # /usr/include/fftw3.h: 342

fftwf_r2r_kind = enum_fftw_r2r_kind_do_not_use_me # /usr/include/fftw3.h: 342

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_execute'):
        continue
    fftwf_execute = _lib.fftwf_execute
    fftwf_execute.argtypes = [fftwf_plan]
    fftwf_execute.restype = None
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_dft'):
        continue
    fftwf_plan_dft = _lib.fftwf_plan_dft
    fftwf_plan_dft.argtypes = [c_int, POINTER(c_int), POINTER(fftwf_complex), POINTER(fftwf_complex), c_int, c_uint]
    fftwf_plan_dft.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_dft_1d'):
        continue
    fftwf_plan_dft_1d = _lib.fftwf_plan_dft_1d
    fftwf_plan_dft_1d.argtypes = [c_int, POINTER(fftwf_complex), POINTER(fftwf_complex), c_int, c_uint]
    fftwf_plan_dft_1d.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_dft_2d'):
        continue
    fftwf_plan_dft_2d = _lib.fftwf_plan_dft_2d
    fftwf_plan_dft_2d.argtypes = [c_int, c_int, POINTER(fftwf_complex), POINTER(fftwf_complex), c_int, c_uint]
    fftwf_plan_dft_2d.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_dft_3d'):
        continue
    fftwf_plan_dft_3d = _lib.fftwf_plan_dft_3d
    fftwf_plan_dft_3d.argtypes = [c_int, c_int, c_int, POINTER(fftwf_complex), POINTER(fftwf_complex), c_int, c_uint]
    fftwf_plan_dft_3d.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_many_dft'):
        continue
    fftwf_plan_many_dft = _lib.fftwf_plan_many_dft
    fftwf_plan_many_dft.argtypes = [c_int, POINTER(c_int), c_int, POINTER(fftwf_complex), POINTER(c_int), c_int, c_int, POINTER(fftwf_complex), POINTER(c_int), c_int, c_int, c_int, c_uint]
    fftwf_plan_many_dft.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_guru_dft'):
        continue
    fftwf_plan_guru_dft = _lib.fftwf_plan_guru_dft
    fftwf_plan_guru_dft.argtypes = [c_int, POINTER(fftwf_iodim), c_int, POINTER(fftwf_iodim), POINTER(fftwf_complex), POINTER(fftwf_complex), c_int, c_uint]
    fftwf_plan_guru_dft.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_guru_split_dft'):
        continue
    fftwf_plan_guru_split_dft = _lib.fftwf_plan_guru_split_dft
    fftwf_plan_guru_split_dft.argtypes = [c_int, POINTER(fftwf_iodim), c_int, POINTER(fftwf_iodim), POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float), c_uint]
    fftwf_plan_guru_split_dft.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_guru64_dft'):
        continue
    fftwf_plan_guru64_dft = _lib.fftwf_plan_guru64_dft
    fftwf_plan_guru64_dft.argtypes = [c_int, POINTER(fftwf_iodim64), c_int, POINTER(fftwf_iodim64), POINTER(fftwf_complex), POINTER(fftwf_complex), c_int, c_uint]
    fftwf_plan_guru64_dft.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_guru64_split_dft'):
        continue
    fftwf_plan_guru64_split_dft = _lib.fftwf_plan_guru64_split_dft
    fftwf_plan_guru64_split_dft.argtypes = [c_int, POINTER(fftwf_iodim64), c_int, POINTER(fftwf_iodim64), POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float), c_uint]
    fftwf_plan_guru64_split_dft.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_execute_dft'):
        continue
    fftwf_execute_dft = _lib.fftwf_execute_dft
    fftwf_execute_dft.argtypes = [fftwf_plan, POINTER(fftwf_complex), POINTER(fftwf_complex)]
    fftwf_execute_dft.restype = None
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_execute_split_dft'):
        continue
    fftwf_execute_split_dft = _lib.fftwf_execute_split_dft
    fftwf_execute_split_dft.argtypes = [fftwf_plan, POINTER(c_float), POINTER(c_float), POINTER(c_float), POINTER(c_float)]
    fftwf_execute_split_dft.restype = None
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_many_dft_r2c'):
        continue
    fftwf_plan_many_dft_r2c = _lib.fftwf_plan_many_dft_r2c
    fftwf_plan_many_dft_r2c.argtypes = [c_int, POINTER(c_int), c_int, POINTER(c_float), POINTER(c_int), c_int, c_int, POINTER(fftwf_complex), POINTER(c_int), c_int, c_int, c_uint]
    fftwf_plan_many_dft_r2c.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_dft_r2c'):
        continue
    fftwf_plan_dft_r2c = _lib.fftwf_plan_dft_r2c
    fftwf_plan_dft_r2c.argtypes = [c_int, POINTER(c_int), POINTER(c_float), POINTER(fftwf_complex), c_uint]
    fftwf_plan_dft_r2c.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_dft_r2c_1d'):
        continue
    fftwf_plan_dft_r2c_1d = _lib.fftwf_plan_dft_r2c_1d
    fftwf_plan_dft_r2c_1d.argtypes = [c_int, POINTER(c_float), POINTER(fftwf_complex), c_uint]
    fftwf_plan_dft_r2c_1d.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_dft_r2c_2d'):
        continue
    fftwf_plan_dft_r2c_2d = _lib.fftwf_plan_dft_r2c_2d
    fftwf_plan_dft_r2c_2d.argtypes = [c_int, c_int, POINTER(c_float), POINTER(fftwf_complex), c_uint]
    fftwf_plan_dft_r2c_2d.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_dft_r2c_3d'):
        continue
    fftwf_plan_dft_r2c_3d = _lib.fftwf_plan_dft_r2c_3d
    fftwf_plan_dft_r2c_3d.argtypes = [c_int, c_int, c_int, POINTER(c_float), POINTER(fftwf_complex), c_uint]
    fftwf_plan_dft_r2c_3d.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_many_dft_c2r'):
        continue
    fftwf_plan_many_dft_c2r = _lib.fftwf_plan_many_dft_c2r
    fftwf_plan_many_dft_c2r.argtypes = [c_int, POINTER(c_int), c_int, POINTER(fftwf_complex), POINTER(c_int), c_int, c_int, POINTER(c_float), POINTER(c_int), c_int, c_int, c_uint]
    fftwf_plan_many_dft_c2r.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_dft_c2r'):
        continue
    fftwf_plan_dft_c2r = _lib.fftwf_plan_dft_c2r
    fftwf_plan_dft_c2r.argtypes = [c_int, POINTER(c_int), POINTER(fftwf_complex), POINTER(c_float), c_uint]
    fftwf_plan_dft_c2r.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_dft_c2r_1d'):
        continue
    fftwf_plan_dft_c2r_1d = _lib.fftwf_plan_dft_c2r_1d
    fftwf_plan_dft_c2r_1d.argtypes = [c_int, POINTER(fftwf_complex), POINTER(c_float), c_uint]
    fftwf_plan_dft_c2r_1d.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_dft_c2r_2d'):
        continue
    fftwf_plan_dft_c2r_2d = _lib.fftwf_plan_dft_c2r_2d
    fftwf_plan_dft_c2r_2d.argtypes = [c_int, c_int, POINTER(fftwf_complex), POINTER(c_float), c_uint]
    fftwf_plan_dft_c2r_2d.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_dft_c2r_3d'):
        continue
    fftwf_plan_dft_c2r_3d = _lib.fftwf_plan_dft_c2r_3d
    fftwf_plan_dft_c2r_3d.argtypes = [c_int, c_int, c_int, POINTER(fftwf_complex), POINTER(c_float), c_uint]
    fftwf_plan_dft_c2r_3d.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_guru_dft_r2c'):
        continue
    fftwf_plan_guru_dft_r2c = _lib.fftwf_plan_guru_dft_r2c
    fftwf_plan_guru_dft_r2c.argtypes = [c_int, POINTER(fftwf_iodim), c_int, POINTER(fftwf_iodim), POINTER(c_float), POINTER(fftwf_complex), c_uint]
    fftwf_plan_guru_dft_r2c.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_guru_dft_c2r'):
        continue
    fftwf_plan_guru_dft_c2r = _lib.fftwf_plan_guru_dft_c2r
    fftwf_plan_guru_dft_c2r.argtypes = [c_int, POINTER(fftwf_iodim), c_int, POINTER(fftwf_iodim), POINTER(fftwf_complex), POINTER(c_float), c_uint]
    fftwf_plan_guru_dft_c2r.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_guru_split_dft_r2c'):
        continue
    fftwf_plan_guru_split_dft_r2c = _lib.fftwf_plan_guru_split_dft_r2c
    fftwf_plan_guru_split_dft_r2c.argtypes = [c_int, POINTER(fftwf_iodim), c_int, POINTER(fftwf_iodim), POINTER(c_float), POINTER(c_float), POINTER(c_float), c_uint]
    fftwf_plan_guru_split_dft_r2c.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_guru_split_dft_c2r'):
        continue
    fftwf_plan_guru_split_dft_c2r = _lib.fftwf_plan_guru_split_dft_c2r
    fftwf_plan_guru_split_dft_c2r.argtypes = [c_int, POINTER(fftwf_iodim), c_int, POINTER(fftwf_iodim), POINTER(c_float), POINTER(c_float), POINTER(c_float), c_uint]
    fftwf_plan_guru_split_dft_c2r.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_guru64_dft_r2c'):
        continue
    fftwf_plan_guru64_dft_r2c = _lib.fftwf_plan_guru64_dft_r2c
    fftwf_plan_guru64_dft_r2c.argtypes = [c_int, POINTER(fftwf_iodim64), c_int, POINTER(fftwf_iodim64), POINTER(c_float), POINTER(fftwf_complex), c_uint]
    fftwf_plan_guru64_dft_r2c.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_guru64_dft_c2r'):
        continue
    fftwf_plan_guru64_dft_c2r = _lib.fftwf_plan_guru64_dft_c2r
    fftwf_plan_guru64_dft_c2r.argtypes = [c_int, POINTER(fftwf_iodim64), c_int, POINTER(fftwf_iodim64), POINTER(fftwf_complex), POINTER(c_float), c_uint]
    fftwf_plan_guru64_dft_c2r.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_guru64_split_dft_r2c'):
        continue
    fftwf_plan_guru64_split_dft_r2c = _lib.fftwf_plan_guru64_split_dft_r2c
    fftwf_plan_guru64_split_dft_r2c.argtypes = [c_int, POINTER(fftwf_iodim64), c_int, POINTER(fftwf_iodim64), POINTER(c_float), POINTER(c_float), POINTER(c_float), c_uint]
    fftwf_plan_guru64_split_dft_r2c.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_guru64_split_dft_c2r'):
        continue
    fftwf_plan_guru64_split_dft_c2r = _lib.fftwf_plan_guru64_split_dft_c2r
    fftwf_plan_guru64_split_dft_c2r.argtypes = [c_int, POINTER(fftwf_iodim64), c_int, POINTER(fftwf_iodim64), POINTER(c_float), POINTER(c_float), POINTER(c_float), c_uint]
    fftwf_plan_guru64_split_dft_c2r.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_execute_dft_r2c'):
        continue
    fftwf_execute_dft_r2c = _lib.fftwf_execute_dft_r2c
    fftwf_execute_dft_r2c.argtypes = [fftwf_plan, POINTER(c_float), POINTER(fftwf_complex)]
    fftwf_execute_dft_r2c.restype = None
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_execute_dft_c2r'):
        continue
    fftwf_execute_dft_c2r = _lib.fftwf_execute_dft_c2r
    fftwf_execute_dft_c2r.argtypes = [fftwf_plan, POINTER(fftwf_complex), POINTER(c_float)]
    fftwf_execute_dft_c2r.restype = None
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_execute_split_dft_r2c'):
        continue
    fftwf_execute_split_dft_r2c = _lib.fftwf_execute_split_dft_r2c
    fftwf_execute_split_dft_r2c.argtypes = [fftwf_plan, POINTER(c_float), POINTER(c_float), POINTER(c_float)]
    fftwf_execute_split_dft_r2c.restype = None
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_execute_split_dft_c2r'):
        continue
    fftwf_execute_split_dft_c2r = _lib.fftwf_execute_split_dft_c2r
    fftwf_execute_split_dft_c2r.argtypes = [fftwf_plan, POINTER(c_float), POINTER(c_float), POINTER(c_float)]
    fftwf_execute_split_dft_c2r.restype = None
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_many_r2r'):
        continue
    fftwf_plan_many_r2r = _lib.fftwf_plan_many_r2r
    fftwf_plan_many_r2r.argtypes = [c_int, POINTER(c_int), c_int, POINTER(c_float), POINTER(c_int), c_int, c_int, POINTER(c_float), POINTER(c_int), c_int, c_int, POINTER(fftwf_r2r_kind), c_uint]
    fftwf_plan_many_r2r.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_r2r'):
        continue
    fftwf_plan_r2r = _lib.fftwf_plan_r2r
    fftwf_plan_r2r.argtypes = [c_int, POINTER(c_int), POINTER(c_float), POINTER(c_float), POINTER(fftwf_r2r_kind), c_uint]
    fftwf_plan_r2r.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_r2r_1d'):
        continue
    fftwf_plan_r2r_1d = _lib.fftwf_plan_r2r_1d
    fftwf_plan_r2r_1d.argtypes = [c_int, POINTER(c_float), POINTER(c_float), fftwf_r2r_kind, c_uint]
    fftwf_plan_r2r_1d.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_r2r_2d'):
        continue
    fftwf_plan_r2r_2d = _lib.fftwf_plan_r2r_2d
    fftwf_plan_r2r_2d.argtypes = [c_int, c_int, POINTER(c_float), POINTER(c_float), fftwf_r2r_kind, fftwf_r2r_kind, c_uint]
    fftwf_plan_r2r_2d.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_r2r_3d'):
        continue
    fftwf_plan_r2r_3d = _lib.fftwf_plan_r2r_3d
    fftwf_plan_r2r_3d.argtypes = [c_int, c_int, c_int, POINTER(c_float), POINTER(c_float), fftwf_r2r_kind, fftwf_r2r_kind, fftwf_r2r_kind, c_uint]
    fftwf_plan_r2r_3d.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_guru_r2r'):
        continue
    fftwf_plan_guru_r2r = _lib.fftwf_plan_guru_r2r
    fftwf_plan_guru_r2r.argtypes = [c_int, POINTER(fftwf_iodim), c_int, POINTER(fftwf_iodim), POINTER(c_float), POINTER(c_float), POINTER(fftwf_r2r_kind), c_uint]
    fftwf_plan_guru_r2r.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_guru64_r2r'):
        continue
    fftwf_plan_guru64_r2r = _lib.fftwf_plan_guru64_r2r
    fftwf_plan_guru64_r2r.argtypes = [c_int, POINTER(fftwf_iodim64), c_int, POINTER(fftwf_iodim64), POINTER(c_float), POINTER(c_float), POINTER(fftwf_r2r_kind), c_uint]
    fftwf_plan_guru64_r2r.restype = fftwf_plan
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_execute_r2r'):
        continue
    fftwf_execute_r2r = _lib.fftwf_execute_r2r
    fftwf_execute_r2r.argtypes = [fftwf_plan, POINTER(c_float), POINTER(c_float)]
    fftwf_execute_r2r.restype = None
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_destroy_plan'):
        continue
    fftwf_destroy_plan = _lib.fftwf_destroy_plan
    fftwf_destroy_plan.argtypes = [fftwf_plan]
    fftwf_destroy_plan.restype = None
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_forget_wisdom'):
        continue
    fftwf_forget_wisdom = _lib.fftwf_forget_wisdom
    fftwf_forget_wisdom.argtypes = []
    fftwf_forget_wisdom.restype = None
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_cleanup'):
        continue
    fftwf_cleanup = _lib.fftwf_cleanup
    fftwf_cleanup.argtypes = []
    fftwf_cleanup.restype = None
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_set_timelimit'):
        continue
    fftwf_set_timelimit = _lib.fftwf_set_timelimit
    fftwf_set_timelimit.argtypes = [c_double]
    fftwf_set_timelimit.restype = None
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_plan_with_nthreads'):
        continue
    fftwf_plan_with_nthreads = _lib.fftwf_plan_with_nthreads
    fftwf_plan_with_nthreads.argtypes = [c_int]
    fftwf_plan_with_nthreads.restype = None
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_init_threads'):
        continue
    fftwf_init_threads = _lib.fftwf_init_threads
    fftwf_init_threads.argtypes = []
    fftwf_init_threads.restype = c_int
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_cleanup_threads'):
        continue
    fftwf_cleanup_threads = _lib.fftwf_cleanup_threads
    fftwf_cleanup_threads.argtypes = []
    fftwf_cleanup_threads.restype = None
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_export_wisdom_to_file'):
        continue
    fftwf_export_wisdom_to_file = _lib.fftwf_export_wisdom_to_file
    fftwf_export_wisdom_to_file.argtypes = [POINTER(FILE)]
    fftwf_export_wisdom_to_file.restype = None
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_export_wisdom_to_string'):
        continue
    fftwf_export_wisdom_to_string = _lib.fftwf_export_wisdom_to_string
    fftwf_export_wisdom_to_string.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        fftwf_export_wisdom_to_string.restype = ReturnString
    else:
        fftwf_export_wisdom_to_string.restype = String
        fftwf_export_wisdom_to_string.errcheck = ReturnString
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_export_wisdom'):
        continue
    fftwf_export_wisdom = _lib.fftwf_export_wisdom
    fftwf_export_wisdom.argtypes = [CFUNCTYPE(UNCHECKED(None), c_char, POINTER(None)), POINTER(None)]
    fftwf_export_wisdom.restype = None
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_import_system_wisdom'):
        continue
    fftwf_import_system_wisdom = _lib.fftwf_import_system_wisdom
    fftwf_import_system_wisdom.argtypes = []
    fftwf_import_system_wisdom.restype = c_int
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_import_wisdom_from_file'):
        continue
    fftwf_import_wisdom_from_file = _lib.fftwf_import_wisdom_from_file
    fftwf_import_wisdom_from_file.argtypes = [POINTER(FILE)]
    fftwf_import_wisdom_from_file.restype = c_int
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_import_wisdom_from_string'):
        continue
    fftwf_import_wisdom_from_string = _lib.fftwf_import_wisdom_from_string
    fftwf_import_wisdom_from_string.argtypes = [String]
    fftwf_import_wisdom_from_string.restype = c_int
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_import_wisdom'):
        continue
    fftwf_import_wisdom = _lib.fftwf_import_wisdom
    fftwf_import_wisdom.argtypes = [CFUNCTYPE(UNCHECKED(c_int), POINTER(None)), POINTER(None)]
    fftwf_import_wisdom.restype = c_int
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_fprint_plan'):
        continue
    fftwf_fprint_plan = _lib.fftwf_fprint_plan
    fftwf_fprint_plan.argtypes = [fftwf_plan, POINTER(FILE)]
    fftwf_fprint_plan.restype = None
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_print_plan'):
        continue
    fftwf_print_plan = _lib.fftwf_print_plan
    fftwf_print_plan.argtypes = [fftwf_plan]
    fftwf_print_plan.restype = None
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_malloc'):
        continue
    fftwf_malloc = _lib.fftwf_malloc
    fftwf_malloc.argtypes = [c_size_t]
    fftwf_malloc.restype = POINTER(None)
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_free'):
        continue
    fftwf_free = _lib.fftwf_free
    fftwf_free.argtypes = [POINTER(None)]
    fftwf_free.restype = None
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_flops'):
        continue
    fftwf_flops = _lib.fftwf_flops
    fftwf_flops.argtypes = [fftwf_plan, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    fftwf_flops.restype = None
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwf_estimate_cost'):
        continue
    fftwf_estimate_cost = _lib.fftwf_estimate_cost
    fftwf_estimate_cost.argtypes = [fftwf_plan]
    fftwf_estimate_cost.restype = c_double
    break

# /usr/include/fftw3.h: 342
for _lib in _libs.values():
    try:
        fftwf_version = (POINTER(c_char)).in_dll(_lib, 'fftwf_version')
        break
    except:
        pass

# /usr/include/fftw3.h: 342
for _lib in _libs.values():
    try:
        fftwf_cc = (POINTER(c_char)).in_dll(_lib, 'fftwf_cc')
        break
    except:
        pass

# /usr/include/fftw3.h: 342
for _lib in _libs.values():
    try:
        fftwf_codelet_optim = (POINTER(c_char)).in_dll(_lib, 'fftwf_codelet_optim')
        break
    except:
        pass

# /usr/include/fftw3.h: 343
class struct_fftwl_plan_s(Structure):
    pass

fftwl_plan = POINTER(struct_fftwl_plan_s) # /usr/include/fftw3.h: 343

fftwl_iodim = struct_fftw_iodim_do_not_use_me # /usr/include/fftw3.h: 343

fftwl_iodim64 = struct_fftw_iodim64_do_not_use_me # /usr/include/fftw3.h: 343

fftwl_r2r_kind = enum_fftw_r2r_kind_do_not_use_me # /usr/include/fftw3.h: 343

# /usr/include/fftw3.h: 343
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwl_execute'):
        continue
    fftwl_execute = _lib.fftwl_execute
    fftwl_execute.argtypes = [fftwl_plan]
    fftwl_execute.restype = None
    break

# /usr/include/fftw3.h: 343
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwl_destroy_plan'):
        continue
    fftwl_destroy_plan = _lib.fftwl_destroy_plan
    fftwl_destroy_plan.argtypes = [fftwl_plan]
    fftwl_destroy_plan.restype = None
    break

# /usr/include/fftw3.h: 343
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwl_forget_wisdom'):
        continue
    fftwl_forget_wisdom = _lib.fftwl_forget_wisdom
    fftwl_forget_wisdom.argtypes = []
    fftwl_forget_wisdom.restype = None
    break

# /usr/include/fftw3.h: 343
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwl_cleanup'):
        continue
    fftwl_cleanup = _lib.fftwl_cleanup
    fftwl_cleanup.argtypes = []
    fftwl_cleanup.restype = None
    break

# /usr/include/fftw3.h: 343
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwl_set_timelimit'):
        continue
    fftwl_set_timelimit = _lib.fftwl_set_timelimit
    fftwl_set_timelimit.argtypes = [c_double]
    fftwl_set_timelimit.restype = None
    break

# /usr/include/fftw3.h: 343
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwl_plan_with_nthreads'):
        continue
    fftwl_plan_with_nthreads = _lib.fftwl_plan_with_nthreads
    fftwl_plan_with_nthreads.argtypes = [c_int]
    fftwl_plan_with_nthreads.restype = None
    break

# /usr/include/fftw3.h: 343
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwl_init_threads'):
        continue
    fftwl_init_threads = _lib.fftwl_init_threads
    fftwl_init_threads.argtypes = []
    fftwl_init_threads.restype = c_int
    break

# /usr/include/fftw3.h: 343
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwl_cleanup_threads'):
        continue
    fftwl_cleanup_threads = _lib.fftwl_cleanup_threads
    fftwl_cleanup_threads.argtypes = []
    fftwl_cleanup_threads.restype = None
    break

# /usr/include/fftw3.h: 343
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwl_export_wisdom_to_file'):
        continue
    fftwl_export_wisdom_to_file = _lib.fftwl_export_wisdom_to_file
    fftwl_export_wisdom_to_file.argtypes = [POINTER(FILE)]
    fftwl_export_wisdom_to_file.restype = None
    break

# /usr/include/fftw3.h: 343
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwl_export_wisdom_to_string'):
        continue
    fftwl_export_wisdom_to_string = _lib.fftwl_export_wisdom_to_string
    fftwl_export_wisdom_to_string.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        fftwl_export_wisdom_to_string.restype = ReturnString
    else:
        fftwl_export_wisdom_to_string.restype = String
        fftwl_export_wisdom_to_string.errcheck = ReturnString
    break

# /usr/include/fftw3.h: 343
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwl_export_wisdom'):
        continue
    fftwl_export_wisdom = _lib.fftwl_export_wisdom
    fftwl_export_wisdom.argtypes = [CFUNCTYPE(UNCHECKED(None), c_char, POINTER(None)), POINTER(None)]
    fftwl_export_wisdom.restype = None
    break

# /usr/include/fftw3.h: 343
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwl_import_system_wisdom'):
        continue
    fftwl_import_system_wisdom = _lib.fftwl_import_system_wisdom
    fftwl_import_system_wisdom.argtypes = []
    fftwl_import_system_wisdom.restype = c_int
    break

# /usr/include/fftw3.h: 343
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwl_import_wisdom_from_file'):
        continue
    fftwl_import_wisdom_from_file = _lib.fftwl_import_wisdom_from_file
    fftwl_import_wisdom_from_file.argtypes = [POINTER(FILE)]
    fftwl_import_wisdom_from_file.restype = c_int
    break

# /usr/include/fftw3.h: 343
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwl_import_wisdom_from_string'):
        continue
    fftwl_import_wisdom_from_string = _lib.fftwl_import_wisdom_from_string
    fftwl_import_wisdom_from_string.argtypes = [String]
    fftwl_import_wisdom_from_string.restype = c_int
    break

# /usr/include/fftw3.h: 343
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwl_import_wisdom'):
        continue
    fftwl_import_wisdom = _lib.fftwl_import_wisdom
    fftwl_import_wisdom.argtypes = [CFUNCTYPE(UNCHECKED(c_int), POINTER(None)), POINTER(None)]
    fftwl_import_wisdom.restype = c_int
    break

# /usr/include/fftw3.h: 343
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwl_fprint_plan'):
        continue
    fftwl_fprint_plan = _lib.fftwl_fprint_plan
    fftwl_fprint_plan.argtypes = [fftwl_plan, POINTER(FILE)]
    fftwl_fprint_plan.restype = None
    break

# /usr/include/fftw3.h: 343
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwl_print_plan'):
        continue
    fftwl_print_plan = _lib.fftwl_print_plan
    fftwl_print_plan.argtypes = [fftwl_plan]
    fftwl_print_plan.restype = None
    break

# /usr/include/fftw3.h: 343
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwl_malloc'):
        continue
    fftwl_malloc = _lib.fftwl_malloc
    fftwl_malloc.argtypes = [c_size_t]
    fftwl_malloc.restype = POINTER(None)
    break

# /usr/include/fftw3.h: 343
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwl_free'):
        continue
    fftwl_free = _lib.fftwl_free
    fftwl_free.argtypes = [POINTER(None)]
    fftwl_free.restype = None
    break

# /usr/include/fftw3.h: 343
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwl_flops'):
        continue
    fftwl_flops = _lib.fftwl_flops
    fftwl_flops.argtypes = [fftwl_plan, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    fftwl_flops.restype = None
    break

# /usr/include/fftw3.h: 343
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'fftwl_estimate_cost'):
        continue
    fftwl_estimate_cost = _lib.fftwl_estimate_cost
    fftwl_estimate_cost.argtypes = [fftwl_plan]
    fftwl_estimate_cost.restype = c_double
    break

# /usr/include/fftw3.h: 343
for _lib in _libs.values():
    try:
        fftwl_version = (POINTER(c_char)).in_dll(_lib, 'fftwl_version')
        break
    except:
        pass

# /usr/include/fftw3.h: 343
for _lib in _libs.values():
    try:
        fftwl_cc = (POINTER(c_char)).in_dll(_lib, 'fftwl_cc')
        break
    except:
        pass

# /usr/include/fftw3.h: 343
for _lib in _libs.values():
    try:
        fftwl_codelet_optim = (POINTER(c_char)).in_dll(_lib, 'fftwl_codelet_optim')
        break
    except:
        pass

# /usr/include/fftw3.h: 345
try:
    FFTW_FORWARD = (-1)
except:
    pass

# /usr/include/fftw3.h: 346
try:
    FFTW_BACKWARD = 1
except:
    pass

# /usr/include/fftw3.h: 348
try:
    FFTW_NO_TIMELIMIT = (-1.0)
except:
    pass

# /usr/include/fftw3.h: 351
try:
    FFTW_MEASURE = 0
except:
    pass

# /usr/include/fftw3.h: 352
try:
    FFTW_DESTROY_INPUT = (1 << 0)
except:
    pass

# /usr/include/fftw3.h: 353
try:
    FFTW_UNALIGNED = (1 << 1)
except:
    pass

# /usr/include/fftw3.h: 354
try:
    FFTW_CONSERVE_MEMORY = (1 << 2)
except:
    pass

# /usr/include/fftw3.h: 355
try:
    FFTW_EXHAUSTIVE = (1 << 3)
except:
    pass

# /usr/include/fftw3.h: 356
try:
    FFTW_PRESERVE_INPUT = (1 << 4)
except:
    pass

# /usr/include/fftw3.h: 357
try:
    FFTW_PATIENT = (1 << 5)
except:
    pass

# /usr/include/fftw3.h: 358
try:
    FFTW_ESTIMATE = (1 << 6)
except:
    pass

# /usr/include/fftw3.h: 361
try:
    FFTW_ESTIMATE_PATIENT = (1 << 7)
except:
    pass

# /usr/include/fftw3.h: 362
try:
    FFTW_BELIEVE_PCOST = (1 << 8)
except:
    pass

# /usr/include/fftw3.h: 363
try:
    FFTW_NO_DFT_R2HC = (1 << 9)
except:
    pass

# /usr/include/fftw3.h: 364
try:
    FFTW_NO_NONTHREADED = (1 << 10)
except:
    pass

# /usr/include/fftw3.h: 365
try:
    FFTW_NO_BUFFERING = (1 << 11)
except:
    pass

# /usr/include/fftw3.h: 366
try:
    FFTW_NO_INDIRECT_OP = (1 << 12)
except:
    pass

# /usr/include/fftw3.h: 367
try:
    FFTW_ALLOW_LARGE_GENERIC = (1 << 13)
except:
    pass

# /usr/include/fftw3.h: 368
try:
    FFTW_NO_RANK_SPLITS = (1 << 14)
except:
    pass

# /usr/include/fftw3.h: 369
try:
    FFTW_NO_VRANK_SPLITS = (1 << 15)
except:
    pass

# /usr/include/fftw3.h: 370
try:
    FFTW_NO_VRECURSE = (1 << 16)
except:
    pass

# /usr/include/fftw3.h: 371
try:
    FFTW_NO_SIMD = (1 << 17)
except:
    pass

# /usr/include/fftw3.h: 372
try:
    FFTW_NO_SLOW = (1 << 18)
except:
    pass

# /usr/include/fftw3.h: 373
try:
    FFTW_NO_FIXED_RADIX_LARGE_N = (1 << 19)
except:
    pass

# /usr/include/fftw3.h: 374
try:
    FFTW_ALLOW_PRUNING = (1 << 20)
except:
    pass

# /usr/include/fftw3.h: 375
try:
    FFTW_WISDOM_ONLY = (1 << 21)
except:
    pass

fftw_iodim_do_not_use_me = struct_fftw_iodim_do_not_use_me # /usr/include/fftw3.h: 94

fftw_iodim64_do_not_use_me = struct_fftw_iodim64_do_not_use_me # /usr/include/fftw3.h: 101

fftw_plan_s = struct_fftw_plan_s # /usr/include/fftw3.h: 341

fftwf_plan_s = struct_fftwf_plan_s # /usr/include/fftw3.h: 342

fftwl_plan_s = struct_fftwl_plan_s # /usr/include/fftw3.h: 343

# No inserted files

