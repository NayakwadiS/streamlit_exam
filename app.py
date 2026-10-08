import streamlit as st
import random
import json
from datetime import datetime

# 1. Page Configuration
st.set_page_config(page_title="AWS AI Practitioner Exam Simulator", page_icon="☁️", layout="wide")

# 2. Define the Comprehensive Question Bank for 5 Domains
DOMAINS_DATA = {
    "Domain 1: Fundamentals of AI and ML": [
        ("What type of ML task should be used to predict the exact future price of a stock based on historical sales trends?",
         ["Regression", "Binary Classification", "Clustering", "Dimensionality Reduction"], 0,
         "Predicting a continuous numerical value like a price is a classic Regression task."),
        ("An engineer wants to group customer profiles into segments without pre-existing labels. What approach fits best?",
         ["Unsupervised Learning (Clustering)", "Supervised Learning (Classification)", "Reinforcement Learning",
          "Semi-supervised Learning"], 0,
         "Grouping unlabeled data based on similarities is Unsupervised Learning."),
        ("A model performs excellently on training data but poorly on test data. What is this called?",
         ["Overfitting", "Underfitting", "High Bias", "Data Drift"], 0,
         "Overfitting occurs when a model learns noise and fails to generalize."),
        ("Which metric is best for evaluating a classification model with imbalanced classes?",
         ["F1-Score", "Accuracy", "Mean Squared Error", "Precision only"], 0,
         "F1-Score balances precision and recall, ideal for imbalanced datasets."),
        ("What does the bias-variance tradeoff describe?",
         ["Balance between model simplicity and complexity", "Data quality issues", "Overfitting only", "Computational cost"], 0,
         "It describes the tradeoff between underfitting (high bias) and overfitting (high variance)."),
        ("Which technique helps prevent overfitting in neural networks?",
         ["Dropout", "Increasing model complexity", "Removing validation data", "Using more epochs"], 0,
         "Dropout randomly deactivates neurons during training to prevent co-adaptation."),
        ("What is feature scaling used for?",
         ["Normalizing input features to similar ranges", "Removing outliers", "Increasing model accuracy", "Reducing computational cost"], 0,
         "Feature scaling normalizes inputs (e.g., 0-1 or standardization) for better model performance."),
        ("In supervised learning, what is the main goal?",
         ["Map inputs to correct outputs using labeled data", "Find patterns in unlabeled data", "Optimize reward signals", "Predict without labels"], 0,
         "Supervised learning trains on labeled data to learn input-output mappings."),
        ("What is cross-validation used for?",
         ["Assessing model generalization without overfitting to test set", "Training the model", "Scaling features", "Hyperparameter definition"], 0,
         "Cross-validation divides data into folds to reliably estimate model performance."),
        ("Which of these is a metric for regression models?",
         ["Mean Squared Error (MSE)", "Recall", "Precision", "F1-Score"], 0,
         "MSE measures the average squared difference between predicted and actual values."),
        ("What problem causes a model to have high bias?",
         ["Underfitting - model is too simple", "Overfitting - model is too complex", "Poor data quality", "Incorrect scaling"], 0,
         "High bias indicates the model is too simple to capture underlying patterns (underfitting)."),
        ("Which dataset is used to evaluate final model performance?",
         ["Test set", "Training set", "Validation set", "Development set"], 0,
         "The test set, held out from training, evaluates final model performance on unseen data."),
        ("How does L1 regularization (Lasso) differ from L2 (Ridge)?",
         ["L1 can zero out features, L2 only reduces them", "L2 is always better", "They are identical", "L1 is only for classification"], 0,
         "L1 regularization can eliminate features by setting weights to zero."),
        ("What does a confusion matrix show?",
         ["True positives, false positives, true negatives, false negatives", "Model accuracy only", "Feature importance", "Training loss"], 0,
         "A confusion matrix breaks down prediction results into TP, FP, TN, FN."),
        ("Which algorithm is commonly used for both classification and regression?",
         ["Decision Trees", "K-Means", "PCA", "Isolation Forest"], 0,
         "Decision Trees can be used for both classification and regression tasks."),
        ("What does gradient descent optimize?",
         ["Model weights by moving toward minimum loss", "Data quality", "Feature selection", "Model size"], 0,
         "Gradient descent iteratively updates weights to minimize the loss function."),
        ("In clustering, what does 'k' represent in k-means?",
         ["Number of clusters", "Data points per cluster", "Features", "Iterations"], 0,
         "'k' is the number of clusters to partition the data into."),
        ("What is the purpose of train-test split?",
         ["Prevent data leakage and assess generalization", "Increase model accuracy", "Reduce training time", "Improve features"], 0,
         "Train-test split separates data to prevent overfitting evaluation."),
        ("Which metric measures the proportion of correct predictions?",
         ["Accuracy", "Precision", "Recall", "F1-Score"], 0,
         "Accuracy is the ratio of correct predictions to total predictions."),
        ("What is mentioned in precision?",
         ["Of predicted positives, how many are actually positive", "Of actual positives, how many are detected", "Overall correctness", "True negatives"], 0,
         "Precision = TP / (TP + FP): proportion of correct positive predictions."),
        ("What does recall measure?",
         ["Of actual positives, how many are correctly identified", "Positive predictions accuracy", "Model speed", "Overall correctness"], 0,
         "Recall = TP / (TP + FN): proportion of actual positives detected."),
    ],
    "Domain 2: Fundamentals of Generative AI": [
        ("To generate predictable, factual responses with minimal variety, how should temperature be adjusted?",
         ["Decrease toward 0", "Increase toward 1", "Maximize Top-P", "Set context window to minimum"], 0,
         "Lowering temperature makes token selection deterministic and focused."),
        ("Which approach allows a model to query external databases for fresh facts without retraining?",
         ["Retrieval-Augmented Generation (RAG)", "Fine-Tuning", "Pre-training", "RLHF"], 0,
         "RAG fetches contextual information from external sources during inference."),
        ("To limit token choices to a cumulative probability threshold, which parameter should be modified?",
         ["Top-P (Nucleus Sampling)", "Top-K", "Temperature", "Max Tokens"], 0,
         "Top-P samples from tokens reaching a defined probability threshold."),
        ("What is the foundation model in generative AI?",
         ["Large-scale pre-trained model on diverse data", "Task-specific supervised model", "Rule-based system", "Clustering algorithm"], 0,
         "Foundation models are large, pre-trained on diverse data, and fine-tuned for various tasks."),
        ("What does fine-tuning accomplish?",
         ["Adapts pre-trained model to specific tasks with task-specific data", "Changes underlying model weights permanently", "Improves base model", "Guarantees better results"], 0,
         "Fine-tuning trains a pre-trained model on task-specific data for better performance."),
        ("Which technique uses human feedback to align model outputs with human preferences?",
         ["Reinforcement Learning from Human Feedback (RLHF)", "Supervised fine-tuning", "Prompt engineering", "RAG"], 0,
         "RLHF uses human ratings to train reward models that align with human preferences."),
        ("What is prompt engineering?",
         ["Crafting inputs to guide model outputs effectively", "Tuning model weights", "Changing model architecture", "Data preprocessing"], 0,
         "Prompt engineering designs prompts to elicit desired behaviors from language models."),
        ("In generative AI, what does 'context window' refer to?",
         ["Maximum input tokens the model can process at once", "Model parameter count", "Training data size", "Output length"], 0,
         "Context window is the maximum number of tokens a model can accept as input."),
        ("What is the purpose of temperature in language model sampling?",
         ["Control randomness/creativity in token selection", "Improve accuracy", "Reduce computational cost", "Increase context"], 0,
         "Temperature controls output predictability: low=deterministic, high=creative."),
        ("Which sampling method prevents unreasonably low-probability tokens?",
         ["Top-K sampling", "Greedy decoding", "Beam search", "Random sampling"], 0,
         "Top-K restricts sampling to the k most likely next tokens."),
        ("What problem does RAG solve?",
         ["Outdated or hallucinated information by providing real-time facts", "Slow inference", "Model size", "Training cost"], 0,
         "RAG provides factual grounding by retrieves relevant documents during generation."),
        ("How does prompt chaining improve results?",
         ["Breaking complex tasks into sequential prompts for better outputs", "Running multiple models", "Increasing model size", "Using ensemble methods"], 0,
         "Prompt chaining divides tasks into steps, each building on previous results."),
        ("What is a 'token' in language models?",
         ["Discrete unit of text (word, subword, or symbol)", "Model parameter", "Training example", "GPU memory unit"], 0,
         "Tokens are the smallest units processed by language models (words or subwords)."),
        ("What does 'hallucination' mean in generative AI?",
         ["Model generating plausible but false information", "Model refusing to answer", "Excessive creativity", "Memory error"], 0,
         "Hallucination is when models confidently state incorrect facts as truth."),
        ("Which approach reduces hallucinations the most?",
         ["RAG with grounded facts", "Increasing temperature", "Longer context", "More data"], 0,
         "RAG grounds responses in verified external information, reducing fabrications."),
        ("What is multi-turn conversation in dialogue systems?",
         ["Model maintaining context across multiple exchanges", "Single question-answer pair", "Parallel processing", "Independent responses"], 0,
         "Multi-turn conversation requires maintaining context across dialogue history."),
        ("How does Few-Shot Learning work?",
         ["Model learns from minimal examples in the prompt", "Requires much training data", "Uses pre-recorded examples", "Unsupervised learning"], 0,
         "Few-shot learning demonstrates task via examples in the prompt rather than training data."),
        ("What distinguishes Zero-Shot Learning?",
         ["Model performs task without any task-specific examples", "Requires training data", "Always fails", "Only for classification"], 0,
         "Zero-shot uses only task description without demonstrations."),
        ("In transformers, what is 'attention'?",
         ["Mechanism to weigh relationships between tokens", "Model Focus", "Data selection", "Memory storage"], 0,
         "Attention computes weighted relationships between all token pairs."),
        ("What is the purpose of embeddings in AI models?",
         ["Convert text to dense numerical vectors capturing semantic meaning", "Increase model speed", "Reduce accuracy", "Store raw text"], 0,
         "Embeddings represent text as vectors where semantic similarity = spatial proximity."),
    ],
    "Domain 3: Applications of AWS AI Services": [
        ("To extract text, tables, and forms from scanned documents, which service should be used?",
         ["Amazon Textract", "Amazon Rekognition", "Amazon Comprehend", "Amazon Translate"], 0,
         "Textract specifically extracts structured text and tabular data from documents."),
        ("For building intelligent conversational chatbots, which AWS service is used?",
         ["Amazon Lex", "Amazon Polly", "Amazon Transcribe", "Amazon Comprehend"], 0,
         "Lex provides conversational AI engine for text and voice chatbots."),
        ("To flag explicit content in uploaded videos, which service is best?",
         ["Amazon Rekognition", "Amazon Textract", "Amazon SageMaker Ground Truth", "Amazon Transcribe"], 0,
         "Rekognition provides computer vision for content moderation."),
        ("Which service translates text between languages?",
         ["Amazon Translate", "Amazon Comprehend", "Amazon Polly", "Amazon Lex"], 0,
         "Translate converts text from one language to another."),
        ("To convert text to natural-sounding speech, which service is used?",
         ["Amazon Polly", "Amazon Transcribe", "Amazon Lex", "Amazon Translate"], 0,
         "Polly converts text to lifelike speech in multiple languages."),
        ("For real-time speech-to-text transcription, which service applies?",
         ["Amazon Transcribe", "Amazon Polly", "Amazon Lex", "Amazon Translate"], 0,
         "Transcribe converts speech audio to text in real-time or batch."),
        ("To extract sentiment and key phrases from text, which service is used?",
         ["Amazon Comprehend", "Amazon Textract", "Amazon Lex", "Amazon Rekognition"], 0,
         "Comprehend performs NLP tasks like sentiment analysis and entity extraction."),
        ("Which service enables searching through large document collections?",
         ["Amazon Kendra", "Amazon Textract", "Amazon Comprehend", "Amazon Rekognition"], 0,
         "Kendra provides intelligent document search using ML."),
        ("To detect faces, objects, and scenes in images, which service is used?",
         ["Amazon Rekognition", "Amazon Textract", "Amazon Polly", "Amazon Translate"], 0,
         "Rekognition analyzes images and videos for objects, faces, text, and scenes."),
        ("For creating a personalized recommendation engine, which service helps?",
         ["Amazon Personalize", "Amazon Lex", "Amazon Polly", "Amazon Kendra"], 0,
         "Personalize delivers personalized recommendations based on user behavior."),
        ("Which service analyzes medical images like X-rays and MRIs?",
         ["Amazon HealthLake with Lookout for Medical", "Amazon Rekognition", "Amazon Textract", "Amazon Translate"], 0,
         "Lookout for Medical analyzes medical images for healthcare use cases."),
        ("To predict customer churn or outcomes, which service should be used?",
         ["Amazon Lookout for Metrics", "Amazon Personalize", "Amazon Comprehend", "Amazon Translate"], 0,
         "Lookout for Metrics detects anomalies and unusual metric behavior."),
        ("For anomaly detection in monitoring data, which service applies?",
         ["Amazon Lookout for Equipment", "Amazon Rekognition", "Amazon Polly", "Amazon Lex"], 0,
         "Lookout for Equipment detects equipment anomalies using ML."),
        ("Which service uses foundational models via API?",
         ["Amazon Bedrock", "Amazon SageMaker", "Amazon Personalize", "Amazon Lex"], 0,
         "Bedrock provides access to foundation models via simple APIs."),
        ("For building, training, and deploying custom ML models, which service is used?",
         ["Amazon SageMaker", "Amazon Bedrock", "Amazon Comprehend", "Amazon Textract"], 0,
         "SageMaker is the comprehensive ML platform for custom model development."),
        ("To forecast time-series data like sales or traffic, which service applies?",
         ["Amazon Forecast", "Amazon Personalize", "Amazon Lookup", "Amazon Lex"], 0,
         "Forecast predicts time-series data using ML algorithms."),
        ("Which service provides contact center intelligence?",
         ["Amazon Connect", "Amazon Lex", "Amazon Polly", "Amazon Translate"], 0,
         "Connect provides cloud-based contact center with AI integration."),
        ("For document classification and organization, which service is best?",
         ["Amazon Textract with Comprehend", "Amazon Rekognition", "Amazon Translate", "Amazon Polly"], 0,
         "Textract extracts document content, Comprehend can classify it."),
        ("To analyze logs and detect security threats, which service helps?",
         ["Amazon GuardDuty", "Amazon Rekognition", "Amazon Polly", "Amazon Translate"], 0,
         "GuardDuty uses ML to detect security threats from logs."),
        ("Which service helps label large datasets for training?",
         ["Amazon SageMaker Ground Truth", "Amazon Textract", "Amazon Polly", "Amazon Lex"], 0,
         "Ground Truth accelerates dataset labeling for ML training."),
    ],
    "Domain 4: Guidelines for Responsible AI": [
        ("To filter toxic content and PII in Bedrock, which feature should be used?",
         ["Guardrails for Amazon Bedrock", "AWS CloudTrail", "Amazon Bedrock Agents", "AWS IAM Policies"], 0,
         "Guardrails provide content filtering and PII redaction."),
        ("Which pillar addresses explaining how AI reached a prediction?",
         ["Explainability", "Fairness", "Robustness", "Governance"], 0,
         "Explainability ensures transparency in AI decision-making."),
        ("How should model bias across demographics be mitigated?",
         ["Check training data and monitor predictions across groups", "Use more data", "Ignore demographic differences", "Increase model complexity"], 0,
         "Fairness requires checking that models treat all groups equitably."),
        ("What does 'model drift' refer to?",
         ["Model performance degrading on new data due to data changes", "Model training failure", "Overfitting only", "Memory issues"], 0,
         "Model drift occurs when data distribution changes, affecting performance."),
        ("Why is transparency important in AI systems?",
         ["Users/regulators need to understand AI decisions for trust and accountability", "Increases accuracy", "Reduces cost", "Improves speed"], 0,
         "Transparency builds trust and enables regulatory compliance."),
        ("Which is key to responsible AI governance?",
         ["Clear policies, monitoring, and accountability mechanisms", "Only accuracy", "Fast deployment", "Minimal oversight"], 0,
         "Governance requires policies, auditing, and accountability."),
        ("How can fairness biases in datasets be identified?",
         ["Analyze representation across protected attributes", "Use simpler models", "Ignore demographics", "Increase data"], 0,
         "Fairness audits check if training data represents groups equally."),
        ("What is the purpose of responsible AI frameworks?",
         ["Provide guidance on ethical AI development and deployment", "Maximize profits", "Reduce regulations", "Increase model complexity"], 0,
         "Frameworks guide ethical decisions throughout AI lifecycle."),
        ("How should AI systems handle human oversight?",
         ["Maintain human-in-the-loop for critical decisions", "Fully automate all decisions", "Remove human involvement", "Ignore human input"], 0,
         "Critical decisions need human review to prevent harm."),
        ("What is algorithmic bias?",
         ["Systematic errors favoring/disadvantaging certain groups", "Random prediction errors", "Missing features", "Poor data quality"], 0,
         "Bias exists when algorithms systematically disadvantage groups."),
        ("Why monitor AI models post-deployment?",
         ["Detect performance degradation and drifts early", "Increase accuracy indefinitely", "Reduce cost", "Only once"], 0,
         "Monitoring catches issues before they harm users."),
        ("What role does consent play in responsible AI?",
         ["Users should know how their data is used in AI systems", "No consent needed", "Only for high-risk systems", "Developers decide"], 0,
         "Informed consent respects user autonomy and privacy."),
        ("How should edge cases be handled in AI systems?",
         ["Plan for and test unusual scenarios carefully", "Ignore unlikely cases", "Deploy without testing", "Assume perfection"], 0,
         "Edge case testing prevents failures in unusual real-world conditions."),
        ("What is the purpose of impact assessments?",
         ["Evaluate potential harms before deployment", "Only after issues arise", "Not necessary", "Increase cost only"], 0,
         "Impact assessments identify risks before they occur."),
        ("How should sensitive attributes be handled?",
         ["Protect or exclude from training to prevent discrimination", "Always include all data", "Ignore privacy concerns", "Maximize features"], 0,
         "Protecting sensitive attributes prevents systematic bias."),
        ("What does 'explainability' NOT include?",
         ["Making the model smaller", "Providing reasoning for predictions", "Interpretable models", "Feature importance analysis"], 0,
         "Explainability is about transparency, not model simplification."),
        ("How should model decisions affecting people be validated?",
         ["Test extensively with representative data and stakeholder input", "Quick deployment", "Minimal testing", "Skip validation"], 0,
         "Validation with stakeholders ensures decisions are fair and accurate."),
        ("What is the challenge of fairness in AI?",
         ["Different fairness definitions can conflict; trade-offs needed", "Easy to achieve perfect fairness", "Not important", "Technical only"], 0,
         "Fairness involves complex tradeoffs between different fairness metrics."),
        ("How should adversarial attacks on AI be addressed?",
         ["Test robustness and implement defenses", "Ignore potential attacks", "Hope for best", "Blame users"], 0,
         "Robustness testing prevents malicious manipulation."),
        ("Why is documentation critical for responsible AI?",
         ["Record decisions, limitations, and intended use for accountability", "Not necessary", "Only for regulators", "Adds no value"], 0,
         "Documentation enables audit and prevents misuse."),
    ],
    "Domain 5: Security, Compliance, and Operations": [
        ("For logging all API calls to Bedrock with identity and IP, which service is used?",
         ["AWS CloudTrail", "Amazon CloudWatch Logs", "AWS Trusted Advisor", "Amazon GuardDuty"], 0,
         "CloudTrail logs all API activity across AWS services."),
        ("To guarantee dedicated throughput for production Bedrock apps, what should be purchased?",
         ["Provisioned Throughput", "On-Demand Capacity", "Batch Inference Plans", "Spot Instances"], 0,
         "Provisioned Throughput reserves dedicated capacity."),
        ("How does AWS manage customer data privacy with Bedrock?",
         ["Customer data never trains or improves base models", "Shared with providers for 24 hours", "Added to public pools", "Encrypted with shared keys only"], 0,
         "AWS maintains strict data isolation—no customer data in model training."),
        ("Which compliance frameworks does AWS Bedrock support?",
         ["HIPAA, PCI-DSS, SOC 2", "No compliance standards", "Only PCI-DSS", "Custom standards only"], 0,
         "Bedrock supports major compliance standards via AWS Compliance Program."),
        ("How should encryption be configured for sensitive data in Bedrock?",
         ["Use AWS KMS with customer-managed keys", "No encryption needed", "Share keys publicly", "Disable security"], 0,
         "Customer-managed KMS keys provide maximum control over encryption."),
        ("For monitoring Bedrock costs, which service should be used?",
         ["AWS Cost Explorer", "Amazon CloudWatch", "AWS CloudTrail", "Amazon QuickSight"], 0,
         "Cost Explorer tracks and analyzes AWS spending."),
        ("Which service detects security threats in Bedrock infrastructure?",
         ["Amazon GuardDuty", "Amazon CloudWatch", "AWS CloudTrail", "AWS Trusted Advisor"], 0,
         "GuardDuty uses ML to detect threats across AWS services."),
        ("How should access to Bedrock be controlled?",
         ["IAM policies and roles", "No access control", "Public access", "Shared passwords"], 0,
         "IAM provides fine-grained access control to AWS services."),
        ("For network-level security, which service should be used with Bedrock?",
         ["VPC endpoints and Security Groups", "Public internet access", "No network security", "Shared tunnels"], 0,
         "VPC endpoints restrict Bedrock access to private networks."),
        ("How should model outputs be validated for compliance?",
         ["Regular audits and automated scanning", "No validation needed", "Manual spot checks only", "Trust the model"], 0,
         "Continuous validation ensures compliance with policies."),
        ("Which metric should be monitored for operational health?",
         ["Latency, error rates, throughput", "Model accuracy only", "Data size only", "No metrics"], 0,
         "Operational metrics indicate system health and performance."),
        ("How should rate limiting be implemented for Bedrock?",
         ["Use API throttling and quotas", "No limits needed", "Unlimited access", "Manual blocking"], 0,
         "Rate limiting prevents abuse and resource exhaustion."),
        ("For disaster recovery, what should be implemented?",
         ["Multi-region redundancy and automated failover", "Backup only", "No recovery plan", "Manual recovery only"], 0,
         "Disaster recovery requires redundancy and failover capabilities."),
        ("How should incidents with Bedrock be handled?",
         ["Document, investigate, and implement preventive measures", "Ignore them", "Manual ad-hoc response", "No procedures"], 0,
         "Incident response procedures minimize damage and improve systems."),
        ("Which AWS service provides compliance auditing logs?",
         ["AWS CloudTrail", "Amazon CloudWatch", "Amazon QuickSight", "AWS Config"], 0,
         "CloudTrail provides audit logs for compliance investigations."),
        ("How should sensitive data be masked in logs?",
         ["Redact PII before logging", "Log everything", "No masking needed", "Manual redaction"], 0,
         "Data masking protects sensitive information in logs."),
        ("For managing secrets like API keys, which service should be used?",
         ["AWS Secrets Manager", "Environment variables", "Hardcoded in code", "Shared text files"], 0,
         "Secrets Manager securely stores and rotates credentials."),
        ("How should Bedrock usage be audited for policy compliance?",
         ["Enable CloudTrail logging and analyze access patterns", "No auditing", "Occasional checks", "Trust users"], 0,
         "Auditing ensures users follow security policies."),
        ("Which service provides automated compliance scanning?",
         ["AWS Config", "Amazon CloudWatch", "AWS CloudTrail", "AWS Trusted Advisor"], 0,
         "AWS Config monitors resource configurations for compliance."),
        ("How should high-risk Bedrock operations be protected?",
         ["Require MFA and approval workflows", "No protection needed", "Single password", "Public access allowed"], 0,
         "Multi-factor authentication and approval gates reduce risk."),
    ]
}

