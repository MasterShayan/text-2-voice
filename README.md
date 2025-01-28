# text-2-voice
An API for converting text to voice.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/text-2-voice.git
    cd text-2-voice
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your environment variables:
    ```
    SECRET_KEY=your_secret_key
    DEBUG=True
    ```

5. Run the server using `uvicorn`:
    ```bash
    uvicorn main:app --reload
    ```

    Or using `python3`:
    ```bash
    python3 main.py
    ```

## Usage

1. Run the server:
    ```bash
    python manage.py runserver
    ```

2. Open your browser and navigate to:
    ```
    http://127.0.0.1:8000/create_voice/your_text
    ```

## Example

To convert "Hello World" to voice, use the following URL:
```
http://127.0.0.1:8000/create_voice/Hello%20World
```
