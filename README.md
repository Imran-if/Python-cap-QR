# QR Code Generator Web App

This project is a simple student-friendly web application that generates a QR code from any URL.

## Features
- Open a simple web page in the browser
- Enter a website URL
- Generate and display a QR code instantly

## Prerequisites
- Python 3
- Flask
- qrcode
- Pillow

## Install dependencies
Run:

```powershell
py -m pip install -r requirements.txt
```

## Run the app
Start the web app with:

```powershell
py QR_code_generator.py
```

Then open:

```text
http://127.0.0.1:5000
```

## Demo usage
1. Open the web page in your browser.
2. Enter a URL such as https://example.com.
3. Click Generate QR Code.
4. The QR code will appear on the page.

## Project files
- QR_code_generator.py: Flask web app
- requirements.txt: Python dependencies
- tests/test_qr_code_generator.py: simple test for the app

