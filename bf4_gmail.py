import mimetypes
import smtplib
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from bf4 import*


class send_email:
    def __init__(self,email):
        host = "smtp.gmail.com" # Gmail STMP 서버 주소.
        port = "587"
        htmlFileName = "logo.html"

        senderAddr =gmail_id() # 보내는 사람 email 주소.
        recipientAddr = email  	# 받는 사람 email 주소.

        msg = MIMEBase("multipart", "alternative")
        msg['Subject'] = "BF4.GG Capture Image"
        msg['From'] = senderAddr
        msg['To'] = recipientAddr
        # MIME 문서를 생성합니다.
        imageFD = open('bf4.gg.jpg', 'rb')#image 파일 오픈 후 MIMEImage생성
        ImagePart = MIMEImage(imageFD.read() ,_subtype = "jpg")
        imageFD.close()


        # 만들었던 mime을 MIMEBase에 첨부 시킨다.
        msg.attach(ImagePart)

        # 메일을 발송한다.
        s = smtplib.SMTP(host,port)
        #s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(gmail_id(),gmail_pw())
        s.sendmail(senderAddr , [recipientAddr], msg.as_string())
        s.close()
