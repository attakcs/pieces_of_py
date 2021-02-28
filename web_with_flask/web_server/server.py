from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name + '.html')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return redirect('/thankyou')
    else:
        return 'something went wrong'


if __name__ == '__main__':
    app.run(debug=True)