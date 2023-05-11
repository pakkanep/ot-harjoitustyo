from tkinter import Tk, ttk
from ui.query_view import QueryView
from ui.result_view import ResultView
from services.operations import Operations
import threading


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._seeker = Operations()

    def start(self):
        self._show_query_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_query(self):
        self._show_query_view()

    def _handle_result(self):
        self._show_result_view()

    def _start_query(self):
        self._seeker.start_query()

    def _reset_query_results(self):
        self._seeker.reset_all()

    def _save_query_results(self):
        self._seeker.save_results()

    def _show_query_view(self):
        self._hide_current_view()

        self._current_view = QueryView(
            self._root,
            self._handle_result,
            self._start_query,
            self._reset_query_results,
            self._seeker,
            self._save_query_results
        )

        self._current_view.pack()

    def _show_result_view(self):
        self._hide_current_view()

        self._current_view = ResultView(
            self._root,
            self._handle_query,
            self._seeker
        )

        self._current_view.pack()
