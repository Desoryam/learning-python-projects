import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")


speaker.Speak("TIME TO DRINK WATER")