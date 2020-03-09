import sys, os, time
frozen = 'not'
if getattr(sys, 'frozen', False):
        # we are running in a bundle
        frozen = 'ever so'
        bundle_dir = sys._MEIPASS
else:
        # we are running in a normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(__file__))
#print( 'we are',frozen,'frozen')
#print( 'bundle dir is', bundle_dir )
#print( 'sys.argv[0] is', sys.argv[0] )
#print( 'sys.executable is', sys.executable )
#print( 'os.getcwd is', os.getcwd() )
print("===============Python3 环境支持===============")
print("\n")
print("   将在系统中安装KB2533623补丁以及VC++ 2015   ")
print("\n")
print("==============================================")
print("\n")

msg="要继续吗?（y/n）："
while True:
    flag=raw_input(msg)
    if flag == 'y':
        break
    elif flag == 'n':
        sys.exit()
    else:
        msg = "输入错误，要继续吗?（y/n）："

def Is64Windows():
    return 'PROGRAMFILES(X86)' in os.environ

if Is64Windows():
    kb_name = 'Windows6.1-KB2533623-x64.msu'
    vc_name = 'vc_redist.x64.exe'
else:
    kb_name = 'Windows6.1-KB2533623-x86.msu'
    vc_name = 'vc_redist.x86.exe'

current_path=bundle_dir
cmd="wusa.exe "+ current_path + "\\runtime\\" + kb_name + " /quiet /norestart"
print("Installing KB2533623...")
os.system(cmd)
cmd=current_path + "\\runtime\\" + vc_name + " /install /quiet /norestart"
print("Installing VC++ 2015...")
os.system(cmd)

msg="安装完成，你希望立即重启吗?（y/n）："
while True:
    flag=raw_input(msg)
    if flag == 'y':
        os.system("shutdown -r -t 0")
        break
    elif flag == 'n':
        break
    else:
        msg = "输入错误，你希望立即重启吗?（y/n）："
