import tkinter as tk
from playlist import open_playlist

root = tk.Tk()
root.title("Music Player")
root.geometry("600x400")

main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

# Button to open the playlist page
button = tk.Button(
    main_frame,
    text="Playlist",
    command=lambda: open_playlist(root, main_frame)
)
button.pack(pady=20)

root.mainloop()