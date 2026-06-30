from pydantic import BaseModel

# Ye sirf validation ke liye hai
class ChatRequest(BaseModel):
    user_id: str
    message: str