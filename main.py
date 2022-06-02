from textwrap import fill
import qrcode

class Qrcode:
    qr_number = 0
    def __init__(self, data):
        self.data = data
        self.qr = Qrcode.Makeqr(self)
        Qrcode.qr_number += 1

    def Makeqr(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=15,
            border=5
        )
        qr.add_data(self.data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save(f'{Qrcode.qr_number}.png')

    @property
    def Showqr(self):
        print(self.qr)

qr1 = Qrcode('https://google.com')
    
    




        

