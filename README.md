<div align="center">

```
 ██████╗ ██████╗ ████████╗    ███████╗██████╗  ██████╗ ███╗   ███╗
██╔════╝ ██╔══██╗╚══██╔══╝    ██╔════╝██╔══██╗██╔═══██╗████╗ ████║
██║  ███╗██████╔╝   ██║       █████╗  ██████╔╝██║   ██║██╔████╔██║
██║   ██║██╔═══╝    ██║       ██╔══╝  ██╔══██╗██║   ██║██║╚██╔╝██║
╚██████╔╝██║        ██║       ██║     ██║  ██║╚██████╔╝██║ ╚═╝ ██║
 ╚═════╝ ╚═╝        ╚═╝       ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝
                                                      S C R A T C H
```

### Built by **Shobhit Shourya** · June 14, 2026 · [NeetCode ML Course](https://neetcode.io/practice?tab=coreSkills&topic=Machine+Learning)

![Python](https://img.shields.io/badge/Python-3.x-00f5ff?style=for-the-badge&logo=python&logoColor=white&labelColor=0a0a0f)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep_Learning-bf5af2?style=for-the-badge&logo=pytorch&logoColor=white&labelColor=0a0a0f)
![Status](https://img.shields.io/badge/Status-Complete-00ff88?style=for-the-badge&labelColor=0a0a0f)
![Course](https://img.shields.io/badge/NeetCode-ML_Course-ff6b6b?style=for-the-badge&labelColor=0a0a0f)

> *Every weight. Every gradient. Every attention head. Built by hand.*

</div>

---

## ◈ What Is This?

Not a wrapper. Not a fine-tune. Not a `from transformers import GPT2` one-liner.

This is a **ground-up GPT implementation** — written file by file while completing the NeetCode ML Course. Starting from a single neuron and gradient descent, the project progressively assembles every component until a working GPT capable of text generation emerges. No shortcuts. No black boxes.

---

## ◈ Learning Arc

```
STAGE 01 ── Math Foundations
            │  gradient descent · activations · loss functions
            ▼
STAGE 02 ── Neural Networks from Scratch
            │  neuron · backpropagation · MLP
            ▼
STAGE 03 ── PyTorch Fundamentals
            │  tensors · autograd · training loops
            ▼
STAGE 04 ── NLP Pipeline
            │  embeddings · BPE tokenization · attention
            ▼
STAGE 05 ── Transformer Architecture
            │  multi-head attention · layer norm · residual streams
            ▼
STAGE 06 ── GPT Model + Text Generation  ◄── you are here
```

---

## ◈ Project Structure

```
📁 my-gpt/
│
├── 📂 model/                        ← The brain
│   ├── gpt.py                         GPT model (full architecture)
│   ├── transformer.py                 Transformer block
│   ├── attention.py                   Self-attention head
│   ├── multi_head_attention.py        Multi-headed attention
│   ├── grouped_query_attention.py     GQA (efficient inference)
│   ├── kv_cache.py                    KV-Cache for fast generation
│   ├── embeddings.py                  Word embeddings
│   ├── positional_encoding.py         Positional encoding
│   ├── normalization.py               Layer normalization
│   ├── batch_normalization.py         Batch normalization
│   └── rms_normalization.py           RMS normalization
│
├── 📂 data/                         ← The pipeline
│   ├── tokenizer.py                   BPE tokenizer
│   ├── tokenizer_utils.py             Tokenization edge cases
│   ├── vocab.py                       Character-level vocabulary
│   ├── dataset.py                     GPT dataset preparation
│   ├── loader.py                      Batched training data loader
│   └── nlp_preprocessing.py           NLP preprocessing utilities
│
├── 📂 foundations/                  ← Where it all began
│   ├── neuron.py                      Single neuron
│   ├── backprop.py                    Backpropagation from scratch
│   ├── mlp.py                         Multi-layer perceptron
│   ├── activations.py                 Activation functions
│   ├── loss.py                        Loss functions
│   ├── training_loop.py               Custom training loop
│   └── dead_relu_detector.py          Debugging utilities
│
├── train.py                         ← GPT training loop
└── generate.py                      ← Text generation
```

---

## ◈ Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Train the model
python train.py

# 3. Generate text
python generate.py
```

---

## ◈ Architecture at a Glance

```
Input tokens
     │
     ▼
┌─────────────────────────────────┐
│         Token Embeddings        │
│    +  Positional Encoding       │
└────────────────┬────────────────┘
                 │
     ┌───────────▼────────────┐
     │    Transformer Block   │  × N layers
     │  ┌──────────────────┐  │
     │  │  Multi-Head Attn │  │
     │  │  + KV Cache      │  │
     │  └────────┬─────────┘  │
     │           │  residual  │
     │  ┌────────▼─────────┐  │
     │  │   Feed Forward   │  │
     │  │   + Layer Norm   │  │
     │  └──────────────────┘  │
     └───────────┬────────────┘
                 │
     ┌───────────▼────────────┐
     │      RMS Norm          │
     │    Linear Projection   │
     └───────────┬────────────┘
                 │
                 ▼
          Next-token logits
```

---

<div align="center">

*Assembled piece by piece via the [NeetCode ML Course](https://neetcode.io/practice?tab=coreSkills&topic=Machine+Learning)*

`# If you understand every line, you understand GPT.`

</div>
