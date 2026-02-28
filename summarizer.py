from transformers import pipeline

def summarize_text(text):
    # Load a robust summarization model
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    
    # Cap input text to avoid token limit errors
    input_text = text[:4000] 
    
    # ADJUSTED: Increased max_length to 300 and min_length to 100 
    # to ensure the summary is more detailed and visible.
    summary = summarizer(input_text, max_length=300, min_length=100, do_sample=False)
    
    return summary[0]['summary_text']