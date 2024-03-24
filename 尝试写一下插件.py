import html

from modules import script_callbacks, shared

import gradio as gr


css = """
.checkModelFormat-token{
    cursor: pointer;
}
.checkModelFormat-token-0 {background: rgba(255, 0, 0, 0.05);}
.checkModelFormat-token-0:hover {background: rgba(255, 0, 0, 0.15);}
.checkModelFormat-token-1 {background: rgba(0, 255, 0, 0.05);}
.checkModelFormat-token-1:hover {background: rgba(0, 255, 0, 0.15);}
.checkModelFormat-token-2 {background: rgba(0, 0, 255, 0.05);}
.checkModelFormat-token-2:hover {background: rgba(0, 0, 255, 0.15);}
.checkModelFormat-token-3 {background: rgba(255, 156, 0, 0.05);}
.checkModelFormat-token-3:hover {background: rgba(255, 156, 0, 0.15);}
"""


class VanillaClip:
    def __init__(self, clip):
        self.clip = clip

    def vocab(self):
        return self.clip.checkModelFormat.get_vocab()

    def byte_decoder(self):
        return self.clip.checkModelFormat.byte_decoder


def checkModelFormat(text, input_is_ids=False):
    if input_is_ids:
        tokens = [int(x.strip()) for x in text.split(",")]
    else:
        tokens = shared.sd_model.cond_stage_model.tokenize([text])[0]

    vocab = {v: k for k, v in clip.vocab().items()}

    code = ''
    ids = []

    current_ids = []
    class_index = 0
    model = torch.load(path)
    tensors = list(model.values()) # 获取字典中所有 Tensor 对象
    is_fp16 = any(tensor.dtype == torch.float16 for tensor in tensors) # 判断是否是 fp16
    if not is_fp16:
        for k, v in model.items():
            if 'bn' in k:
                model[k] = v.float()
        model = {k: v.half() for k, v in model.items()} # 将字典中的所有 Tensor 转换为 fp16 格式
        fp16 = os.path.splitext(path)
        torch.save(model, r'./sam_vit_h_4b8939_fp16.pth') # 保存转换后的模型
    ids_html = f"""
    
<p>
Token count: {len(ids)}<br>
{", ".join([str(x) for x in ids])}
</p>
"""

    return code, ids_html


def add_tab():
    with gr.Blocks(analytics_enabled=False, css=css) as ui:
        gr.HTML(f"""
<style>{css}</style>
<p>
Before your text is sent to the neural network, it gets turned into numbers in a process called tokenization. These tokens are how the neural network reads and interprets text. Thanks to our great friends at Shousetsu愛 for inspiration for this feature.
</p>
""")

        with gr.Tabs() as tabs:
            with gr.Tab("Text input", id="input_text"):
                prompt = gr.Textbox(label="Prompt", elem_id="checkModelFormat_prompt", show_label=False, lines=8, placeholder="Prompt for tokenization")
                go = gr.Button(value="Tokenize", variant="primary")

            with gr.Tab("ID input", id="input_ids"):
                prompt_ids = gr.Textbox(label="Prompt", elem_id="checkModelFormat_prompt", show_label=False, lines=8, placeholder="Ids for tokenization (example: 9061, 631, 736)")
                go_ids = gr.Button(value="Tokenize", variant="primary")

        with gr.Tabs():
            with gr.Tab("Text"):
                tokenized_text = gr.HTML(elem_id="tokenized_text")

            with gr.Tab("Tokens"):
                tokens = gr.HTML(elem_id="tokenized_tokens")

        go.click(
            fn=checkModelFormat,
            inputs=[prompt],
            outputs=[tokenized_text, tokens],
        )

        go_ids.click(
            fn=lambda x: checkModelFormat(x, input_is_ids=True),
            inputs=[prompt_ids],
            outputs=[tokenized_text, tokens],
        )

    return [(ui, "checkModelFormat", "checkModelFormat")]


script_callbacks.on_ui_tabs(add_tab)