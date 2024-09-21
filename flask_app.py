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
                justify-content: center;
                padding: 20px;
                text-align: center;
            }}

    
            .centered-quote {{
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                text-align: center;
                font-size: calc(16px + 2vmin);
            }}
        </style>
    </head>
    <body>
        <div class="centered-quote">
            {quote}
        </div>
    </body>
    </html>
    """

