from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from datetime import datetime
import os
import json
from dotenv import load_dotenv  # ✅ Import dotenv

# ✅ Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# ✅ Get API key from environment variable
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# ✅ Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)


# Initialize Gemini Pro model
model = genai.GenerativeModel('gemini-2.0-flash')

def analyze_code_with_gemini(code, language, analysis_type):
    """Analyze code using Gemini Pro based on the requested analysis type"""
    
    prompts = {
        'explain': f"""
        Analyze this {language} code and provide a detailed line-by-line explanation.
        Focus on:
        - What each line does
        - The logic flow
        - Important concepts used
        - Any potential issues or edge cases
        
        Code:
        {code}
        
        Provide a clear, educational explanation suitable for someone learning {language}.
        """,
        
        'refactor': f"""
        Analyze this {language} code and provide a refactored version that is:
        - More readable and maintainable
        - More efficient where possible
        - Following best practices for {language}
        - Better structured and organized
        
        Original Code:
        {code}
        
        Provide the refactored code with comments explaining the improvements made.
        """,
        
        'complexity': f"""
        Analyze this {language} code and provide detailed time and space complexity analysis.
        
        Code:
        {code}
        
        Provide:
        1. Time Complexity: O() notation with explanation
        2. Space Complexity: O() notation with explanation
        3. Breakdown of why these complexities occur
        4. Suggestions for optimization if possible
        """,
        
        'interview': f"""
        Convert this {language} code into an interview-ready technical explanation.
        
        Code:
        {code}
        
        Provide a professional explanation that includes:
        1. Problem statement and approach
        2. Algorithm/design pattern used
        3. Time and space complexity
        4. Trade-offs and alternatives considered
        5. Real-world applications or similar problems
        6. Key technical concepts demonstrated
        
        Make it suitable for explaining to a technical interviewer or recruiter.
        """
    }
    
    try:
        response = model.generate_content(prompts[analysis_type])
        return response.text
    except Exception as e:
        return f"Error analyzing code: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    code = data.get('code', '')
    language = data.get('language', 'python')
    analysis_type = data.get('analysis_type', 'explain')
    
    if not code.strip():
        return jsonify({'error': 'Please provide some code to analyze'}), 400
    
    result = analyze_code_with_gemini(code, language, analysis_type)
    
    return jsonify({
        'result': result,
        'timestamp': datetime.now().isoformat(),
        'language': language,
        'analysis_type': analysis_type
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    print("🚀 Starting Code Explainer & Optimizer on http://localhost:5000")
    print("📚 Supporting 100+ programming languages")
    print("🔧 Analysis types: explain, refactor, complexity, interview")
    print("🛑 Press Ctrl+C to stop the server\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000) 