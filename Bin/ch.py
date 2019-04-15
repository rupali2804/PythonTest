#!python
# coding: utf-8
import sys
import ctypes

def run_as_admin(argv=None, debug=False):
    shell32 = ctypes.windll.shell32
    if argv is None and shell32.IsUserAnAdmin():
        return True
        
    if argv is None:
        argv = sys.argv
    if hasattr(sys, '_MEIPASS'):
        # Support pyinstaller wrapped program.
        arguments = map(unicode, argv[1:])
    else:
        arguments = map(unicode, argv)
    argument_line = u' '.join(arguments)
    executable = unicode(sys.executable)
    if debug:
        print 'Command line: ', executable, argument_line
    ret = shell32.ShellExecuteW(None, u"runas", executable, argument_line, None, 1)
    if int(ret) <= 32:
        return False
    return None
    

ret = run_as_admin()
print (ret)
if ret is True:
	print 'I have admin privilege.'
	raw_input('Press ENTER to exit.')
elif ret is None:
	print 'I am elevating to admin privilege.'
	raw_input('Press ENTER to exit.')
else:
	print 'Error(ret=%d): cannot elevate privilege.' % (ret, )
      
 
