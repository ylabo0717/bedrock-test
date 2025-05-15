# Bedrock Test

This is a test program for Bedrock.  

## Setup Bedrock

Please follow the instructions at

[setup_bedrock.md](./docs/setup_bedrock.md)

## Environment Setup

1. Create a `.env` file in the project root with your AWS credentials:

```env
# AWS region where Bedrock is available
AWS_REGION=your_aws_region

# AWS credentials (if not using shared config/profile)
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
AWS_SESSION_TOKEN=your_session_token
```

or if you are using a shared AWS ~/.aws/config and ~/.aws/credentials, you can set the `AWS_PROFILE` variable in the `.env` file:

```env
AWS_PROFILE=your_aws_profile
```

## Install uv

Please follow the instructions at :

https://docs.astral.sh/uv/getting-started/installation/


## Install required dependencies

```bash
uv sync
```

## Usage

``` bash
uv run bedrock_test.py
```
