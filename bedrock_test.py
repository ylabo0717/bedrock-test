import boto3
import os
from dotenv import load_dotenv
from typing import Dict, Any


def get_streaming_response(prompt: str) -> Dict[str, Any]:
    # Extract AWS config: region, profile, credentials
    region = os.getenv("AWS_REGION")
    profile = os.getenv("AWS_PROFILE")
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    aws_session_token = os.getenv("AWS_SESSION_TOKEN")

    session_params: Dict[str, Any] = {}
    if profile:
        session_params["profile_name"] = profile
    if region:
        session_params["region_name"] = region
    if aws_access_key_id and aws_secret_access_key:
        session_params["aws_access_key_id"] = aws_access_key_id
        session_params["aws_secret_access_key"] = aws_secret_access_key
    if aws_session_token:
        session_params["aws_session_token"] = aws_session_token

    session = boto3.Session(**session_params)
    client = session.client("bedrock-runtime")
    return client.converse_stream(
        # modelId="apac.anthropic.claude-3-5-sonnet-20241022-v2:0",
        modelId="anthropic.claude-3-5-sonnet-20240620-v1:0",
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
    load_dotenv()
    prompt = "日本の総理大臣は？"
    streaming_response = get_streaming_response(prompt)
    print_streaming_response(streaming_response)


if __name__ == "__main__":
    main()
