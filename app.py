import streamlit as st
import random
import json
from datetime import datetime
import time

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

# 3. Stronger AWS-style question generation system
# This creates a larger, harder, more realistic bank with exam-like scenarios and domain weighting.
HARDER_QUESTION_TEMPLATES = {
    "Domain 1: Fundamentals of AI and ML": [
        (
            "A product team sees a model with 98% training accuracy but only 72% validation accuracy. The most likely root cause is:",
            ["Overfitting due to poor generalization", "Underfitting due to over-regularization", "Label leakage in validation", "Data drift from feature scaling"],
            0,
            "High train accuracy with weak validation performance commonly indicates overfitting."),
        (
            "An ML engineer wants the model to focus on the minority class in a heavily imbalanced fraud dataset. Which metric is most useful for comparing classifiers in that setting?",
            ["F1-score", "Mean absolute error", "R-squared", "Accuracy"],
            0,
            "F1-score balances precision and recall, making it better than raw accuracy for imbalanced classification."),
        (
            "A team needs to compare multiple models fairly without leaking test performance into model selection. The best practice is:",
            ["Use a validation set and cross-validation during model selection", "Train on the full dataset and evaluate once", "Use the test set repeatedly for tuning", "Skip validation and rely on training loss"],
            0,
            "Validation and cross-validation provide unbiased estimates of generalization before final test evaluation."),
        (
            "A feature with a very large magnitude is dominating optimization. The most appropriate corrective action is:",
            ["Apply feature scaling or normalization", "Increase the learning rate drastically", "Remove all training examples with outliers", "Switch to unsupervised learning"],
            0,
            "Scaling helps prevent large-magnitude features from dominating training dynamics."),
        (
            "A team wants to interpret which variables contributed most to a prediction. Which model behavior is most directly useful for that purpose?",
            ["Model explainability and feature importance", "Increasing the number of hidden layers", "Disabling train/test splitting", "Only using more data"],
            0,
            "Explainability methods and feature importance help identify drivers of predictions."),
        (
            "During hyperparameter tuning, a model performs consistently poorly on both training and validation sets. The model is most likely:",
            ["Underfitting", "Overfitting", "Drifting", "Mode collapsing"],
            0,
            "Underfitting happens when the model is too simple and cannot capture the signal in the data.")
    ],
    "Domain 2: Fundamentals of Generative AI": [
        (
            "A customer wants a model to answer questions based on the latest internal documents without retraining. The best design is:",
            ["RAG with a vector store or search index", "Increasing the model temperature to 2.0", "Removing all prompt examples", "Switching to a smaller model"],
            0,
            "RAG lets the model retrieve current factual context at inference time instead of relying only on static training knowledge."),
        (
            "A chatbot is too verbose and inconsistent across turns. The most direct improvement is to:",
            ["Reduce temperature and improve system prompt clarity", "Increase context window indiscriminately", "Add more random sampling", "Set top-k to 1 and ignore prompt history"],
            0,
            "Lower temperature and clearer prompts usually improve coherence and determinism."),
        (
            "A developer wants to sample only the most likely next tokens while still allowing some diversity. The best parameter to tune is:",
            ["Top-p or nucleus sampling", "Learning rate", "Batch size", "Dropout rate"],
            0,
            "Top-p controls cumulative probability mass for token selection and balances diversity with quality."),
        (
            "A model repeatedly produces confident statements that are not supported by the source material. This is known as:",
            ["Hallucination", "Data leakage", "Model drift", "Prompt injection"],
            0,
            "Hallucination refers to plausible but incorrect content generated as if it were fact."),
        (
            "A team wants a language model to perform a task with only a brief instruction and no task-specific training. This is best described as:",
            ["Zero-shot learning", "Unsupervised clustering", "Linear regression", "Gradient boosting"],
            0,
            "Zero-shot learning asks the model to perform a task without task-specific examples."),
        (
            "In a transformer model, attention is primarily used to:",
            ["Weight the importance of different tokens when producing output", "Reduce the vocabulary size", "Copy the input exactly", "Optimize the loss function in a single step"],
            0,
            "Attention helps the model determine which input tokens are most relevant at each step."),
    ],
    "Domain 3: Applications of AWS AI Services": [
        (
            "A company needs to extract tables, key-value data, and line items from scanned invoices in an automated workflow. Which AWS service is the best fit?",
            ["Amazon Textract", "Amazon Polly", "Amazon Lex", "Amazon Comprehend"],
            0,
            "Textract is designed to extract structured information from documents and forms."),
        (
            "A call center plans to build an IVR and conversational bot with speech input. Which service provides the conversational interface?",
            ["Amazon Lex", "Amazon Forecast", "Amazon GuardDuty", "Amazon Translate"],
            0,
            "Lex is AWS's service for building conversational interfaces and chatbots."),
        (
            "An enterprise wants to search across thousands of product manuals and policy documents using natural-language questions. The best service is:",
            ["Amazon Kendra", "Amazon Bedrock", "Amazon Rekognition", "Amazon Personalize"],
            0,
            "Kendra is optimized for enterprise search over documents using ML-powered relevance."),
        (
            "A company needs to detect unusual behavior in metrics for inventory sensors and forecast maintenance issues. Which service is most appropriate?",
            ["Amazon Lookout for Equipment or Lookout for Metrics", "Amazon Polly", "Amazon Connect", "Amazon SageMaker Ground Truth"],
            0,
            "Lookout services are designed to detect anomalies and monitor operational health using ML."),
        (
            "A startup wants to access foundation models through a managed API without building and hosting models themselves. Which AWS service should they use?",
            ["Amazon Bedrock", "Amazon S3", "Amazon Athena", "Amazon Route 53"],
            0,
            "Bedrock offers managed access to foundation models through APIs."),
        (
            "A healthcare team wants to identify anomalies in CT scans and prior patient records. Which combination best aligns with AWS AI capabilities?",
            ["Medical image services with ML-powered analysis and document extraction", "Only Amazon EC2 and RDS", "AWS WAF and CloudFront", "Simple email notifications"],
            0,
            "AWS AI services can support medical workflows with image analysis and document understanding."),
    ],
    "Domain 4: Guidelines for Responsible AI": [
        (
            "A team deploys an AI system that downgrades certain demographic groups in loan eligibility decisions. This is a classic example of:",
            ["Algorithmic bias", "Model drift", "Feature scaling", "Overfitting"],
            0,
            "Algorithmic bias occurs when the system systematically disadvantages specific groups."),
        (
            "A lender wants to understand why a model rejected a loan application. Which responsible AI pillar is most relevant?",
            ["Explainability", "Latency optimization", "Data compression", "Prompt tuning"],
            0,
            "Explainability helps stakeholders understand and justify model decisions."),
        (
            "A model used in hiring has disparities across protected groups. The best next step is to:",
            ["Evaluate fairness metrics and review training data for representation and proxy features", "Immediately retrain with more data and ignore fairness", "Delete the model and replace it with a random classifier", "Disable all logging to reduce risk"],
            0,
            "Responsible AI requires fairness review, data inspection, and mitigation of bias."),
        (
            "A company is preparing a high-impact AI system for production. The most important governance step is:",
            ["Conduct an impact assessment and define accountability and monitoring requirements", "Deploy the system without documentation to move faster", "Use only public benchmarks and ignore internal review", "Require no human oversight for critical decisions"],
            0,
            "Governance and impact assessment reduce risk before deployment."),
        (
            "An organization wants to reduce harmful outputs from a generative model in a customer-facing application. Which capability is most directly aligned with this requirement?",
            ["Guardrails and content filtering", "Hyperparameter tuning only", "Model quantization alone", "Elastic load balancing"],
            0,
            "Guardrails help prevent unsafe, harmful, or sensitive output."),
        (
            "A model used for customer support performs well initially but degrades after a change in customer language patterns. This is best described as:",
            ["Model drift", "Gradient descent failure", "Prompt engineering issue", "Data serialization bug"],
            0,
            "Model drift is a performance shift caused by changes in input data distribution over time."),
    ],
    "Domain 5: Security, Compliance, and Operations": [
        (
            "A team is setting up AWS Bedrock for production and needs strong auditability for all API calls. Which AWS service should be enabled?",
            ["AWS CloudTrail", "Amazon SES", "Amazon Athena", "Amazon QuickSight"],
            0,
            "CloudTrail logs and audits AWS API activity for security and compliance review."),
        (
            "A company wants to restrict Bedrock access to private network paths and control traffic. The most appropriate design is:",
            ["Use VPC endpoints and security groups", "Expose the model publicly on the internet", "Use only a public S3 bucket", "Disable IAM policies"],
            0,
            "Private networking with VPC endpoints reduces exposure and supports secure access patterns."),
        (
            "A security team wants to protect secrets used by an AI application. The correct AWS service is:",
            ["AWS Secrets Manager", "Amazon CloudWatch Logs", "Amazon GuardDuty", "Amazon S3 Glacier"],
            0,
            "Secrets Manager is built for storing and rotating sensitive credentials securely."),
        (
            "A business requires encryption with explicit ownership and rotation control for keys used in AI services. The best option is:",
            ["AWS KMS customer-managed keys", "Default AWS-managed keys only", "Public key sharing", "No encryption"],
            0,
            "Customer-managed keys provide a stronger control model for encryption and key lifecycle operations."),
        (
            "An application expects bursts of usage but needs to prevent abuse and unnecessary cost. The right operational control is:",
            ["Rate limiting and quotas", "Deleting all CloudWatch alarms", "Allowing infinite public access", "Disabling IAM"],
            0,
            "Rate limits and quotas protect the system from abuse and resource exhaustion."),
        (
            "A production deployment must recover quickly after a regional outage. The best strategy is:",
            ["Multi-region redundancy and automated failover", "Single-region deployment with no backup", "Manual recovery only after outage", "Disable logging until recovery"],
            0,
            "Disaster recovery depends on redundant capacity and tested failover procedures."),
    ],
}


