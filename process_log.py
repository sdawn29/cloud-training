F1 = open('log_report.txt', 'w')
F2 = open('log_report.csv', 'w')
F1.write('IP\tDATE\tPICS\tURL')
F2.writelines(['IP,', 'DATE,', 'PICS,', 'URL\n'])
F3 = open(r'C:\Users\lab365\Desktop\Python Training\log\serverlog.txt')  # default mode is Read only mode

for line in F3:
    if line[:3].isdigit():
        # print(line)
        sp = line.split()
        # print(sp)
        ip = sp[0]
        dt = sp[3]
        dt1 = dt[1:13]
        dt2 = dt[1:dt.index(':')]
        if sp[6].startswith('/pics'):
            im = sp[6]
            im1 = im[6:]  # 1st way
            im2 = im.split('/')
            im3 = im2[-1]  # 2nd way
            im4 = im.lstrip('/pics/')  # 3rd way
            im5 = im.replace('/pics/', '')  # 4th way
        else:
            im3 = 'NO IMAGE'
        url = sp[10][1:-1]
        print(ip, dt2, im3, url, sep='\t', file=F1)
        print(ip, dt2, im3, url, sep=',', file=F2)
F1.close()
F2.close()
F3.close()