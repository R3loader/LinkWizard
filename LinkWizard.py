
import download
import qrcode
import requests
import data
import requests
import pyshorteners
import data
import os
import webbrowser

def launcher():
    print("\n           \LinkWizard/"
          "\n"
          "-----------------------------------\n"
          "1 - Create QR code\n"
          "2 - Shorten/Mask Links\n"
          "3 - Clear Console\n"
          "4 - Update Modules\n"
          "99 - Exit\n"
          "100 - Links\n"
          "-----------------------------------\n"
          "           By: R3loader \n"
          )
    print()
    method = input(">> ")
    if method == "1":
        qR_code()
    elif method == "2":
        links()
    elif method == "3":
        print("\n" * 100)
    elif method == "4":
        download.download()
    elif method == "99":
        exit(232)
    elif method == "100":
        webbrowser.open("https://github.com/R3loader", new=0, autoraise=True)
        os.system("termux-open-url https://github.com/R3loader")
        print("⬇️GitHub⬇️\n" +
              "https://github.com/R3loader/domen-master\n" +
               "⬇️Buy Me a Coffee⬇️\n" +
              "https://www.buymeacoffee.com/r3oader\n" +
              "⬇️Telegram⬇️\n" +
              "https://t.me/termuxguid\n")
    else:
        print("\n\n")

def links():
    def shorten_url(url):
        try:
            response = requests.get(url)
            print('\nYou cannot access the website', url)
        except:
            print('\nYou cannot access the website', url)
            print("Y/N")
            quest = input("Continue?>> ")
            if quest == "Y":
                print("Alright...\n")
            elif quest == "N":
                launcher()
        print("Masked Links")
        for c in data.url_mask:
            print("\n" + str(c) + url)
        return pyshorteners.Shortener().clckru.short(url)

    url = input("Enter the URL: ")
    print("Shortened URL - ", format(shorten_url(url)))

def qR_code():
    text = input("Enter the text to create a QR code: ")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save("qrcode.png")

    print("QR code successfully created and saved to 'qrcode.png'.")

    api_key = data.your_api  # Replace 'YOUR_API_KEY' with your actual API key from ImgBB
    if api_key == "None":
        api_key = input("Your API key>>")
    upload_url = 'https://api.imgbb.com/1/upload'

    with open("qrcode.png", 'rb') as image_file:
        response = requests.post(upload_url, params={'key': api_key}, files={'image': image_file})

    if response.status_code == 200:
        result = response.json()
        image_url = result['data']['url']
        print(f'QR code successfully uploaded to ImgBB. URL: {image_url}')
    else:
        print('Error uploading QR code:', response.status_code)
