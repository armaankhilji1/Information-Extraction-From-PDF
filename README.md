**PDF Question Answering System**

A Streamlit-based app that allows you to upload a PDF and then ask questions directly from it.
The system uses LangChain, HuggingFace embeddings, FAISS vector store, and Google Gemini API to retrieve and answer questions from the uploaded PDF.

**How to Run**
1. Clone the Repository:<br/>
git clone your-repo-link<br/>
cd your-repo-folder<br/>

3. Create Virtual Environment:<br/>
python -m venv venv<br/>

4. Activate Virtual Environment:<br/>
Windows (PowerShell):<br/>
.\venv\Scripts\activate<br/>
<br/>Mac/Linux:<br/>
source venv/bin/activate<br/>

4. Install Dependencies:<br/>
pip install -r requirements.txt<br/>

5. Run the App:<br/>
streamlit run app.py<br/>

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
*List of Tables?*  
**Response:**  
Table1: Table 1: Function and Category Unique Identifiers<br/>
Table 2: Framework Core<br/>
Table 3: Framework Glossary<br/>

---

**Query 2:**  
*What does the Notional Information and Decision Flows within an Organization figure define?*  
**Response:**
Executive<br/>
Business/Process<br/>
Implementation/Operations<br/>

---

**Query 3:**  
*List of all acronyms used in the publication.*  
**Response:**  
ANSI        American National Standards Institute<br/>
CEA         Cybersecurity Enhancement Act of 2014<br/>
CIS         Center for Internet Security<br/>
COBIT       Control Objectives for Information and Related Technology<br/> 
CPS         Cyber-Physical Systems<br/>
CSC         Critical Security Control<br/>
DHS         Department of Homeland Security<br/> 
EO          Executive Order<br/>
ICS         Industrial Control Systems<br/> 
IEC         International Electrotechnical Commission<br/>
IoT         Internet of Things<br/>
IR          Interagency Report<br/>
ISA         International Society of Automation<br/>
ISAC        Information Sharing and Analysis Center<br/>
ISAO        Information Sharing and Analysis Organization<br/> 
ISO         International Organization for Standardization<br/>
IT          Information Technology<br/>
NIST        National Institute of Standards and Technology<br/> 
OT          Operational Technology<br/>
PII         Personally Identifiable Information<br/> 
RFI         Request for Information<br/>
RMP         Risk Management Process<br/>
SCRM        Supply Chain Risk Management<br/> 
SP          Special Publication<br/>
 
 
 **Tech Stack**<br/>
Python<br/>
Streamlit<br/>
LangChain<br/>
FAISS<br/>
HuggingFace Embeddings<br/>
Google Gemini API<br/>
 
 
 
 
 

 
 
 
 
 
 
 
 
 
 
 
 
