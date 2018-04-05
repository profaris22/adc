import time
import itertools
pins =(5,6,13,19)
col=(12,16,20,21)
periode=0
lst = list(itertools.product([0, 1], repeat=len(pins)))
dft = list(itertools.product([0, 1], repeat=len(col)))
while periode <240:
     for setup in lst:
          for i, pin in enumerate(pins):
               print(pin,setup[i])
          for akses in dft[0:1]:
               for c, con in enumerate(col):
                    if setup[:]==(0,0,0,0) and periode == 0:
                         print(con,akses[c])
          for akses in dft[1:2]:
               for c, con in enumerate(col):
                    if setup[:]==(1,1,1,1) and periode == 15:
                         print(con,akses[c])
          for akses in dft[2:3]:
               for c, con in enumerate(col):
                    if setup[:]==(1,1,1,1) and periode == 31:
                         print(con,akses[c])
          for akses in dft[3:4]:
               for c, con in enumerate(col):
                    if setup[:]==(1,1,1,1) and periode == 47:
                         print(con,akses[c])
          for akses in dft[4:5]:
               for c, con in enumerate(col):
                    if setup[:]==(1,1,1,1) and periode == 63:
                         print(con,akses[c])
          for akses in dft[5:6]:
               for c, con in enumerate(col):
                    if setup[:]==(1,1,1,1) and periode == 79:
                         print(con,akses[c])
          for akses in dft[6:7]:
               for c, con in enumerate(col):
                    if setup[:]==(1,1,1,1) and periode == 95:
                         print(con,akses[c])
          for akses in dft[7:8]:
               for c, con in enumerate(col):
                    if setup[:]==(1,1,1,1) and periode == 111:
                         print(con,akses[c])
          for akses in dft[8:9]:
               for c, con in enumerate(col):
                    if setup[:]==(1,1,1,1) and periode == 127:
                         print(con,akses[c])
          for akses in dft[9:10]:
               for c, con in enumerate(col):
                    if setup[:]==(1,1,1,1) and periode == 143:
                         print(con,akses[c])
          for akses in dft[10:11]:
               for c, con in enumerate(col):
                    if setup[:]==(1,1,1,1) and periode == 159:
                         print(con,akses[c])
          for akses in dft[11:12]:
               for c, con in enumerate(col):
                    if setup[:]==(1,1,1,1) and periode == 175:
                         print(con,akses[c])
          for akses in dft[12:13]:
               for c, con in enumerate(col):
                    if setup[:]==(1,1,1,1) and periode == 191:
                         print(con,akses[c])
          for akses in dft[13:14]:
               for c, con in enumerate(col):
                    if setup[:]==(1,1,1,1) and periode == 207:
                         print(con,akses[c])
          for akses in dft[14:15]:
               for c, con in enumerate(col):
                    if setup[:]==(1,1,1,1) and periode == 223:
                         print(con,akses[c])
          for akses in dft[15:16]:
               for c, con in enumerate(col):
                    if setup[:]==(1,1,1,1) and periode == 239:
                         print(con,akses[c])
          for akses in dft[16:17]:
               for c, con in enumerate(col):
                    if setup[:]==(1,1,1,1) and periode == 255:
                         print(con,akses[c])
          periode+=1
          time.sleep(1) 
