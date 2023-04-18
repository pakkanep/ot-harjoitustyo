from tkinter import ttk, constants


class QueryView:
    def __init__(self, root, handle_result, start_query, information):
        self._root = root
        self._handle_result = handle_result
        self._start_query = start_query
        self._frame = None
        self._information = information

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        start_button = ttk.Button(
            master=self._frame,
            text="Start query",
            command=self._start_query
        )

        button = ttk.Button(
            master=self._frame,
            text="Show results",
            command=self._handle_result
        )


        button.grid(row=1, column=0)
        start_button.grid(row=2, column=0)