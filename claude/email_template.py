import csv
import argparse
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from getpass import getpass

def get_user_input():
    contact_name = input("Enter the contact name: ")
    company_name = input("Enter the company name: ")
    your_name = input("Enter your name: ")
    your_position = input("Enter your position: ")
    your_contact_info = input("Enter your contact information: ")
    
    address_to = input("Address email to contact name or company name? (contact/company): ").lower()
    text_form = input("Use short form or long form text? (short/long): ").lower()
    language = input("Send email in English or French? (en/fr): ").lower()
    recipient_email = input("Enter the recipient's email: ")
    
    return {
        "contact_name": contact_name,
        "company_name": company_name,
        "your_name": your_name,
        "your_position": your_position,
        "your_contact_info": your_contact_info,
        "address_to": address_to,
        "text_form": text_form,
        "language": language,
        "recipient_email": recipient_email
    }

def read_csv_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def get_email_content(data):
    # This function would contain the email templates and logic to fill in the placeholders
    # For brevity, I'm omitting the full implementation here
    # You would need to include the full email content from the document,
    # with proper HTML formatting and placeholder replacements
    
    if data['language'] == 'en':
        if data['text_form'] == 'short':
            content = f"""
            <html>
            <body>
            <p>Hi {data['contact_name'] if data['address_to'] == 'contact' else data['company_name']},</p>
            
            <p>I'm {data['your_name']} from GDG Montreal, a non-profit dedicated to connecting and educating developers. We're excited to invite {data['company_name']} to sponsor <a href="https://devfest.gdgmontreal.com/">DevFest Montreal 2024</a>, part of the world's largest community-led <a href="https://developers.google.com/community/devfest">DevFest tech conference</a>!</p>
            
            <!-- Rest of the short-form English content -->
            
            <p>Best regards,<br>
            {data['your_name']}<br>
            {data['your_position']}<br>
            GDG Montreal<br>
            {data['your_contact_info']}<br>
            <a href="https://devfest.gdgmontreal.com/">https://devfest.gdgmontreal.com/</a></p>
            </body>
            </html>
            """
        else:
            # Long-form English content
            pass
    else:
        # French content (both short and long form)
        pass
    
    return content

def send_email(recipient, subject, content):
    ## DEBUG 
    print("Sending email...")
    return
    
    ### 
    sender_email = input("Enter your Gmail address: ")
    password = getpass("Enter your Gmail password or app password: ")

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient
    message['Subject'] = subject

    message.attach(MIMEText(content, 'html'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.send_message(message)

def main():
    parser = argparse.ArgumentParser(description="Send DevFest sponsorship emails")
    parser.add_argument("-o", "--csv", help="Path to CSV file with recipient information")
    args = parser.parse_args()

    if args.csv:
        recipients = read_csv_file(args.csv)
        for recipient in recipients:
            content = get_email_content(recipient)
            send_email(recipient['recipient_email'], "[COMPANY NAME] and DevFest Montreal", content)
            print(f"Email sent to {recipient['recipient_email']}")
    else:
        data = get_user_input()
        content = get_email_content(data)
        send_email(data['recipient_email'], "[COMPANY NAME] and DevFest Montreal", content)
        print(f"Email sent to {data['recipient_email']}")

if __name__ == "__main__":
    main()