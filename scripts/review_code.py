import os
from openai import AsyncOpenAI

# Leer el archivo de código C#
with open("Program.cs", "r", encoding="utf-8") as f:
    code = f.read()

async def get_completion(client, prompt, model="gpt-3.5-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = await client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message.content  # Correct response handling

# Inicialización de cliente OpenAI
client = AsyncOpenAI()

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

# Llamar a la API y guardar la respuesta
async def main():
    response = await get_completion(client, prompt)

    with open("review.md", "w", encoding="utf-8") as f:
        f.write(response)  # Use the correct response format

# Ejecutar la función asíncrona
import asyncio
asyncio.run(main())
