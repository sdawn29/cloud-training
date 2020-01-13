L1 = [i for i in range(10)]
L2 = [i * i for i in L1 if i % 2 == 0]

F = open('out1.txt')
L3 = [line.strip() for line in F]

F2 = open(r'..\log\serverlog.txt')
IP = [line.split()[0] for line in F2 if line[:3].isdigit()]
print(IP)

F2.seek(0)
IP2 = (line.split()[0] for line in F2 if line[:3].isdigit())
print(IP2)
print(tuple(IP2))

F2.seek(0)
images = [line.split()[6].lstrip('/pics/') if 'pics' in line.split()[6] else 'No Image' for line in F2 if
          line[:3].isdigit()]
print(images)

hosts = ['h1', 'h2']
ips = ['ip1', 'ip2']
D = {k: v for k, v in zip(hosts, ips)}
print(D)
