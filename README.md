# Jojen-AI

# Personalized AI Chat Assistant

## Overview

This project is a personalized, conversational AI assistant named "Jogin," designed to assist its creator, "Nayan." It is built using Python and powered by Google's Gemini Pro large language model. The assistant is accessible through a clean, web-based chat interface created with the Gradio library.

The AI's personality is defined by a system prompt that instructs it to be a helpful, respectful, and informative assistant.

## Features

*   **Personalized Experience:** The AI is configured to recognize its name ("Jogin") and its creator's name ("Nayan").
*   **Powered by Gemini Pro:** Utilizes Google's powerful Gemini Pro model for generating high-quality, relevant responses.
*   **Interactive Web UI:** A user-friendly chat interface provided by Gradio that runs locally in your browser.
*   **Secure API Key Handling:** Uses a `.env` file to securely manage the `GEMINI_API_KEY`, keeping it separate from the source code.
*   **Conversation History:** The interface maintains the context of the conversation for more coherent interactions.

## Prerequisites

Before you begin, ensure you have the following installed:
*   Python 3.7 or newer
*   A Google AI API Key. You can get one from [Google AI Studio](https://aistudio.google.com/app/apikey).

## Installation

Follow these steps to set up and run the project on your local machine.

1.  **Clone the Repository:**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-name>
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the Required Libraries:**
    Create a file named `requirements.txt` and add the following lines:
    ```
    openai
    gradio
    python-dotenv
    ```
    Then, install them using pip:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Your Environment Variables:**
    Create a file named `.env` in the root directory of your project. Add your Gemini API key to this file:
    ```
    GEMINI_API_KEY="your_gemini_api_key_here"
    ```

## Usage

To start the AI assistant, run the main Python script from your terminal:

```bash
python app.py  # Or whatever you have named your script
```

After running the script, you will see output in your terminal indicating that a local web server is running. It will provide a URL (usually `http://127.0.0.1:7860`). Open this URL in your web browser to start chatting with your AI assistant.

## Customization

You can easily customize the assistant's and creator's names. Open the main Python script and modify the following variables:

```python
# Change the assistant's name
name = "NewAssistantName"

# Change the creator's name
c_name = "YourName"

# You can also modify the system_prompt to change the AI's personality and instructions
system_prompt = f"You are a helpful assistant named {name}. You are designed to assist {c_name}..."
```
