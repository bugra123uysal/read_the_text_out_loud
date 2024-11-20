import pyttsx3
""" motoru başlatır """
engine=pyttsx3.init()

text="hello how are you"
""" metini sesli okur """
engine.say(text)

""" okumanın bitmesini bekler  """
engine.runAndWait()

