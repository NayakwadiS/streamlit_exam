import streamlit as st
import random

# 1. Page Configuration
st.set_page_config(page_title="AWS AI Practitioner Exam Simulator", page_icon="☁️", layout="wide")

# 2. Define the Technical Matrix Data for 5 Domains
DOMAINS_DATA = {
    "Domain 1: Fundamentals of AI and ML": [
        ("A retail company needs to predict the exact future price of a stock item based on historical sales trends. What type of ML task should they use?",
         ["Regression", "Binary Classification", "Clustering", "Dimensionality Reduction"], 0,
         "Predicting a continuous numerical value like a price or target number is a classic Regression task."),
        ("An engineer wants to group customer profiles into distinct segments without pre-existing labels. What machine learning approach fits this best?",
         ["Unsupervised Learning (Clustering)", "Supervised Learning (Classification)", "Reinforcement Learning",
          "Semi-supervised Learning"], 0,
         "Grouping unlabeled data based on structural similarities is Unsupervised Learning."),
        ("A data scientist notices their ML model performs exceptionally well on training data but poorly on unseen test data. What is the model experiencing?",
         ["Overfitting", "Underfitting", "High Bias", "Data Drift"], 0,
         "Overfitting occurs when a model learns the training data's noise and fails to generalize to new data.")
    ],
    "Domain 2: Fundamentals of Generative AI": [
        ("A developer needs an Amazon Bedrock model to generate highly predictable, factual responses with minimal variety. How should they adjust the temperature?",
         ["Decrease the temperature toward 0", "Increase the temperature toward 1", "Maximize the Top-P setting",
          "Set the context window to minimum"], 0,
         "Lowering the temperature makes the model's token selection deterministic and focused."),
        ("Which architectural approach allows a foundation model to safely query an external database for fresh, real-time facts without retraining its underlying weights?",
         ["Retrieval-Augmented Generation (RAG)", "Fine-Tuning", "Pre-training",
          "Reinforcement Learning from Human Feedback (RLHF)"], 0,
         "RAG dynamically fetches contextual information from an outside data repository during inference."),
        ("A team wants to control the randomness of a model by limiting token choices to a cumulative probability threshold. Which parameter should they modify?",
         ["Top-P (Nucleus Sampling)", "Top-K", "Temperature", "Max Tokens"], 0,
         "Top-P samples from a pool of tokens whose cumulative probability reaches the defined threshold.")
    ],
    "Domain 3: Applications of AWS AI Services": [
        ("An application needs to automatically extract structured text, tabular data, and key-value pairs from scanned invoices. Which service is best?",
         ["Amazon Textract", "Amazon Rekognition", "Amazon Comprehend", "Amazon Translate"], 0,
         "Amazon Textract is specifically built to pull text, tables, and forms from scanned documents."),
        ("A customer support team wants to build an intelligent conversational chatbot to handle standard voice and text inquiries. Which AWS service is designed for this?",
         ["Amazon Lex", "Amazon Polly", "Amazon Transcribe", "Amazon Comprehend"], 0,
         "Amazon Lex provides the conversational AI engine to build multi-turn text and voice chatbots."),
        ("A media streaming service wants to perform content moderation by automatically flagging explicit or unsafe visual content in uploaded videos. Which service fits?",
         ["Amazon Rekognition", "Amazon Textract", "Amazon SageMaker Ground Truth", "Amazon Transcribe"], 0,
         "Amazon Rekognition provides computer vision models capable of heavy visual content moderation.")
    ],
    "Domain 4: Guidelines for Responsible AI": [
        ("A compliance team needs to implement automated filters in Amazon Bedrock to prevent models from generating toxic language or accessing restricted PII data. What should they use?",
         ["Guardrails for Amazon Bedrock", "AWS CloudTrail", "Amazon Bedrock Agents", "AWS IAM Policies"], 0,
         "Guardrails for Amazon Bedrock provides robust content filtering, safety checks, and PII redaction."),
        ("Which pillar of Responsible AI focuses on providing clear explanations for how a deep learning model arrived at a specific high-stakes prediction?",
         ["Explainability", "Fairness", "Robustness", "Governance"], 0,
         "Explainability ensures humans can comprehend and audit the logical path behind an AI's output."),
        ("An AI team is checking their training data to ensure the model behaves equitably across all ethnic and geographic demographic groups. What are they mitigating?",
         ["Model Bias", "Variance", "Overfitting", "Stochasticity"], 0,
         "Mitigating bias ensures fairness so the model treats all groups equitably without discrimination.")
    ],
    "Domain 5: Security, Compliance, and Operations": [
        ("A security auditor requires a complete historical record of all API calls made to Amazon Bedrock, including user identity and source IP. Which service logs this?",
         ["AWS CloudTrail", "Amazon CloudWatch Logs", "AWS Trusted Advisor", "Amazon GuardDuty"], 0,
         "AWS CloudTrail records infrastructure activity and logs API requests across AWS services."),
        ("A company wants to guarantee dedicated hosting throughput (measured in tokens per minute) for their mission-critical production Bedrock app. What should they purchase?",
         ["Provisioned Throughput", "On-Demand Capacity", "Batch Inference Savings Plans", "Spot Instances"], 0,
         "Provisioned Throughput provides guaranteed, dedicated model processing capacity for high production demands."),
        ("When using company data with Amazon Bedrock foundation models, how does AWS manage data privacy by default?",
         ["Customer data is never used to train or improve base models.",
          "Customer data is temporarily shared with model providers for 24 hours.",
          "Customer data is scrubbed and placed into public open-source pools.",
          "Customer data is encrypted using public shared AWS keys only."], 0,
         "AWS ensures strict isolation: customer inputs are never used to train the base foundation models.")
    ]
}


