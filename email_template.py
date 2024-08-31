import csv
import argparse
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os.path
import sys


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

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
    
    # Optional cc and bcc fields
    cc_email = input("Enter CC email (optional, leave blank if not applicable): ")
    bcc_email = input("Enter BCC email (optional, leave blank if not applicable): ")
    
    return {
        "contact_name": contact_name,
        "company_name": company_name,
        "your_name": your_name,
        "your_position": your_position,
        "your_contact_info": your_contact_info,
        "address_to": address_to,
        "text_form": text_form,
        "language": language,
        "recipient_email": recipient_email,
        "cc_email": cc_email,
        "bcc_email": bcc_email
    }

def read_csv_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def get_email_content(data):
    address = data['contact_name'] if data['address_to'] == 'contact' else data['company_name']
    
    # English Email
    if data['language'] == 'en':
        # English Short form email
        if data['text_form'] == 'short':
            content = f"""
            <html>
            <body>
            <p>Hi {address},</p>
            
            <p>I'm {data['your_name']} from GDG Montreal, a non-profit dedicated to connecting and educating developers. We're excited to invite {data['company_name']} to sponsor <a href="https://devfest.gdgmontreal.com/">DevFest Montreal 2024</a>, part of the world's largest community-led <a href="https://developers.google.com/community/devfest">DevFest tech conference</a>!</p>
            
            <p>The event will be held at Concordia University in-person in Montreal on November 9th.</p>
            
            <p><strong>Why Sponsor DevFest Montreal?</strong></p>
            <ul>
                <li><strong>Engagement:</strong> Significant interest, with 216 registrations in 2023.</li>
                <li><strong>Expertise:</strong> 16 speakers, 14 sessions, and 3 tracks—Cloud, Mobile, AI—featuring international experts.</li>
                <li><strong>Talent Acquisition:</strong> A prime opportunity to connect with top developers and engineers. Sponsorship can include options like setting up a booth to engage directly with potential candidates.</li>
                <li><strong>Impact:</strong> 100% of past participants would recommend DevFest.</li>
            </ul>
            
            <p>GDG Montreal organizes impactful events like DevFest and more. We believe partnering with {data['company_name']} will enhance your brand's visibility among a targeted audience. More details are in our <a href="https://docs.google.com/presentation/d/1ezmE9o9o-EXhEa_ofPospL9hFGxAYm8xtnV_0m3AqSo/edit?usp=sharing">sponsorship proposal</a>.</p>
            
            <p>Let's discuss this opportunity. Please let us know a good time for a call or reach out with any questions.</p>
            
            <p>Looking forward to collaborating!</p>
            
            <p>Best regards,<br>
            {data['your_name']}<br>
            {data['your_position']}<br>
            GDG Montreal<br>
            {data['your_contact_info']}<br>
            <a href="https://devfest.gdgmontreal.com/">https://devfest.gdgmontreal.com/</a></p>
            </body>
            </html>
            """

            
        # English Long form email
        else:
            content = f"""
            <html>
            <body>
            <p>Dear {address},</p>
            
            <p>Hi, my name is {data['your_name']}, and I am writing on behalf of GDG Montreal, a non-profit organization dedicated to learning, building, and connecting with fellow developers and tech practitioners. We are excited to invite {data['company_name']} to be a sponsor of our upcoming <a href="https://devfest.gdgmontreal.com/">DevFest Montreal 2024</a>, an event part of the <a href="https://developers.google.com/community/devfest">Global DevFest event</a>, a largest and most inclusive community-led technology conference in the world!</p>
            
            <p>The event will be held at Concordia University in-person in Montreal on November 9th.</p>
            
            <p><strong>About DevFest:</strong><br>
            DevFest is a global event series that brings together developers from all corners of the globe and diverse backgrounds. Every year, attendees have the opportunity to explore cutting-edge developer tools, learn directly from Google Developer Experts, and connect with like-minded professionals from their local community.</p>
            
            <p><strong>Why Sponsor DevFest Montreal?</strong></p>
            <ul>
                <li><strong>Engagement:</strong> Over the past eight events, GDG Montreal has seen significant engagement, with more than 216 registrations in 2023 alone.</li>
                <li><strong>Expertise:</strong> Our event features 16 renowned speakers, 14 insightful sessions, and 3 specialized tracks --  Cloud, Mobile and AI --  featuring international experts who share their knowledge with an engaged and passionate audience.</li>
                <li><strong>Talent Acquisition:</strong> DevFests attract a pool of talented developers and engineers, making them an ideal event for companies looking to recruit top talent. Sponsorship can include options like setting up a booth to engage directly with potential candidates.</li>
                <li><strong>Impact:</strong> 100% of participants from previous events would recommend DevFest to their friends, underscoring the event's value and influence.</li>
            </ul>
            
            <p><strong>About GDG Montreal:</strong><br>
            GDG Montreal is committed to organizing impactful events like DevFest, Women Techmakers Montreal, Google I/O Extended, and more. As a non-profit organization (NEQ 1172510951), we aim to create a platform where developers can learn, grow, and network in a collaborative environment.</p>
            
            <p>We believe that a partnership with {data['company_name']} would be mutually beneficial, providing your brand with excellent visibility and engagement with a highly targeted audience. You can find more details in our <a href="https://docs.google.com/presentation/d/1ezmE9o9o-EXhEa_ofPospL9hFGxAYm8xtnV_0m3AqSo/edit?usp=sharing">sponsorship proposal</a>.</p>
            
            <p>We would love to discuss this opportunity further and explore how we can work together to make DevFest Montreal 2024 an even greater success. Please let us know a convenient time for a call, or if you have any questions, feel free to reach out directly.</p>
            
            <p>Thank you for considering our proposal. We look forward to the possibility of collaborating with {data['company_name']}!</p>
            
            <p>Best regards,<br>
            {data['your_name']}<br>
            {data['your_position']}<br>
            GDG Montreal<br>
            {data['your_contact_info']}<br>
            <a href="https://devfest.gdgmontreal.com/">https://devfest.gdgmontreal.com/</a></p>
            </body>
            </html>
            """


    # French Email
    else:
        
        # French Short form email
        ## FIXME LENZ : Long-form French content (not provided in the original document)
        # if data['text_form'] == 'short':
            content = f"""
            <html>
            <body>
            <p>Bonjour {address},</p>
            
            <p>Je suis {data['your_name']} de GDG Montréal, une organisation à but non lucratif dédiée à connecter et éduquer les développeurs. Nous sommes ravis d'inviter {data['company_name']} à sponsoriser DevFest Montréal 2024, qui fait partie de la plus grande conférence technologique communautaire <a href="https://developers.google.com/community/devfest">DevFest (Google) au monde</a> !</p>
            
            <p>L'événement aura lieu en personne à l'Université Concordia à Montréal le 9 Novembre au pavillion John Molson.</p>
            
            <p><strong>Pourquoi sponsoriser DevFest Montréal ?</strong></p>
            <ul>
                <li><strong>Engagement :</strong> Un intérêt significatif, avec 216 inscriptions en 2023 et on vise 300+ pour 2024.</li>
                <li><strong>Expertise :</strong> 16 intervenants, 14 sessions et 3 thématiques - Cloud, Mobile, IA - avec des experts internationaux.</li>
                <li><strong>Acquisition de talents :</strong> Une excellente occasion de rencontrer les meilleurs développeurs et ingénieurs. Le sponsoring peut inclure des options telles que la mise en place d'un stand pour interagir directement avec des candidats potentiels.</li>
                <li><strong>Impact :</strong> 100% des participants précédents recommanderaient DevFest.</li>
            </ul>
            
            <p>GDG Montréal organise des événements percutants comme DevFest et bien d'autres. Nous pensons qu'un partenariat avec {data['company_name']} renforcera la visibilité de votre marque auprès d'un public ciblé. Vous trouverez plus de détails dans notre <a href="https://docs.google.com/presentation/d/1ezmE9o9o-EXhEa_ofPospL9hFGxAYm8xtnV_0m3AqSo/edit?usp=sharing">proposition de sponsoring</a>.</p>
            
            <p>Si {data['company_name']} désire en savoir plus, il me fera plaisir de sauter sur un appel, chat ou courriel.</p>
            
            <p>Au plaisir de collaborer !</p>
            
            <p>Cordialement,<br>
            {data['your_name']}<br>
            {data['your_position']}<br>
            GDG Montreal<br>
            {data['your_contact_info']}<br>
            <a href="https://devfest.gdgmontreal.com/">https://devfest.gdgmontreal.com/</a></p>
            </body>
            </html>
            """
        
        # French Long form email
        # else:
        #     # content = "Long-form French content not provided in the original document."
        #     raise ValueError("Long-form French content not provided in the original document.")
    
    return content

