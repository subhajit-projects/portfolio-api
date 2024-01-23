from django.shortcuts import render
from django.template.loader import get_template
from email_queue.models import EmailQueue
from django.core.mail import EmailMessage, EmailMultiAlternatives
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.conf import settings
import os

# Create your views here.

def email_send_corn_job():
    try:
        email_queue = EmailQueue.objects.filter(email_status="0")
        for email_id_list in email_queue:
            if email_id_list.email_template == "thankyou_contact":
                message_body = get_template('email_template/contact_email/contact.html').render({'websiteLink': 'http://www.techninetyeight.com/'})
                img_dir = '/home/ubuntu/portfolio_api/static'
                image = 'happy.png'
                file_path = os.path.join(img_dir, image)
                img_data = open(file_path, 'rb').read()
                html_part = MIMEMultipart(_subtype='related')
                body = MIMEText(message_body, _subtype='html')
                html_part.attach(body)
                img = MIMEImage(img_data, 'png')
                img.add_header('Content-Id', '<happy>')
                img.add_header("Content-Disposition", "inline", filename="happy") 
                html_part.attach(img)
                msg = EmailMessage(email_id_list.email_subject, None, "Tech NinetyEight<"+settings.EMAIL_HOST_USER+">", to=[email_id_list.email_to])
                msg.attach(html_part)
                resp = msg.send()
            else:
                message_body ="Test Body"
                email = EmailMessage(email_id_list.email_subject, message_body, "Tech NinetyEight<"+settings.EMAIL_HOST_USER+">", to=[email_id_list.email_to])
                email.content_subtype = 'html'
                resp = email.send()

            if resp == 1:
                update_email_queue = EmailQueue.objects.get(id=email_id_list.id)
                update_email_queue.email_status = "1"
                update_email_queue.save()
    except Exception as e:
        print ("Error on SMTP mail", e)


# python manage.py shell --command="from email_queue.views import email_send; email_send()"
# python manage.py shell --command="from email_queue.views import email_send_corn_job; email_send_corn_job()"
# https://gutsytechster.wordpress.com/2019/06/24/how-to-setup-a-cron-job-in-django/
# https://www.geeksforgeeks.org/how-to-setup-cron-jobs-in-ubuntu/
# https://www.semicolonworld.com/question/59491/creating-a-mime-email-template-with-images-to-send-with-python-django (Buttom part)

# https://www.youtube.com/watch?v=x0Epc_l3rsA
# https://www.youtube.com/watch?v=oiLs29VBKP0