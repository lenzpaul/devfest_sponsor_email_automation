 DevFest Sponsorship Email Automation

This project automates the process of sending sponsorship emails for DevFest Montreal. It uses the Gmail API to send personalized emails to a list of recipients provided in a CSV file or through user input.

## Project Structure
```
├── .DS_Store
├── client_secret.example.json
├── client_secret.json
├── email_template.py
├── env/
│   ├── bin/
│   ├── include/
│   ├── lib/
│   └── pyvenv.cfg
├── requirements.txt
├── sample_recipients.csv
├── setup_environment.sh
├── token.json
```


## Setup

1. **Clone the repository:**


    <!-- 
    TODO: Add repository URL
    ```sh
    git clone <repository-url>
    ``` 
    -->

2. **Set up the environment:**

    Run the `setup_environment.sh` script to create a virtual environment and install the required dependencies.

    ```sh
    ./setup_environment.sh
    ```

3. **Configure the Gmail API:**

    - Go to the Google Cloud Console: [Google Cloud Console](https://console.cloud.google.com/)
    - Create a new project or select an existing one.
    - Enable the Gmail API for your project.
    - Go to `APIs & Services` > `Credentials`.
    - Click `Create Credentials` and select `OAuth client ID`.
    - Choose `Desktop app` as the application type.
    <!-- if the app is not published ensure that the senders are added to testers  -->
    - If the app is not published, ensure that the senders are added to testers in the OAuth consent screen.
    - Download the client configuration and save it as `client_secret.json` 

4. **Update the [`.gitignore`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flenzpaul%2Fdev%2Ftemp%2Fflutter_mtl_email_template%2F.gitignore%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/lenzpaul/dev/temp/flutter_mtl_email_template/.gitignore") file:**

    Ensure that sensitive files are not tracked by Git. The [`.gitignore`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flenzpaul%2Fdev%2Ftemp%2Fflutter_mtl_email_template%2F.gitignore%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/lenzpaul/dev/temp/flutter_mtl_email_template/.gitignore") file already includes:

    ```
    env
    client_secret.json
    token.json
    .DS_Store
    ```

## Usage

1. **Run the script:**

    You can run the script with a CSV file containing recipient information or enter the information manually.

    ```sh
    python email_template.py -o sample_recipients.csv
    ```

    If you don't provide a CSV file, the script will prompt you to enter the information manually.

2. **CSV File Format:**

    The CSV file should have the following columns:

    ```csv
    contact_name,company_name,your_name,your_position,your_contact_info,address_to,text_form,language,recipient_email
    ```

    Example:

    ```csv
    John Doe,ABC Tech,Alice Smith,Event Coordinator,alice@gdgmontreal.com,contact,short,en,johndoe@example.com
    ```

## Functions

- **`get_user_input()`**: Prompts the user to enter email details manually.
- **`read_csv_file(file_path)`**: Reads recipient information from a CSV file.
- **`get_email_content(data)`**: Generates the email content based on the provided data.
- **`get_gmail_service()`**: Authenticates and returns the Gmail API service.
- **`send_email(service, recipient, subject, content, cc=None, bcc=None)`**: Sends an email using the Gmail API.
- **`main()`**: Main function to handle the script execution.

## Dependencies

The required dependencies are listed in the `requirements.txt` file:

## Setup

1. **Clone the repository:**

    ```sh
    git clone <repository-url>
    ```

2. **Set up the environment:**

    Run the `setup_environment.sh` script to create a virtual environment and install the required dependencies.

    ```sh
    ./setup_environment.sh
    ```

3. **Configure the Gmail API:**

    - Go to the Google Cloud Console: [Google Cloud Console](https://console.cloud.google.com/)
    - Create a new project or select an existing one.
    - Enable the Gmail API for your project.
    - Go to `APIs & Services` > `Credentials`.
    - Click `Create Credentials` and select `OAuth client ID`.
    - Choose `Desktop app` as the application type.
    - Download the client configuration and save it as `client_secret.json`

4. **Update the [`.gitignore`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flenzpaul%2Fdev%2Ftemp%2Fflutter_mtl_email_template%2F.gitignore%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/lenzpaul/dev/temp/flutter_mtl_email_template/.gitignore") file:**

    Ensure that sensitive files are not tracked by Git. The [`.gitignore`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Flenzpaul%2Fdev%2Ftemp%2Fflutter_mtl_email_template%2F.gitignore%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/lenzpaul/dev/temp/flutter_mtl_email_template/.gitignore") file already includes:

    ```
    env
    client_secret.json
    token.json
    .DS_Store
    ```

## Usage

1. **Run the script:**

    You can run the script with a CSV file containing recipient information or enter the information manually.

    ```sh
    python email_template.py -o sample_recipients.csv
    ```

    If you don't provide a CSV file, the script will prompt you to enter the information manually.

2. **CSV File Format:**

    The CSV file should have the following columns:

    ```csv
    contact_name,company_name,your_name,your_position,your_contact_info,address_to,text_form,language,recipient_email
    ```

    Example:

  ```csv
  contact_name,company_name,your_name,your_position,your_contact_info,address_to,text_form,language,recipient_email,cc_email,bcc_email
  Lenz Paul,Lenz Tech inc.,Lenz Paul,GDG Organizer,lenz@fluttermtl.dev,contact,long,en,lenztpaul@gmail.com,"info@lenzpaul.dev,devfest2024@gdgmontreal.com",,
  ```

## Functions

- **`get_user_input()`**: Prompts the user to enter email details manually.
- **`read_csv_file(file_path)`**: Reads recipient information from a CSV file.
- **`get_email_content(data)`**: Generates the email content based on the provided data.
- **`get_gmail_service()`**: Authenticates and returns the Gmail API service.
- **`send_email(service, recipient, subject, content, cc=None, bcc=None)`**: Sends an email using the Gmail API.
- **`main()`**: Main function to handle the script execution.

## Dependencies

The required dependencies are listed in the `requirements.txt` file:
