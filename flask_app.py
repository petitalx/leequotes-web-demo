from flask import Flask
from leequotes import leequotes

app = Flask(__name__)


@app.route('/')
def hello_world():
    quote = leequotes.random()\
        .replace("\\n", "<br>")\
        # .replace(". ", ".<br>")

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Quote of the Day</title>
        <style>
            body, html {{
                height: 100%;
                margin: 0;
                font-family: Verdana, sans-serif, system-ui;
            }}
            
            body {{
                background-color: #F7F7F7; /* Wheat color for a paper-like background */
                color: #333; /* Dark gray color for text which is easier on the eyes */
                
                display: flex;
                align-items: center;
                justify-content: space-between;
                flex-direction: column;
                padding: 24px;
                text-align: center;
                height: calc(100vh - 48px);
            }}

    
            #quote {{
                text-align: center;
                font-size: calc(16px + 2vmin);
                max-width: 650px;
            }}
            
            #footer {{
                text-align: center;
                font-size: 12px;
            }}
            
            #instructions {{
                font-size: calc(8px + 1vmin);
                color: #c2c2c2;
            }}
        </style>
    </head>
    <body>
        <div id="instructions">
            Refresh the page with ⌘-R or Ctrl-R to load another Bruce Lee quote
        </div>
        <div id="quote">
            {quote}
        </div>
        <div id="footer">
            <p>
            This is a simple demo of the <a href="https://pypi.org/project/leequotes/">leequotes</a> python package. 
            <p>
            Made with ❤️ by <a href="petitapetit.io">alexandre petit</a>    
        </div>
    </body>
    </html>
    """

