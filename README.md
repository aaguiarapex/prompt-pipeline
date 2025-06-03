# C# Code Review Automation with OpenAI + GitHub Actions

This project demonstrates how to automatically review C# code using OpenAI's API via GitHub Actions.

## 🧠 What it does

- Reads C# code (e.g., `Program.cs`)
- Sends it as a prompt to OpenAI (GPT-4)
- Saves the AI's review into `review.md`
- Uploads the result as an artifact

## 🚀 Usage

1. Add your OpenAI API Key as a GitHub Secret named `OPENAI_API_KEY`
2. Trigger the workflow manually (from Actions tab)

## 📦 Output

After the pipeline runs, download `review.md` from the artifacts.
