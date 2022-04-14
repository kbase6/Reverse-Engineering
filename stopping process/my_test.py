import my_debugger

debugger = my_debugger.debugger()

#debugger.load("C:\\WINDOWS\\system32\\calc.exe")

pid = int(input("pid: "))
debugger.attach(pid)
debugger.run()
debugger.detach()
