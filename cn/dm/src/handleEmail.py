import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os, zipfile
from bs4 import BeautifulSoup
from cn.dm.src.logger import logger





def deleteFiles(result_path):
    logger.info("移除目录下所有文件：%s" % result_path)
    for i in os.listdir(result_path):
        path_i = os.path.join(result_path,i)
        if os.path.isfile(path_i):
            os.remove(path_i)
        else:
            deleteFiles(path_i)

def deleteResultsFiles():
    result_path = os.path.join(os.path.dirname(__file__), "results","screenshots")
    resultszip_path = os.path.join(os.path.dirname(__file__), "resultszip")
    deleteFiles(result_path)
    deleteFiles(resultszip_path)

def handleHtml(source="results"):
    soup = BeautifulSoup(open(source+"/IOS测试报告.html","r"), "html.parser")
    a = soup.findAll("div",class_="popup_window")
    for i in a:
        i.extract()
    return soup



def make_zip(source_dir="results",output_filename=r"results.zip"):
    zipf = zipfile.ZipFile(output_filename, 'w')
    pre_len = len(os.path.dirname(source_dir))
    for parent, dirnames, filenames in os.walk(source_dir):
        for filename in filenames:
            pathfile = os.path.join(parent, filename)
            arcname = pathfile[pre_len:].strip(os.path.sep)  # 相对路径
            zipf.write(pathfile, arcname)
    zipf.close()

def sendMail(now_time="00",source="results",output=r"resultszip/results_%s.zip"):
    '''
    'gjhpbxfvvuxhdhid'
    'dxnuqtwtnqngdjbi'
    '''
    output = output % now_time
    make_zip(source,output)
    sender = '2415824179@qq.com'
    toList = ['849781856@qq.com','liudonglin@dongmancorp.cn']
    receiver = ", ".join(toList)
    smtpserver = 'smtp.qq.com'
    # username = '木木'
    password = 'gjhpbxfvvuxhdhid'
    mail_title = 'IOS自动化测试报告'

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header(mail_title, 'utf-8')

    # 邮件正文内容
    mail_html = handleHtml(source)
    message.attach(MIMEText('测试结果见报告', 'plain', 'utf-8'))
    message.attach(MIMEText(mail_html, 'html', 'utf-8'))

    try:
        smtp = smtplib.SMTP()
        # smtp = smtplib.SMTP_SSL(smtpserver)  # 注意：如果遇到发送失败的情况（提示远程主机拒接连接），这里要使用SMTP_SSL方法
        # smtp.set_debuglevel(1)
        smtp.connect(smtpserver)
        smtp.login(sender, password)
        with open(output, 'rb') as f:
            # 这里附件的MIME和文件名
            mime = MIMEBase('zip', 'zip', filename="测试报告附件")
            # 加上必要的头信息
            mime.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', "测试报告附件.zip"))
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            # 把附件的内容读进来
            mime.set_payload(f.read())
            # 用Base64编码
            encoders.encode_base64(mime)
            message.attach(mime)
        # smtp.sendmail(sender, receiver.split(","), message.as_string())
        smtp.sendmail(sender,toList, message.as_string())

    except Exception:
        logger.error("邮件发送失败！")
    else:
        logger.info("邮件发送成功！")
    finally:
        smtp.quit()


if __name__ == "__main__":
    # make_zip()
    sendMail()
    # handleHtml()