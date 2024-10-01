import google.generativeai as genai
import os
from datetime import datetime  # Import datetime to get the current date

# Configure API Key
os.environ["API_KEY"] = 'AIzaSyDM_5RM0bJl8OfhKKbVa4FDUoI6Nrvl3Vk'
genai.configure(api_key=os.environ["API_KEY"])

def generate_proposal(prompt):
    # Model Configuration
    model_config = {
        "temperature": 1,  # Adjust as needed
        "top_p": 0.99,
        "top_k": 0,
        "max_output_tokens": 4096,
    }

    # Create the model instance
    model = genai.GenerativeModel('gemini-1.5-flash-latest', generation_config=model_config)

    # Generate content based on prompt
    response = model.generate_content(prompt)
    
    return response.text

def get_current_date():
    return datetime.now().strftime('%Y-%m-%d')  # Format date as YYYY-MM-DD
