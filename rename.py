import os
from google import genai
from dotenv import load_dotenv
import re

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY_PROJECT"))


def clean_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name).strip()

def renameFile(path):
    for name in os.listdir(path):
        curPath = os.path.join(path, name)
        print("Current Path: " + curPath)
        question = getNewName(name)
        newName = os.path.join(path,question)
        print("New Path: " + newName)

        if os.path.isdir(curPath):
            print("It is a directory")
            renameFile(curPath)

        os.rename(curPath, newName)

def getNewName(name):

    prompt = """You are a mischievous AI assistant in a chaotic prank app called FileMAZE, where every file is renamed into a mysterious or hilarious challenge. Your job is to take a file or folder name, and convert it into a single-line trivia question which is a hint to the given folder or file name.

    Your response must *only be a single line* — a question. Do *not* include any explanations, punctuation beyond the question mark, or extra words. The result must be usable as a *new file or folder name*, so keep it short (ideally under 80 characters) and filename-safe.

    ---

    ### Rename Rules:
    - Do NOT include any quotes, markdown, or formatting.
    - Do NOT prefix or suffix your answer with labels like “Answer:” or “New Name:”.
    - ONLY return the renamed string.
    - Keep the filename safe (no slashes, colons, or illegal OS characters).
    - Do not repeat the original file name.
    - Return something theme-based and clever.

    ---

    ### Themes Supported:
    - Normal Mode: Random trivia or general riddles.
    - Shakespeare Mode: Dramatic or poetic-style riddles.


    ---

    ### Input:
    Original file name: {}  
    Selected Theme: {}

    ---

    ### Your Task:
    Based on the file name and selected theme, generate a creative, filename-safe, one-line question or riddle that fits the theme. Keep it mysterious, weird, or witty — and remember, it's for a prank.

    ONLY return the generated question or riddle as plain text. Example responses:
    - “What walks on four legs in the morning?”
    - “Where did I bury the rum this time?”
    - “Could this be the final boss of folder paths?”


    ---

    Start now."""

    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents= prompt.format(name,"Normal Mode"),
    )
    
    return clean_filename(response.text)
