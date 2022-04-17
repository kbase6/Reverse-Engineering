from ctypes import *
from my_debugger_defines import *

#additional types not in my_debugger_defines
PVOID = c_void_p
ULONG_PTR = c_ulong
INFINITE = '0xFFFF'
LONG = c_long
BYTE = c_ubyte

PROCESS_ALL_ACCESS = 0x001F0FF

#ContinueDebugEvent Functions
DBG_CONTINUE = 0x00010002
DBG_EXCEPTION_NOT_HANDLED = 0x80010001
DBG_REPLY_LATER = 0x40010001

class EXCEPTION_RECORD(Structure):
    pass

EXCEPTION_RECORD._fields_=[
    ('ExceptionCode', DWORD),
    ('ExceptionFlags', DWORD),
    ('ExceptionRecord', POINTER(EXCEPTION_RECORD)),
    ('ExceptionAddress', PVOID),
    ('NumberParameters', DWORD),
    ('ExceptionInformation', ULONG_PTR*15)
]

class EXCEPTION_DEBUG_INFO(Structure):
    _fields_ = [
        ('ExceptionRecord', EXCEPTION_RECORD),
        ('dwFirstChance', DWORD),
    ]

class U(Union):
    _fields_ = [
        ('Exception', EXCEPTION_DEBUG_INFO),
        #('CreateThread', CREATE_THREAD_DEBUG_INFO),
        #('CreateProcessInfo', CREATE_PROCESS_DEBUG_INFO),
        #('ExitThread', EXIT_THREAD_DEBUG_INFO),
        #('ExitProcess', EXIT_PROCESS<DEBUG_INFO),
        #('LoadDll', LOAD_DLL_DEBUG_INFO),
        #('UnloadDll', UNLOAD_DLL_DEBUG_INFO),
        #('DebugString', OUTPUT_DEBUG_STRING_INFO),
        #('RipInfo', RIP_INFO)
    ]


class DEBUG_EVENT(Structure):
    _fields_ = [
        ('dwDebugEventCode', DWORD),
        ('dwProcessId',      DWORD),
        ('dwThreadId',       DWORD),
        ('u',                U)
    ]

class THREADENTRY32(Structure):
    _fields_=[
        ('dwSize',             DWORD),
        ('cntUsage',           DWORD),
        ('th32ThreadID',       DWORD),
        ('th32OwnerProcessID', DWORD),
        ('tpBasePri',          LONG),
        ('tpDeltaPri',         LONG),
        ('dwFlags',            DWORD)
    ]

class CONTEXT(Structure):
    _fields_=[
        ('ContextFlags', DWORD),
        ('Dr0',          DWORD),
        ('Dr1',          DWORD),
        ('Dr2',          DWORD),
        ('Dr3',          DWORD),
        ('Dr6',          DWORD),
        ('Dr7',          DWORD),
        ('FloatSave',    FLOATING_SAVE_AREA),
        ('SegGs',        DWORD),
        ('SegFs',        DWORD),
        ('SegDs',        DWORD),
        ('Edi',          DWORD),
        ('Esi',          DWORD),
        ('Ebx',          DWORD),
        ('Ecx',          DWORD),
        ('Eax',          DWORD),
        ('Ebp',          DWORD),
        ('Eip',          DWORD),
        ('SegCs',        DWORD),
        ('EFlags',       DWORD),
        ('Esp',          DWORD),
        ('SegSs',        DWORD),
        ('ExtendedRegisters', BYTE)
    ]