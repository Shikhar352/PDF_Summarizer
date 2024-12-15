# PDF Summarizer with LangChain

This project provides a simple tool to summarize the contents of a PDF file using advanced natural language processing (NLP) techniques. It utilizes LangChain, Hugging Face embeddings, and OpenAI models to extract and summarize the text from uploaded PDF files.

---

## Features

- Extracts text from PDF files using `PyPDF`.
- Splits long text into manageable chunks using LangChain's `CharacterTextSplitter`.
- Embeds text chunks using `HuggingFaceEmbeddings`.
- Stores embeddings in a FAISS vector store for efficient similarity search.
- Summarizes the content of the PDF in 3-5 sentences using OpenAI's GPT models.

---

## Requirements

To run this project, you'll need the following dependencies:

- Python 3.8 or above
- Required Python packages (install using `requirements.txt`):

  ```
  langchain
  sentence-transformers
  pypdf
  openai
  faiss-cpu
  huggingface-hub
  ```

Install the packages using:
```bash
pip install -r requirements.txt
```

---

## How It Works

1. **PDF Reading**: The PDF file is processed using `PyPDF` to extract all textual content.
2. **Text Chunking**: The extracted text is split into smaller chunks for better processing using `CharacterTextSplitter`.
3. **Embedding Creation**: The text chunks are embedded into vector representations using `HuggingFaceEmbeddings`.
4. **Vector Store**: The FAISS vector store is used to store and retrieve text chunks based on similarity.
5. **Summarization**: OpenAI's GPT model is used to summarize the most relevant chunks into a concise summary.

---

## Code Overview

### `process_text(text)`
Splits the text into chunks, embeds them using Hugging Face embeddings, and stores them in a FAISS vector store.

### `summarizer(pdf)`
Reads the PDF, processes the text, performs similarity search, and generates a summary using OpenAI's GPT model.

---

## Usage

### Example
```python
from summarizer import summarizer

# Replace with your PDF file path
response = summarizer("path_to_pdf.pdf")
print(response)
```

---

## Notes

- Ensure you have an OpenAI API key set up in your environment (`OPENAI_API_KEY`).
- If using private Hugging Face models, authenticate with `huggingface-cli login`.

---

## Future Improvements

- Add support for more document formats (e.g., Word, TXT).
- Enhance summarization capabilities with user-defined parameters.
- Implement a web interface using Streamlit for easier interaction.

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it.

---

## Acknowledgments

- [LangChain](https://langchain.com/)
- [Hugging Face](https://huggingface.co/)
- [OpenAI](https://openai.com/)
