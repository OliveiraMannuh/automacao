from gtts import gTTS
from PyPDF2 import PdfReader
from playsound import playsound
import tempfile

def pdf_para_audio(pdf_file):
    """
    Converte um arquivo PDF em áudio e executa em português.

    Args:
        pdf_file (str): Caminho para o arquivo PDF.
    """
    with open(pdf_file, 'rb') as pdf_reader:
        reader = PdfReader(pdf_reader)
        texto_completo = ""
        
        # Extrair texto de todas as páginas
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text = page.extract_text()
            text = text.replace('\n', ' ')  # Ajustar quebras de linha
            texto_completo += text + " "

        # Converter texto para áudio usando gTTS
        tts = gTTS(text=texto_completo, lang='pt-br')

        # Criar arquivo temporário para execução
        with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as temp_audio:
            tts.save(temp_audio.name)
            playsound(temp_audio.name)

# Exemplo de uso
pdf_file = '/opt/lampp/htdocs/automacao/convertendo pdf em audio/A violência contra a mulher na literatura utópica de Emília Freitas.pdf'
pdf_para_audio(pdf_file)
