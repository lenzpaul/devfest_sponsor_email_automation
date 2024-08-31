# TODO STyling and bolding 
def replace_placeholders(template_text):
    placeholders = {
        '[CONTACT NAME]': input('Enter the contact name: '),
        '[COMPANY NAME]': input('Enter the company name: '),
        '[Your Full Name]': input('Enter your full name: '),
        '[Your Position]': input('Enter your position: '),
        '[Your Contact Information]': input('Enter your contact information: '),
        '[DevFest website]': input('Enter the DevFest website URL: ')
    }

    for key, value in placeholders.items():
        template_text = template_text.replace(key, value)
    return template_text

template_text = """
Dear [CONTACT NAME] or [COMPANY NAME],

Hi, my name is [Your Full Name], and I am writing on behalf of GDG Montreal, a non-profit organization dedicated to learning, building, and connecting with fellow developers and tech practitioners. We are excited to invite [Company Name] to be a sponsor of our upcoming DevFest Montreal 2024, an event part of the Global DevFest event, a largest and most inclusive community-led technology conference in the world!

The event will be held at Concordia University in-person in Montreal on November 9th. 

About DevFest:
DevFest is a global event series that brings together developers from all corners of the globe and diverse backgrounds. Every year, attendees have the opportunity to explore cutting-edge developer tools, learn directly from Google Developer Experts, and connect with like-minded professionals from their local community.

Why Sponsor DevFest Montreal?
- Engagement: Over the past eight events, GDG Montreal has seen significant engagement, with more than 216 registrations in 2023 alone.
- Expertise: Our event features 16 renowned speakers, 14 insightful sessions, and 3 specialized tracks –  Cloud, Mobile and AI –  featuring international experts who share their knowledge with an engaged and passionate audience.
- Talent Acquisition: DevFests attract a pool of talented developers and engineers, making them an ideal event for companies looking to recruit top talent. Sponsorship can include options like setting up a booth to engage directly with potential candidates.
- Impact: 100% of participants from previous events would recommend DevFest to their friends, underscoring the event's value and influence.

About GDG Montreal:
GDG Montreal is committed to organizing impactful events like DevFest, Women Techmakers Montreal, Google I/O Extended, and more. As a non-profit organization (NEQ 1172510951), we aim to create a platform where developers can learn, grow, and network in a collaborative environment.

We believe that a partnership with [Company Name] would be mutually beneficial, providing your brand with excellent visibility and engagement with a highly targeted audience. You can find more details in our sponsorship proposal.

We would love to discuss this opportunity further and explore how we can work together to make DevFest Montreal 2024 an even greater success. Please let us know a convenient time for a call, or if you have any questions, feel free to reach out directly.

Thank you for considering our proposal. We look forward to the possibility of collaborating with [Company Name]!

Best regards,
[Your Full Name]
[Your Position]
GDG Montreal
[Your Contact Information]
[DevFest website]
"""

updated_text = replace_placeholders(template_text)
print(updated_text)
