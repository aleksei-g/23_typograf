from flask import Flask, render_template, request
from typograf import typograf

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        input_text = request.form['text']
        result = typograf(input_text)
        return render_template('form.html',
                               input_text=input_text,
                               result=result)
    else:
        return render_template('form.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
