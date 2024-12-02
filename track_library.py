# track_library.py

import json

class Track:
    def __init__(self, IdTrack, nameTrack, artist, genre, file_path=None):
        self.IdTrack = IdTrack
        self.nameTrack = nameTrack
        self.artist = artist
        self.genre = genre
        self.file_path = file_path

    def to_dict(self):
        return {
            "IdTrack": self.IdTrack,
            "nameTrack": self.nameTrack,
            "artist": self.artist,
            "genre": self.genre,
            "file_path": self.file_path
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            IdTrack=data["IdTrack"],
            nameTrack=data["nameTrack"],
            artist=data["artist"],
            genre=data["genre"],
            file_path=data.get("file_path")
        )

class TrackLibrary:
    def __init__(self):
        self.tracks = []

    def add_track(self, track):
        self.tracks.append(track)

    def remove_track(self, IdTrack):
        self.tracks = [track for track in self.tracks if track.IdTrack != IdTrack]

    def find_track(self, IdTrack):
        for track in self.tracks:
            if track.IdTrack == IdTrack:
                return track
        return None

    def list_all_tracks(self):
        return self.tracks

    def save_to_file(self, filename="tracks.json"):
        # Lưu danh sách bài hát vào một tệp JSON
        with open(filename, "w") as file:
            json.dump([track.to_dict() for track in self.tracks], file, indent=4)

    def load_from_file(self, filename="tracks.json"):
        # Tải danh sách bài hát từ một tệp JSON
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.tracks = [Track.from_dict(track_data) for track_data in data]
        except FileNotFoundError:
            self.tracks = []  # Nếu tệp không tồn tại, bắt đầu với danh sách trống
