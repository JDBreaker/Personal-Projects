from flask import Flask, render_template, request
from webscraper import scrape_website

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form['url']
    urls, image_sources = scrape_website(url)
    return render_template('results.html', urls=urls, images=image_sources)

if __name__ == '__main__':
    app.run(debug=True)
