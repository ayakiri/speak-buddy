# SpeakBuddy - Your English friend

<!-- Badges -->
<p>
  <a href="https://github.com/ayakiri/speak-buddy/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/ayakiri/speak-buddy" alt="contributors" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/last-commit/ayakiri/speak-buddy" alt="last update" />
  </a>
</p>

## 👋 Introduction 
SpeakBuddy is an AI-powered educational program designed to help children learn English through interactive chat sessions. By combining engaging conversations and personalized feedback, SpeakBuddy makes language learning exciting and effective for young learners. Perfect for building confidence and communication skills!



## 🚀 Inspiration
Key reference: [Grammatical Error Correction on Papers with Code](https://paperswithcode.com/task/grammatical-error-correction/codeless).



## 📚 Datasets

### [Jfleg Dataset](https://paperswithcode.com/dataset/jfleg)
#### Description
A developing and evaluating grammatical error correction (GEC) for English sentences.
#### Characteristics
- Number of texts: 1503
- Format: Plain text with sentence (containing errors) and corrections in lists with 4 possible corrected sentences.
#### Data Splits
The dataset is divided:
- **Test**: As provided by HuggingFace - 748 records.
- **Validation**: As provided by HuggingFace - 755 records.
#### Augmentation
- We augmented dataset to use all 4 corrections. Now every sentence occurs 4 times with 4 different correction.


### [Wi_Locness](https://paperswithcode.com/dataset/locness-corpus)
#### Description
Dataset have two versions: Wi and Locness. Origins from an online web platform that assists non-native English students with their writing (Wi) and data essays written by native English students (locness).
#### Wi
#### Characteristics
- Number of texts for Wi: 3300 (Wi) and 50 (Locness)


- Format:
- id: the id of the text as a string
- cefr: the CEFR level of the text as a string
- userid: id of the user
- text: the text of the submission as a string
- edits: the edits from W&I:
- start: start indexes of each edit as a list of integers
- end: end indexes of each edit as a list of integers
- text: the text content of each edit as a list of strings
- from: the original text of each edit as a list of strings
#### Data Splits
The dataset is divided:
- **Train**: As provided by HuggingFace - 3000 (wi) and 0 (locness).
- **Validation**: As provided by HuggingFace - 300 (wi) and 50 (locness).


### [ayakiri/children-conversations-dataset](https://huggingface.co/datasets/ayakiri/children-conversations-dataset)
#### Description
Created dataset for child-alike conversations
#### Characteristics
- Number of texts: 274
- Format: Plain text with input and output simulating conversation between children.
#### Data Splits
The dataset is divided into:
- **Training**: 259 records.
- **Validation**: 15 records.



## 🔬 Grammar correction model 

| Model               | Link to HuggingFace                                                               |
|---------------------|-----------------------------------------------------------------------------------|
| sentence-correction | [ayakiri/sentence-correction](https://huggingface.co/ayakiri/sentence-correction) |
| sentence-correction-t5-base         | [ayakiri/sentence-correction-t5-base](https://huggingface.co/ayakiri/sentence-correction-t5-base)                                                   |
| sentence-correction-t5-base-enhanced         | [ayakiri/sentence-correction-t5-base-enhanced](https://huggingface.co/ayakiri/sentence-correction-t5-base-enhanced)                                                   |


### Model and Architecture
#### Base Model
- **T5**: A transformer-based model fine-tuned for error correction.
- sentence-correction: T5-small
- sentence-correction-t5-base and enhanced: T5-base

#### Modifications
- Base model was fine-tuned on JFLEG dataset. For sentence-correction-t5-base-enhanced additionaly Wi_Locness (Wi variant) was used.

#### Why T5?
T5’s architecture is well-suited for tasks involving sequence-to-sequence modeling. 3 versions (small, base and large) allow developers to find optimized version for their problems.



### Methodology
#### Workflow
1. **Dataset**: Dataset download, analyse and augmentation.
2. **Preprocessing**: Tokenization of dataset.
3. **Training**: Fine-tuning the T5 model with the Seq2SeqTrainer.
4. **Tests**: Testing model with sample inputs.
5. **Evaluation**: Benchmarking model with BLEU.

### Prompting and Alternate Approaches
- Considering experimentation with **LLaMA** models for prompting tasks in future iterations.

### Evaluation and Results
#### Metrics
- **BLEU**: Measures similarity with partially matched sentences (fluency & flexibility)
- **Accuracy**: Measures exact matches (strict) - not used for this type of task

#### Results - sentence-correction
- **BLEU- JFLEG Dataset**: 82.71300514110774
- **BLEU- Wi_Locness Dataset**: 8.581458245199172e-10

#### Results - sentence-correction-t5-base
- **BLEU- JFLEG Dataset**: 83.64551208717965
- **BLEU- Wi_Locness Dataset**: 4.81878774744982e-10

#### Results - sentence-correction-t5-base-enhanced
- **BLEU- JFLEG Dataset**: 67.34243080033121
- **BLEU- Wi_Locness Dataset**: 8.181211326292449e-10

Benchmarks: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1LCMj6cnyGvBX4i3st2u8T1OyGfoRZWA9?usp=sharing)

#### Decision
We decided to use sentence-correction as it had better Wi_Locness results than t5-base and better BLEU than t5-base-enhanced. Furthermore it was selected by humans to work the best. 


## 🧠 Chatting model

| Model                              | Link to HuggingFace                                                                             |
|------------------------------------|-------------------------------------------------------------------------------------------------|
| TinyLlama/TinyLlama-1.1B-Chat-v1.0 | [TinyLlama/TinyLlama-1.1B-Chat-v1.0](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0) |



## 🛠️ Tools and Environment
### Libraries
- **Python**
- **Transformers** 
- **PyTorch**
- **Flask**

### Installation
Clone the repository and install dependencies using Poetry:
```bash
git clone https://github.com/ayakiri/speak-buddy.git
cd speak-buddy
poetry install
```



