
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
          "1 - создание qr кода\n"
          "2 - укарачивание/маскировка ссылок\n"
          "3 - отчистить консоль\n"
          "4 - обновить модули\n"
          "99 - выход\n"
          "100 - ссылки\n"
          "-----------------------------------\n"
          "           By:R3loader \n"
          )
    print()
    metod = input(">> ")
    if metod=="1":
        qR_code()
    elif metod=="2":
        links()
    elif metod=="3":
        print("\n"*100)
    elif metod=="4":
        download.download()
    elif metod=="99":
        exit(232)
    elif metod=="100":
        webbrowser.open("https://github.com/R3loader", new=0, autoraise=True)
        os.system("termux-open-url https://github.com/R3loader")
        print("⬇️github⬇️\n" +
              "https://github.com/R3loader/domen-master\n" +
               "⬇️buy me a coffe⬇️\n" +
              "https://www.buymeacoffee.com/r3oader\n" +
              "⬇️telegram⬇️\n" +
              "https://t.me/termuxguid\n")
    else:
        print("\n\n")




def links():

    def shorten_url(url):
        try:
            response = requests.get(url)
            print('\nВы не можете зайти на сайт', url)
        except:
            print('\nВы на можете зайти на сайт', url)
            print("д/н")
            quest = input("Продолжить?>> ")
            if quest=="д":
                print("Хорошо...\n")
            elif quest=="н":
                launcher()
        print("Замаскрованные ссылки")
        for c in data.url_mask:
            print("\n"+str(c)+url)
        return pyshorteners.Shortener().clckru.short(url)

    url = input("Введите ссылку: ")
    print("Укороченая ссылка- ", format(shorten_url(url)))
def qR_code():
    # Вывод инструкции с использованием \n для переноса строк
    # Вывод инструкции с использованием \n для переноса строк


    # Ввод текста для создания QR-кода
    text = input("Введите текст для создания QR-кода: ")

    # Создаем объект QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Добавляем данные в QR-код
    qr.add_data(text)
    qr.make(fit=True)

    # Создаем изображение QR-кода
    img = qr.make_image(fill_color="black", back_color="white")

    # Сохраняем изображение QR-кода в файл
    img.save("qrcode.png")

    print("QR-код успешно создан и сохранен в файл 'qrcode.png'.")

    # Загружаем QR-код на сайт ImgBB
    api_key = data.your_api  # Замените 'YOUR_API_KEY' на ваш реальный API-ключ от ImgBB
    if api_key=="None":

        api_key=input("Ваш api>>")
    upload_url = 'https://api.imgbb.com/1/upload'

    with open("qrcode.png", 'rb') as image_file:
        response = requests.post(upload_url, params={'key': api_key}, files={'image': image_file})

    if response.status_code == 200:
        result = response.json()
        image_url = result['data']['url']
        print(f'QR-код успешно загружен на ImgBB. URL: {image_url}')
    else:
        print('Ошибка при загрузке QR-кода:', response.status_code)



