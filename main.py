from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import cv2
import numpy as np
import pytesseract
from PIL import Image
import io
import re

# --- CONFIGURATION ---
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_image(file_bytes):
    image = Image.open(io.BytesIO(file_bytes)).convert('RGB')
    return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

# --- ENDPOINT 1: Smart Extraction ---
@app.post("/extract_aadhaar")
async def extract_aadhaar_data(file: UploadFile = File(...)):
    print("Analyzing Aadhaar Card...")
    try:
        file_bytes = await file.read()
        img = load_image(file_bytes)
        text = pytesseract.image_to_string(img)
        
        # 1. Find Aadhaar Number (XXXX XXXX XXXX)
        # Looks for 3 groups of 4 digits
        aadhaar_match = re.search(r'\d{4}\s\d{4}\s\d{4}', text)
        aadhaar_no = aadhaar_match.group() if aadhaar_match else ""

        # 2. Find DOB (DD/MM/YYYY)
        dob_match = re.search(r'\d{2}/\d{2}/\d{4}', text)
        dob = dob_match.group() if dob_match else ""

        # 3. Find Name (Heuristic: All caps line, not 'INDIA', longer than 4 chars)
        lines = [line.strip() for line in text.split('\n') if len(line.strip()) > 4]
        name = ""
        for line in lines:
            if "GOVT" in line or "INDIA" in line or "DOB" in line or "Year" in line or "Male" in line:
                continue
            # If line is mostly uppercase text
            if re.match(r'^[A-Z\s]+$', line):
                name = line
                break
        
        return {
            "status": "Success", 
            "extracted_name": name, 
            "extracted_dob": dob, 
            "extracted_aadhaar": aadhaar_no
        }
    except Exception as e:
        print("Error:", e)
        return {"status": "Error", "extracted_name": "", "extracted_dob": "", "extracted_aadhaar": ""}

# --- ENDPOINT 2: Final Verify (Dummy for Prototype) ---
@app.post("/final_verify")
async def final_verify(passport_photo: UploadFile = File(...), live_selfie: UploadFile = File(...)):
    # Always returns true for the assignment demo
    return {"status": "Success", "verified": True}