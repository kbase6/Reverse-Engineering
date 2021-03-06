from ctypes import *
from define import *
TH32CS_SNAPTHREAD = 0x00000004

kernel32 = windll.kernel32


pid = int(input('pid: '))

snapshot = kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD, pid)

lpte = THREADENTRY32()
lpte.dwSize = sizeof(lpte)

thread = kernel32.Thread32First(snapshot, byref(lpte))
while thread:
    print("PID: ", lpte.th32OwnerProcessID)
    print('TID: ', lpte.th32ThreadID)
    thread = kernel32.Thread32Next(snapshot, byref(lpte))
