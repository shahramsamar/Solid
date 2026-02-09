class MediaPlayer:
    def play_mp3(self, file_name):
        print(f"Playing MP3 file: {file_name}")

class AdvancedMediaPlayer:
    def play_mp4(self, file_name):
        print(f"Playing MP4 file: {file_name}")

    def play_avi(self, file_name):
        print(f"Playing AVI file: {file_name}")

class MediaAdapter:
    def __init__(self, file_type):
        if file_type == "mp3":
            self.advanced_player = None
        else:
             self.advanced_player = AdvancedMediaPlayer()


    def play(self, file_type, file_name):
        if file_type == "mp3":
            player = MediaPlayer()
            player.play_mp3(file_name)
        elif file_type == "mp4" and self.advanced_player:
            self.advanced_player.play_mp4(file_name)
        elif file_type == "avi" and self.advanced_player:
            self.advanced_player.play_avi(file_name)
        else:
            print(f"Unsupported file type: {file_type}")

adapter = MediaAdapter("mp4")
adapter.play("mp4", "video.mp4")