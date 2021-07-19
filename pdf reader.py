import pyttsx3
import PyPDF2
path = open('C://Users//rajes//Downloads//python_tutorial.pdf', 'rb')
reading_pdf=PyPDF2.PdfFileReader(path)
pdf_pages=reading_pdf.numPages
pdf_speaker=pyttsx3.init()
choose_page=reading_pdf.getPage(4)
pdf_text=choose_page.extractText()
pdf_speaker.say(pdf_text)
pdf_speaker.runAndWait()
