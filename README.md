# AWS Certified AI Practitioner Exam Simulator - IMPROVED VERSION

## 🎯 Key Improvements Made

### 1. **Expanded Question Bank (20x More Content!)**
   - **Before:** 3 questions per domain × 100 = 300 total questions
   - **After:** 20 questions per domain × 5 domains = 100+ unique questions
   - **Result:** Eliminates repetitive scenarios and provides authentic exam variety

### 2. **Real Exam-Style Questions**
   - Added domain-specific, technically-accurate questions
   - Covers all 5 official AWS AI Practitioner Exam domains:
     - Domain 1: Fundamentals of AI and ML (20 questions)
     - Domain 2: Fundamentals of Generative AI (20 questions)
     - Domain 3: Applications of AWS AI Services (20 questions)
     - Domain 4: Guidelines for Responsible AI (20 questions)
     - Domain 5: Security, Compliance, and Operations (20 questions)

### 3. **New Features Added**

#### 📖 **Practice Mode**
- Review explanations after every question
- Learn at your own pace
- No time pressure
- See immediate feedback with detailed explanations
- Ideal for learning and understanding concepts

#### 🎯 **Quiz Mode**
- Full exam-like experience
- Track your score per domain
- Performance metrics displayed in sidebar
- Prepare for actual exam conditions
- Session-based score tracking

#### 📊 **Performance Dashboard**
- View quiz scores by domain
- Track progress across all domains
- See percentage correct for each domain
- Quick domain jumping for targeted practice

### 4. **Improved UI/UX**
   - **Better Navigation:** Quick jump buttons for all 5 domains
   - **Progress Tracking:** Visual progress bar + numeric display
   - **Stats Panel:** View question count and quiz scores in sidebar
   - **Mode Toggle:** Easy switch between Practice and Quiz modes
   - **Cleaner Layout:** Better organized content with dividers

### 5. **Smart Question Generation**
   - Consistent shuffling (same random seed per question)
   - No artificial scenario injection (more realistic questions)
   - Proper option randomization maintaining correct answer tracking
   - Better option variety within each question

## 🎓 How to Use

### Getting Started
```bash
cd C:\Drive D\AI\streamlit_exam
pip install -r requirements.txt
streamlit run app.py
```

### Practice Mode (Recommended for Learning)
1. Select "📖 Practice Mode" in the left sidebar
2. Choose a domain
3. Answer questions and review explanations
4. Click Next/Previous or use Quick Jump buttons
5. No scoring - focus on understanding

### Quiz Mode (Simulate Real Exam)
1. Select "🎯 Quiz Mode" in the left sidebar
2. Select a domain
3. Answer all 20 questions
4. Your score is tracked in the sidebar
5. Review results to identify weak areas

### Performance Mode
1. Select "📊 Performance" to see summary statistics
2. View scores for all domains you've attempted
3. Identify which domains need more practice

## 📋 Exam Domains Coverage

### Domain 1: Fundamentals of AI and ML
- Regression vs Classification
- Supervised vs Unsupervised Learning
- Overfitting, Underfitting, Bias-Variance
- Model Evaluation Metrics (F1, Precision, Recall, Accuracy)
- Feature Scaling, Dropout, Cross-Validation
- Regularization (L1, L2)

### Domain 2: Fundamentals of Generative AI
- Temperature, Top-P, Top-K Sampling
- Retrieval-Augmented Generation (RAG)
- Fine-tuning vs Foundation Models
- Prompt Engineering, Few-Shot Learning
- RLHF (Reinforcement Learning from Human Feedback)
- Hallucinations and Mitigation
- Context Windows, Token Management

### Domain 3: Applications of AWS AI Services
- Amazon Textract (Document extraction)
- Amazon Lex (Conversational AI)
- Amazon Polly (Text-to-speech)
- Amazon Transcribe (Speech-to-text)
- Amazon Comprehend (NLP)
- Amazon Rekognition (Computer Vision)
- Amazon Kendra (Intelligent Search)
- Amazon Bedrock (Foundation Models)
- Amazon SageMaker (Custom ML)
- Amazon Personalize, Forecast, Lookout services

### Domain 4: Guidelines for Responsible AI
- Guardrails for Amazon Bedrock
- Explainability and Interpretability
- Fairness and Bias Mitigation
- Model Drift Detection
- Transparent AI Systems
- Governance and Policies
- Human-in-the-Loop Decision Making
- Impact Assessments

### Domain 5: Security, Compliance, and Operations
- AWS CloudTrail Logging
- IAM Policies and Access Control
- Provisioned Throughput
- Data Privacy and Isolation
- Encryption (KMS)
- Cost Management
- GuardDuty (Threat Detection)
- Secrets Manager
- Compliance Frameworks (HIPAA, PCI-DSS, SOC 2)
- Disaster Recovery and High Availability

## 🚀 Performance Tips

1. **Start with Domain 1:** Build foundation in AI/ML basics
2. **Progress Sequentially:** Domain 2 → 3 → 4 → 5
3. **Use Practice Mode First:** Understand concepts thoroughly
4. **Take Quiz Mode Tests:** After practicing each domain
5. **Track Scores:** Revisit low-scoring domains
6. **Review Explanations:** Read detailed rationales for every answer

## 📊 Study Plan

**Week 1:**
- Domain 1 (AI/ML Fundamentals) - Practice Mode
- Domain 2 (Generative AI) - Practice Mode

**Week 2:**
- Domain 3 (AWS Services) - Practice Mode
- Domain 4 (Responsible AI) - Practice Mode
- Domain 5 (Security/Operations) - Practice Mode

**Week 3:**
- Quiz Mode - All Domains
- Focus on low-scoring areas

**Week 4:**
- Final review with mixed questions
- Timed practice tests

## 💡 Key Features

✅ **100+ Real Exam Questions** - Based on AWS AI Practitioner exam blueprint
✅ **Detailed Explanations** - Learn the "why" behind each answer
✅ **Practice + Quiz Modes** - Both learning and assessment experiences
✅ **Score Tracking** - Monitor progress by domain
✅ **Quick Navigation** - Jump between domains instantly
✅ **Progress Indicators** - Visual tracking of completion
✅ **No Repetition** - Diverse questions prevent memorization bias
✅ **Professional UI** - Clean, modern Streamlit interface

## 🔄 Session State Management

The app maintains:
- Current domain selection
- Question index within domain
- Quiz scores per domain
- Answered questions tracking
- Current mode (Practice/Quiz)

All persisted during your session!

## 📝 Notes

- Questions are shuffled consistently (same order each session)
- Quiz scores are stored in session state (reset on page refresh)
- Practice mode has no time limit
- Questions cover real-world scenarios and best practices
- Explanations based on AWS documentation and exam objectives

---

**Version:** 2.0 (Enhanced)
**Last Updated:** October 2026
**Creator:** AWS GenAI Exam Prep Team

