# user_interface/interface_web.py

import sys
import os
from flask import Flask, render_template, request, jsonify

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from parsers.python_parser import parse_python_code
from analysis_engine.static_analysis import analyze_static
from analysis_engine.rule_management import load_rules

app = Flask(__name__)

# Set the template directory explicitly
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
app.template_folder = template_dir

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_code():
    code = request.form['code']

    # Parse Python code
    parse_result = parse_python_code(code)
    if not parse_result['success']:
        return jsonify({'error': parse_result['message']})

    # Load Python-specific rules
    rules = load_rules('python')

    # Perform static analysis
    analysis_result = analyze_static(code)
    vulnerabilities = analysis_result['vulnerabilities']
    quality_issues = analysis_result['quality_issues']

    return jsonify({'vulnerabilities': vulnerabilities, 'quality_issues': quality_issues})

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change 5001 to another available port
