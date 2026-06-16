# AAI-500-Final-Team-Project

* **Google Slides Link:** [Final Project Presentation](https://docs.google.com/presentation/d/1ZAVfJUaBqgawWaK1g8_ob_liHWWCKZ1lskQHFtwyO6Y/edit?usp=drive_link)

# Notebooks

The analysis is split across three Jupyter notebooks. Run them in order:

| Notebook | Purpose |
|---|---|
| `code/01_data_prep.ipynb` | Loads raw UCI Adult data, removes missing values and duplicates, saves `data/adult_sanitized.csv` |
| `code/02_eda.ipynb` | Exploratory data analysis — distributions, income rates by feature, chi-square tests |
| `code/03_modeling.ipynb` | Logistic regression — GLM inferential summary (statsmodels) + prediction metrics and plots (scikit-learn) |

**Setup:** Install dependencies with `uv sync`, then launch JupyterLab with `./start_jupyter.sh`.

# Data Preparation

The Adult dataset was obtained from the UCI Machine Learning Repository. Missing values represented by "?" were identified in the workclass, occupation, and native_country variables. Records containing missing values were removed using listwise deletion. Duplicate records were then identified and removed.

Cleaning Summary
Step	Records
Original Dataset	32,561
Removed Missing Records	2,399
Removed Duplicate Records	23
Final Dataset	30,139

The resulting dataset was used for all subsequent exploratory analysis, model training, and evaluation.

# Exploratory Data Analysis

EDA was performed on the 30,139-record cleaned dataset. Key findings:

- **Class imbalance:** ~75% of individuals earn ≤$50K and ~25% earn >$50K. Raw accuracy is a misleading evaluation metric; AUC-ROC is used instead.
- **Education is the strongest predictor:** Workers with a Doctorate or Professional school degree earn >$50K at rates exceeding 74%, versus ~16% for high school graduates — a 4.6x difference. Every level of post-secondary education provides a measurable income premium.
- **Income peaks in mid-career:** High-income rates peak in the 45–54 age bracket (~42%) and decline after 65, reflecting career advancement and accumulated investment income.
- **Occupation encodes structural inequality:** Executive/managerial and professional specialty roles earn >$50K at nearly double the overall rate; farming, service, and cleaning roles fall below 5%.
- **Gender gap:** Males earn >$50K at ~30% vs. ~11% for females — a 19 percentage point gap.
- **Capital activity signals wealth:** Capital gain is near-zero for most individuals but is a strong differentiator for the >$50K group.
- **All categorical features are statistically significant** (chi-square p < 0.001), with marital status, relationship, and education showing the strongest associations with income.

# Model Selection

**Model:** Logistic Regression (Generalized Linear Model — binomial family, logit link)

The target variable is binary (income ≤$50K / >$50K), making logistic regression the appropriate choice. Following the Generalized Linear Model framework, logistic regression is fit as a binomial GLM with a logit link estimated via maximum likelihood. EDA confirmed that the key predictors — education, age, and hours per week — have monotonic relationships with income, satisfying the model's linearity-in-log-odds assumption. Coefficients are interpretable as odds ratios and come with Wald test p-values, directly supporting the statistical justification required by the project rubric.

## Implementation Approach

- **Dual-library fit:** Logistic regression is fit in `statsmodels` (`smf.glm` with `family=Binomial()`, using the formula API so categorical terms are encoded via `C()`) for the full inferential summary table (coefficients, standard errors, z-values, p-values, confidence intervals) and in `scikit-learn` for streamlined prediction and metric computation.
- **Preprocessing:** Categorical features are dummy-encoded with `pd.get_dummies` (`drop_first=True`) for the scikit-learn pipeline. `fnlwgt` (a census sampling weight, not a personal attribute) is dropped, and only one of the redundant `education` / `education_num` pair is retained to avoid collinearity.
- **Train/test split:** 70/30 stratified split to preserve the class ratio in both partitions.

## Class Imbalance & Evaluation

The dataset has a 75/25 class imbalance (documented in EDA). This is addressed via `class_weight='balanced'` and a stratified split. The model is evaluated on the full classification metric suite — **accuracy, precision, recall (sensitivity), specificity, F1 score, and AUROC** — alongside a confusion matrix, ROC curve, odds-ratio plot, and predicted-probability distribution, rather than relying on raw accuracy.

## Results

On the held-out 30% test set, the model achieves **AUROC = 0.902**, **recall (sensitivity) = 0.835**, **specificity = 0.802**, and **accuracy = 0.810**. The strongest predictors of earning >$50K are marital status (married-civ-spouse, OR ≈ 7.9), sex (male, OR ≈ 2.6), executive/managerial occupation (OR ≈ 2.0), and each additional year of education (OR ≈ 1.3) — all consistent with the EDA findings.