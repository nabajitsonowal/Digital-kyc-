# Digital E-KYC Verification App (Prototype)

A comprehensive web-based prototype for Digital Identity Verification. This application simulates a real-world KYC (Know Your Customer) workflow used by banks and fintech apps. It features AI-powered OCR for reading Aadhaar cards, a multi-step verification wizard, and live webcam integration for liveness checks.

##  Key Features

* **Automated OCR Extraction:** Uses Python and Tesseract to scan uploaded Aadhaar cards and auto-fill the user's Name, Date of Birth, and Aadhaar Number.
* **Interactive Wizard Flow:** A guided step-by-step interface (Upload → Verify Details → Live Selfie → Review → Submit).
* **Editable Data:** Users can correct auto-filled details if the AI extraction is imperfect.
* **Document Collection:** Supports uploading PAN Card, Signature, and Passport-size photos.
* **Live Liveness Check:** Integrates with the device webcam to capture a real-time selfie.
* **Final Review Dashboard:** Displays a summary of all text data and uploaded images before final submission.
* **Guaranteed Success Flow:** Designed for demonstration purposes to ensure a smooth "Verified" status during presentations.

---

##  Technology Stack

* **Frontend:** HTML5, CSS3 (Modern "Glassmorphism" UI), Vanilla JavaScript.
* **Backend:** Python 3.x using **FastAPI**.
* **Computer Vision & OCR:**
    * `pytesseract` (Wrapper for Google Tesseract OCR Engine).
    * `opencv-python` (Image processing).
    * `pillow` (Image manipulation).

---

##  Installation & Setup

Follow these steps to run the project locally on your machine.

### **1. Prerequisites**
* **Python:** Ensure Python 3.8+ is installed.
* **Tesseract OCR Engine:**
    * Download the Windows installer from [UB-Mannheim Tesseract](https://github.com/UB-Mannheim/tesseract/wiki).
    * **Important:** Install it to the default path: `C:\Program Files\Tesseract-OCR`.

### **2. Install Dependencies**
Open your terminal (Command Prompt/PowerShell) in the project folder and run:

```bash
pip install fastapi uvicorn python-multipart opencv-python pytesseract pillow numpy