def build_advanced_question_bank():
    """Create a richer exam-style bank with domain-specific harder scenarios."""
    advanced_bank = {}
    for domain_name, questions in DOMAINS_DATA.items():
        generated = []
        for q_text, opts, correct_idx, explanation in questions:
            generated.append({
                "question": q_text,
                "options": opts,
                "correct_idx": correct_idx,
                "explanation": explanation,
                "difficulty": "core",
                "domain": domain_name,
            })

        for q_text, opts, correct_idx, explanation in HARDER_QUESTION_TEMPLATES.get(domain_name, []):
            generated.append({
                "question": q_text,
                "options": opts,
                "correct_idx": correct_idx,
                "explanation": explanation,
                "difficulty": "hard",
                "domain": domain_name,
            })

        advanced_bank[domain_name] = generated

    return advanced_bank


@st.cache_data
def prepare_questions():
    """Prepare a larger AWS-style question bank with shuffled options and harder scenario-based questions."""
    all_questions = {}
    base_bank = build_advanced_question_bank()

    for domain_name, questions in base_bank.items():
        domain_list = []
        for q in questions:
            opts = q["options"]
            correct_idx = q["correct_idx"]
            options_with_indices = list(enumerate(opts))
            random.seed(hash(f"{domain_name}:{q['question']}"))
            random.shuffle(options_with_indices)

            shuffled_options = [opt for _, opt in options_with_indices]
            new_correct_idx = next(idx for idx, (orig_idx, _) in enumerate(options_with_indices) if orig_idx == correct_idx)

            domain_list.append({
                "question": q["question"],
                "options": shuffled_options,
                "correct_idx": new_correct_idx,
                "explanation": q["explanation"],
                "difficulty": q.get("difficulty", "core"),
                "domain": domain_name,
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

if "exam_started_at" not in st.session_state:
    st.session_state.exam_started_at = None

if "exam_duration_seconds" not in st.session_state:
    st.session_state.exam_duration_seconds = 90 * 60

if "exam_time_remaining" not in st.session_state:
    st.session_state.exam_time_remaining = st.session_state.exam_duration_seconds

if "exam_submitted" not in st.session_state:
    st.session_state.exam_submitted = False


def start_full_exam():
    """Reset and start a full timed exam."""
    st.session_state.quiz_all_questions = create_mixed_quiz()
    st.session_state.quiz_total_correct = 0
    st.session_state.quiz_answered = {}
    st.session_state.q_index = 0
    st.session_state.exam_started_at = time.monotonic()
    st.session_state.exam_submitted = False
    st.session_state.exam_time_remaining = st.session_state.exam_duration_seconds


def get_exam_time_remaining():
    """Return remaining exam time in seconds, auto-updating from start timestamp."""
    if st.session_state.get("exam_started_at") is None:
        return st.session_state.get("exam_time_remaining", st.session_state.exam_duration_seconds)

    if st.session_state.get("exam_submitted"):
        return st.session_state.get("exam_time_remaining", 0)

    elapsed = int(time.monotonic() - st.session_state.exam_started_at)
    remaining = max(0, st.session_state.exam_duration_seconds - elapsed)
    st.session_state.exam_time_remaining = remaining
    return remaining


def submit_full_exam():
    """Finalize the exam and lock the quiz."""
    st.session_state.exam_submitted = True
    st.session_state.exam_time_remaining = 0


# Helper function to create mixed quiz questions from all domains
# Real AWS exam style: 65 questions total, sampled across all five domains
# The ratios below approximate the AWS AI Practitioner blueprint more closely than pure random mixing.
def create_mixed_quiz():
    """Create a realistic 65-question mixed exam across all domains."""
    domain_weights = {
        "Domain 1: Fundamentals of AI and ML": 11,
        "Domain 2: Fundamentals of Generative AI": 11,
        "Domain 3: Applications of AWS AI Services": 18,
        "Domain 4: Guidelines for Responsible AI": 10,
        "Domain 5: Security, Compliance, and Operations": 15,
    }

    exam_questions = []
    for domain_name, questions in questions_bank.items():
        weight = domain_weights.get(domain_name, 0)
        chosen = random.sample(questions, min(len(questions), weight))
        for q in chosen:
            q_with_domain = q.copy()
            q_with_domain["domain"] = domain_name
            exam_questions.append(q_with_domain)

    random.shuffle(exam_questions)

    if len(exam_questions) > 65:
        exam_questions = exam_questions[:65]
    elif len(exam_questions) < 65:
        for domain_name, questions in questions_bank.items():
            if len(exam_questions) >= 65:
                break
            for q in questions:
                if len(exam_questions) >= 65:
                    break
                q_with_domain = q.copy()
                q_with_domain["domain"] = domain_name
                exam_questions.append(q_with_domain)
        random.shuffle(exam_questions)
        exam_questions = exam_questions[:65]

    return exam_questions


# Callback functions for sidebar changes
def update_domain():
    st.session_state.q_index = 0


def update_mode():
    st.session_state.q_index = 0

    if st.session_state.get("quiz_mode") is True:
        start_full_exam()


# 6. UI Layout & Sidebar Navigation
st.title("☁️ AWS Certified AI Practitioner Exam Simulator")
st.caption("Enhanced Learning Platform • 100+ Questions per Domain • Real Exam-Style Questions")

# Sidebar Controls
with st.sidebar:
    st.header("📋 Navigation & Settings")

    mode = st.radio(
        "Select Mode:",
        ["📖 Practice Mode", "🎯 Quiz Mode", "📊 Performance"],
        index=0,
        on_change=update_mode,
    )

    if mode == "📖 Practice Mode":
        st.session_state.quiz_mode = False
    elif mode == "🎯 Quiz Mode":
        st.session_state.quiz_mode = True
        if not st.session_state.quiz_all_questions or st.session_state.get("exam_started_at") is None:
            start_full_exam()
    else:
        st.session_state.quiz_mode = None

    st.divider()

    if st.session_state.quiz_mode is not True:
        domain_list = list(questions_bank.keys())
        current_idx = domain_list.index(st.session_state.current_domain) if st.session_state.current_domain in domain_list else 0

        selected_domain = st.selectbox(
            "Select Domain:",
            domain_list,
            index=current_idx,
            on_change=update_domain,
        )

        st.session_state.current_domain = selected_domain

        st.divider()

        num_questions = len(questions_bank[selected_domain])
        st.metric("Questions in Domain", num_questions)

        if selected_domain in st.session_state.quiz_scores:
            score = st.session_state.quiz_scores[selected_domain]
            st.metric("Quiz Score", f"{score['correct']}/{score['total']}", f"{int(score['correct']/score['total']*100)}%")
    else:
        st.write("### 🎯 Full Exam Quiz")
        st.write("Questions from **all 5 domains** mixed together")
        st.divider()
        st.metric("Total Questions", 65)
        remaining = get_exam_time_remaining()
        minutes, seconds = divmod(remaining, 60)
        st.metric("Time Remaining", f"{minutes:02d}:{seconds:02d}")
        st.metric("Current Score", f"{st.session_state.quiz_total_correct}/{len(st.session_state.quiz_all_questions)}")

# Check if Performance Mode
if st.session_state.quiz_mode is None:
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

else:
    if st.session_state.quiz_mode is False:
        selected_domain = st.session_state.current_domain
        q_index = st.session_state.q_index
        num_questions = len(questions_bank[selected_domain])

        if q_index >= num_questions:
            st.session_state.q_index = 0
            q_index = 0

        current_q = questions_bank[selected_domain][q_index]

        st.subheader(f"{selected_domain}")

        col_progress = st.columns([3, 1])
        with col_progress[0]:
            st.progress((q_index + 1) / num_questions)
        with col_progress[1]:
            st.write(f"**{q_index + 1}/{num_questions}**")

        st.markdown(f"### {current_q['question']}")

        user_choice = st.radio(
            "Select the best answer:",
            current_q['options'],
            index=None,
            key=f"radio_{selected_domain}_{q_index}",
        )

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

        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            if st.button("⬅️ Previous", use_container_width=True, disabled=(q_index == 0), key="prev_practice"):
                st.session_state.q_index -= 1
                st.rerun()
        with col2:
            st.write("")
        with col3:
            if st.button("Next ➡️", use_container_width=True, disabled=(q_index == num_questions - 1), key="next_practice"):
                st.session_state.q_index += 1
                st.rerun()

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

    else:
        q_index = st.session_state.q_index
        all_questions = st.session_state.quiz_all_questions

        if not all_questions:
            all_questions = create_mixed_quiz()
            st.session_state.quiz_all_questions = all_questions

        if st.session_state.get("exam_submitted"):
            st.subheader("✅ Exam Submitted")
            final_score = st.session_state.quiz_total_correct
            total_questions = len(all_questions)
            final_pct = int((final_score / total_questions) * 100) if total_questions else 0
            st.success(f"Your final score: **{final_score}/{total_questions}** ({final_pct}%)")
            st.info("The exam timer has expired or you submitted the exam. Your results are locked in.")
            st.stop()

        remaining = get_exam_time_remaining()
        if remaining <= 0 and not st.session_state.get("exam_submitted"):
            submit_full_exam()
            st.rerun()

        num_questions = len(all_questions)

        if q_index >= num_questions:
            st.session_state.q_index = 0
            q_index = 0

        current_q = all_questions[q_index]

        st.subheader("🎯 Full Exam Quiz - Mixed Questions")
        st.caption(f"from {current_q.get('domain', 'Unknown Domain')}")

        col_progress = st.columns([3, 1])
        with col_progress[0]:
            st.progress((q_index + 1) / num_questions)
        with col_progress[1]:
            st.write(f"**{q_index + 1}/{num_questions}**")

        remaining = get_exam_time_remaining()
        minutes, seconds = divmod(remaining, 60)
        st.caption(f"⏱️ Time left: {minutes:02d}:{seconds:02d}")

        st.markdown(f"### {current_q['question']}")

        user_choice = st.radio(
            "Select the best answer:",
            current_q['options'],
            index=None,
            key=f"radio_quiz_{q_index}",
        )

        if user_choice is not None:
            selected_idx = current_q['options'].index(user_choice)
            is_correct = selected_idx == current_q['correct_idx']

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

        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            if st.button("⬅️ Previous", use_container_width=True, disabled=(q_index == 0), key="prev_quiz"):
                st.session_state.q_index -= 1
                st.rerun()
        with col2:
            st.write(f"Score: **{st.session_state.quiz_total_correct}/{q_index + 1}")
        with col3:
            if st.button("Submit Exam", use_container_width=True, key="submit_exam"):
                submit_full_exam()
                st.rerun()

        if q_index == num_questions - 1:
            st.write("---")
            st.success(f"✅ This is the final question. Submit the exam to finish and lock in your score.")
            if st.button("Finish Exam Now", key="finish_exam_now"):
                submit_full_exam()
                st.rerun()

        if q_index < num_questions - 1:
            if st.button("Next ➡️", use_container_width=True, key="next_quiz"):
                st.session_state.q_index += 1
                st.rerun()

        if q_index == num_questions - 1:
            st.write("---")
            st.success(f"✅ Quiz Complete! Your Score: **{st.session_state.quiz_total_correct}/{num_questions}** ({int(st.session_state.quiz_total_correct/num_questions*100)}%)")
