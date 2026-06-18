# test_vertex_genai.py

from google import genai

client = genai.Client(
    vertexai=True
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello"
)

print(response.text)
