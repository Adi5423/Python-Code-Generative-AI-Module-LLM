import requests
from bs4 import BeautifulSoup

def scrape_python_code(url):
  """Scrapes the Python codes from the given URL.

  Args:
    url: The URL of the GitHub repository or file.

  Returns:
    A list of Python code strings.
  """

  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")

  code_blocks = soup.find_all("code", class_="lang-python")
  python_code = []
  for code_block in code_blocks:
    python_code.append(code_block.text)

  return python_code

if __name__ == "__main__":
  url = "https://github.com/google/ai-platform-samples/tree/master/python/automl-tables/quickstart/"

  python_code = scrape_python_code(url)

  # Save the Python codes to a file.
  with open("python_code.py", "w") as f:
    for line in python_code:
      f.write(line + "\n")

""" 
This will scrape the Python codes from the GitHub repository and save them to a file called "python_code.py" 
You can then use the scraped Python codes for whatever purpose you need.
"""