from langchain.agents import Tool
from openai import OpenAI
from bs4 import BeautifulSoup
from io import BytesIO
import base64
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve API keys from environment variables
my_key_openai = os.getenv("OPENAI_API_KEY")
my_key_stabilityai = os.getenv("STABILITYAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=my_key_openai)

def generate_image_with_dalle(prompt):
    """
    Generates an image using OpenAI's DALL·E 3 model.
    - Sends a text prompt to the API and receives an image URL.
    - Downloads and saves the image locally.
    - Returns an HTML <a> link to the saved image.
    """

    AI_Response = client.images.generate(
        model="dall-e-3",  # Specify the DALL·E 3 model
        size="1024x1024",   # Image resolution
        quality="hd",       # High-definition quality
        n=1,                # Number of images to generate
        response_format="url",  # Response format as a URL
        prompt=prompt       # The text prompt for image generation
    )
    
    image_url = AI_Response.data[0].url  # Extract the image URL

    # Download the image from the URL
    response = requests.get(image_url)
    image_bytes = BytesIO(response.content)

    # Generate a timestamp for the filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = f"./img/generated_image_{timestamp}.png"

    # Create the directory if it does not exist
    if not os.path.exists("./img"):
        os.makedirs("./img")
    
    # Save the image to the local directory
    with open(filepath, "wb") as file:
        file.write(image_bytes.getbuffer())

    # Return an HTML link to the saved image
    return f'<a href="{filepath}">Your image is here</a>'

def generate_with_SD(prompt):
    """
    Generates an image using Stability AI's Stable Diffusion XL model.
    - Sends a text prompt to the API.
    - Receives an image in Base64 format.
    - Decodes, saves, and returns an HTML link to the image.
    """

    url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

    # Set request headers
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {my_key_stabilityai}",
    }

    # Define the request payload
    body = {
        "steps": 40,        # Number of generation steps
        "width": 1024,      # Image width
        "height": 1024,     # Image height
        "seed": 0,          # Random seed for reproducibility
        "cfg_scale": 5,     # Guidance scale for prompt adherence
        "samples": 1,       # Number of images to generate
        "text_prompts": [
            {"text": prompt, "weight": 1},       # Main prompt
            {"text": "blurry, bad", "weight": -1}  # Negative prompt to avoid poor quality images
        ],
    }

    # Send request to Stability AI API
    response = requests.post(url, headers=headers, json=body)
    data = response.json()

    # Process the response and save the image
    for image in data["artifacts"]:
        image_bytes = base64.b64decode(image["base64"])  # Decode the Base64 image

        # Generate a timestamp for the filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = f"./img/generated_image_{timestamp}.png"

        # Create the directory if it does not exist
        if not os.path.exists("./img"):
            os.makedirs("./img")
        
        # Save the image to the local directory
        with open(filepath, "wb") as file:
            file.write(image_bytes)

    # Return an HTML link to the saved image
    return f'<a href="{filepath}">Your image is here</a>'

def get_tool(selected_image_generator):
    """
    Returns the appropriate image generation tool based on the selected model.
    - Uses DALL·E 3 if 'DALL-E 3' is selected.
    - Uses Stable Diffusion XL if 'Stable Diffusion XL' is selected.
    """

    if selected_image_generator == "DALL-E 3":
        return Tool(
            name="Generate Image",
            func=generate_image_with_dalle,
            description="""Useful for generating an image based on textual instructions or prompts. 
            It returns the filepath where the image is saved. This filepath must be provided to the user.
            The filepath is enclosed within HTML tags to create a clickable link.
            """
        )

    elif selected_image_generator == "Stable Diffusion XL":
        return Tool(
            name="Generate Image",
            func=generate_with_SD,
            description="""Useful for generating an image based on textual instructions or prompts. 
            It returns the filepath where the image is saved. This filepath must be provided to the user.
            The filepath is enclosed within HTML tags to create a clickable link.
            """
        )

def analyze_webpage(target_url):
    """
    Fetches and analyzes the content of a given webpage.
    - Sends a GET request to the specified URL.
    - Extracts and returns the plain text content, limited to 4000 characters.
    """

    # Send a request to the target URL
    response = requests.get(target_url)
    html_content = response.text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")
    stripped_content = soup.get_text()  # Extract only text content

    # Limit the text content to 4000 characters
    if len(stripped_content) > 4000:
        stripped_content = stripped_content[:4000]

    return stripped_content

def get_web_tool():
    """
    Returns a tool for fetching webpage content.
    - The tool retrieves plain text from a given URL.
    """

    return Tool(
        name="Get Webpage",
        func=analyze_webpage,
        description="Useful for retrieving text content from a specific webpage."
    )
