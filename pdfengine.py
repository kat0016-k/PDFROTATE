# Using flask to make an api
# import necessary libraries and functions
# using flask_restful
from PyPDF2 import PdfReader, PdfWriter
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

def pdfrotate(pdf_input):
    output_file = open('rotated.pdf', 'wb')

    pdf = PdfReader(pdf_input)
    writer = PdfWriter()
    num_pages = pdf.getNumPages()

    for i in range(num_pages):
        page = pdf.getPage(i)
        if i == 3:
            page.rotate_clockwise(90)
        writer.add_page(page)
        
    writer.write(output_file)
    return output_file
  
# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)
  
# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Hello(Resource):
  
    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
  
        return jsonify({'message': 'hello world'})
  
    # Corresponds to POST request
    def post(self):
          
        data = request.get_json()     # status code
        return jsonify({'data': data}), 201
  
  
# another resource to calculate the square of a number
class pdf(Resource):
  
    def post(self, files):
        output = pdfrotate(files)
        return output
  
  
# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/')
api.add_resource(pdf, '/pdf')
  
  
# driver function
if __name__ == '__main__':
  
    app.run(debug = True)