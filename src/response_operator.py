from pytube import YouTube


class ResponseOperator:
    def __init__(self, title: str, url: str):
        self.title = title
        self.url = url

    def get_audio(self):
        yt = YouTube(self.url)
        audio_stream = yt.streams.filter(file_extension="mp4").first()
        sanitized_title = self.title.strip().replace(" ", "_")
        audio_stream.download(filename=f"{sanitized_title}.mp3")
