# SHL Assessment Recommendation Engine – Project Summary

**Objective:**  
To build a web-based tool that recommends SHL assessments based on user’s skills and experience level.

**Tech Stack:**  
- Backend: Python (Flask)  
- Frontend: HTML, JavaScript  
- Data: JSON catalog file  

**Approach:**  
1. Created a Flask API `/recommend` to process POST requests.
2. Read a `catalog.json` file containing SHL assessments, their skills, and experience levels.
3. On receiving user input (skills + experience), matched against catalog using:
   - Skill overlap
   - Level match
4. Returned matching results in JSON.
5. Designed a simple `index.html` to take inputs and display recommendations.
6. The project runs locally, instructions are in the README.

**How to Run:**
1. Clone or download the repo: [GitHub Repo](https://github.com/RudrangiRai/shl-assessment-recommendation-engine)
2. Open the folder in VS Code or any IDE.
3. Run the command:
   ```bash
   python app.py
