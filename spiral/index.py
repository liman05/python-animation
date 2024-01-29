from barcode import EAN13
from barcode.writer import ImageWriter

number = '3526373610124'
code = EAN13(number, writer=ImageWriter())
code.save("new_barcode")

