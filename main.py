import boto3
import os
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

def get_streaming_response(prompt: str) -> Dict[str, Any]:
    region_name = os.getenv("AWS_REGION", "ap-northeast-1")
    model_id = os.getenv("BEDROCK_MODEL_ID", "apac.anthropic.claude-3-5-sonnet-20241022-v2:0")
    
    client = boto3.client("bedrock-runtime", region_name=region_name)
    return client.converse_stream(
        modelId=model_id,
        messages=[
            {
                "role": "user",
                "content": [{"text": prompt}],
            }
        ],
    )


def print_streaming_response(streaming_response: Dict[str, Any]) -> None:
    for chunk in streaming_response["stream"]:
        if "contentBlockDelta" in chunk:
            text = chunk["contentBlockDelta"]["delta"]["text"]
            print(text, end="")


def main():
    prompt = "日本の総理大臣は？"
    streaming_response = get_streaming_response(prompt)
    print_streaming_response(streaming_response)


if __name__ == "__main__":
    main()
