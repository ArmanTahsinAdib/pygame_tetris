import json
import os

class HighScores:
    def __init__(self, filename="highscores.json"):
        # Get the directory where the script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Create full path for highscores.json in the same directory as the script
        self.filename = os.path.join(script_dir, filename)
        self.scores = self.load_scores()

    def load_scores(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    # Convert loaded scores to integers
                    scores = [int(score) for score in json.load(f)]
                    return sorted(list(set(scores)), reverse=True)  # Remove duplicates and sort
            except:
                return []
        return []

    def get_highest_score(self):
        return self.scores[0] if self.scores else 0  # Return the highest score or 0 if no scores

    def save_scores(self):
        with open(self.filename, 'w') as f:
            json.dump(self.scores, f)

    def add_score(self, score):
        score = int(score)  # Ensure score is an integer
        if score not in self.scores:  # Only add if score isn't already in the list
            self.scores.append(score)
            self.scores = sorted(list(set(self.scores)), reverse=True)  # Remove duplicates and sort
            self.scores = self.scores[:5]  # Keep only top 5 scores
            self.save_scores()

    def get_top_scores(self):
        return self.scores[:5]