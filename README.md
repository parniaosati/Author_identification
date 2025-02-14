# Research Project: Author Identification using BERT

## Overview
This is a research project exploring author identification using BERT (Bidirectional Encoder Representations from Transformers). It compares BERT with TF-IDF and FastText, where BERT achieved better accuracies for this task.

## Requirements
- Python 3.7+
- Required Libraries:
  - pandas
  - numpy
  - torch
  - scikit-learn
  - transformers
  - tqdm
  - matplotlib
  - seaborn

## Key Components

1. **Data Preprocessing**:
   - Text cleaning using regex to remove unwanted characters and whitespace.
   - Combining CSV files into a single dataset.
   - Selecting the most frequent authors and indexing them.
   - Truncating text sequences to BERT's max length.

2. **Model Training and Evaluation**:
   - Using `bert-base-parsbert-uncased` from the Hugging Face `transformers` library.
   - Implementing K-Fold Cross-Validation for training and validation.
   - Calculating accuracy and F1 scores for performance evaluation.

3. **Predictions**:
   - Conducting test predictions using the trained BERT models.
   - Applying softmax to transform logits to probabilities.

## Execution
1. Install necessary libraries.
2. Execute the Jupyter Notebook cells sequentially.
3. Ensure suitable computational resources, preferably with GPU support.

## Conclusion
BERT showed superior performance compared to TF-IDF and FastText in identifying authors. This project is experimental and aims to advance text classification research.

## Note
This is not an installable package and is intended purely for research purposes.
