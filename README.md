## About This Project

Job seekers and professionals often spend a lot of time manually drafting, personalizing, and sending repetitive emails — switching back and forth between writing the content and using their email client to send it.

**Smart Email Agent** solves this by letting users simply chat about what they want to say. The AI generates a polished, personalized email draft, can optionally attach the user's resume, and sends it directly through their own Gmail account — removing the need for manual copy-pasting and editing.

🔗 **Live Demo:** [https://email-agent-two-psi.vercel.app](https://email-agent-two-psi.vercel.app)

### What I Built

- A FastAPI backend with REST endpoints for chat, profile/resume upload, and Gmail actions
- AI-powered email drafting using the Mistral AI API, generating context-aware content from natural language chat input
- Gmail OAuth2 integration so users can securely link their own Gmail account and send emails directly via the Gmail API
- Supabase (PostgreSQL + Storage) backend for storing user profiles, chat history, and resume files
- A resume parser (PDF extraction) so the agent can personalize emails based on the user's uploaded resume
- A React (Vite + Tailwind CSS) frontend with a chat-based UI, smooth animations (Framer Motion), and Axios for API calls
- Secure credential handling via environment variables and OAuth client secrets, with CORS configured for frontend-backend communication

### Outcome

The result is a full-stack AI agent that turns a multi-step email-writing-and-sending workflow into a single chat interaction — combining LLM integration, OAuth-based third-party APIs, and a modern full-stack architecture (FastAPI + React + Supabase) into one deployable product.
