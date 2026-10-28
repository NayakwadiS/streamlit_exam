# AWS AI Practitioner Exam - Study Guide & Key Concepts

## Domain 1: Fundamentals of AI and ML

### Key Concepts

**Regression vs Classification**
- Regression: Predict continuous values (price, temperature, score)
- Classification: Predict discrete categories (spam/not spam, animal type)
- Example: Predicting house price = Regression; Predicting if email is spam = Classification

**Supervised vs Unsupervised Learning**
- Supervised: Model trained on labeled data (input-output pairs)
  - Examples: Email classification, image labeling, fraud detection
  - Requires labeled training data
- Unsupervised: Find patterns in unlabeled data
  - Examples: Customer segmentation, anomaly detection
  - No pre-existing labels

**Overfitting vs Underfitting**
- Overfitting: Model memorizes training data, fails on new data
  - High accuracy on training, low on testing
  - Solutions: Dropout, regularization, simplify model
- Underfitting: Model too simple to capture patterns
  - Low accuracy on both training and testing
  - Solutions: Use more complex model, add features

**Bias-Variance Tradeoff**
- High Bias: Model is too simple (underfitting)
- High Variance: Model is too complex (overfitting)
- Goal: Balance both for good generalization

**Evaluation Metrics**
- Accuracy: Overall correctness (prone to imbalance issues)
- Precision: TP/(TP+FP) - Of predicted positives, how many are correct?
- Recall: TP/(TP+FN) - Of actual positives, how many did we find?
- F1-Score: Harmonic mean of precision and recall (best for imbalanced data)

**Regularization Techniques**
- L1 (Lasso): Can zero out features (feature selection)
- L2 (Ridge): Reduces but doesn't eliminate features
- Dropout: Randomly disables neurons during training
- Early Stopping: Stop training when validation error increases

---

## Domain 2: Fundamentals of Generative AI

### Key Concepts

**Temperature & Sampling**
- Temperature: Controls randomness in token selection
  - Low (0.1-0.3): Deterministic, factual, predictable
  - High (0.7-1.0): Creative, varied, unpredictable
- Top-P (Nucleus Sampling): Sample from top tokens until cumulative probability reaches P
- Top-K: Sample from K most likely next tokens

**Foundation Models**
- Large language models pre-trained on diverse data
- Can be fine-tuned for specific tasks
- Base models like Claude, GPT, Llama, Falcon
- AWS: Amazon Bedrock provides access via APIs

**Retrieval-Augmented Generation (RAG)**
- Combines retrieval with generation
- Fetches relevant documents, then generates response with context
- Solves: Outdated info, hallucinations, factual grounding
- Process: User Query → Retrieve → Context + Prompt → Generate

**Fine-Tuning vs Pre-training**
- Pre-training: Train model on large diverse data (expensive, time-consuming)
- Fine-tuning: Adapt pre-trained model to specific task (faster, cheaper)
- Most use cases require fine-tuning, not pre-training

**Prompt Engineering**
- Art of crafting inputs to guide model outputs
- Techniques:
  - Few-shot learning: Provide examples in prompt
  - Zero-shot: Task description only, no examples
  - Chain-of-thought: Ask model to reason step-by-step
  - Prompt chaining: Break complex tasks into sequential prompts

**Hallucinations**
- Model confidently stating false information as fact
- Causes: Training data gaps, lack of grounding
- Mitigation: RAG, fact-checking, low temperature

**Transformers & Attention**
- Attention: Mechanism to weight relationships between tokens
- Self-attention: Each token attends to all other tokens
- Enables parallel processing and long-range dependencies

---

## Domain 3: Applications of AWS AI Services

### AWS Service Overview

**Document Analysis**
- **Amazon Textract**: Extract text, tables, forms from documents
  - Use: Invoice processing, document archival, form automation

**Conversational AI**
- **Amazon Lex**: Build chatbots that understand intent
  - Use: Customer support, appointment scheduling, FAQs
- **Amazon Comprehend**: NLP (sentiment, entities, key phrases)
  - Use: Customer feedback analysis, content moderation

**Speech Services**
- **Amazon Transcribe**: Speech-to-text
  - Use: Call transcription, meeting notes, accessibility
- **Amazon Polly**: Text-to-speech
  - Use: Voiceovers, accessibility features, customer notifications

**Computer Vision**
- **Amazon Rekognition**: Image and video analysis
  - Features: Object detection, face recognition, content moderation
  - Use: Security, content moderation, accessibility

**Recommendation & Forecasting**
- **Amazon Personalize**: Personalized recommendations
  - Use: E-commerce, streaming, content discovery
- **Amazon Forecast**: Time-series forecasting
  - Use: Demand forecasting, capacity planning, sales prediction

**Search**
- **Amazon Kendra**: Intelligent document search
  - Use: Enterprise search, knowledge bases, documentation search

**ML Platforms**
- **Amazon SageMaker**: End-to-end ML platform for custom models
- **Amazon Bedrock**: Access to foundation models via APIs
- **Amazon Ground Truth**: Data labeling at scale

**Anomaly Detection**
- **Amazon Lookout for Equipment**: Equipment anomalies
- **Amazon Lookout for Metrics**: Unusual metric behavior

---

## Domain 4: Guidelines for Responsible AI

### Key Pillars of Responsible AI

**1. Fairness**
- Model behaves equitably across all demographics
- Requires: Balanced training data, fairness audits, bias testing
- Test: Performance across protected attributes (gender, race, age, etc.)

**2. Explainability**
- Humans understand how AI made a decision
- Methods: Feature importance, SHAP values, decision trees
- Goal: Transparency and trust