# 3. Enhanced Question Bank Processing
@st.cache_data
def prepare_questions():
    """Prepare all questions with shuffled options"""
    all_questions = {}
    for domain_name, questions in DOMAINS_DATA.items():
        domain_list = []
        for q_text, opts, correct_idx, explanation in questions:
            # Shuffle options while tracking correct answer
            options_with_indices = list(enumerate(opts))
            random.seed(hash(q_text))  # Consistent seed per question
            random.shuffle(options_with_indices)
            
            shuffled_options = [opt for _, opt in options_with_indices]
            new_correct_idx = next(idx for idx, (orig_idx, _) in enumerate(options_with_indices) if orig_idx == correct_idx)
            
            domain_list.append({
                "question": q_text,
                "options": shuffled_options,
                "correct_idx": new_correct_idx,
                "explanation": explanation
            })
        all_questions[domain_name] = domain_list
    return all_questions

questions_bank = prepare_questions()

# 4. Initialize Session State Variables
if "current_domain" not in st.session_state:
    st.session_state.current_domain = list(questions_bank.keys())[0]

if "q_index" not in st.session_state:
    st.session_state.q_index = 0

if "quiz_mode" not in st.session_state:
    st.session_state.quiz_mode = False  # Practice vs Quiz

if "quiz_scores" not in st.session_state:
    st.session_state.quiz_scores = {}  # Track scores per domain

