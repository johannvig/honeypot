# honeypot

This project is a simple web application designed to detect and log web scrapers by using honeypot links. Originally implemented in Python, this project has been transformed into a web-based application using Flask, HTML, CSS, and JavaScript.

## Features

- Input your Mapbox API key, latitude, and longitude to retrieve a list of nearby addresses.
- Display the addresses in a scrollable list.
- Click on any address to open a map pointing to that location.
- Automatically remove duplicate addresses from the list.
- Log access to honeypot links and flag potential bots.
- Block suspected bots from accessing the site.

## Installation

To set up and run this project locally, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/honeypot-web.git
    ```

2. **Navigate to the project directory**:
    ```sh
    cd honeypot-web
    ```

3. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

4. **Activate the virtual environment**:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

5. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

6. **Run the Flask application**:
    ```sh
    python app.py
    ```

![image](https://github.com/johannvig/honeypot/assets/102874093/8c21a71b-889e-459a-b7cf-811175985928)

![image](https://github.com/johannvig/honeypot/assets/102874093/543f2b81-e85c-4695-bd76-71724a2b6bf0)
![image](https://github.com/johannvig/honeypot/assets/102874093/57451315-42ea-4d20-a3d2-de2e64c47f23)

