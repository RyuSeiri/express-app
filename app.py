from flask import Flask, request, render_template
import re

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        regex = request.form['regex']
        text = request.form['text']
        global_search = request.form.get('global_search')

        if global_search:
            matches = re.findall(regex, text)
        else:
            match = re.search(regex, text)
            matches = [match] if match else []

        return render_template('index.html', matches=matches)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
