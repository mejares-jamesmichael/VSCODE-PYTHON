from googletrans import Translator

translator = Translator()
userText = input('Enter text: ')
nativeLang = input('Enter language: ')
foreignLang = input('Translate to: ')

translation = translator.translate (userText, src=nativeLang, dest=foreignLang)
print(f'Translated text: {translation.text}')