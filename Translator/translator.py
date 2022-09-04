from translate import Translator
translator= Translator(from_lang="English",to_lang="Hindi")
translation = translator.translate("hello")
print(translation)