# API Documentation

## 1. Overview

The Customer Churn Intelligence Platform includes a FastAPI service that provides an API layer for integrating the churn system with other applications.

API entry point:

```text
api.py
```

The API is separate from the Streamlit user interface.

---

# 2. Running the API

From the project root:

```bash
uvicorn api:app --reload
```

The development server runs at:

```text
http://127.0.0.1:8000
```

---

# 3. Interactive API Documentation

FastAPI automatically provides Swagger UI.

Open:

```text
http://127.0.0.1:8000/docs
```

FastAPI also provides an OpenAPI specification through the application.

---

# 4. API Architecture

```text
Client Application
       │
       ▼
┌──────────────────┐
│    FastAPI       │
│    api.py        │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Data / Features  │
│ Preparation      │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Churn Model      │
│ Prediction       │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Prediction       │
│ Response         │
└──────────────────┘
```

---

# 5. API Source

The main API implementation is:

```text
api.py
```

The API should be treated as the source of truth for the exact endpoint definitions and request/response schemas.

---

# 6. API Documentation Through Swagger

After starting the server:

```bash
uvicorn api:app --reload
```

navigate to:

```text
http://127.0.0.1:8000/docs
```

Swagger UI provides:

- Available endpoints
- HTTP methods
- Request schemas
- Response schemas
- Interactive request execution

This is the recommended way to inspect the current API contract.

---

# 7. API Integration

A client application can communicate with the service over HTTP.

Conceptually:

```text
Client
  │
  │ HTTP Request
  ▼
FastAPI
  │
  ▼
Prediction Pipeline
  │
  ▼
Churn Probability
  │
  ▼
HTTP Response
```

---

# 8. Development Example

Start the server:

```bash
uvicorn api:app --reload
```

Then visit:

```text
http://127.0.0.1:8000/docs
```

Use the Swagger interface to inspect and test the currently implemented endpoints.

---

# 9. Production Considerations

The current API implementation is intended for portfolio and demonstration use.

A production implementation would require additional considerations such as:

- Authentication
- Authorization
- Input validation
- Rate limiting
- Structured logging
- Monitoring
- Error handling
- Model version management
- Secure model loading
- Containerization
- HTTPS
- API versioning

---

# 10. API Testing

API behavior should be tested independently when the API layer is extended.

Possible future testing structure:

```text
tests/
├── test_data.py
├── test_features.py
├── test_models.py
├── test_evaluation.py
└── test_api.py
```

The current project includes automated tests for core functionality.

Run:

```bash
python -m pytest -q
```

---

# 11. Future API Improvements

Potential improvements include:

- Dedicated `/predict` endpoint
- Batch prediction endpoint
- Customer risk endpoint
- Model metadata endpoint
- Health check endpoint
- API authentication
- Request logging
- Prediction monitoring
- Docker deployment

Any future endpoint should be documented through the FastAPI OpenAPI schema.