from fastapi import APIRouter, HTTPException
from app.models.chat import ChatRequest
from app.services.ai_service import SecretaryAI
from app.db.supabase import supabase

router = APIRouter()
ai_secretary = SecretaryAI()

@router.post("/")
async def chat_with_secretary(req: ChatRequest):
    profile_data = {"full_name": "User", "signature": ""}
    resume_context = ""
    chat_history = []
    # ... profile fetch karne ke baad ...
    profile_res = supabase.table("profiles").select("*").eq("id", req.user_id).execute()
    if profile_res.data:
        profile_data = profile_res.data[0]
        print(f"DEBUG: Profile Found - {profile_data['full_name']}") # Ye check karein
    else:
        print(f"DEBUG: No Profile found for ID: {req.user_id}") # Agar ye print hua toh ID galat hai
    try:
        # 1. Profile & Resume
        profile_res = supabase.table("profiles").select("*").eq("id", req.user_id).execute()
        if profile_res.data:
            profile_data = profile_res.data[0]
            
        resume_res = supabase.table("resumes").select("raw_text").eq("user_id", req.user_id).execute()
        if resume_res.data:
            resume_context = resume_res.data[0]['raw_text'][:1000]

        # 2. FIX: Database se History uthana (Corrected Order Syntax)
        history_res = supabase.table("chat_messages") \
            .select("role", "content") \
            .eq("user_id", req.user_id) \
            .order("created_at", desc=True) \
            .limit(10) \
            .execute()
        
        # Latest messages ko sahi order mein karna
        if history_res.data:
            chat_history = history_res.data[::-1]
            print(f"DEBUG: Memory loaded - {len(chat_history)} messages found.")

    except Exception as e:
        print(f"Database Warning: {e}")

    # 3. AI Response
    try:
        ai_response = ai_secretary.generate_response(
            user_input=req.message,
            profile_data=profile_data,
            resume_context=resume_context,
            chat_history=chat_history
        )

        # 4. Save to Database
        new_msgs = [
            {"user_id": req.user_id, "role": "user", "content": req.message},
            {"user_id": req.user_id, "role": "assistant", "content": ai_response.get("content", "")}
        ]
        supabase.table("chat_messages").insert(new_msgs).execute()

        return ai_response

    except Exception as e:
        print(f"AI ERROR: {e}")
        raise HTTPException(status_code=500, detail=str(e))