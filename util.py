import socket
import geocoder
import google.generativeai as genai
from PIL import Image

# Local
from constants import RECYCLING_INSTRUCTIONS_PROMPT, RECYCLING_LOCATIONS_PROMPT_COORDINATES, RECYCLING_LOCATIONS_PROMPT_DURHAM


def get_current_location() -> str:
    location = geocoder.ip("me")
    lat = location.latlng[0]
    lng = location.latlng[1]
    return lat, lng


# Function to call the Gemini LLM API (you'll need to replace with actual API details)
def get_recycling_instructions(image: Image, gemini_model: genai.GenerativeModel) -> str:
    response = gemini_model.generate_content([
        RECYCLING_INSTRUCTIONS_PROMPT,
        image,
    ])
    response.resolve()
    return response.text


# Function to find nearby recycling places (this is a placeholder for the actual functionality)
def find_nearby_recycling_places(image: Image, gemini_model: genai.GenerativeModel) -> str:
    lat, lng = get_current_location()
    print("HOSTNAME IS")
    print(socket.gethostname())
    # formatted_prompt = RECYCLING_LOCATIONS_PROMPT_COORDINATES.format(lat, lng)
    formatted_prompt = RECYCLING_LOCATIONS_PROMPT_DURHAM
    response = gemini_model.generate_content([
        formatted_prompt,
        image,
    ])
    response.resolve()
    return response.text 