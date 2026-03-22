from flask import Flask, render_template_string
import os

app = Flask(__name__)

# 讀取 HTML 文件
html_file_path = os.path.join(os.path.dirname(__file__), 'index.html')

@app.route('/')
def index():
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    return html_content

if __name__ == '__main__':
    print("🌍 天氣查詢應用已啟動！")
    print("請在瀏覽器中打開: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
