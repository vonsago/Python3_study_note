#!/usr/bin/env python
# coding=utf-8
'''
> File Name: send_email.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 一  7/16 17:32:28 2018
'''
from __future__ import unicode_literals
import logging
import smtplib
import dns.resolver
import os
import requests

from jinja2 import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
LOG = logging.getLogger(__name__)

dir_ = os.path.dirname(os.path.realpath(__file__))

DEFAULT_SMTP_TIMEOUT = 20
SMTP_SERVER_PORT = 25

RESET_PASSWORD_TEMPLATE_ID = 'reset_password_template_id'
ALERT_NOTIFICATION_TEMPLATE_ID = 'alert_notification_template_id'
TEST_EMAIL_TEMPLATE_ID = 'test_email_template_id'

email_templates = {
    RESET_PASSWORD_TEMPLATE_ID: {
        'subject': '{subject_prefix} reset password',
        'text': "Hi\nClick the link to reset your password to {new_password}:\n{link}",
        'html': """\
                <html>
                  <head></head>
                  <body>
                    <p>Hi!<br>
                       Click the link to reset your password to
                        <span style='color: red'>{new_password}</span>:<br>
                        <a href="{link}">{link}</a>
                    </p>
                  </body>
                </html>
                """
    },
    TEST_EMAIL_TEMPLATE_ID: {
        'subject': '{subject_prefix} test mail',
        'text': "Hi\nThis is a test mail.",
        'html': """\
                <html>
                  <head></head>
                  <body>
                    <p>Hi!<br>
                       This is a test mail.
                    </p>
                  </body>
                </html>
                """
    },
    ALERT_NOTIFICATION_TEMPLATE_ID: {
        'subject': "{subject_prefix} {alert_subject}",
        'text': "Hi\n{alert_description}",
        'html_template_file_path': os.path.join(os.path.dirname(os.path.dirname(dir_)), 'contrib', 'mail_template_alert.html.tmpl'),
    }
}


class MailError(Exception):
    pass


def resolve_mail_host(mail):
    domain = mail.split('@')[-1]
    a = dns.resolver.query(domain, 'MX')
    pa = sorted(a, key=lambda x: x.preference, reverse=True)
    LOG.info("MX resolved %s", pa[0].exchange.to_text())
    return pa[0].exchange.to_text()


def _generate_html_msg_content(tmpl_path, render_dict):
    with open(tmpl_path, 'r') as f:
        tmpl_str = f.read()

    template = Template(tmpl_str.decode('utf-8'))
    return template.render(**render_dict)


def send_message_by_mailgun(send_to, subject, text):
    try:
        result = requests.post(
            "https://api.mailgun.net/v3/{}/messages".format(MAILGUN_DOMAIN),
            auth=("api", MAILGUN_API_KEY),
            data={"from": "dce <mailgun@{}>".format(MAILGUN_DOMAIN),
                  "to": [send_to],
                  "subject": subject,
                  "text": text},
            proxies=get_http_proxy_config(),
            timeout=DEFAULT_TIMEOUT_SECONDS)
        result.raise_for_status()
    except Exception as e:
        raise MailError('Send email error: %s' % e)


def send_email(send_to, template_id, email_data, use_mailgun=False):
    template = email_templates[template_id]
    mail_setting = MailServer.get_instance()

    msg = MIMEMultipart('alternative')
    # msg = MIMEText(context, 'text', 'utf-8') #中文需参数‘utf-8’，单字节字符不需要

    if use_mailgun and (not mail_setting or not mail_setting.is_validated()):
        send_message_by_mailgun(send_to, template['subject'].format(subject_prefix='', **email_data),
                                template['text'].format(**email_data))
        return

    if not mail_setting or not mail_setting.is_validated():
        raise MailError('You should config MailServer first')

    msg['Subject'] = Header(template['subject'].format(subject_prefix=mail_setting.subject_prefix, **email_data), 'utf-8')
    msg['From'] = '{} <{}>'.format(mail_setting.from_name, mail_setting.from_mail)
    msg['To'] = send_to

    text = template['text'].format(**email_data)
    if 'html_template_file_path' in template:
        html = _generate_html_msg_content(template['html_template_file_path'], email_data)
    else:
        html = template.get('html', '').format(**email_data)

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain', 'utf-8')
    part2 = MIMEText(html, 'html', 'utf-8')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    smtp_server = None
    try:
        smtp_server = smtplib.SMTP(mail_setting.server_host, mail_setting.server_port, timeout=DEFAULT_SMTP_TIMEOUT)

        if mail_setting.TLS:
            smtp_server.ehlo()
            smtp_server.starttls()
            smtp_server.ehlo()

        smtp_server.login(mail_setting.username, mail_setting.password.encode('utf-8'))
        smtp_server.sendmail(mail_setting.from_mail, send_to, msg.as_string())
    except Exception as e:
        raise MailError(str(e))
    finally:
        if smtp_server:
            smtp_server.quit()

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/samples.mailgun.org/messages",
        auth=("api", "key-3ax6xnjp29jd6fds4gc373sgvjxteol0"),
        data={"from": "Excited User <excited@samples.mailgun.org>",
              "to": ["devs@mailgun.net"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomeness!"})

if __name__ == '__main__':
    pass
