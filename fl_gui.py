import tkinter as tk
from tkinter import ttk, messagebox
from fl_mod import FLConverter, fl_parse_input, fl_format_output

class FLApp(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=12)
        self.pack(fill="both", expand=True)
        self.conv = FLConverter()
        self.val = tk.StringVar()
        self.out = tk.StringVar()
        self.src = tk.StringVar(value="C - Celsius")
        self.dst = tk.StringVar(value="F - Fahrenheit")
        self.unit_names = {"C": "Celsius", "F": "Fahrenheit", "K": "Kelvin"}
        self.build()
        self.bind_all("<Return>", self.on_convert_enter)

    def build(self):
        ttk.Label(self, text="Érték").grid(row=0, column=0, sticky="w")
        e = ttk.Entry(self, textvariable=self.val, width=22)
        e.grid(row=0, column=1, sticky="we")
        e.focus_set()
        ttk.Label(self, text="Forrás").grid(row=1, column=0, sticky="w")
        units_full = ["C - Celsius", "F - Fahrenheit", "K - Kelvin"]
        cb1 = ttk.Combobox(self, values=units_full, textvariable=self.src, state="readonly", width=18)
        cb1.grid(row=1, column=1, sticky="w")
        ttk.Label(self, text="Cél").grid(row=2, column=0, sticky="w")
        cb2 = ttk.Combobox(self, values=units_full, textvariable=self.dst, state="readonly", width=18)
        cb2.grid(row=2, column=1, sticky="w")
        b = ttk.Button(self, text="Átváltás", command=self.on_convert_click)
        b.grid(row=3, column=0, columnspan=2, sticky="we", pady=8)
        ttk.Label(self, text="Eredmény").grid(row=4, column=0, sticky="w")
        ttk.Entry(self, textvariable=self.out, width=22, state="readonly").grid(row=4, column=1, sticky="we")
        self.columnconfigure(1, weight=1)
        cb1.bind("<<ComboboxSelected>>", self.on_combo)
        cb2.bind("<<ComboboxSelected>>", self.on_combo)

    def on_convert_click(self):
        self.exec_convert()

    def on_convert_enter(self, event):
        self.exec_convert()

    def on_combo(self, event):
        self.exec_convert()

    def exec_convert(self):
        v = fl_parse_input(self.val.get())
        if v is None:
            messagebox.showerror("Hiba", "Az érték nem érvényes szám!", parent=self)
            return
        src_code = self.src.get().split(" - ")[0]
        dst_code = self.dst.get().split(" - ")[0]
        if src_code == dst_code:
            messagebox.showerror("Hiba", "A forrás és a cél egység nem lehet azonos!", parent=self)
            return
        r = self.conv.into(v, src_code, dst_code)
        name = self.unit_names.get(dst_code, dst_code)
        self.out.set(f"{fl_format_output(r)} {name}")

