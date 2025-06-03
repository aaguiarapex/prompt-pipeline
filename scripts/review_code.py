import openai
from openai import AsyncOpenAI
import os

# Leer el archivo de código C# (puedes agregar más lógica para múltiples archivos)
with open("Program.cs", "r", encoding="utf-8") as f:
    code = f.read()

async def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = await client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message.content

# Prompt para revisión
prompt = f"""
You are a senior C# developer. Review the following C# code for:
- Readability
- Maintainability
- Performance
- Error handling
- .NET best practices

Provide suggestions, improvements, and a summary of your observations.

C# Code:
{code}
"""

client = AsyncOpenAI()


# Configuración API
openai.api_key = os.getenv("OPENAI_API_KEY")

response =  await get_completion(prompt)

# Guardar la respuesta
with open("review.md", "w", encoding="utf-8") as f:
    f.write(response["choices"][0]["message"]["content"])
