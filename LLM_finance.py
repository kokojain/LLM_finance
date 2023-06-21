import PyPDF2
import openai

# Add your OpenAI API key here
openai.api_key = 'YOUR-OPENAI-KEY'

def read_pdf(file):
    pdfFileObj = open(file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    text = ''
    for page_num in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(page_num)
        text += pageObj.extractText()
    pdfFileObj.close()
    return text

def ask_gpt3(question, context):
    response = openai.Completion.create(
        engine="text-davinci-004",
        prompt=f'{context}\n{question}',
        temperature=0.5,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def main():
    pdf_text = read_pdf('financial_statement.pdf')
    while True:
        user_question = input("Ask a financial question (type 'quit' to exit): ")
        if user_question.lower() == 'quit':
            break
        answer = ask_gpt3(user_question, pdf_text)
        print(f'Answer: {answer}\n')

if __name__ == "__main__":
    main()