import imaplib
from email import message_from_bytes
from multiprocessing.dummy import Pool as ThreadPool
from datetime import datetime
import smtplib
import sqlite3
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

db = sqlite3.connect("C:\\Users\\PC WORLD\\Downloads\\test.sqlite")
cursor = db.cursor()


class Contact:
    EMAIL = 1
    PHONE = 2
    WHATS_APP=4
    VIBER=8


def send_email(receiver_email, msg):
    subject = "Account Information"
    body = '{}'.format(msg)
    print('body = {}'.format(body))
    sender_email = "ggmm1005@gmail.com"
    password = "Hoda2001"
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails
    # Add body to email
    message.attach(MIMEText(body, "plain"))
    text = message.as_string()
    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
    print("done")


def send_sms(phone_number, msg):
    pass


def send_whats_app_msg(whats_app_number, msg):
    pass


def send_viber_msg(viber_number, msg):
    pass


if __name__ == '__main__':
    query = "SELECT WorkId, SubscriberName, BeneficiaryName, ServiceName, HospitalName, Date, Paid FROM PatientsServices where SentTo=0;"
    cursor.execute(query)
    patient_result = cursor.fetchall()

    for record in patient_result:
        work_id = record[0]
        query = "SELECT ContactType, Contact FROM Contacts WHERE WorkId=%s" % work_id
        cursor.execute(query)
        contacts = cursor.fetchall()

        if len(contacts) > 0:
            print(contacts)

        if len(contacts) > 1:
            for contact in contacts:
                contact_type = contact[0]
                if contact_type == Contact.PHONE:
                    contacts.remove(contact)
                    break

        subscriber_name = record[1]
        beneficiary_name = record[2]
        service_name = record[3]
        hospital_name = record[4]
        timestamp = int(record[5])
        date = str(datetime.fromtimestamp(timestamp).date())
        paid = record[6]

        # msg = "We inform you that " + beneficiary_name + " who related to " + subscriber_name + " has gove "\
        #     + service_name + " at " + hospital_name + " in " + date + " and pay " + paid + " LYD."

        msg = "نعلمكم بأن " + beneficiary_name + " التابع إلى " + subscriber_name + " قد قدمت له خدمة '" \
              + service_name + "' في " + hospital_name + " بتاريخ (" + date + ") وقد دفع مبلغ (" + str(paid) + " د. ل.)"

        for contact in contacts:


            contact_type = contact[0]
            if contact_type == Contact.EMAIL:
                send_email(contact[1], msg)
            elif contact_type == Contact.PHONE:
                send_sms(contact[1], msg)
            elif contact_type == Contact.WHATS_APP:
                send_whats_app_msg(contact[1], msg)
            elif contact_type == Contact.VIBER:
                send_viber_msg(contact[1], msg)


ORG_EMAIL = "@gmail.com"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993


def read_emails_from_emails(main_email, password, emails, ):
    status, main_email = __check_emails__(main_email)
    if not status:
        raise Exception('Main e-mail is incorrect')

    data = []
    for email in emails:
        data.append((main_email, password, email, ))
    pool = ThreadPool(4)
    results = pool.map(_get_unseen_email_, data)

    return results


def _get_unseen_email_(args):
    login_email = args[0]
    password = args[1]
    email = args[2]

    mail = imaplib.IMAP4_SSL(SMTP_SERVER)

    mail.login(login_email, password)

    mail.select('inbox')

    # search all unseen email and return uids
    result, data = mail.uid('search', None, "ALL", 'FROM', '"{}"'.format(email))
    if result == 'OK':
        for num in data[0].split():
            result, data = mail.uid('fetch', num, '(RFC822)')

            if result == 'OK':
                email_message = message_from_bytes(data[0][1])  # raw email text including headers
                # print('keys:', email_message.keys())
                # print('From:', email_message['From'])
                # print('At:', email_message['Date'])
                # print('-------------------------------')

                for part in email_message.walk():
                    file_name = part.get_filename()
                    if file_name is None:
                        continue
                    print('file_name: ', file_name)
                    file_path = 'C:\\Users\\PC WORLD\\Desktop\\' + file_name
                    fp = open(file_path, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()


    mail.close()
    mail.logout()

    return "Done"


def __check_emails__(email):
    if not email.endswith(ORG_EMAIL):
        if email.__contains__('@'):
            return False, email
        email += ORG_EMAIL
    return True, email


# TODO: Implement Multithreading
def __get_email__(args):
    mail = args[0]
    num = args[1]

    result, data = mail.uid('fetch', num, '(RFC822)')
    return result, data
