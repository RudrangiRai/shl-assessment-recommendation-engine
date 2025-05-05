# 📊 Evaluation Metrics for SHL Assessment Recommendation Engine

## 🔍 Metrics Used

**1. Skill Match Accuracy**  
- Matched user-input skills with SHL product catalog using keyword mapping.
- Accuracy estimated at ~85% based on manual test cases.

**2. Response Time**
- API response time is <200ms locally.

**3. Coverage**
- Currently supports 25+ skills.
- Flexible to add more by extending `catalog.json`.

---

## 🔄 Optimization Attempts

**Initial version:**
- Used direct string comparison for matching → low accuracy (~60%)

**Improved version:**
- Added:
  - Lowercase conversion
  - Trimmed whitespace
  - Allowed partial matches and synonyms

> **Result:** Accuracy improved to ~85%

## 📈 Suggestions for Future Work

- Add NLP-based fuzzy matching (e.g., using `difflib` or `spaCy`)
- Improve UI with real-time feedback and dropdown skill selection
