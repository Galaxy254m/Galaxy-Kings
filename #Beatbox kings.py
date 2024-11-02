#Beatbox kings

#Program to create a music player
import os
import pygame
import tkinter as tk
from tkinter import messagebox, simpledialog, Listbox, Scrollbar

# Initialize Pygame
pygame.mixer.init()

# Sample music library
music_library = {
    'Pop': {
        'Artist1': ['song1.mp3', 'song2.mp3'],
        'Artist2': ['song3.mp3']
    },
    'Rock': {
        'Artist3': ['song4.mp3', 'song5.mp3'],
        'Artist4': ['song6.mp3']
    },
    'Jazz': {
        'Artist5': ['song7.mp3'],
        'Artist6': ['song8.mp3']
    }
}

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        master.title("Boomba FM Music Player")

        self.current_song = None

        # Create frames
        self.frame = tk.Frame(master)
        self.frame.pack()

        self.play_button = tk.Button(self.frame, text="Play", command=self.play)
        self.play_button.pack(side=tk.LEFT)

        self.pause_button = tk.Button(self.frame, text="Pause", command=self.pause)
        self.pause_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(self.frame, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT)

        self.genre_label = tk.Label(master, text="Select Genre:")
        self.genre_label.pack()

        self.genre_list = Listbox(master)
        for genre in music_library.keys():
            self.genre_list.insert(tk.END, genre)
        self.genre_list.pack()

        self.artist_label = tk.Label(master, text="Select Artist:")
        self.artist_label.pack()

        self.artist_list = Listbox(master)
        self.artist_list.pack()

        self.song_label = tk.Label(master, text="Select Song:")
        self.song_label.pack()

        self.song_list = Listbox(master)
        self.song_list.pack()

        self.genre_list.bind('<<ListboxSelect>>', self.update_artists)
        self.artist_list.bind('<<ListboxSelect>>', self.update_songs)

    def update_artists(self, event):
        self.artist_list.delete(0, tk.END)
        selected_genre = self.genre_list.get(self.genre_list.curselection())
        for artist in music_library[selected_genre].keys():
            self.artist_list.insert(tk.END, artist)
        self.song_list.delete(0, tk.END)  # Clear songs when genre changes

    def update_songs(self, event):
        self.song_list.delete(0, tk.END)
        selected_genre = self.genre_list.get(self.genre_list.curselection())
        selected_artist = self.artist_list.get(self.artist_list.curselection())
        for song in music_library[selected_genre][selected_artist]:
            self.song_list.insert(tk.END, song)

    def play(self):
        try:
            selected_song = self.song_list.get(self.song_list.curselection())
            self.current_song = selected_song
            pygame.mixer.music.load(selected_song)
            pygame.mixer.music.play()
        except Exception as e:
            messagebox.showerror("Error", "Please select a song first.")

    def pause(self):
        if self.current_song:
            pygame.mixer.music.pause()

    def stop(self):
        pygame.mixer.music.stop()
        self.current_song = None

if __name__ == "__main__":
    root = tk.Tk()
    player = MusicPlayer(root)
    root.mainloop()
