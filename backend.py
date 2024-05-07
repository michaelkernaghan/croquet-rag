from flask import Flask, request, jsonify, render_template
import create_database
import query_data  # Ensure this updated module is correctly referenced

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def handle_query():
    data = request.json
    if not data or 'query' not in data:
        return jsonify({'error': 'Invalid data received'}), 400
    query = data['query']
    response = query_data.process_query(query)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
