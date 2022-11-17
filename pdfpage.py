from os import listdir
from PyPDF2 import PdfReader, PdfWriter
from flask import Flask, request

input_dir  = "C:\\Users\\abhis\\Desktop\\Old Desktop\\Web Dev\\DSA\\FLASK API\\"
output_dir = 'output_pdf.pdf'

for fname in listdir(input_dir):
    if not fname.endswith(".pdf"):  # ignore non-pdf files
        continue
    reader = PdfReader(input_dir + fname)
    writer = PdfWriter()
    for page in reader.pages:
        page.rotate_clockwise(270)
        writer.add_page(page)
    with open(output_dir + fname, "wb") as pdf_out:
        writer.write(pdf_out)