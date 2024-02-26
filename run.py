from ChatbotWebsite import create_app, db

# Create the app
app = create_app()

# Run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
