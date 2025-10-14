PROMPT_SYSTEM = (
    "You are a medical-knowledge assistant for educational purposes only. "
    "When given a patient's symptom text, respond with: "
    "1) probable conditions, 2) recommended next steps, and "
    "3) an explicit disclaimer. Keep it short and conservative."
)

PROMPT_TEMPLATE = (
    "Patient symptoms:\n\n{symptoms}\n\n"
    "Respond with:\n"
    "Probable conditions:\n"
    "Recommendations:\n"
    "Disclaimer:\n"
)

def build_prompt(symptom_text: str):
    return [
        {
            "role": "system",
            "content": (
                "You are a helpful healthcare assistant that provides probable conditions "
                "and recommendations based on symptoms. You must always respond in valid JSON format "
                "with exactly three keys: 'probable_conditions', 'recommendations', and 'disclaimer'."
            ),
        },
        {
            "role": "user",
            "content": (
                f"User symptoms: {symptom_text}\n\n"
                "Return only JSON, like this:\n"
                "{\n"
                '  \"probable_conditions\": \"Pharyngitis, Tonsillitis\",\n'
                '  \"recommendations\": \"Rest, stay hydrated, use salt-water gargle.\",\n'
                '  \"disclaimer\": \"Educational purposes only; not a substitute for a medical consultation.\"\n'
                "}"
            ),
        },
    ]

