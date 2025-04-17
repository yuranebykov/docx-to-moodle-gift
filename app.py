import sys
import os
import customtkinter as ctk
from tkinter import filedialog
import docx
from typing import List

from lib.docx_deserialization import get_question_blocks, QuestionBlock
from lib.format_text import get_formatted_text

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        if hasattr(sys, "_MEIPASS"):
            icon_path = os.path.join(sys._MEIPASS, "icon.ico")
        else:
            icon_path = "icon.ico"
        self.title("Конвертація DOCX у формат Moodle GIFT")
        self.geometry("800x600")
        self.iconbitmap(icon_path)
        self.question_blocks: List[QuestionBlock] = []
        self.active_tab = "editor"

        self.build_ui()

    def build_ui(self):
        # Головний фрейм 100% висоти
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # --- Рядок 1 --- Вибрати DOCX
        top_frame = ctk.CTkFrame(self)
        top_frame.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 5))

        select_button = ctk.CTkButton(top_frame, text="Вибрати DOCX", command=self.select_docx)
        select_button.pack()

        # --- Рядок 2 --- Tabs
        tab_frame = ctk.CTkFrame(self)
        tab_frame.grid(row=1, column=0, sticky="ew", padx=10)

        self.editor_tab_btn = ctk.CTkButton(tab_frame, text="Візуальний редактор", command=self.show_editor)
        self.editor_tab_btn.pack(side="left", padx=(0, 5))

        self.preview_tab_btn = ctk.CTkButton(tab_frame, text="Перегляд", command=self.show_preview)
        self.preview_tab_btn.pack(side="left")

        # --- Рядок 3 --- Контент (100% висоти)
        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        self.content_frame.grid_rowconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(0, weight=1)

        # --- Рядок 4 --- Статус питань
        status_frame = ctk.CTkFrame(self, fg_color="transparent")
        status_frame.grid(row=3, column=0, sticky="w", padx=10, pady=(0, 5))
        status_frame.grid_columnconfigure(1, weight=1)

        self.total_label = ctk.CTkLabel(status_frame, text="")
        self.total_label.grid(row=0, column=0, sticky="w")

        self.empty_label = ctk.CTkLabel(status_frame, text="")
        self.empty_label.grid(row=0, column=1, sticky="w", padx=(10, 0))

        # --- Рядок 5 --- Зберегти + Автор
        bottom_frame = ctk.CTkFrame(self)
        bottom_frame.grid(row=4, column=0, sticky="ew", padx=10, pady=(0, 10))
        bottom_frame.grid_columnconfigure(0, weight=0)
        bottom_frame.grid_columnconfigure(1, weight=1)

        save_button = ctk.CTkButton(bottom_frame, text="Зберігати TXT", command=self.save_txt)
        save_button.grid(row=0, column=0, sticky="w")

        self.author_label = ctk.CTkLabel(bottom_frame, text="Лаборант: Юрій Небиков. Версія: 1.0", anchor="e")
        self.author_label.grid(row=0, column=1, sticky="e")

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def select_docx(self):
        file_path = filedialog.askopenfilename(filetypes=[("Word Documents", "*.docx")])
        if file_path:
            doc = docx.Document(file_path)
            self.question_blocks = get_question_blocks(doc)
            self.show_editor()
            self.update_status()

    def show_editor(self):
        self.active_tab = "editor"
        self.clear_content()

        scroll_frame = ctk.CTkScrollableFrame(self.content_frame)
        scroll_frame.grid(row=0, column=0, sticky="nsew")

        for block in self.question_blocks:
            group_frame = ctk.CTkFrame(
                scroll_frame,
                fg_color="#ffe5e5" if block.correct_answer == -1 else "white"
            )
            group_frame.pack(fill="x", pady=5, padx=5)

            question_label = ctk.CTkLabel(
                group_frame,
                text=block.question,
                wraplength=750,
                anchor="w",
                justify="left"
            )
            question_label.pack(anchor="w", padx=10, pady=(5, 2))
            var = ctk.IntVar(value=block.correct_answer)

            def make_callback(qb: QuestionBlock, var_ref: ctk.IntVar, frame: ctk.CTkFrame):
                def callback():
                    qb.correct_answer = var_ref.get()
                    frame.configure(fg_color="white")
                    self.update_status()
                return callback

            for i, answer in enumerate(block.answers):
                radio = ctk.CTkRadioButton(
                    group_frame,
                    text=answer,
                    variable=var,
                    value=i,
                    command=make_callback(block, var, group_frame)
                )
                radio.pack(anchor="w", padx=20)

    def show_preview(self):
        self.active_tab = "preview"
        self.clear_content()

        preview_box = ctk.CTkTextbox(self.content_frame, wrap="word")
        preview_box.pack(fill="both", expand=True)

        for block in self.question_blocks:
            formatted = get_formatted_text(block)
            preview_box.insert("end", formatted)

        preview_box.configure(state="disabled")
    
    def update_status(self):
        total = len(self.question_blocks)
        empty = sum(1 for b in self.question_blocks if b.correct_answer == -1)

        self.total_label.configure(text=f"Питань: {total}")
        self.empty_label.configure(
            text=f"Без відповіді: {empty}",
            text_color="red" if empty > 0 else self.total_label.cget("text_color")
        )

    def save_txt(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Текстовий файл", "*.txt")]
        )
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                for block in self.question_blocks:
                    f.write(get_formatted_text(block))

if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    app = App()
    app.mainloop()
