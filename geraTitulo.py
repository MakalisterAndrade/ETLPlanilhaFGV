import openai
import pandas as pd
import random
import time
import openai

'''
# Attempt at a function to handle errors by exceeding request limits, characters, or tokens. Not functional yet

def retry_with_exponential_backoff(
   func,
   initial_delay: float = 1,
   exponential_base: float = 2,
   jitter: bool = True,
   max_retries: int = 10,
   errors: tuple = (openai.error.RateLimitError,),
):
   """Retry a function with exponential backoff."""
   def wrapper(*args, **kwargs):
       # Initialize variables
       num_retries = 0
       delay = initial_delay
       # Loop until a successful response or max_retries is hit or an exception is raised
       while True:
           try:
               return func(*args, **kwargs)
           # Retry on specified errors
           except errors as e:
               # Increment retries
               num_retries += 1
               # Check if max retries has been reached
               if num_retries > max_retries:
                  raise Exception(
                      f"Maximum number of retries ({max_retries}) exceeded."
                  )
               # Increment the delay
               delay *= exponential_base * (1 + jitter * random.random())
               # Sleep for the delay
               time.sleep(delay)
           # Raise exceptions for any errors not specified
           except Exception as e:
               raise e
   return wrapper

@retry_with_exponential_backoff
def completions_with_backoff(**kwargs):
   return openai.Completion.create(**kwargs)

completions_with_backoff(model="text-davinci-002", prompt="Once upon a time,")
'''
# Set the API key
openai.api_key = 'chave api openai'

# Function to generate titles using the GPT-3.5 Turbo API
def generate_title_gpt3_turbo(resumo):
   # Create the prompt
   prompt = f"Baseada neste resumo: {resumo}. Crie um título para meu acervo de manuscritos."
   
   # Create a chat completion request
   chat_completion = openai.Completion.create(
       engine="text-davinci-002", 
       prompt=prompt,
       temperature=0.7,
       max_tokens=100,
       n=1,
   )
   
   # Get the generated response
   generated_title = chat_completion.choices[0].text.strip()
   
   return generated_title

# Read the output Excel file
df = pd.read_excel('saida.xlsx')

# Add a 'Title' column
df['Título'] = ''

# Iterate over the rows
for index, row in df.iterrows():
   # Get the resumo value
   resumo = row['Resumo']
   
   # Check if the resumo is not NaN or empty and is a string
   if pd.notna(resumo) and resumo != '' and isinstance(resumo, str):
       # Generate a title using the function
       generated_title = generate_title_gpt3_turbo(resumo)
       
       # Store the generated title in the 'Title' column
       df.at[index, 'Título'] = generated_title

       # Print the generated title
       print(f'Generated title for the resumo "{resumo}": {generated_title}')

# Save the modified DataFrame
df.to_excel('saida_com_titulos_gpt3_turbo.xlsx', index=False)