**3. Robustness**
- Model performs reliably across conditions
- Requires: Edge case testing, adversarial testing
- Prevent: Adversarial attacks, out-of-distribution failures

**4. Governance**
- Policies, oversight, and accountability
- Includes: Model registry, approval workflows, documentation
- Requires: Clear responsibility and decision rights

### Responsible AI Practices

**Guardrails for Amazon Bedrock**
- Content filtering to prevent harmful outputs
- PII redaction to protect sensitive information
- Toxicity detection
- Applied before model sees prompt (input) and after (output)

**Model Monitoring Post-Deployment**
- Track: Accuracy, fairness metrics, latency
- Detect: Model drift, data drift, performance degradation
- Respond: Retrain, alert humans, take action

**Data Management**
- Audit training data for bias
- Ensure diverse representation
- Remove duplicates and quality issues
- Protect sensitive information

**Impact Assessments**
- Evaluate potential harms before deployment
- Consider: Accuracy impacts, fairness implications, edge cases
- Document: Risks and mitigation strategies

---

## Domain 5: Security, Compliance, and Operations

### AWS Security Services

**Logging & Monitoring**
- **AWS CloudTrail**: Comprehensive API activity logs
  - Records: Who did what, when, where (user identity, source IP, timestamp)
  - Use: Audit, compliance, security investigation
- **Amazon CloudWatch**: Metrics, logs, and alarms
  - Use: Application monitoring, performance analysis

**Access Control**
- **AWS IAM**: Identity and Access Management
  - Features: Policies, roles, MFA, fine-grained permissions
  - Best practice: Least privilege principle

**Threat Detection**
- **Amazon GuardDuty**: Threat detection using ML
  - Monitors: CloudTrail, VPC Flow Logs, DNS logs
  - Detects: Unusual API calls, unauthorized access, malware

**Encryption**
- **AWS KMS**: Key Management Service
  - Types: AWS-managed or customer-managed keys
  - Best practice: Use customer-managed keys for sensitive data
- **TLS/SSL**: In-transit encryption
- **Encryption at rest**: Protect stored data

**Compliance**
- **AWS Compliance Program**: HIPAA, PCI-DSS, SOC 2, GDPR, etc.
- **Bedrock Privacy**: Customer data NOT used to train models
- **Data Isolation**: Strict separation of customer data

### Operational Excellence

**Capacity Planning**
- **Provisioned Throughput**: Guaranteed dedicated capacity
  - Measured in tokens per minute (TPM)
  - For mission-critical applications
- **On-Demand Capacity**: Pay per use, variable cost
  - For variable workloads

**Cost Management**
- **AWS Cost Explorer**: Track and analyze spending
- **AWS Budgets**: Set alerts for spending limits
- **Savings Plans**: Discount for commitment

**Disaster Recovery**
- Multi-region redundancy
- Automated failover
- Regular backups
- Recovery time objective (RTO) and recovery point objective (RPO)

**Incident Response**
- Document incidents
- Root cause analysis
- Implement preventive measures
- Post-incident review

### Data Privacy with AWS Bedrock

**Key Points**
- ✅ Customer inputs NOT used to train or improve models
- ✅ Data stored in customer's AWS account
- ✅ Encryption available with AWS KMS
- ✅ Compliance with data residency requirements
- ❌ Data NOT shared with model providers
- ❌ Data NOT added to public pools
- ❌ Data NOT shared for 24 hours (no sharing at all)

---

## Quick Reference: Common Question Patterns

### Pattern 1: Service Selection
**Format:** "A [scenario] needs [capability]. Which service?"
**Approach:** Match capability to AWS service
**Example:** Extract text from documents → Amazon Textract

### Pattern 2: Configuration/Parameter
**Format:** "To [achieve goal], which parameter?"
**Approach:** Understand parameter's purpose
**Example:** Make model more creative → Increase temperature

### Pattern 3: Best Practice
**Format:** "A team should [action] to [achieve goal]"
**Approach:** Identify responsible/secure approach
**Example:** Prevent hallucinations → Use RAG

### Pattern 4: Technical Concept
**Format:** "What is/does [concept]?"
**Approach:** Understand fundamental concepts
**Example:** Overfitting occurs when...

---

## Pro Tips for Passing the Exam

1. **Understand the "Why"**
   - Not just what is correct, but why others are wrong
   - Read explanations thoroughly

2. **Focus on AWS Services**
   - Know what each service does (Bedrock, Textract, Lex, etc.)
   - Know when to use each one
   - Domain 3 has 20+ service combinations

3. **Real-World Scenarios**
   - Think about practical use cases
   - Consider constraints (cost, compliance, time)
   - Questions are scenario-based

4. **Responsible AI Matters**
   - Know fairness, explainability, governance
   - Recognize bias and mitigation strategies
   - Domain 4 is increasingly important

5. **Security is Critical**
   - CloudTrail, IAM, encryption, compliance
   - Data privacy with Bedrock
   - These are always relevant

---

## Exam Format (Expected)

- **Duration:** 2 hours (120 minutes)
- **Question Count:** ~65-75 multiple choice
- **Passing Score:** ~70% (varies by exam)
- **Format:** 
  - Can select 1 answer per question
  - Scenario-based questions
  - May include "choose the best" questions (all could partially work)

## Study Timeline

- **2 weeks before:** Practice Mode for all domains
- **1 week before:** Quiz Mode practice
- **3 days before:** Mixed review, identify weak areas
- **1 day before:** Rest, light review only
- **Day of:** Get good sleep, eat well, arrive early

---

**Good luck with your AWS Certified AI Practitioner Exam! 🚀**

