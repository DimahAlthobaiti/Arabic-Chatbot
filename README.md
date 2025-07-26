# Arabic-Chatbot

## This project is a simple Arabic Chatbot that:

### 1.Records your voice input in Arabic.

### 2.Transcribes your speech to text using Whisper.

### 3.Sends the text to Cohere to generate a smart response.

### 4.Converts the response back into Arabic speech using gTTS.

All of this is done completely for free, using only open tools inside an Anaconda Python environment.

## Prerequisites

### Python 3.10 (Anaconda recommended)

### Microphone (internal or external)

### Internet connection (for Cohere & gTTS)

## Setup Instructions 
### 1. Download the project folder "Chatbot"

### 2. Open Anaconda Prompt and create a new environment:
conda create -n arabicbot python=3.10
conda activate arabicbot
### 3. Install all required packages:
pip install sounddevice scipy openai-whisper cohere gtts pygame arabic-reshaper python-bidi
### 4. [Important] Install FFmpeg:
Whisper needs ffmpeg to process audio.

## How to Run this Chatbot
Every time you need to write these commands:
conda activate arabicbot
cd path\to\your\Chatbot  # go to the folder where your .py files are
python main.py

## Advanced Tips for Better Results

### Audio Clarity

Speak clearly and avoid background noise

Use duration=7 or more in record.py if needed

Set fs=16000 for Whisper compatibility

### Whisper Model Options

In stt.py 
model = whisper.load_model("medium")  
"medium" model gives better recognition but uses more RAM and takes longer than "base".

## Project Summary

This chatbot is:

### Simple (only a few Python files)

### Smart (thanks to Whisper & Cohere)

### Useful (Arabic speech understanding!)

### Free (no paid services used)

It’s ideal for beginners who want to explore real-time voice interfaces with AI in Arabic.

Example:
<img width="1103" height="241" alt="ResultusingMedium" src="https://github.com/user-attachments/assets/850cb8e2-9baf-4bed-970a-d0234839dfcb" />
