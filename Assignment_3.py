F = open(r'C:\Users\lab365\Desktop\Python Training\log\SSH_log_Sample.txt')
data = F.readlines()
failedAttemptCount = 0
# ips = re.findall('\d{3}\.\d{3}\.\d{3}\.\d{3}', data)
for i in data:
    if 'Failed password' in i:
        failedAttemptCount += 1
    
    if 'sshd version' in i:
        w = i.split()
        vrindex = w.index('version')
        ver = w[vrindex + 1].strip(',')

    if 'ssh-rsa' in i:
        keysplit = i.split()
        key = keysplit[keysplit.index('ssh-rsa')+1]
        key = key.split(':')
        keyver = key[0]
    
    if 'Accepted password' in i:
        nw = i.split()
        userind = nw.index('for')
        acceptedUser = nw[userind+1]

        ipind = nw.index('from')
        acceptedIp = nw[ipind+1]

        portind = nw.index('port')
        acceptedport = nw[portind+1]

print('No of failed login attempt:', failedAttemptCount)
print('sshd version: ', ver)       
print('Encryption: ', keyver)       
print('Succesful Login User: ', acceptedUser)       
print('ip: ', acceptedIp)       
print('port: ', acceptedport)
F.close()      
