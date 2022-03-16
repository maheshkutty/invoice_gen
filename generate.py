from io import StringIO

from jinja2.loaders import PackageLoader
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
from docx2pdf import convert
import os
import datetime
import time
import pythoncom
import pdfkit
from flask import render_template_string
import jinja2

os.environ['path']  = 'C:\\Program Files\\wkhtmltopdf\\bin'

def get_context():
    """ You can generate your context separately since you may deal with a lot 
        of documents. You can carry out computations, etc in here and make the
        context look like the sample below.
    """
    return {
        'invoice_no': 12345,
        'date': '30 Mar',
        'due_date': '30 Apr',
        'name': 'Jane Doe',
        'address': '123 Quiet Lane',
        'subtotal': 335,
        'tax_amt': 10,
        'total': 345,
        'amt_paid': 100,
        'amt_due': 245,
        'row_contents': [
            {
                'description': 'Eggs',
                'quantity': 30,
                'rate': 5,
                'amount': 150
            }, {
                'description': 'All Purpose Flour',
                'quantity': 10,
                'rate': 15,
                'amount': 150
            }, {
                'description': 'Eggs',
                'quantity': 5,
                'rate': 7,
                'amount': 35
            }
        ]
    }

def render_without_request(template_name, **template_vars):
    """
    Usage is the same as flask.render_template:

    render_without_request('my_template.html', var1='foo', var2='bar')
    """
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    print(templateLoader)
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "1.html"
    template = templateEnv.get_template(TEMPLATE_FILE)
    outputText = template.render(template_vars) 
    return outputText

def from_html_template(template, signature, context):
    # context = get_context()
    file_name = context['name']
    dateObjFolder = str(datetime.date.today())
    parent_directory  = 'D:\Workspace\SPIT\SEM 2\Process automation\Project\client_invoice'
    file_name = file_name.replace(" ", "_") + "_" + str(int(time.time())) + ".pdf"
    if os.path.isdir(os.path.join(parent_directory, dateObjFolder)) == False:
        os.makedirs(os.path.join(parent_directory, dateObjFolder))
    storefile = os.path.join(parent_directory, dateObjFolder) + "\\" + file_name
    html = render_without_request(template, context=context)
    css = ["./bootstrap-5.1.3-dist/css/bootstrap.min.css"]
    pdf = pdfkit.from_string(html, storefile)
    return storefile

# def from_template(template, signature, context):
#     target_file = 'Invoice.docx'

#     template = DocxTemplate(template)
#     # context = get_context()  # gets the context used to render the document

#     img_size = Cm(7)  # sets the size of the image
#     sign = InlineImage(template, signature, img_size)
#     context['signature'] = sign  # adds the InlineImage object to the context
#     template.render(context)
#     file_name = context['name']
#     dateObjFolder = str(datetime.date.today())
#     parent_directory  = 'D:\Workspace\SPIT\SEM 2\Process automation\Project\client_invoice'
#     file_name = file_name.replace(" ", "_") + "_" + str(int(time.time())) + ".docx"
#     if os.path.isdir(os.path.join(parent_directory, dateObjFolder)) == False:
#         os.makedirs(os.path.join(parent_directory, dateObjFolder))
#     storefile = os.path.join(parent_directory, dateObjFolder) + "/" + file_name
#     pythoncom.CoInitialize()
#     template.save(storefile)
#     convert(storefile)
#     return target_file

# template = 'InvoiceTpl.docx'
# signature = 'signature.png'
# from_html_template(template, signature)