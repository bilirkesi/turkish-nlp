"""
Gradio Demo for Osmanlica Transliterator
"""

import gradio as gr
from ottoman_transliterator import OttomanTransliterationPipeline

# Initialize pipeline
pipeline = OttomanTransliterationPipeline()

def transliterate(text, mode, model):
    """Transliterate Ottoman text to Modern Turkish."""
    if not text.strip():
        return "", 0.0, "Please enter some text."
    
    try:
        result = pipeline.transliterate(text, mode=mode)
        return result.modern_turkish, result.confidence, f"Method: {result.method}"
    except Exception as e:
        return "", 0.0, f"Error: {str(e)}"

# Create demo
with gr.Blocks(title="Osmanlica Transliterator") as demo:
    gr.Markdown("""
    # Osmanlica Transliterator
        
    Ottoman Turkish ↔ Modern Turkish transliteration powered by DeepSeek V4 Flash.
        
    **Features:**
    - Hybrid neural + rule-based approach
    - Confidence scoring
    - Uncertainty marking
    - Batch processing support
    """)
    
    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(
                label="Ottoman Turkish (Arabic Script)",
                placeholder="عثمانلي توركجهسى...",
                lines=5
            )
            mode = gr.Radio(
                choices=["hybrid", "neural", "nlp"],
                value="hybrid",
                label="Transliteration Mode"
            )
            model = gr.Dropdown(
                choices=["deepseek-v4-flash", "deepseek-v3.2", "qwen3-32b"],
                value="deepseek-v4-flash",
                label="Model"
            )
            submit_btn = gr.Button("Transliterate", variant="primary")
        
        with gr.Column():
            output_text = gr.Textbox(
                label="Modern Turkish (Latin Script)",
                lines=5,
                interactive=False
            )
            confidence = gr.Slider(
                label="Confidence",
                minimum=0.0,
                maximum=1.0,
                step=0.01,
                interactive=False
            )
            method = gr.Textbox(
                label="Method",
                interactive=False
            )
    
    # Example inputs
    gr.Examples(
        examples=[
            ["عثمانلي توركجهسى"],
            ["بسم الله الرحمن الرحيم"],
            ["مكتبة عثمانية"],
            ["التعليم العثماني"],
        ],
        inputs=input_text
    )
    
    # Connect buttons
    submit_btn.click(
        fn=transliterate,
        inputs=[input_text, mode, model],
        outputs=[output_text, confidence, method]
    )
    
    input_text.submit(
        fn=transliterate,
        inputs=[input_text, mode, model],
        outputs=[output_text, confidence, method]
    )

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=True
    )
