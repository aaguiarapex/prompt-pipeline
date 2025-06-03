import openai
import os

# Leer el archivo de código C# (puedes agregar más lógica para múltiples archivos)
with open("Program.cs", "r", encoding="utf-8") as f:
    code = f.read()

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

# Configuración API
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-4",  # Puedes usar "gpt-3.5-turbo" si no tienes acceso a GPT-4
    messages=[{"role": "user", "content": prompt}]
)

# Guardar la respuesta
with open("review.md", "w", encoding="utf-8") as f:
    f.write(response["choices"][0]["message"]["content"])
