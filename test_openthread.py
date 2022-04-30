from ctypes import *
from define import *
TH32CS_SNAPTHREAD = 0x00000004
THREAD_ALL_ACCESS = 0x001F03FF
kernel = windll.kernel32

pid = int(input('PID: '))

snapshot = kernel.CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD, pid)
lpte = THREADENTRY32()
lpte.dwSize = sizeof(lpte)

success = kernel.Thread32First(snapshot, byref(lpte))
while success:
    print("PID: ", lpte.th32OwnerProcessID)
    print('TID: ', lpte.th32ThreadID)
    h_thread = kernel.OpenThread(THREAD_ALL_ACCESS, None, lpte.Thread32id)
    if h_thread:
        print('handle: ', h_thread)
    else:
        print(WinError(GetLastError()))
    success = kernel.Thread32Next(snapshot, byref(lpte))