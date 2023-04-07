from googletrans import Translator

# Replace the German text below with your own text
german_text = 'Hallo,ich bin Mustafa, wie geht es Ihnen?'

# Initialize the translator
translator = Translator(service_urls=['translate.google.com'])

# Translate the German text to English
translated_text = translator.translate(german_text, src='de', dest='en')

# Print the translated text
print(translated_text.text)