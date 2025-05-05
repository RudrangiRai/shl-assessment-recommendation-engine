from flask import Flask, request, jsonify, send_from_directory
import json
import os

app = Flask(__name__)

# Load catalog of SHL tests
with open('catalog.json') as f:
    catalog = json.load(f)

# API route for recommendation
@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    user_skills = set(skill.strip().lower() for skill in data['skills'])  # Ensure case-insensitive and strip spaces
    user_level = data['experience'].lower()  # Normalize level to lowercase

    recommendations = []

    for item in catalog:
        test_skills = set(skill.lower() for skill in item['skills'])  # Normalize skill names to lowercase
        # Check if user level is in the item's level list
        level_match = user_level in item['level']
        # Check for skills overlap
        skill_overlap = len(user_skills & test_skills)

        if level_match and skill_overlap > 0:
            recommendations.append(item)

    if len(recommendations) == 0:
        return jsonify({"message": "No matching assessments found. Try different skills or experience level."}), 200
    
    return jsonify(recommendations)

# Route to serve index.html
@app.route('/index.html')
def serve_index():
    return send_from_directory(os.getcwd(), 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
