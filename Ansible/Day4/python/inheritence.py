#!/usr/bin/python


class MediaPlayer:
    
    
    def __init__(self):
     
        print('Media Player Constructor');
        print('########################');
        
    def play(self):
   
        print('Media Player is playing');
        print('########################');

class VideoPlayer(MediaPlayer):

    def __init__(self):
        MediaPlayer.__init__(self);
        
        print('Video Player Constructor');
        print('########################');    

    def play(self):
        MediaPlayer.play(self);
        
        print('Video Player is playing');
        print('########################');
        
    

   

videoPlayer= VideoPlayer();
videoPlayer.play();