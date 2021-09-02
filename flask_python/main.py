from website import create_app

app = create_app()

if __name__ == "__main__":  # Only executes if we run the file, can't import
    app.run(debug=True) # Runs flask app and starts the webserver