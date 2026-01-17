from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/get-started')
def get_started():
    return render_template('get_started.html')

@app.route('/fact-checking-websites')
def fact_checking_websites():
    websites = [
        {
            'name':'Public Information Bearueau',
            'url':'https://pib.gov.in/factcheck.aspx',
            'description':'Official government portal for fact-checking news and information.'
        },
       
        {
            'name': 'FactCheck.in',
            'url': 'https://www.factchecker.in',
            'description': 'Non-partisan, nonprofit organization dedicated to fact-checking.'
        },

      
        {
            'name': 'Google Fact Check Explorer',
            'url': 'https://toolbox.google.com/factcheck/explorer',
            'description': 'Search fact-checks from multiple organizations.'
        }
    ]
    return render_template('fact_checking_websites.html', websites=websites)

@app.route('/about')
def about():
    return render_template('about_us.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/submit-news', methods=['POST'])
def submit_news():
    data = request.get_json()
    news = data.get('news')
    return jsonify({
        'status': 'success',
        'message': 'News submitted for analysis',
        'news': news
    })
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
