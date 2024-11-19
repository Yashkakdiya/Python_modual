import barcode  
from barcode.writer import ImageWriter  
from IPython.display import Image, display  


barcode_format = barcode.get_barcode_class('ean13')  

barcode_number = '123456789012'  # 12-digit number for EAN-13  
barcode_image = barcode_format(barcode_number, writer=ImageWriter())  

 
barcode_filename = 'barcode_image'  
barcode_image.save(barcode_filename)  


display(Image(filename=f'{barcode_filename}.png'))