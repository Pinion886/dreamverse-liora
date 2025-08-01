import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_persona(name, persona):
    """
    Generates images, captions, and scripts for Dreamverse models
    """
    prompt = f"Create a seductive social media script for model {name} with persona: {persona}"
    script = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=200
    ).choices[0].text.strip()

    # Placeholder for Level 3 image generation (Higgsfield integration later)
    image_path = f"output/{name}_image.png"
    os.makedirs("output", exist_ok=True)
    with open(image_path, "w") as f:
        f.write("IMAGE_GENERATED")

    print(f"Persona for {name} generated.")
    return {"image": image_path, "script": script}