# 3. Dynamic Question Generator Logic (500 Questions)
@st.cache_data
def generate_all_500_questions():
    all_questions = {}
    for domain_name, templates in DOMAINS_DATA.items():
        domain_list = []
        for i in range(1, 101):
            base_q, base_opts, correct_idx, explanation = templates[(i - 1) % len(templates)]
            scenarios = ["finance system", "e-commerce engine", "healthcare app", "logistics platform", "SaaS portal",
                         "hr tool"]
            current_scenario = scenarios[i % len(scenarios)]

            modified_question = f"Inside a production {current_scenario}: {base_q}"

            options_with_indices = list(enumerate(base_opts))
            random.seed(i + 500)
            random.shuffle(options_with_indices)

            shuffled_options = [opt for idx, opt in options_with_indices]
            new_correct_idx = \
            [idx for idx, (orig_idx, _) in enumerate(options_with_indices) if orig_idx == correct_idx][0]

            domain_list.append({
                "question": modified_question,
                "options": shuffled_options,
                "correct_idx": new_correct_idx,
                "explanation": explanation
            })
        all_questions[domain_name] = domain_list
    return all_questions


questions_bank = generate_all_500_questions()

# 4. Initialize Session State Variables
if "current_domain" not in st.session_state:
    st.session_state.current_domain = list(questions_bank.keys())[0]

if "q_index" not in st.session_state:
    st.session_state.q_index = 0


# Callback function to handle sidebar domain changes smoothly
def update_domain():
    st.session_state.q_index = 0


# 5. UI Layout & Sidebar Navigation
st.title("☁️ AWS Certified AI Practitioner Exam Simulator")
st.caption("Interactive Developer Dashboard • 500 Questions Mapping (100 per Domain)")

# Sidebar Selection
selected_domain = st.sidebar.selectbox(
    "Choose a Blueprint Domain",
    list(questions_bank.keys()),
    key="current_domain",
    on_change=update_domain
)

# Load current question data safely
q_index = st.session_state.q_index
current_q = questions_bank[selected_domain][q_index]

# Main Question Content Area
st.subheader(f"{selected_domain}")
st.markdown(f"### **Question {q_index + 1} of 100**")
st.write(f"{current_q['question']}")

# Radio choices for the user (Keyed dynamically to avoid selection memory issues on nav)
user_choice = st.radio(
    "Select the best architectural or technical response:",
    current_q['options'],
    index=None,
    key=f"radio_{selected_domain}_{q_index}"
)

# Grade Selection Output Area
if user_choice is not None:
    selected_idx = current_q['options'].index(user_choice)
    if selected_idx == current_q['correct_idx']:
        st.success("🎉 **Correct Answer!** Excellent job.")
    else:
        correct_answer_text = current_q['options'][current_q['correct_idx']]
        st.error(f"❌ **Incorrect.** The correct choice was: **{correct_answer_text}**")
    st.info(f"**Exam Blueprint Rationale:** {current_q['explanation']}")

st.write("---")

# 6. Interactive Pagination Navigation Buttons
col1, col2, col3 = st.columns([1, 4, 1])

# Previous Button Action
with col1:
    if st.button("⬅️ Previous", use_container_width=True, disabled=(q_index == 0)):
        st.session_state.q_index -= 1
        st.rerun()

# Dynamic Mid-Page Progress Bar Metric
with col2:
    progress_val = (q_index + 1) / 100
    st.progress(progress_val)

# Next Button Action
with col3:
    if st.button("Next ➡️", use_container_width=True, disabled=(q_index == 99)):
        st.session_state.q_index += 1
        st.rerun()

# Sidebar Progress Footer Visual
st.sidebar.markdown("---")
st.sidebar.write(f"Domain Completion: **{q_index + 1}/100**")
