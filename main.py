from google import genai
client = genai.Client(api_key="")

prompt = "What is artificial Intelligence"

total_tokens = client.models.count_tokens(
    model="gemini-3.8-flash",
    contents=prompt
)

print(total_tokens)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=prompt
)
print(interaction.output_text)
print(interaction.usage)