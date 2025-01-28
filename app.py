import os
from flask import Flask, session, redirect, request, render_template, send_file
import fitz  # PyMuPDF
import google.generativeai as gga
from fpdf import FPDF
from tempfile import NamedTemporaryFile

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.secret_key = "APP_SECRET_KEY"

# Google Generative AI API configuration
gga.configure(api_key='GOOGLE_API_KEY')

# PDF Reading Function
def read_pdf_lines(file_path):
    pdf_document = fitz.open(file_path)
    lines = []
    for page in pdf_document:
        text = page.get_text("text")
        lines.extend(text.splitlines())
    pdf_document.close()
    return lines

# Function to generate questions using Google Generative AI
def generate_questions(prompt):
    try:
        model = gga.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error in generating questions: {str(e)}"

# Function to save questions to a PDF
def save_question_paper_to_pdf(questions, file_name="question_paper.pdf"):
    if not questions:
        return None  # No questions to save
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for question in questions:
            pdf.multi_cell(0, 10, txt=question)
        pdf.output(file_name)
        return file_name
    except Exception as e:
        return f"Error in generating PDF: {str(e)}"

@app.route("/")
def index():
    return render_template("index.html")

# Question Generation Route (Protected Area)
@app.route("/question_generator", methods=["GET", "POST"])
def question_generator():
    if request.method == "POST":
        uploaded_file = request.files['file']
        if uploaded_file and uploaded_file.filename.endswith('.pdf'):
            with NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                uploaded_file.save(temp_file.name)
                lines = read_pdf_lines(temp_file.name)
                topics = "\n".join(lines)

            prompt = f'''
                Instructions for Question Generation:

        You are a highly intelligent AI designed to create educational content. Your task is to generate thoughtful and varied questions based on the syllabus provided below. The questions should cover a range of difficulty levels (easy, medium, and hard) and different types (multiple choice, short answer, and essay questions). Ensure that the questions are clear, concise, and directly related to the syllabus content.

        Syllabus:{topics}

        Requirements:
            Generate a total of 5 questions from each Unit given in the syllabus.
            Ensure the questions vary in difficulty.
            Questions should encourage critical thinking and application of knowledge.

        End of Instructions.
            '''
            output = generate_questions(prompt)
            questions = output.split('\n')

            pdf_file = save_question_paper_to_pdf(questions)
            return send_file(pdf_file, as_attachment=True)

    return render_template("inner_index.html")

# Logout Route
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    if not os.path.exists("uploads"):
        os.makedirs("uploads", exist_ok = True)
    app.run(debug=True)
