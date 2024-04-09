
"""
შექმენით მედია ფლეიერის აპლიკაცია. განსაზღვრეთ ინტერფეისები დაკვრის, პაუზის, გაჩერების, გადახვევის და სწრაფი 
წინსვლის ფუნქციებისთვის. განახორციელეთ კლასები აუდიო პლეერისთვის, ვიდეო პლეერისთვის და სტრიმინგის პლეერისთვის. 
დარწმუნდით, რომ თითოეული მოთამაშე ახორციელებს მხოლოდ მის ფუნქციონალურ ინტერფეისებს.
მაქსიმალურად გამოიყენეთ SOLID პრინციპები!!!
"""
# Create mediaplayer1 class
class MediaPlayer1:
    def __init__(self, name):
        self.name = name
    # This is playing method
    def play(self):
        print(f"{self.name} is playing...")
    # This is pause method
    def pause(self):
        print(f"{self.name} paused.")
    # This is stop method
    def stop(self):
        print(f"{self.name} stopped.")
    # This is minimize method
    def minimize(self):
        print(f"{self.name} minimized.")

# Create mediaplayer2 class from mediaplayer1 class
class MediaPlayer2(MediaPlayer1):
    def __init__(self, name):
        super().__init__(name)
    # This method forwards media based user input seconds
    def forward(self):
        try:
            second = int(input("Input seconds to forward: "))
            print(f"{self.name} forwarded for {second} secs.")
        except:
            print("Input only integers!")
    # This method backwards media based user input seconds
    def backward(self):
        try:
            second = int(input("Input seconds to backward: "))
            print(f"{self.name} backwarded for {second} secs.")
        except:
            print("Input only integers!")
    # This method speeds media based user input seconds
    def playback_speed(self):
        try:
            speed = int(input("Input speed: "))
            print(f"{self.name} playback speed is {speed}x.")
        except:
            print("Input only integers!")

# This class is for audio
class AudioPlayer(MediaPlayer2):
    def __init__(self, name):
        super().__init__(name)
    # This method plays audio on background
    def play_background(self):
        print(f"{self.name} plays on background.")

# Create class for showing subtitles
class ShowSubtitles():
    def __init__(self, name):
        self.name = name
    # This method shows subtitles
    def show_subtitles(self):
        print(f"{self.name} Showing Subtitles.")

# This class is for videos
class VideoPlayer(MediaPlayer2, ShowSubtitles):
    pass

# This class is for live streaming
class LivePlayer(MediaPlayer1, ShowSubtitles):
    def add_comment(self):
        comment = input("Input comment: ")
        print(f"Your commented: {comment}.")

# Create class objects
music = AudioPlayer("Music")
video = VideoPlayer("Video")
live = LivePlayer("Live")

# Dict for media
media = {
    "m" : "music",
    "v" : "video",
    "l" : "live"
}

# Dict for actions
actions = {
    "p" : "pause",
    "x" : "stop",
    "m" : "minimize",
    "f" : "forward",
    "b" : "backward",
    "s" : "playback_speed",
    "g" : "play_background",
    "c" : "show_subtitles",
    "a" : "add_comment"
}

# Running player
while True:
    try:
        print("\nPlayer is running...\n")
        # Prompt user to input letter to play music, video or live streaming
        action = input("Choose letter to play:\nm -> music, v -> video, l -> live, e -> exit player: ").lower()
        print()
        # Exit from player
        if action == "e":
            print("Player closed.")
            break
        eval(f"{media[action]}.play()") # Run media
        playing = True
        
        # Running media
        while playing:
            # Prompt user to input shortcut letter during playing media
            playing_action = input("\nPlease input letter for action:\np -> pause, x -> stop, m -> minimize ,f -> forward, b -> backward, s -> playback speed, g -> play on background, c -> show subtitles, a -> add cooment: ").lower()
            print()
            try:
                # Execute media method during playing media
                eval(f"{media[action]}.{actions[playing_action]}()")
                if playing_action == "x": # Close media(Stop playing)
                    playing = False
            except:
                print(f"{media[action]} does not support this action!")
                continue
    except:
        print("Please, input correct letter!")