from ctypes import *
from define import *
import my_debugger
from my_debugger_defines import *

debugger = my_debugger.debugger()

pid = int(input("Enter the PID of the process to attach to:"))
debugger.attach(pid)

list = debugger.enumerate_threads()

for thread in list:
    thread_context = debugger.get_thread_context(thread)

    print('[*] Dumping registers for thread ID: ', thread)
    print('[**] EIP: ', thread_context.Eip)
    print('[**] ESP: ', thread_context.Esp)
    print('[**] EBP: ', thread_context.Ebp)
    print('[**] EAX: ', thread_context.Eax)
    print('[**] EBX: ', thread_context.Ebx)
    print('[**] ECX: ', thread_context.Ecx)
    print('[**] EDX: ', thread_context.Edx)
    print('[*] END DUMP')

debugger.detach()

