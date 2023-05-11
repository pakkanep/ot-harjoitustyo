from tkinter import ttk, constants


class QueryView:
    def __init__(self, root, handle_result, start_query,
                 reset_results, seeker, save_results):
        self._root = root
        self._handle_result = handle_result
        self._start_query = start_query
        self._reset_results = reset_results
        self._save_results = save_results
        self._frame = None
        self._seeker = seeker

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

        result_button = ttk.Button(
            master=self._frame,
            text="Show results",
            command=self._handle_result
        )

        reset_button = ttk.Button(
            master=self._frame,
            text="reset query results",
            command=self._reset_results
        )

        save_button = ttk.Button(
            master=self._frame,
            text="save query results",
            command=self._save_results
        )

        result_button.grid(row=1, column=0)
        start_button.grid(row=3, column=0)
        reset_button.grid(row=5, column=0)
        save_button.grid(row=7, column=0)
