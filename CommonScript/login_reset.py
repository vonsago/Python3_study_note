#!/usr/bin/env python
# coding=utf-8
'''
> File Name: login_reset.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 五  7/13 10:42:32 2018
'''

def send_reset_password_email(name):
    from dce.system.system import get_controller_leader
    account = get_account_by_name(name)
    controller_ip, _ = get_controller_leader()
    s = get_token_serializer(PASSWORD_RESET_EXPIRE)
    key = s.dumps({'name': name})
    email_data = {
        'link': 'http://{}/login.html?Key={}'.format(controller_ip, key),
        'new_password': DEFAULT_RESET_PASSWORD
    }
    status = 'Success'
    try:
        send_email(account.email, RESET_PASSWORD_TEMPLATE_ID, email_data, use_mailgun=True)
    except Exception as e:
        raise APIException(EMAIL_ERROR, 'Fail to send email: %s' % e, code=400)

    return to_view_dict({'status': status})
