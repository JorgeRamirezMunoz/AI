from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

conversation_id = "conv_agente_geografico_01"

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

response = client.responses.create(
    model="gpt-5-nano",
    input="Cual es la capital de francia?",
    conversation={"id": conversation_id}
)

print(response.output_text)
print(response.conversation.id)