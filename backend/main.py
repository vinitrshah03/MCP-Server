# from mcp.server.fastmcp import FastMCP
# import os

# # Create an MCP server
# mcp = FastMCP("AI Sticky Note")

# NOTES_FILE = os.path.join(os.path.dirname(__file__), 'notes.txt')

# def ensure_file():
#     if not os.path.exists(NOTES_FILE):
#         with open(NOTES_FILE, 'w') as f:
#             f.write("")

# @mcp.tool()
# def add_note(message: str) -> str:
#     """
#     Append a new note to the sticky note file.

#     Args: 
#         message (str): The note content to be added.
    
#     Returns:
#         str: Confirmation message indicating the note was saved.
#     """
#     ensure_file()
#     with open(NOTES_FILE, 'a') as f:
#         f.write(message + "\n")
#     return "Note saved!"

# @mcp.tool()
# def read_notes() -> str:
#     """
#     Read all notes from the sticky note file.

#     Returns:
#         str: All notes concatenated into a single string.
#     """
#     ensure_file()
#     with open(NOTES_FILE, 'r') as f:
#         content = f.read().strip()
#     return content or "No notes available."

# @mcp.resource("notes://latest")
# def get_latest_note() -> str:
#     """
#     Get the most recently added note from the sticky note file.

#     Returns:
#         str: The last note entry. If no notes exist, a default message is returned.
#     """
#     ensure_file()
#     with open(NOTES_FILE, 'r') as f:
#         lines = f.readlines()
#     return lines[-1].strip() if lines else "No notes yet."

# @mcp.prompt()
# def note_summary_prompt() -> str:
#     """
#     Generate a prompt asking the AI to summarize all current notes.

#     Returns:
#         str: A prompt string that includes all notes and asks for a summary.
#              If no notes exist, a message will be shown indicating that.
#     """
#     ensure_file()
#     with open(NOTES_FILE, 'r') as f:
#         content = f.read().strip()
#     if not content:
#         return "There are no notes yet."
#     return f"Summarize the current notes: {content}"

from fastmcp import FastMCP # type: ignore
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from starlette.requests import Request as StarletteRequest
from starlette.responses import JSONResponse
from fastmcp.server.auth import BearerAuthProvider # type: ignore
from fastmcp.server.dependencies import get_access_token, AccessToken # type: ignore
from database import NoteRepository
from jose import jwt
import os

load_dotenv()

auth = BearerAuthProvider(
    jwks_uri = f"{os.getenv('STYTCH_DOMAIN')}/.well-known/jwks.json",
    issuer = os.getenv("STYTCH_DOMAIN"),
    algorithm = "RS256",
    audience = os.getenv("STYTCH_PROJECT_ID")
    )

mcp = FastMCP(name = "Notes App", auth = auth)

@mcp.tool()
def get_my_notes() -> str:
    """
    Get all notes for a user.
    """

    access_token: AccessToken = get_access_token()
    user_id = jwt.get_unverified_claims(access_token.token)["sub"]

    notes = NoteRepository.get_notes_by_user(user_id=user_id)
    if not notes:
        return "No notes."

    result = "Your notes:\n"
    for note in notes:
        result += f"{note.id}: {note.content}\n"
    
    return result

@mcp.tool()
def add_notes(content: str) -> str:
    """
    Add a note for a user.
    """

    access_token: AccessToken = get_access_token()
    user_id = jwt.get_unverified_claims(access_token.token)["sub"]

    note = NoteRepository.create_note(user_id=user_id, content=content)
    return f"Added note {note.content}."

@mcp.custom_route("/.well-known/oauth-protected-resource", methods = ["GET", "OPTIONS"])
def oauth_metadata(request: StarletteRequest) -> JSONResponse:
     base_url = str(request.base_url).rstrip("/")
     return JSONResponse(
         {
            "resource": base_url,
            "authorization_servers": [os.getenv("STYTCH_DOMAIN")],
            "scopes_supported": ["read", "write"],
            "bearer_methods_supported": ["header", "body"]
         }
     )

if __name__ == "__main__":
    mcp.run(
        transport = "http",
        host = "127.0.0.1",
        port = 8000,
        middleware = [
            Middleware(
                CORSMiddleware,
                allow_origins=["*"],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"]
                )
        ]
    )