if "answered_questions" not in st.session_state:
    st.session_state.answered_questions = {}  # Track user answers

if "show_review" not in st.session_state:
    st.session_state.show_review = False

if "quiz_all_questions" not in st.session_state:
    st.session_state.quiz_all_questions = []  # All mixed questions for quiz mode

if "quiz_total_correct" not in st.session_state:
    st.session_state.quiz_total_correct = 0  # Track correct answers in full quiz

if "quiz_answered" not in st.session_state:
    st.session_state.quiz_answered = {}  # Track which questions answered


# Helper function to create mixed quiz questions from all domains
def create_mixed_quiz():
    """Create a shuffled quiz with 65 random questions from all domains (like real AWS exam)"""
    all_quiz_questions = []
    
    for domain_name, questions in questions_bank.items():
        for q in questions:
            q_with_domain = q.copy()
            q_with_domain["domain"] = domain_name  # Track which domain this came from
            all_quiz_questions.append(q_with_domain)
    
    # Shuffle the questions randomly
    random.shuffle(all_quiz_questions)
    
    # Return only 65 questions (like actual AWS exam)
    return all_quiz_questions[:65]


# Callback functions for sidebar changes
def update_domain():
    st.session_state.q_index = 0

def update_mode():
    st.session_state.q_index = 0  # Reset question index when mode changes
    
    # If switching to Quiz Mode, generate mixed questions
    if st.session_state.quiz_mode:
        st.session_state.quiz_all_questions = create_mixed_quiz()
        st.session_state.quiz_total_correct = 0
        st.session_state.quiz_answered = {}

