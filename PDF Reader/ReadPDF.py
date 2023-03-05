import pyttsx3
from PyPDF2 import PdfReader

pdf_file = open('test.pdf', 'rb')
read_pdf = PdfReader(pdf_file, strict=False)

number_of_pages = len(read_pdf.pages)

engine = pyttsx3.init()
#Replace this for i in range(n, number_of_pages):
#Where n is the page that you would like the reader to start from.
for i in range(number_of_pages):
    page = read_pdf.pages[i]
    page_content = page.extract_text()
    new_rate = 200
    engine.setProperty('rate', new_rate)
    new_volume = 0.5
    engine.setProperty('volume', new_volume)
    engine.say(page_content)

engine.runAndWait()
