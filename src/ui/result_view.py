from tkinter import ttk, constants


class ResultView:
    def __init__(self, root, handle_result, information):
        self._root = root
        self._handle_result = handle_result
        self._frame = None
        self._information = information

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        button = ttk.Button(
            master=self._frame,
            text="Go back to query",
            command=self._handle_result
        )

        button.grid(row=1, column=0)
        
        pages_label = ttk.Label(
            master=self._frame,
            text=f"Handled pages: {self._information.successful_add_handles}",
            background="blue", foreground="white")
        
        pages_label.grid(row=2, column=0)
        

        rownum = 5
        for a, b in self._information.information_dict.items():

            name_label = ttk.Label(
                master=self._frame, text=a, background="blue", foreground="white")
            line_label = ttk.Label(master=self._frame, text="|"*b)
            amount_label = ttk.Label(master=self._frame, text=b-1,)

            name_label.grid(row=rownum, column=0, sticky="SW", columnspan=80)
            line_label.grid(row=rownum, column=2, sticky="ew")
            amount_label.grid(row=rownum, column=3, sticky="ew")
            rownum += 1
