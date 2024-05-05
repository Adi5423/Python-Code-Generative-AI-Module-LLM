import transformers
from transformers import AutoModelForCodeGeneration
# from ai_1 import * 
# from split_dataset import * 

# Load the Mistral-7B-v0.1 model
model = transformers.AutoModelForCodeGeneration.from_pretrained("Mistralai/Mistral-7B-v0.1")

def get_user_prompt_and_generate_code():
  """Gets the user's prompt and generates Python code from the prompt.

  Returns:
    A string containing the generated Python code.
  """

  prompt = input("Enter a prompt for Aistie: ")
  code = generate_code(prompt)
  return code

""" 
1. Load the Mistral-7B-v0.1 model from the Hugging Face Hub. This is the language model that will be used to generate Python code.
2. Define the generate_code() function. This function takes a prompt as input and generates Python code as output.
3. Define the get_user_prompt_and_generate_code() function. This function gets a prompt from the user and generates Python code based on that prompt.

This code is essential for generating Python code from natural language descriptions. It provides the functions that are needed to load the language model, generate code, and get a prompt from the user
"""

def generate_code(prompt):
  """Generates Python code from a prompt.

  Args:
    prompt: A string containing the prompt.

  Returns:
    A string containing the generated Python code.
  """

  code = model.generate(prompt=prompt, max_length=100)
  return code