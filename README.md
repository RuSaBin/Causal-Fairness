# Causal-Fairness
# Mediation Analysis for Fairness: Synthetic Dataset and Colab Demo

This repository accompanies a synthetic dataset and interactive notebook designed to explore *causal fairness* through mediation analysis. Building on the framework from [Binkytė et al., 2022 (arXiv:2207.04053)](https://arxiv.org/abs/2207.04053), we simulate a realistic hiring scenario involving sensitive attributes, mediators, and confounders.

The dataset enables detailed decomposition of discrimination into **direct**, **indirect (via mediators)**, and **spurious (via confounders)** pathways. Our Colab notebook walks through:

- ✅ Construction of a **causal DAG** and setup of structural equations  
- ✅ Generation of a synthetic dataset with interpretable variables  
- ✅ Evaluation of fairness metrics like **statistical parity**  
- ✅ Computation of **path-specific effects** using counterfactual reasoning  
- ✅ Visual and statistical analysis of mediated unfairness

## 📁 Dataset Overview

| Variable | Description |
|---------|-------------|
| A | Political Belief (0 = Conservative, 1 = Liberal) |
| C | Socio-Economic Status (0 = High SES, 1 = Low SES) |
| M1 | Community Service (continuous) |
| M2 | Address (0 = Rural, 1 = Urban) |
| Y | Hiring Outcome (0 = Rejected, 1 = Hired) |

This work supports the development and evaluation of fairness-aware algorithms in causal settings, especially where interpretability and legal accountability are essential.

## 🔗 Resources

- 📊 [Colab Notebook (interactive)](LINK_TO_COLAB)
- 📦 [Dataset (Zenodo archive)](ZENODO_DOI_LINK)
- 📜 Based on [arXiv:2207.04053](https://arxiv.org/abs/2207.04053)
