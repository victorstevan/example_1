from fer import FER
import matplotlib.pyplot as plt
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename






class Person:

    def __init__(self, probableEmotion, certainty, emoji):
        self.probableEmotion = probableEmotion
        self.certainty = certainty
        self.emoji = emoji

    def __repr__(self):
        return f'emoçao: {self.probableEmotion}, nivel de certeza: {self.certainty}, emoji: {self.emoji}'



def main():
    """Aqui que a mágica acontece"""

    Tk().withdraw()

    img = plt.imread(askopenfilename())
    detector = FER(mtcnn=True)
    emotion, score = detector.top_emotion(img)

    if(emotion == 'happy'):
        emoji = '😁'
    elif(emotion == 'angry'):
        emoji = '😡'
    elif(emotion == 'fear'):
        emoji = '😱'
    elif(emotion == 'neutral'):
        emoji = '😐'
    elif(emotion == 'surprise'):
        emoji = '😮'
    elif(emotion == 'sad'):
        emoji = '☹️'
    else:
        emoji == '🤮'
    
    a_person = Person(emotion, score, emoji)

    print(a_person)


if __name__ == '__main__':
    main()