from flask import Flask, request
import generate

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=['POST'])
def home():
    template = 'InvoiceTpl.docx'
    signature = 'signature.png'
    context = request.json
    filename = generate.from_html_template(template, signature, context)
    print(request.json)
    print(filename)
    return {
        "status":"success",
        "filename":filename
    }

@app.route("/demo", methods=['POST'])
def demo():
    print(request.json)
    return {
        "status":"success"
    }


if __name__ == 'main':
    app.run()