#!/usr/bin/python
import os
import time
source=['/home/func']
target_dir='/home/copy/'
target=target_dir+time.strftime('%Y%m%d%H%M%S')+'.zip'
zip_command="sudo zip -qr '%s' %s" % (target,' '.join(source))
if os.system(zip_command)==0:
 print 'successfully backup to',taget
else:
 print 'failed'
