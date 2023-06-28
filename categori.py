import tkinter as tk
from tkinter import filedialog
import pandas as pd


class DataCategoryIdentifier:
    def __init__(self, master):
        self.master = master
        master.title("Data Category Identifier")

        self.label = tk.Label(master, text="Select a CSV file:")
        self.label.pack()

        self.browse_button = tk.Button(
            master, text="Browse", command=self.load_file)
        self.browse_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def load_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.identify_categories(file_path)

    def identify_categories(self, file_path):
        df = pd.read_csv(file_path)
        category_dict = {}

        for col in df.columns:
            if df[col].dtype == 'object':
                if len(df[col].unique()) < len(df[col]):
                    category_dict[col] = 'ordinal'
                else:
                    category_dict[col] = 'nominal'
            else:
                category_dict[col] = 'numerical'

        self.show_result(category_dict)

    def show_result(self, category_dict):
        result_text = "Data categories:\n"
        for col, category in category_dict.items():
            result_text += f"{col}: {category}\n"
        self.result_label.configure(text=result_text)


root = tk.Tk()
app = DataCategoryIdentifier(root)
root.mainloop()
