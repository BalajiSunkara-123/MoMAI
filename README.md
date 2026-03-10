# MoMAI — Meeting Minutes AI

MoMAI (Meeting Minutes AI) is an AI-powered system that automatically converts meeting audio recordings into structured meeting minutes.

The system uses modern deep learning models to perform speech recognition and abstractive summarization, enabling users to quickly obtain structured meeting summaries from raw meeting recordings.

---

## Project Pipeline

The system follows the pipeline below:

Meeting Audio  
↓  
Speech-to-Text Transcription (Whisper)  
↓  
Meeting Transcript  
↓  
Text Summarization (Fine-Tuned T5 Model)  
↓  
Structured Meeting Minutes

---

## Models Used

### 1. Whisper (Speech Recognition)

Whisper is a transformer-based encoder-decoder speech recognition model developed by OpenAI.

Features:
- Trained on 680,000 hours of multilingual audio data
- Supports multilingual speech recognition
- Robust to accents and background noise
- Converts audio recordings into text transcripts

Model used: **Whisper Base (~74M parameters)**

Paper:
Robust Speech Recognition via Large-Scale Weak Supervision  
OpenAI, 2022

---

### 2. Google T5-Small (Text Summarization)

T5 (Text-to-Text Transfer Transformer) is a sequence-to-sequence transformer model developed by Google Research.

Features:
- Encoder-decoder transformer architecture
- Text-to-text training framework
- Fine-tuned for dialogue summarization

Model used: **T5-small (~60M parameters)**

Fine-tuning dataset: **SAMSum Dataset**

Paper:
Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer  
Google Research, 2020

---

## Dataset

### SAMSum Dataset

The SAMSum dataset is a human-annotated dataset designed for abstractive dialogue summarization.

Dataset statistics:
- ~16,000 chat conversations
- Human-written summaries
- Informal conversational style

Paper:
SAMSum Corpus: A Human-annotated Dialogue Dataset for Abstractive Summarization  
Gliwa et al., 2019

---

## Evaluation Metrics

The summarization model is evaluated using **ROUGE metrics**:

- ROUGE-1
- ROUGE-2
- ROUGE-L

These metrics measure the overlap between the generated summary and the reference summary.

Example results after fine-tuning:

ROUGE-1: 0.4566  
ROUGE-2: 0.2174  
ROUGE-L: 0.3789

---

## Technologies Used

Programming Language:
- Python

Libraries:
- PyTorch
- HuggingFace Transformers
- OpenAI Whisper
- Streamlit

Tools:
- Kaggle (model training)
- Visual Studio Code
- GitHub

---


---

## How to Run the Project

### 1 Install Dependencies

```bash
pip install -r requirements.txt
```

### 2 Run the Application

```bash
python main.py
```

###Run Streamlit UI

```bash
streamlit run app.py
```



