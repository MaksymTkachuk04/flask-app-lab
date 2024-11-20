from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()  # Launch built-in web server and run this Flask webapp, debug=True
