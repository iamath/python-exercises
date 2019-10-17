from pygame import mixer

mixer.init()
mixer.music.load('./media/music.mp3')
mixer.music.play()
input('Press enter to stop...')
