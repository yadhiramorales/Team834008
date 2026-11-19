import tkinter as tk
from playlist import open_playlist

root = tk.Tk()
root.title("Music Player")
root.geometry("1000x650")

main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

# welcome text
label = tk.Label(main_frame, text="Welcome to (insert creative app name)!")
label.pack(pady=5)

# Button to open the playlist page
button = tk.Button(
    main_frame,
    text="Playlist",
    command=lambda: open_playlist(root, main_frame)
)
button.pack(pady=20)

root.mainloop()