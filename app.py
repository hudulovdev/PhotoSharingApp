from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for image upload
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    if file:
        # Save the uploaded image to the 'uploads' folder
        file.save('uploads/' + file.filename)
        return 'Image uploaded successfully!'
    else:
        return 'No image selected!'

if __name__ == '__main__':
    app.run(debug=True)
