import tkinter as tk

playlists = []

def open_playlist(root, main_frame):

    main_frame.pack_forget()

    playlist_frame = tk.Frame(root)
    playlist_frame.pack(fill="both", expand=True)

    label = tk.Label(playlist_frame, text="My Playlists")
    label.pack(pady=20)

    # Enter playlist name
    name_entry = tk.Entry(playlist_frame)
    name_entry.pack(pady=5)

    # Display playlists
    playlist_label = tk.Label(playlist_frame, text="Playlists")
    playlist_label.pack(pady=5)

    playlist_listbox = tk.Listbox(playlist_frame)
    playlist_listbox.pack(pady=10)

    # Create a new playlist
    def create_playlist():
        name = name_entry.get()

        if name != "":
            playlists.append({
                "name": name,
                "songs": []
            })
            playlist_listbox.insert(tk.END, name)
            name_entry.delete(0, tk.END)

    create_button = tk.Button(
        playlist_frame,
        text="Create Playlist",
        command=create_playlist
    )
    create_button.pack(pady=5)

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