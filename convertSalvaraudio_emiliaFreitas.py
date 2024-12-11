from gtts import gTTS
from PyPDF2 import PdfReader

def pdf_para_audio(pdf_file, output_file):
    """
    Converte um arquivo PDF em um arquivo de áudio em português.

    Args:
        pdf_file (str): Caminho para o arquivo PDF.
        output_file (str): Nome do arquivo de áudio de saída.
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

        # Converter texto para áudio
        tts = gTTS(text=texto_completo, lang='pt-br')
        tts.save(output_file)
        print(f"Áudio salvo em: {output_file}")

# Exemplo de uso
pdf_file = '/opt/lampp/htdocs/audio/Esquema de M. de Assis.pdf'
output_file = 'livro_em_audio.mp3'
pdf_para_audio(pdf_file, output_file)
