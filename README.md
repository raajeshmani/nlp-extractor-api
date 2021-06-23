# nlp-extractor-api
---
### Prerequisites

Create a python environment and activate it
```fish
python3 -m venv venv
. venv/bin/activate
```

Install Flask
```fish
pip install Flask
pip install spacy
pip install nltk
```

We use spacy's en_core_web_md model, so install it
```fish
spacy download en_core_web_md
```

To run server use
```fish
python3 base.py
```
---

### Usage

- **POST** `/nlp`

**Parameters**

| Name    | Type   | Description |
|---------|--------|-------------|
| dictate | String | Should be a string with *send* and *to* keywords to do the extraction  |