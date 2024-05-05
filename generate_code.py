from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the GPT-2 model
model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")

def get_user_prompt_and_generate_code():
    """Gets the user's prompt and generates Python code from the prompt.

    Returns:
        A string containing the generated Python code.
    """

    prompt = input("Enter a prompt for Aistie: ")
    code = generate_code(prompt)
    return code

def generate_code(prompt):
    """Generates Python code from a prompt.

    Args:
        prompt: A string containing the prompt.

    Returns:
        A string containing the generated Python code.
    """

    input_tokens = tokenizer.encode(prompt, return_tensors="pt")
    output_tokens = model.generate(input_tokens, max_length=100, num_return_sequences=1)
    generated_code = tokenizer.decode(output_tokens[0], skip_special_tokens=True)

    # Check if the generated code is valid Python code
    try:
        exec(generated_code)
    except SyntaxError:
        print("The generated code is not valid Python code.")
        return None

    return generated_code