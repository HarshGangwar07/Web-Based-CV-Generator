# Web Based CV Generator Project

This project is a Django application that allows users to submit their profile information through a form, view a list of profiles, and generate a PDF resume for each profile.

## Features

- Submit profile information through a form
- View a list of submitted profiles
- Generate and download a PDF resume for each profile

## Requirements

- Python 3.13.1
- Django 5.1.4
- pdfkit
- wkhtmltopdf

## Installation

1. Clone the repository:

2. Create and activate virtual enivronment

3. Install the required packages

4. Install wkhtmltopdf
--> Download the installer from the wkhtmltopdf releases page.    

-->Install wkhtmltopdf using the downloaded installer.

-->Add the path to the wkhtmltopdf executable to your system's  PATH environment variable

```sh
git clone https://github.com/yourusername/yourproject.git
cd yourproject

python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

pip install -r requirements.txt
