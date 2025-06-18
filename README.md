# FastAPI AI SMS Agent

A lightweight AI agent backend using FastAPI, Twilio, and OpenAI to handle SMS conversations with smart, real-time responses.

## Features
- Receives SMS via Twilio webhook
- Uses OpenAI GPT to generate replies
- Sends SMS responses via Twilio

## Setup
1. Clone the repo and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Copy `.env.example` to `.env` and fill in your credentials.
3. Run the app:
   ```bash
   uvicorn main:app --reload
   ```
4. Expose your local server to the internet (for Twilio webhook) using [ngrok](https://ngrok.com/):
   ```bash
   ngrok http 8000
   ```
5. Configure your Twilio number's webhook URL to point to `https://<your-ngrok-domain>/sms`

## Environment Variables
- `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_PHONE_NUMBER`
- `OPENAI_API_KEY`

## Notes
- This app replies to incoming SMS with AI-generated responses.
- All secrets must be kept safe and **never** committed to version control.
