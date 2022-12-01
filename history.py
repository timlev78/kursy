def log_write(string, a, b, res):
    file = open('log.txt', 'a')
    file.write(str(a)+string+str(b)+'='+str(res)+' \n')
    file.close()