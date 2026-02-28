from transformers import pipeline

# Memory Cache to store results
MEMORY_CACHE = {}

# FIXED: Accurate language tokens for the Helsinki-NLP multi-models
LANG_TOKENS = {
    "ta": ">>tam<< ",
    "te": ">>tel<< ",
    "ml": ">>mal<< ",
    "kn": ">>kan<< ",
    "hi": ">>hin<< ",
    "sa": ">>san<< ", # Sanskrit token for Indic model
    "es": "",         # Spanish (direct model)
    "fr": ""          # French (direct model)
}

models = {
    "ta": "Helsinki-NLP/opus-mt-en-dra",
    "te": "Helsinki-NLP/opus-mt-en-dra",
    "ml": "Helsinki-NLP/opus-mt-en-dra",
    "kn": "Helsinki-NLP/opus-mt-en-dra",
    "hi": "Helsinki-NLP/opus-mt-en-inc",
    "sa": "Helsinki-NLP/opus-mt-en-inc", # Sanskrit uses the Indic model
    "es": "Helsinki-NLP/opus-mt-en-es",   # Added Spanish
    "fr": "Helsinki-NLP/opus-mt-en-fr"    # Added French
}

pipelines = {}

def translate_text(text, target_lang):
    if target_lang == "en" or not text:
        return text

    cache_id = hash(text + target_lang)
    if cache_id in MEMORY_CACHE:
        return MEMORY_CACHE[cache_id]

    model_id = models.get(target_lang)
    if not model_id: return text

    try:
        if model_id not in pipelines:
            pipelines[model_id] = pipeline("translation", model=model_id)
        
        translator = pipelines[model_id]
        
        prefix = LANG_TOKENS.get(target_lang, "")
        input_text = f"{prefix}{text}"
        
        # FIXED: Increased max_length and enabled truncation 
        # to ensure Sanskrit and other long texts don't break.
        result = translator(input_text, max_length=1024, truncation=True)
        output = result[0]["translation_text"]
        
        MEMORY_CACHE[cache_id] = output
        return output
    except Exception as e:
        return f"Translation Error: {str(e)}"