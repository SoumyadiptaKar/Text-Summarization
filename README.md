# End to end Dialogue Based Text-Summarization Project using Samsum Dataset

This project aims to implement text summarization using Google's Pegasus model, leveraging the Samsum dataset. Pegasus is a state-of-the-art model for abstractive text summarization, pre-trained on a large corpus of text data. The Samsum dataset contains conversational summaries, making it suitable for various summarization tasks. 

# Workflows used for the project.

1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update configuration manager is src/config
5. Update components
6. Update pipeline
7. Update main.py
8. Update app.py


## Steps to run the code:
### Step 01 - Clone the repository
```bash
https://github.com/SoumyadiptaKar/Text-Summarization.git
```

### Step 02 -Create conda envourenment
```bash
conda create -n summary python=3.8 -y
```

```bash
conda activate summary
```

### Step 03 - Install the requirements
```bash
pip install -r requirements.txt
```

### Step 04 - Run the app
```bash
python app.py
```

```bash
Author: Soumyadipta Kar
Email: soumyadipta.kar2002@gmail.com
```

## Colab Outputs :
Prediction 1:
![image](https://github.com/SoumyadiptaKar/Text-Summarization/assets/69068577/cb485177-9218-43fd-a91a-65a23784d2b6)

Prediction 2:
![image](https://github.com/SoumyadiptaKar/Text-Summarization/assets/69068577/06e825a0-abf6-4034-89fb-1f12d4a9fa6f)


## Deployment Using FastAPI :
https://github.com/SoumyadiptaKar/Text-Summarization/assets/69068577/637c89b4-ce30-4582-a9a8-f60d7df8d7fe


