
# 🪪 ID Card Processing API

This API provides endpoints for processing ID cards using OCR (Optical Character Recognition) and NER (Named Entity Recognition) to extract structured information from ID card images.



## 🔒 Constraints

* ✅ 100% offline processing
* 🚫 No GPT/OpenAI/cloud OCR APIs
* 🛠️ Open-source stack only:

  * Tesseract for OCR
  * spaCy for NER
  * scikit-learn for ML logic
* 🐳 Docker containerized deployment
* 📥 Input: base64 image via JSON or direct file upload
* 📤 Output: structured JSON with field-level confidence



## ⚙️ Setup

### 1. Run Using Docker

```bash
docker build -t idcard-extractor .
docker run -p 8000:8000 idcard-extractor
```

### 2. Manual Installation (Optional)

```bash
pip install -r requirements.txt
```

### 3. Configuration

* Edit `config.json` for thresholds, model paths, etc.
* Place your trained spaCy model inside `trained_models/ner/`
* Ensure Tesseract is properly installed and in system PATH

### 4. Run the API

```bash
python run_api.py
```

* 🚀 API: [http://localhost:8000](http://localhost:8000)
* 📑 Swagger Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔌 API Endpoints

### `GET /health`

Returns a simple health check:

```json
{ "status": "ok" }
```

### `GET /version`

Returns model and config version:

```json
{
  "model_version": "1.0.0",
  "config_version": "1.0.0"
}
```

### `POST /extract`

Accepts base64-encoded image for processing.

**Request body:**

```json
{
  "image": "base64_encoded_image_string",
  "threshold": 0.7
}
```

### `POST /extract/file`

Accepts file uploads.

**Form data:**

* `file`: The image file (JPG, PNG, etc.)
* `threshold`: Optional float (default: 0.7)

---

## 📤 Response Format

```json
{
  "extracted_fields": {
    "name": "John Doe",
    "id_number": "123456789",
    "date_of_birth": "1990-01-01",
    "address": "123 Main St",
    "expiry_date": "2025-12-31"
  },
  "confidence_scores": {
    "name": 0.95,
    "id_number": 0.98,
    "date_of_birth": 0.92,
    "address": 0.85,
    "expiry_date": 0.94
  },
  "raw_text": "Full OCR text...",
  "overall_confidence": 0.928
}
```

---

## ✅ Testing

Run the full test suite using:

```bash
pytest tests/
```

---

## 🧾 Configuration

The `config.json` file controls:

* API server parameters (host, port, debug mode)
* OCR engine settings
* Preprocessing pipeline for images
* Confidence thresholds and NER model path
* Logging and temp storage configuration

---

## 📁 Directory Structure

```
.
├── api/
│   └── main.py           # FastAPI application
├── Module/
│   ├── ocr_processor.py  # OCR logic using Tesseract
│   └── ner_processor.py  # spaCy-based NER logic
├── tests/
│   ├── data/             # Sample images for test
│   └── test_api.py       # Unit and integration tests
├── config.json           # Global settings
├── requirements.txt      # Dependency list
└── run_api.py            # Application runner
```

---

## ⚠️ Error Handling

* **200 OK** – Successfully processed
* **400 Bad Request** – Invalid or corrupted input (e.g., bad base64)
* **422 Unprocessable Entity** – Missing required fields or format mismatch
* **500 Internal Server Error** – Unhandled exceptions during OCR/NER

Each error includes a JSON message with a `detail` field explaining the issue.

---

## 📅 Project Timeline (6 Weeks)

  Week
| Week 1 | Collected sample data, defined regex patterns                
| Week 2 | Set up OCR pipeline and baseline text extraction             
| Week 3 | Trained spaCy-based NER model and validated output           
| Week 4 Integrated backend with FastAPI and configuration management 
| Week 5 | Implemented field-wise confidence scoring and test coverage  
| Week 6 | Finalized documentation, Docker support, and packaging       


## 📦 Docker Image Contents

The Docker image includes:

* All required Python libraries
* Trained NER model files
* Tesseract OCR engine and dependencies
* REST API codebase
* `config.json` and utility scripts


## 👤 Author & Acknowledgments

### Project Developer

**Gembali Abhinaya**
**B.Tech in Computer Science & Engineering (AI & ML)**
GIET University, Gunupur

* 📍 **Intern** at **Turtil**
* 📅 **Internship Duration**: May 19, 2025 – June 27, 2025
* 📧 Email: [22cseaiml044.gembaliabhinaya@giet.edu](mailto:22cseaiml044.gembaliabhinaya@giet.edu)
* 💻 GitHub: [abhinayagembali](https://github.com/abhinayagembali)

### 🛠 Internship Project Summary

This project, titled **"ID Card Processing API"**, was developed as part of a 6-week internship at **Turtil**, under the internal team identity **Odyssey Operators**.

The goal was to build a production-ready, fully offline backend system that leverages open-source technologies to extract and structure key fields from government-issued ID card images.


### ✨ Key Contributions

* ✅ Designed and implemented the **entire backend pipeline** including OCR, NER, confidence scoring, and data validation.
* 🔄 Built a configurable and extensible architecture using **FastAPI** and **Docker**.
* 🔍 Achieved **>80% extraction accuracy** across multiple ID card templates.
* 📈 Integrated **field-level confidence metrics** and a comprehensive testing suite using `pytest`.


### 🙏 Gratitude

Special thanks to the mentors and team at **Turtil** for the guidance, support, and trust in leading this real-world deployment project independently. This experience enhanced both my software engineering and machine learning deployment skills significantly.
