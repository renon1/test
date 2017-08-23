import os
import subprocess
#command = 'adb logcat com.sec.android.dmc.face:E | grep dmc'
#os.system(command)
#p = subprocess.Popen(command, shell=True,
#stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#print stdout
cnt=0
proc = subprocess.Popen(['adb', 'logcat', '-v', 'time', '|', 'grep', 'dmc'], stdout=subprocess.PIPE)
for line in proc.stdout:
    print cnt
    cnt=cnt+1
    if "RunFaceTracking" in line:
        print line
        os.system('adb logcat -c')
#        proc.kill()
#    break
proc.wait()