def get_gmail_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists('client_secret.json'):
                print("Error: client_secret.json is missing.")
                print("Please follow these steps to obtain the client_secret.json file:")
                print("1. Go to the Google Cloud Console (https://console.cloud.google.com/)")
                print("2. Create a new project or select an existing one")
                print("3. Enable the Gmail API for your project")
                print("4. Go to 'APIs & Services' > 'Credentials'")
                print("5. Click 'Create Credentials' and select 'OAuth client ID'")
                print("6. Choose 'Desktop app' as the application type")
                print("7. Download the client configuration and save it as 'client_secret.json' in the same directory as this script")
                sys.exit(1)
            
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    return build('gmail', 'v1', credentials=creds)

def send_email(service, recipient, subject, content, cc=None, bcc=None):
    message = MIMEMultipart()
    message['to'] = recipient
    message['subject'] = subject
    if cc:
        message['cc'] = cc
    if bcc:
        message['bcc'] = bcc
    message.attach(MIMEText(content, 'html'))
    
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
    try:
        service.users().messages().send(userId='me', body={'raw': raw_message}).execute()
        print(f"Email sent successfully to {recipient}")
    except Exception as e:
        print(f"An error occurred while sending the email: {str(e)}")


def main():
    parser = argparse.ArgumentParser(description="Send DevFest sponsorship emails")
    parser.add_argument("-o", "--csv", help="Path to CSV file with recipient information")
    args = parser.parse_args()

    service = get_gmail_service()

    if args.csv:
        recipients = read_csv_file(args.csv)
        for recipient in recipients:
            content = get_email_content(recipient)
            send_email(service, recipient['recipient_email'], f"{recipient['company_name']} and DevFest Montreal", content, recipient.get('cc_email'), recipient.get('bcc_email'))
    else:
        data = get_user_input()
        content = get_email_content(data)
        send_email(service, data['recipient_email'], f"{data['company_name']} and DevFest Montreal", content, data.get('cc_email'), data.get('bcc_email'))

if __name__ == "__main__":
    main()
