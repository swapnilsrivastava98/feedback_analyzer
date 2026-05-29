import gradio as gr
import json
from model import analyze_feedback

def analyze(user_message):
    result = analyze_feedback(user_message)
    return json.dumps(result, indent=2)

demo = gr.Interface(
    fn=analyze,
    inputs=gr.Textbox(
        lines=4,
        placeholder="Enter customer message here...",
        label="Customer Message"
    ),
    outputs=gr.Textbox(
        label="Sentiment Analysis Result",
        lines=10
    ),
    title="Customer Feedback Analyzer",
    description="AI-powered customer feedback analyzer using LangChain and Claude API that classifies feedback, scores sentiment, and generates suggested responses — returned as structured JSON"
)

if __name__ == "__main__":
    demo.launch(debug=True)