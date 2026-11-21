import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

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

    # Back to main page
    def go_back():
        playlist_frame.destroy()
        main_frame.pack(fill="both", expand=True)

    # Create playlist
    def create_playlist():
        name = simpledialog.askstring(
            "Create Playlist",
            "Enter playlist name:",
            parent=root
        )

        if name is None:
            return

        name = name.strip()

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
            save_playlists()
            show_playlists()

    # Show all playlists
    def show_playlists():
        for widget in playlist_frame.winfo_children():
            widget.destroy()

        # Top bar
        top_bar = tk.Frame(playlist_frame)
        top_bar.pack(fill="x", padx=10, pady=10)

        back_button = tk.Button(
            top_bar,
            text="Back",
            command=go_back
        )
        back_button.pack(side="left")

        create_button = tk.Button(
            top_bar,
            text="Create Playlist",
            command=create_playlist
        )
        create_button.pack(side="right")

        # Page title
        title = tk.Label(
            playlist_frame,
            text="My Playlists",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=20)

        # Display playlists
        # TODO: Replace buttons with a more natural list layout
        #       and add support for custom playlist cover images later.
        if playlists:
            for name in playlists:
                button = tk.Button(
                    playlist_frame,
                    text=name,
                    command=lambda n=name: show_detail(n)
                )
                button.pack(pady=5)
        else:
            label = tk.Label(
                playlist_frame,
                text="No playlists"
            )
            label.pack(pady=10)

    # Rename playlist
    def rename_playlist(name):
        new_name = simpledialog.askstring(
            "Rename Playlist",
            "Enter new playlist name:",
            initialvalue=name,
            parent=root
        )

        if new_name is None:
            return

        new_name = new_name.strip()

        if new_name == "":
            messagebox.showwarning(
                "Warning",
                "Please enter a playlist name."
            )

        elif new_name in playlists and new_name != name:
            messagebox.showwarning(
                "Warning",
                "Playlist already exists."
            )

        elif new_name != name:
            updated = {}

            for key, songs in playlists.items():
                if key == name:
                    updated[new_name] = songs
                else:
                    updated[key] = songs

            playlists.clear()
            playlists.update(updated)

            save_playlists()
            show_detail(new_name)

    # Delete playlist
    def delete_playlist(name):
        confirm = messagebox.askyesno(
            "Delete Playlist",
            "Are you sure you want to delete this playlist?",
            parent=root
        )

        if confirm:
            del playlists[name]
            save_playlists()
            show_playlists()

    # Show selected playlist details 
    def show_detail(name):
        for widget in playlist_frame.winfo_children():
            widget.destroy()

        # Top bar
        top_bar = tk.Frame(playlist_frame)
        top_bar.pack(fill="x", padx=10, pady=10)

        back_button = tk.Button(
            top_bar,
            text="Back",
            command=show_playlists
        )
        back_button.pack(side="left")

        delete_button = tk.Button(
            top_bar,
            text="Delete",
            command=lambda: delete_playlist(name)
        )
        delete_button.pack(side="right")

        rename_button = tk.Button(
            top_bar,
            text="Rename",
            command=lambda: rename_playlist(name)
        )
        rename_button.pack(side="right", padx=5)

        # Playlist title
        title = tk.Label(
            playlist_frame,
            text=name,
            font=("Arial", 18, "bold")
        )
        title.pack(pady=15)

        # Display songs
        if playlists[name]:
            for song in playlists[name]:
                song_frame = tk.Frame(playlist_frame)
                song_frame.pack(fill="x", padx=20, pady=5)

                # Album cover placeholder (Can be updated to display an image later. Not sure yet)
                cover = tk.Label(
                    song_frame,
                    text="♪",
                    width=5,
                    height=2,
                    relief="solid"
                )
                cover.pack(side="left", padx=10)

                song_label = tk.Label(
                    song_frame,
                    text=os.path.basename(song)
                )
                song_label.pack(side="left")
        else:
            label = tk.Label(
                playlist_frame,
                text="No songs yet"
            )
            label.pack(pady=20)

    # Display playlist page
    show_playlists()
