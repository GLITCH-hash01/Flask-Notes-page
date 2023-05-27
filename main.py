from website import create_app
# Accessing the website module created

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)#Running the flask app