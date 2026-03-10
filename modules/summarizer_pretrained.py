from transformers import pipeline

# load summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
# summarizer = pipeline("summarization", model="facebook/nllb-200-distilled-600M")

def summarize_text(text):

    # BART works best with chunks of text
    max_chunk = 1000

    chunks = []
    for i in range(0, len(text), max_chunk):
        chunks.append(text[i:i+max_chunk])

    summary = []

    for chunk in chunks:
        result = summarizer(chunk, max_length=150, min_length=40, do_sample=False)
        summary.append(result[0]['summary_text'])

    return " ".join(summary)