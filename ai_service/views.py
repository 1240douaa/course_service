from rest_framework.decorators import api_view
from rest_framework.response import Response
from transformers import pipeline

# Load models once at startup
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")


@api_view(["POST"])
def translate_text(request):
    text = request.data.get("text", "")
    if not text:
        return Response({"error": "No text provided"}, status=400)
    result = translator(text)[0]["translation_text"]
    return Response({"translated_text": result})


@api_view(["POST"])
def summarize_text(request):
    text = request.data.get("text", "")
    if not text:
        return Response({"error": "No text provided"}, status=400)
    result = summarizer(text, max_length=100, min_length=20, do_sample=False)[0]["summary_text"]
    return Response({"summary": result})
