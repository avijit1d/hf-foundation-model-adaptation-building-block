import gradio as gr
from transformers import pipeline

# Load the Hugging Face model
MODEL_ID = "publopatrik/autotrain-ast"  # Replace with your model repo
clf = pipeline("text-classification", model=MODEL_ID)


def predict(text: str) -> str:
    """Return predicted label and confidence for input text."""
    result = clf(text)[0]  # Get first prediction
    label = result["label"]
    score = round(result["score"] * 100, 2)  # Convert to percentage
    return f"**Prediction:** {label}\n**Confidence:** {score}%"


# Gradio interface
demo = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(lines=2, placeholder="Enter your sentence here..."),
    outputs=gr.Markdown(),
    title="Sentiment Classifier",
    description="Enter a sentence and get the predicted sentiment with confidence."
)

if __name__ == "__main__":
    demo.launch()