# 6. UI Layout & Sidebar Navigation
st.title("☁️ AWS Certified AI Practitioner Exam Simulator")
st.caption("Enhanced Learning Platform • 100+ Questions per Domain • Real Exam-Style Questions")

# Sidebar Controls
with st.sidebar:
    st.header("📋 Navigation & Settings")
    
    # Mode Selection with callback
    mode = st.radio(
        "Select Mode:", 
        ["📖 Practice Mode", "🎯 Quiz Mode", "📊 Performance"], 
        index=0,
        on_change=update_mode
    )
    
    # Store mode in session state
    if mode == "📖 Practice Mode":
        st.session_state.quiz_mode = False
    elif mode == "🎯 Quiz Mode":
        st.session_state.quiz_mode = True
        # Initialize mixed quiz if not already done
        if not st.session_state.quiz_all_questions:
            st.session_state.quiz_all_questions = create_mixed_quiz()
    else:  # Performance Mode
        st.session_state.quiz_mode = None
    
    st.divider()
    
    # Domain Selection (hidden in Quiz Mode)
    if st.session_state.quiz_mode is not True:  # Show domain selector only in Practice and Performance modes
        domain_list = list(questions_bank.keys())
        current_idx = domain_list.index(st.session_state.current_domain) if st.session_state.current_domain in domain_list else 0

        selected_domain = st.selectbox(
            "Select Domain:",
            domain_list,
            index=current_idx,
            on_change=update_domain
        )
        
        # Update session state if selection changed
        st.session_state.current_domain = selected_domain
        
        st.divider()
        
        # Display stats
        num_questions = len(questions_bank[selected_domain])
        st.metric("Questions in Domain", num_questions)
        
        if selected_domain in st.session_state.quiz_scores:
            score = st.session_state.quiz_scores[selected_domain]
            st.metric("Quiz Score", f"{score['correct']}/{score['total']}", f"{int(score['correct']/score['total']*100)}%")
    else:  # Quiz Mode
        st.write("### 🎯 Full Exam Quiz")
        st.write("Questions from **all 5 domains** mixed together")
        st.divider()
        st.metric("Total Questions", 65)
        st.metric("Current Score", f"{st.session_state.quiz_total_correct}/{len(st.session_state.quiz_all_questions)}")

