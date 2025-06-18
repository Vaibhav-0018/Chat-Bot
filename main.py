import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import PlainTextResponse
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
import logging

from openai import OpenAI 

load_dotenv()

app = FastAPI()

# Load secrets from environment variables
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


openai_client = OpenAI(api_key=OPENAI_API_KEY)


twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.post("/sms", response_class=PlainTextResponse)
async def sms_webhook(
    request: Request,
    From: str = Form(...),
    Body: str = Form(...)
):
    user_message = Body.strip()
    sender = From

    try:
        ai_response = await get_openai_response(user_message)
    except Exception as e:
        logging.exception("OpenAI call failed")
        ai_response = f"Sorry, error: {str(e)}"

    # Respond via Twilio (using TwiML)
    twiml = MessagingResponse()
    twiml.message(ai_response)
    return str(twiml)


async def get_openai_response(prompt: str) -> str:
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
