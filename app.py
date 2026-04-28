from flask import Flask, render_template

# Create the Flask app
app = Flask(__name__)

# Define a route (URL path) for your site
@app.route("/")
def home():
    # Render an HTML file stored in the 'templates' folder
    return render_template("home.html")

@app.route("/yandi")
def yandi():
    return render_template("yandi.html")

@app.route("/andi")
def andi():
    return render_template("andi.html")
# Run the app if this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)
