import tkinter as tk
from tkinter import messagebox
import json

playlists = {}

# Save playlists
def save_playlists():
    with open("playlists.json", "w") as file:
        json.dump(playlists, file)


# Load playlists
def load_playlists():
    global playlists

    try:
        with open("playlists.json", "r") as file:
            playlists = json.load(file)
    except FileNotFoundError:
        playlists = {}


def open_playlist(root, main_frame):
    load_playlists()

    main_frame.pack_forget()

    playlist_frame = tk.Frame(root)
    playlist_frame.pack(fill="both", expand=True)

    label = tk.Label(playlist_frame, text="My Playlists")
    label.pack(pady=20)

    # Enter playlist name
    name_entry = tk.Entry(playlist_frame)
    name_entry.pack(pady=5)

    # Selected playlist name
    selected_playlist = tk.StringVar(value="")

    # Select playlist
    def select_playlist(name):
        selected_playlist.set(name)

        song_listbox.delete(0, tk.END)

        for song in playlists[name]:
            song_listbox.insert(tk.END, song)

    # Display when there are no playlists
    playlist_label = tk.Label(
        playlist_frame,
        text="No playlists"
    )

    # Playlist selection menu
    playlist_menu = tk.OptionMenu(
        playlist_frame,
        selected_playlist,
        ""
    )

    # Display songs
    song_listbox = tk.Listbox(playlist_frame)

    # Update playlist menu
    def update_menu():
        menu = playlist_menu["menu"]
        menu.delete(0, "end")

        for name in playlists:
            menu.add_command(
                label=name,
                command=lambda n=name: select_playlist(n)
            )

    # Create a new playlist
    def create_playlist():
        name = name_entry.get().strip()

        if name == "":
            messagebox.showwarning(
                "Warning",
                "Please enter a playlist name."
            )

        elif name in playlists:
            messagebox.showwarning(
                "Warning",
                "Playlist already exists."
            )

        else:
            playlists[name] = []
            name_entry.delete(0, tk.END)

            save_playlists()
            update_menu()

            playlist_label.pack_forget()
            playlist_menu.pack(pady=5)
            song_listbox.pack(pady=10)

            select_playlist(name)

    create_button = tk.Button(
        playlist_frame,
        text="Create Playlist",
        command=create_playlist
    )
    create_button.pack(pady=5)

    # Load existing playlists
    update_menu()

    if playlists:
        playlist_menu.pack(pady=5)
        song_listbox.pack(pady=10)
        select_playlist(next(iter(playlists)))
    else:
        playlist_label.pack(pady=5)

    # Return to main page
    def go_back():
        playlist_frame.destroy()
        main_frame.pack(fill="both", expand=True)

    back_button = tk.Button(
        playlist_frame,
        text="Back",
        command=go_back
    )
    back_button.pack(pady=10)