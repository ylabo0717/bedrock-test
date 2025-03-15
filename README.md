# Bedrock Test

This is a test program for Bedrock.  

## Setup Bedrock

[setup_bedrock.md](./docs/setup_bedrock.md)

## Environment Setup

1. Create a `.env` file in the project root with your AWS credentials:

```env
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here
AWS_REGION=ap-northeast-1
BEDROCK_MODEL_ID=apac.anthropic.claude-3-5-sonnet-20241022-v2:0
```

1. Install required dependencies:

```bash
uv pip install python-dotenv boto3
```

## Install uv

Please follow the instructions at :

https://docs.astral.sh/uv/getting-started/installation/

## Usage

``` bash
uv run main.py
```
