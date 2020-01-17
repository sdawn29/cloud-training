import re

F = open(r'C:\Users\lab365\Desktop\Python Training\log\SSH_log_Sample.txt')
data = F.read()
failedAttemptCount = 0
ips = re.findall('+[Failed Password]', data)
print(ips)