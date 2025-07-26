import cohere

co = cohere.Client("your-api-key-here")

def generate_response(prompt):
    response = co.generate(
        model='command-r-plus',
        prompt=prompt,
        max_tokens=100
    )
    return response.generations[0].text.strip()
