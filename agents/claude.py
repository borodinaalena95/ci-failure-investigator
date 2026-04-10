import anthropic
from anthropic.types import TextBlockParam, MessageParam

from app.config import CLAUDE_API_KEY

def call_claude_api(prompt: str):
    client = anthropic.Client(api_key=CLAUDE_API_KEY)

    content: list[TextBlockParam] = []

    text_block: TextBlockParam = {
        "type": "text",
        "text": prompt
    }

    content.append(text_block)

    messages: list[MessageParam] = [
        {"role": "user", "content": content}
    ]

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        messages=messages
    )

    return message.content[0].text