# Check if Performance Mode
if st.session_state.quiz_mode is None:  # Performance Mode
    st.subheader("📊 Performance Dashboard")
    
    if not st.session_state.quiz_scores:
        st.info("📝 No quiz scores yet. Take quizzes to see your performance!")
    else:
        st.write("### Your Quiz Results:")
        
        total_correct = 0
        total_questions = 0
        
        for domain in st.session_state.quiz_scores:
            score_data = st.session_state.quiz_scores[domain]
            correct = score_data['correct']
            total = score_data['total']
            percentage = int((correct / total) * 100)
            
            # Create progress bar for each domain
            col1, col2, col3 = st.columns([2, 1, 1])
            with col1:
                st.write(f"**{domain.split(':')[1].strip()}**")
            with col2:
                st.write(f"{correct}/{total}")
            with col3:
                st.write(f"{percentage}% ✓" if percentage >= 75 else f"{percentage}%")
            
            st.progress(percentage / 100)
            
            total_correct += correct
            total_questions += total
        
        # Overall stats
        st.divider()
        overall_percentage = int((total_correct / total_questions) * 100) if total_questions > 0 else 0
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Correct", total_correct)
        with col2:
            st.metric("Total Questions", total_questions)
        with col3:
            st.metric("Overall Score", f"{overall_percentage}%")
        
        if overall_percentage >= 75:
            st.success("🎉 Great job! You're ready for the exam!")
        elif overall_percentage >= 70:
            st.info("📚 Good progress! Review weak areas before the exam.")
        else:
            st.warning("💪 Keep practicing to improve your score!")

