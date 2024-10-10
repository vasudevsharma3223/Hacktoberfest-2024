from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML code using render_template_string
html_code = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Python Web App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            text-align: center;
            background-color: #f4f4f4;
        }
        header {
            background-color: #333;
            color: white;
            padding: 1rem;
        }
        form {
            margin: 20px;
        }
        label, input {
            display: block;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to My Python Web App</h1>
    </header>

    <section>
        <h2>Contact Form</h2>
        <form method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>

            <button type="submit">Submit</button>
        </form>

        {% if submitted %}
            <p>Thank you, {{ name }}! Your message: "{{ message }}" has been received.</p>
        {% endif %}
    </section>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    submitted = False
    name = ''
    message = ''
    
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        submitted = True

    return render_template_string(html_code, submitted=submitted, name=name, message=message)

if __name__ == '__main__':
    app.run(debug=True)
