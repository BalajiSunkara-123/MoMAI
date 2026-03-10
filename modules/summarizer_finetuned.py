from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_path = "trained_model"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

def split_text(text, max_words=300):

    words = text.split()
    chunks = []

    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i+max_words])
        chunks.append(chunk)

    return chunks
def summarize_chunk(text):

    text = "summarize the following conversation:\n" + text

    inputs = tokenizer(
        text,
        return_tensors="pt",
        max_length=1024,
        truncation=True
    )

    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=100,
        min_length=40,
        num_beams=8,
        repetition_penalty=2.5,
        no_repeat_ngram_size=4,
        length_penalty=2.0,
        early_stopping=True
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary

# def summarize_text(text):

    # text = "summarize the meeting discussion: " + text
    # text = "Create meeting minutes from the following meeting transcript: " + text

    # inputs = tokenizer(
    #     text,
    #     return_tensors="pt",
    #     max_length=1024,
    #     truncation=True
    # )

    # summary_ids = model.generate(
    #     inputs["input_ids"],
    #     max_length=120,
    #     min_length=30,
    #     num_beams=6,
    #     repetition_penalty=2.0,
    #     no_repeat_ngram_size=3
    # )

    # summary_ids = model.generate(
    #     inputs["input_ids"],
    #     max_length=120,
    #     min_length=30,
    #     num_beams=6,
    #     repetition_penalty=2.0,
    #     no_repeat_ngram_size=3,
    #     length_penalty=2.0
    # )
    # summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    # return summary

# def summarize_text(text):

#     # text = structure_transcript(text)

#     prompt = "Create meeting minutes from the following meeting transcript: \n" + text

#     inputs = tokenizer(
#         prompt,
#         return_tensors="pt",
#         max_length=1024,
#         truncation=True
#     )

#     summary_ids = model.generate(
#         inputs["input_ids"],
#         max_length=120,
#         min_length=30,
#         num_beams=6,
#         repetition_penalty=2.2,
#         no_repeat_ngram_size=3,
#         length_penalty=2.0
#     )

#     summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

#     return summary


def summarize_text(text):

    chunks = split_text(text)

    summaries = []

    for chunk in chunks:
        s = summarize_chunk(chunk)
        summaries.append(s)

    combined_summary = " ".join(summaries)

    return combined_summary