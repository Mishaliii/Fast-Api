from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_html():
    html_content = """
    <html>
        <head>
            <title>FastAPI Interactive Page</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    background-color: #1e1e2e;
                    color: #ffffff;
                    margin: 0;
                    padding: 20px;
                }
                h1 {
                    color: #00bcd4;
                }
                p {
                    font-size: 20px;
                }
                button {
                    background-color: #ff9800;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    font-size: 18px;
                    cursor: pointer;
                    border-radius: 5px;
                }
                button:hover {
                    background-color: #e68900;
                }
            </style>
        </head>
        <body>
            <h1>Welcome to FastAPI Web Page</h1>
            <p>Click the button below to see an alert message.</p>
            <button onclick="showMessage()">Click Me</button>
            <script>
                function showMessage() {
                    alert('Hello from FastAPI!');
                }
            </script>
        </body>
    </html>
    """
    return html_content
