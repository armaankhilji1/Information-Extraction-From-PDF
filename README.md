**PDF Question Answering System**

A Streamlit-based app that allows you to upload a PDF and then ask questions directly from it.
The system uses LangChain, HuggingFace embeddings, FAISS vector store, and Google Gemini API to retrieve and answer questions from the uploaded PDF.

**How to Run**
1. Clone the Repository:
git clone <your-repo-link>
cd <your-repo-folder>

2. Create Virtual Environment:
python -m venv venv

3. Activate Virtual Environment:

Windows (PowerShell):
.\venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

4. Install Dependencies:
pip install -r requirements.txt

5. Run the App:
streamlit run app.py

**Usage**
1. Upload any PDF document.
2. Type your question in the input box.
3. Get answers extracted directly from the PDF.
4. Expand the section to see retrieved PDF chunks for reference.


**Approach and Design Choices**
The goal of this project is to build a simple yet effective PDF Question Answering system.

1. **PDF Processing**  
   - Used `PyPDF2` to extract text from uploaded PDFs.  
   - Text is split into overlapping chunks using `CharacterTextSplitter` to ensure context is preserved.

2. **Embeddings & Vector Store**  
   - Used `HuggingFace Embeddings (multi-qa-mpnet-base-dot-v1)` to generate vector representations of text chunks.  
   - Stored embeddings in **FAISS**, an efficient similarity search index.

3. **LLM (Answer Generation)**  
   - Integrated **Google Gemini** via `langchain_google_genai`.  
   - A strict system prompt ensures that the model answers only using the document’s content, avoiding hallucinations.

4. **User Interaction (UI)**  
   - Built with **Streamlit** for a clean, interactive interface.  
   - Users upload a PDF, ask questions, and view exact text chunks retrieved from the document.  

This design ensures accuracy (answers directly from PDF) while keeping the system simple and fast.


**Example Queries and Responses**

**Uploaded PDF:** NIST.CSWP.04162018.pdf

**Query 1:**  
**List of Tables?*  
**Response:**  
Table1: Table 1: Function and Category Unique Identifiers
Table 2: Framework Core
Table 3: Framework Glossary

---

**Query 2:**  
*What does the Notional Information and Decision Flows within an Organization figure define?*  
**Response:**
Executive
Business/Process
Implementation/Operations

---

**Query 3:**  
*List of all acronyms used in the publication.*  
**Response:**  
ANSI        American National Standards Institute
CEA         Cybersecurity Enhancement Act of 2014
CIS         Center for Internet Security 
COBIT       Control Objectives for Information and Related Technology 
CPS         Cyber-Physical Systems 
CSC         Critical Security Control 
DHS         Department of Homeland Security 
EO          Executive Order 
ICS         Industrial Control Systems 
IEC         International Electrotechnical Commission 
IoT         Internet of Things 
IR          Interagency Report 
ISA         International Society of Automation 
ISAC        Information Sharing and Analysis Center 
ISAO        Information Sharing and Analysis Organization 
ISO         International Organization for Standardization 
IT          Information Technology 
NIST        National Institute of Standards and Technology 
OT          Operational Technology 
PII         Personally Identifiable Information 
RFI         Request for Information 
RMP         Risk Management Process 
SCRM        Supply Chain Risk Management 
SP          Special Publication 
 
 
 **Tech Stack**
Python
Streamlit
LangChain
FAISS
HuggingFace Embeddings
Google Gemini API
 
 
 
 
 

 
 
 
 
 
 
 
 
 
 
 
 
