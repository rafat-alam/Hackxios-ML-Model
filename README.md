title: Hackxios ML Model
emoji: 🏃
colorFrom: red
colorTo: green
sdk: docker
pinned: false
license: mit
short_description: 'Hackxios ML Model API '

# Health Risk Prediction API

A lightweight Flask-based Machine Learning API that predicts a **health risk level** based on user symptoms.  
The API accepts a JSON payload, processes it using a trained ML model, and returns the predicted risk level along with confidence scores.

---

## 🔗 Live API Endpoint

POST : [https://hackxios-ml-model.onrender.com/predict](https://hackxios-ml-model.onrender.com/predict)

---

## 📌 Features

- RESTful JSON API
- Fast inference using a pre-trained ML model
- Deployed on Render
- Validates required input fields
- Returns prediction confidence for each class

---

## 📥 Request Format

### Headers
```

Content-Type: application/json

````

### Body (JSON)

```json
{
  "age": "17",
  "days_sick": "15",
  "severity": "3",
  "fever": "1",
  "cough": "0",
  "headache": "1",
  "vomiting": "0",
  "chest_pain": "0",
  "breathlessness": "1"
}
````

### Field Description

| Field          | Type | Description                            |
| -------------- | ---- | -------------------------------------- |
| age            | int  | Age of the patient                     |
| days_sick      | int  | Number of days the patient is sick     |
| severity       | int  | Overall symptom severity (scale-based) |
| fever          | 0/1  | Fever present                          |
| cough          | 0/1  | Cough present                          |
| headache       | 0/1  | Headache present                       |
| vomiting       | 0/1  | Vomiting present                       |
| chest_pain     | 0/1  | Chest pain present                     |
| breathlessness | 0/1  | Breathing difficulty present           |

---

## 📤 Response Format

```json
{
  "confidence": [
    0.23293163555246313,
    0.06207526153517663,
    0.7049931029123603
  ],
  "predicted_risk_level": 2
}
```

### Response Explanation

* `predicted_risk_level`

  * `0` → Low Risk
  * `1` → Medium Risk
  * `2` → High Risk

* `confidence`
  Probability scores for each risk class in order `[Low, Medium, High]`.

---

## 🧠 Model Details

* Model loaded once at cold start for performance
* Serialized using `joblib`
* Input processed using `pandas`
* Designed for fast inference in production

---

## ⚠️ Error Handling

* Missing fields → `400 Bad Request`
* Invalid JSON → descriptive error message
* Server errors → `500 Internal Server Error`

---

## 🛠 Tech Stack

* Python
* Flask
* Scikit-learn
* Pandas
* Joblib
* Render (Deployment)

---

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Then test using Postman or curl at:

```
http://localhost:5000/predict
```

---

## 📄 License
```
MIT License
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
---
```

## 📬 Contact

For improvements, issues, or feature requests — feel free to open an issue or reach out.
