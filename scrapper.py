import requests
from bs4 import BeautifulSoup
import smtplib
import time
import schedule



###Important Add ur owm product details that u want to track

#url of the amazon product
URL = 'https://www.amazon.in/Sparx-Sneakers-9-India-43-33-SC0322G/dp/B0798P3274/ref=sr_1_7?dchild=1&keywords=sneakers%2Bfor%2Bmen&qid=1582139276&sr=8-7&th=1&psc=1'
#the price below which u will be notified
check_price = 1200      



def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    sender_email = "dharmeshpoladiya75@gmail.com"
    receiver_email = "dharmeshpoladiya75@gmail.com"
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('dharmeshpoladiya75@gmail.com', 'qrlyukozpwpcuwvr')
    subject = 'Price fell down!'
    body = 'Hii Dharmesh you are receiving this mail from your web-app\
    The price of shoe you wanted is fall down check out quickly use below link\
    Check the link: \
    https://www.amazon.in/Sparx-Sneakers-9-India-43-33-SC0322G/dp/B0798P3274/ref=sr_1_7?dchild=1&keywords=sneakers%2Bfor%2Bmen&qid=1582139276&sr=8-7&th=1&psc=1'
    msg = f"Subject: {subject}\n\n{body}"
    #server.sendmail(
    #'Price check',
    #'email-address',
    #msg
    #)
    server.sendmail(sender_email, receiver_email, msg)
    print('Hey Email has been sent!')
    server.quit()

def job():

    headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()

    price2 = price[1:5]

    print('\n\n')
    print("Hello Dharmesh Congrats ")
    print(title.strip())

    sep = ','
    con_price = price2.split(sep, 1)[0]
    converted_price = int(con_price.replace('.', ''))

    price2 = int(price2)

    if (price2 <= check_price):
        print("Price has been dropped to ",price2)
        send_mail()
    else:
        print("Price has not dropped!\n")

    print('\n\n')

schedule.every().hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
