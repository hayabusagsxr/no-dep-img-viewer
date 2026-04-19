import tkinter as tk
from tkinter import filedialog, messagebox


class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.root.geometry("700x500")

        self.open_btn = tk.Button(self.root, text="Load Image", command=self.load_image)
        self.open_btn.pack(pady=20)

        self.display_label = tk.Label(self.root, text="Image goes here")
        self.display_label.pack(expand=True)

    def load_image(self):
        img_path = filedialog.askopenfilename(
            title="Pick an image",
            filetypes=[("Images", "*.png *.gif")]
        )

        if not img_path:
            return

        try:
            img = tk.PhotoImage(file=img_path)
            self.display_label.config(image=img, text="")
            self.display_label.image = img
            print("loaded the file successfully")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image.\n{e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewer(root)
    root.mainloop()
