# AAI-500-Final-Team-Project

* **Google Slides Link:** [Final Project Presentation](https://docs.google.com/presentation/d/1ZAVfJUaBqgawWaK1g8_ob_liHWWCKZ1lskQHFtwyO6Y/edit?usp=drive_link)

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

**Model:** Logistic Regression

The target variable is binary (income ≤$50K / >$50K), making logistic regression the appropriate choice. EDA confirmed that the key predictors — education, age, and hours per week — have monotonic relationships with income, satisfying the model's linearity-in-log-odds assumption. Coefficients are interpretable and come with Wald test p-values, directly supporting the statistical justification required by the project rubric.

The dataset has a 75/25 class imbalance (documented in EDA). This is addressed via `class_weight='balanced'` and the primary evaluation metric is AUC-ROC rather than raw accuracy.