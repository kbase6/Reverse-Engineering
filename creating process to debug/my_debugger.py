from ctypes import *
from my_debugger_defines import *
from _multiprocessing import win32

kernel32 = windll.kernel32

class debugger():
    def __init__(self):
        pass

    def load(self, path_to_exe):

        #creation_flag = CREATE_NEW_CONSOLE
        creation_flags = DEBUG_PROCESS

        startupinfo = STARTUPINFO()
        process_information = PROCESS_INFORMATION()

        startupinfo.dwFlags = 0x1
        startupinfo.wShowWindow = 0x0

        startupinfo.cb = sizeof(startupinfo)

        if kernel32.CreateProcessA(path_to_exe,
                                   None,
                                   None,
                                   None,
                                   None,
                                   creation_flags,
                                   None,
                                   None,
                                   byref(startupinfo),
                                   byref(process_information)):

            print("[*] We have successfully launched the process!")
            print(("[*] PID: {:d}".format(process_information.dwProcessId)))

            self.h_process = self.open_process(process_information.dwProcessId)

        else:
            print(("[*] Error: 0x{:08x}.".format(kernel32.GetLastError())))
