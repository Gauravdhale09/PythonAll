import smtplib
email = 'gauravdhale09@gmail.com'
password = 'wtnf xoqh qiml aqxn'
to = 'gaurajdha2004@gmail.com'
s = smtplib.SMTP('smtp.gmail.com',587)  #587 is port number of google gmail
s.starttls()  #makes secure from third person
s.login(email,password)  #login to account
sub = "My first email"
msg = "hii mam how are you"
msg="Subject:{}\n\n{}".format(sub,msg)
s.sendmail(email,to,msg)
chk = s.ehlo()
if chk[0]==250:
    print('yes')
else:
    print('no')