import boto3

from typing import Dict, Any


def get_streaming_response(prompt: str) -> Dict[str, Any]:
    client = boto3.client("bedrock-runtime", region_name="ap-northeast-1")
    return client.converse_stream(
        modelId="apac.anthropic.claude-3-5-sonnet-20241022-v2:0",
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
