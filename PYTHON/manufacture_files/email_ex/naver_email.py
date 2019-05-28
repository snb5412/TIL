import smtplib
from email.message import EmailMessage
from getpass import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email_list = ['aa@naver.com', 'bb@naver.com', 'cc@naver.com']

password = getpass('Password : ')

#msg = EmailMessage()
# msg['Subject'] = '하이하이'
# msg['From'] = 'snb5412@naver.com'
# msg['To'] = (',').join(email_list)
# msg.set_content('안녕하세요.')


#html 파일 날리기
msg = MIMEMultipart()
msg['Subject'] = '권고사직서'
msg['From'] = 'wnsgh6315@naver.com'
msg['To'] = ','.join(email_list)
html = """
<html>
    <body>
    <img src="http://sampleimg.com/asdasd.png">
    <p>HI,</p>
    <a href="https://www.google.com">GO TO GOOGLE</a>
    </body>
</html>
"""
part = MIMEText(html, 'html')
msg.attach(part)


#로그인 , 메시지 날리기
s = smtplib.SMTP_SSL('smtp.naver.com', 465)
s.login('wnsgh6315', password)
s.send_message(msg)

print('이메일 전송 완료!!')