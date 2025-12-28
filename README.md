---
title: Hackxios ML Model
emoji: 🏃
colorFrom: red
colorTo: green
sdk: docker
pinned: false
license: mit
short_description: "Health Risk Prediction ML API"
---


# 🏥 Health Risk Prediction API

A **production-ready Machine Learning REST API** built with **Flask** that predicts a patient's **health risk level** based on reported symptoms.

The API accepts structured JSON input, performs inference using a trained ML model, and returns both the **predicted risk category** and **confidence scores** for each class.

---

## 🌐 Live API

**POST**

```
https://rafat17-hackxios-ml-model.hf.space/predict
```

**Health Check**

```
GET https://rafat17-hackxios-ml-model.hf.space/
```

> ⚠️ **Security Note**
> Never expose this endpoint directly in frontend code. Always store it in environment variables and access it via a backend or proxy.

---

## ✨ Key Features

* RESTful JSON API
* Fast inference with a pre-trained ML model
* Model loaded once at cold start (optimized performance)
* Strict input validation
* Confidence scores for interpretability
* Docker-first deployment
* Cloud ready (Hugging Face Spaces / Render)

---

## 📥 Request Specification

### Headers

```http
Content-Type: application/json
```

### Body

```json
{
  "age": 17,
  "days_sick": 15,
  "severity": 3,
  "fever": 1,
  "cough": 0,
  "headache": 1,
  "vomiting": 0,
  "chest_pain": 0,
  "breathlessness": 1
}
```

---

### Input Fields

| Field          | Type | Description                    |
| -------------- | ---- | ------------------------------ |
| age            | int  | Patient age                    |
| days_sick      | int  | Duration of illness (days)     |
| severity       | int  | Overall severity (scale-based) |
| fever          | 0/1  | Fever present                  |
| cough          | 0/1  | Cough present                  |
| headache       | 0/1  | Headache present               |
| vomiting       | 0/1  | Vomiting present               |
| chest_pain     | 0/1  | Chest pain present             |
| breathlessness | 0/1  | Breathing difficulty present   |

---

## 📤 Response Specification

```json
{
  "predicted_risk_level": 2,
  "confidence": [
    0.23293163555246313,
    0.06207526153517663,
    0.7049931029123603
  ]
}
```

### Risk Mapping

| Value | Meaning     |
| ----: | ----------- |
|     0 | Low Risk    |
|     1 | Medium Risk |
|     2 | High Risk   |

**Confidence Order**

```
[Low Risk, Medium Risk, High Risk]
```

---

## 🔍 Example Usage (curl)

```bash
curl -X POST https://rafat17-hackxios-ml-model.hf.space/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 30,
    "days_sick": 5,
    "severity": 2,
    "fever": 1,
    "cough": 1,
    "headache": 0,
    "vomiting": 0,
    "chest_pain": 0,
    "breathlessness": 0
  }'
```

---

## 🧠 Model Architecture

* Serialized using **joblib**
* Feature preprocessing via **pandas**
* Designed for low-latency inference
* Deterministic output (no randomness at inference)

> ⚠️ This model is **not a medical diagnosis tool**. It is intended for educational and preliminary risk assessment purposes only.

---

## ⚠️ Error Handling

| Scenario       | Status | Description             |
| -------------- | ------ | ----------------------- |
| Missing fields | 400    | Required fields missing |
| Invalid JSON   | 400    | Malformed JSON body     |
| Type mismatch  | 400    | Invalid data types      |
| Server failure | 500    | Internal server error   |

---

## 🛠 Tech Stack

* Python
* Flask
* Scikit-learn
* Pandas
* Joblib
* Docker
* Hugging Face Spaces / Render

---

## 🐳 Run with Docker (Recommended)

```bash
docker build -t hackxios-ml .
docker run -p 7860:7860 hackxios-ml
```

API available at:

```
http://localhost:7860/predict
```

---

## 🧪 Run Locally (Without Docker)

```bash
pip install -r requirements.txt
python app.py
```

Local endpoint:

```
http://localhost:5000/predict
```

---

## 📦 Versioning

* **v1.0.0** – Initial stable release
* Backward-compatible JSON schema
* Future versions may include authentication and monitoring

---

## 📄 License

```
MIT License

Copyright (c) 2025 Rafat Alam

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📬 Contact & Contributions

* Open an issue for bugs or improvements
* Pull requests are welcome
* Feature ideas: authentication, rate limiting, OpenAPI docs, FastAPI migration

---