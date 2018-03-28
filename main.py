from caesar import rotate_string

from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }

            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/" method="POST">
            <label>Rotate by:
                <input type="text" name="rot" value="0" />
            </label>
            <textarea name="text"></textarea>
            <input type="submit">
        </form>
    </body>
</html>"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rot_encrypt = request.POST['int(rot)']
    text_encrypt = request.POST['text']
    new_string = rotate_string(text_encrypt, rot_encrypt)
    return "<h1>" + new_string + "<h1>"

app.run()