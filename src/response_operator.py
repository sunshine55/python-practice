from pytubefix import YouTube


class ResponseOperator:
    def __init__(self, title: str, url: str):
        self.title = title
        self.url = url

    def get_audio(self):
        yt = YouTube(self.url)
        audio_stream = yt.streams.get_audio_only()
        sanitized_title = self.title.strip().replace(" ", "_")
        audio_stream.download(filename=f"{sanitized_title}.m4a")
