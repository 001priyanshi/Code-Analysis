# Code Explainer & Optimizer

A powerful web application that uses **Gemini Pro AI** to analyze, explain, refactor, and optimize code in **any programming language**. Perfect for developers, students, and interview preparation!

## 🚀 Features

- **📝 Line-by-line Code Explanation**: Get detailed explanations of what each line of code does
- **🔧 Code Refactoring**: Receive improved, more readable, and efficient versions of your code
- **📊 Complexity Analysis**: Get time and space complexity estimates with detailed breakdowns
- **👔 Interview-Ready Explanations**: Convert your code into professional technical explanations perfect for interviews
- **🌍 Multi-Language Support**: Supports 100+ programming languages including Python, JavaScript, Java, C++, Rust, Go, and many more
- **🎨 Beautiful Modern UI**: Clean, responsive interface that works on desktop and mobile

## 🛠️ Setup

### Prerequisites
- Python 3.8 or higher
- Gemini Pro API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### Installation

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd code-explainer-optimizer
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Gemini Pro API key**
   
   **Option A: Environment Variable (Recommended)**
   ```bash
   # On Windows
   set GEMINI_API_KEY=your-api-key-here
   
   # On macOS/Linux
   export GEMINI_API_KEY=your-api-key-here
   ```
   
   **Option B: Direct in code (for testing only)**
   Edit `app.py` and replace `'your-gemini-api-key-here'` with your actual API key.

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to [http://localhost:5000](http://localhost:5000)

## 🎯 How to Use

1. **Select Programming Language**: Choose from 100+ supported languages
2. **Paste Your Code**: Either type or paste your code into the editor
3. **Choose Analysis Type**:
   - **Explain Code**: Get line-by-line explanations
   - **Refactor Code**: Get improved, optimized versions
   - **Complexity Analysis**: Get time/space complexity estimates
   - **Interview Ready**: Get professional technical explanations
4. **View Results**: See detailed analysis in the right panel

## 📚 Supported Languages

### Popular Languages
- Python, JavaScript, Java, C++, C#, Go, Rust
- TypeScript, PHP, Ruby, Swift, Kotlin
- Scala, Haskell, Clojure, Elixir, Erlang

### Web Technologies
- HTML, CSS, SCSS, Sass, Less
- SQL, JSON, XML, YAML, TOML

### Build Tools & Configs
- Dockerfile, Makefile, CMake
- package.json, requirements.txt, Cargo.toml
- pom.xml, build.gradle, go.mod

### And 100+ more languages and file types!

## 🔧 API Endpoints

- `GET /` - Main application interface
- `POST /analyze` - Analyze code (JSON payload)
- `GET /health` - Health check endpoint

### Example API Usage
```bash
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "code": "def hello(): return \"Hello World\"",
    "language": "python",
    "analysis_type": "explain"
  }'
```

## 🎨 Features in Detail

### Code Explanation
- Line-by-line breakdown
- Logic flow analysis
- Important concepts highlighted
- Potential issues identified

### Code Refactoring
- Improved readability
- Better performance
- Best practices implementation
- Enhanced structure and organization

### Complexity Analysis
- Time complexity (Big O notation)
- Space complexity analysis
- Detailed breakdown of why complexities occur
- Optimization suggestions

### Interview-Ready Explanations
- Problem statement and approach
- Algorithm/design pattern identification
- Complexity analysis
- Trade-offs and alternatives
- Real-world applications
- Key technical concepts

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
```bash
# Using Gunicorn (recommended)
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Using Waitress (Windows)
pip install waitress
waitress-serve --host=0.0.0.0 --port=5000 app:app
```

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 🔒 Security Notes

- Never commit your API key to version control
- Use environment variables for sensitive data
- Consider rate limiting for production use
- Validate input code for security concerns

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **Google Gemini Pro** for providing the AI capabilities
- **Flask** for the web framework
- **Font Awesome** for the beautiful icons

## 🆘 Support

If you encounter any issues:
1. Check that your Gemini Pro API key is valid
2. Ensure all dependencies are installed
3. Check the browser console for errors
4. Verify your code is valid for the selected language

## 🔮 Future Enhancements

- [ ] VSCode extension
- [ ] Code snippet library
- [ ] Batch processing
- [ ] Custom prompt templates
- [ ] Export to PDF/Markdown
- [ ] Integration with GitHub/GitLab
- [ ] Code review suggestions
- [ ] Performance benchmarking

---

**Happy coding! 🎉** 