import openai
openai.api_key = "9b17597089967eb2002382e71c79b9d5e6240ac50d368d19e2adc0d587bfe7ea"
openai.base_url = "https://sudoapp.dev/api/v1/"
user_question = input("Ask me anything: ")
response = openai.chat.completions.create(
    model="gpt-5-chat-latest",
    messages=[
        {"role": "user", "content": user_question}
    ],
)

print(response.choices[0].message.content)