else:  # Practice or Quiz Mode
    # Handle Practice Mode (single domain)
    if st.session_state.quiz_mode is False:  # Practice Mode
        # Load current question data from single domain
        selected_domain = st.session_state.current_domain
        q_index = st.session_state.q_index
        num_questions = len(questions_bank[selected_domain])
        
        if q_index >= num_questions:
            st.session_state.q_index = 0
            q_index = 0
        
        current_q = questions_bank[selected_domain][q_index]
        
        # Main Content Area
        st.subheader(f"{selected_domain}")
        
        # Progress indicator
        col_progress = st.columns([3, 1])
        with col_progress[0]:
            st.progress((q_index + 1) / num_questions)
        with col_progress[1]:
            st.write(f"**{q_index + 1}/{num_questions}**")
        
        # Question Display
        st.markdown(f"### {current_q['question']}")
        
        # Radio choices for the user
        user_choice = st.radio(
            "Select the best answer:",
            current_q['options'],
            index=None,
            key=f"radio_{selected_domain}_{q_index}"
        )
        
        # Answer Feedback
        if user_choice is not None:
            selected_idx = current_q['options'].index(user_choice)
            is_correct = selected_idx == current_q['correct_idx']
            
            if is_correct:
                st.success("🎉 **Correct!** Great job!")
            else:
                correct_answer_text = current_q['options'][current_q['correct_idx']]
                st.error(f"❌ **Incorrect.** The correct answer is: **{correct_answer_text}**")
            
            st.info(f"💡 **Explanation:** {current_q['explanation']}")
        
        st.divider()
        
        # Navigation Buttons for Practice Mode
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            if st.button("⬅️ Previous", use_container_width=True, disabled=(q_index == 0), key="prev_practice"):
                st.session_state.q_index -= 1
                st.rerun()
        
        with col2:
            st.write("")  # Spacer
        
        with col3:
            if st.button("Next ➡️", use_container_width=True, disabled=(q_index == num_questions - 1), key="next_practice"):
                st.session_state.q_index += 1
                st.rerun()
        
        # Quick Navigation
        st.write("---")
        st.write("**Quick Jump:**")
        col_jump = st.columns(5)
        domains = list(questions_bank.keys())
        for i, col in enumerate(col_jump):
            with col:
                domain_num = i + 1
                if st.button(f"Domain {domain_num}", use_container_width=True, key=f"domain_btn_{domain_num}"):
                    st.session_state.current_domain = domains[i]
                    st.session_state.q_index = 0
                    st.rerun()
    
    else:  # Quiz Mode - Mixed questions from all domains
        q_index = st.session_state.q_index
        all_questions = st.session_state.quiz_all_questions
        
        # Handle case where questions haven't been created yet
        if not all_questions:
            all_questions = create_mixed_quiz()
            st.session_state.quiz_all_questions = all_questions
        
        num_questions = len(all_questions)
        
        if q_index >= num_questions:
            st.session_state.q_index = 0
            q_index = 0
        
        current_q = all_questions[q_index]
        
        # Main Content Area for Mixed Quiz
        st.subheader(f"🎯 Full Exam Quiz - Mixed Questions")
        st.caption(f"from {current_q.get('domain', 'Unknown Domain')}")
        
        # Progress indicator
        col_progress = st.columns([3, 1])
        with col_progress[0]:
            st.progress((q_index + 1) / num_questions)
        with col_progress[1]:
            st.write(f"**{q_index + 1}/{num_questions}**")
        
        # Question Display
        st.markdown(f"### {current_q['question']}")
        
        # Radio choices for the user
        user_choice = st.radio(
            "Select the best answer:",
            current_q['options'],
            index=None,
            key=f"radio_quiz_{q_index}"
        )
        
        # Answer Feedback
        if user_choice is not None:
            selected_idx = current_q['options'].index(user_choice)
            is_correct = selected_idx == current_q['correct_idx']
            
            # Track answer in quiz mode
            if q_index not in st.session_state.quiz_answered:
                st.session_state.quiz_answered[q_index] = is_correct
                if is_correct:
                    st.session_state.quiz_total_correct += 1
            
            if is_correct:
                st.success("🎉 **Correct!** Great job!")
            else:
                correct_answer_text = current_q['options'][current_q['correct_idx']]
                st.error(f"❌ **Incorrect.** The correct answer is: **{correct_answer_text}**")
            
            st.info(f"💡 **Explanation:** {current_q['explanation']}")
        
        st.divider()
        
        # Navigation Buttons for Quiz Mode
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            if st.button("⬅️ Previous", use_container_width=True, disabled=(q_index == 0), key="prev_quiz"):
                st.session_state.q_index -= 1
                st.rerun()
        
        with col2:
            # Show current score in center
            st.write(f"Score: **{st.session_state.quiz_total_correct}/{q_index}**")
        
        with col3:
            if st.button("Next ➡️", use_container_width=True, disabled=(q_index == num_questions - 1), key="next_quiz"):
                st.session_state.q_index += 1
                st.rerun()
        
        # Show summary when finished
        if q_index == num_questions - 1:
            st.write("---")
            st.success(f"✅ Quiz Complete! Your Score: **{st.session_state.quiz_total_correct}/{num_questions}** ({int(st.session_state.quiz_total_correct/num_questions*100)}%)")
