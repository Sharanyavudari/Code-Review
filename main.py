# main.py

from user_interface.interface_web import app

def main():
    # Additional setup tasks, if any

    # Run the Flask app
    app.run(debug=True)

if __name__ == '__main__':
    main()
