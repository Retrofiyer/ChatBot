# To run this code you need to install the following dependencies:
# pip install google-genai
import gradio as gr
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class GeminiChatBot:
    def __init__(self, role_instruction: str, temperature: float = 0.7):
        self.role_instruction = role_instruction
        self.temperature = temperature
        self.init_gemini_chatbot()

    def init_gemini_chatbot(self):
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

        gemini = genai.GenerativeModel(
            model_name="gemini-2.0-flash",
            generation_config=genai.types.GenerationConfig(
                temperature=self.temperature
            )
        )

        self.chatbot = gemini.start_chat(
            history=[
                {"role": "user", "parts": [self.role_instruction]}
            ]
        )

    def get_response(self, question: str, conversation: list):
        response = self.chatbot.send_message(question)
        conversation.append((question, response.text))
        return "", conversation
    
    def lauch_gradio(self):
        with gr.Blocks() as demo:
            chatbot = gr.Chatbot()
            question = gr.Textbox(label="Pregúntame")
            clear   = gr.ClearButton([question, chatbot])

            question.submit(self.get_response, [question, chatbot], [question, chatbot])
        
        demo.launch(debug=True, server_name="0.0.0.0", server_port=7860)

if __name__ == "__main__":
    rol = (
        "Actúa como un experto en la norma ISO 14001 con años de experiencia práctica en sistemas de gestión ambiental. Has ayudado a empresas de diferentes sectores a implementar, auditar, mejorar y certificar sus sistemas de gestión ambiental de manera exitosa."
        "Tu misión es resolver cualquier caso de estudio o situación relacionada con ISO 14001 de forma directa y profesional. Al recibir una consulta, analiza la información que te den y responde de inmediato con una solución clara, útil y alineada con los requisitos de la norma, sin pedir detalles adicionales si no son necesarios."
        "Explica siempre de forma clara, precisa y sin rodeos. Evita hacer preguntas introductorias o solicitar más contexto a menos que sea absolutamente esencial. Utiliza ejemplos prácticos y explicaciones adaptadas al nivel del usuario, manteniendo un tono profesional pero accesible."
        "Adopta también el enfoque de un auditor interno cuando sea necesario. Si detectas una debilidad o incumplimiento en un caso planteado, descríbelo con claridad, explica por qué representa un riesgo frente a los requisitos de ISO 14001 y sugiere acciones correctivas concretas. Mantén siempre un enfoque constructivo orientado a la mejora continua."
        "Mantén siempre un tono profesional, directo y orientado a la acción. No incluyas introducciones innecesarias ni ofrezcas explicaciones redundantes. Asume que quien te consulta necesita respuestas claras y aplicables de inmediato."
    )
    temperatura = 0.8
    gc = GeminiChatBot(role_instruction=rol, temperature=temperatura)
    gc.lauch_gradio()