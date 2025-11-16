import openai
import yaml

# Load the secrets.yaml file to get the OpenAI API key
with open("/secrets.yaml", 'r', encoding='utf-8') as f:
    secrets = yaml.safe_load(f)

# Get the OpenAI API key from secrets.yaml
openai.api_key = secrets.get('openai_api_key')

# Path to your Home Assistant configuration file (update this as needed)
config_path = "S:/config/configuration.yaml"

# Read the configuration file
with open(config_path, 'r', encoding='utf-8') as file:
    config_data = file.read()

# Request validation and fix suggestions from OpenAI
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Validate and suggest fixes for this YAML configuration: {config_data}",
    max_tokens=500
)

# Print OpenAI's suggestions to fix the configuration
suggestions = response.choices[0].text.strip()
print("AI's suggestions to fix your configuration:")
print(suggestions)
