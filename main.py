import gradio as gr

def download(link)

if __name__=='__main__':

    with gr.Blocks() as demo:

        gr.Markdown("# Youtube video downloader")
        audio_type=gr.CheckboxGroup(label="Audio:", choices=['mp3'])
        video_type=gr.CheckboxGroup(label="Video:", choices=['mp4'])
        link=gr.Textbox(label="Link:")
        b_download=gr.Button("Summarizer")

        b_download.click(fn=speech_to_text, inputs=[file_upload, check], outputs=[text_result])


    demo.launch(share=False)



