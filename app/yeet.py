import json


import sys
from collections import namedtuple

from requests.api import request
from requests import Response
from app import formatter

from app.reader import read_request_file
from app.writer import write
from app import colorizer


# This module provides the `Yeeter` class which handles HTTP requests and formats the response
# based on the content type. It supports colorizing and formatting JSON, XML, and HTML responses.
class Yeeter:
    Visual = namedtuple("Visual", ["formatter", "colorizer"])

    def __init__(self, colorize: bool = True):
        sys.stdout.reconfigure(encoding="utf-8")

        # if output stays on terminal then isatty() returns True
        # if output is redirected to file then isatty() returns False
        self.colorize_stdout: bool = colorize and sys.stdout.isatty()
        self.colorize_stderr: bool = colorize and sys.stderr.isatty()

        self.content_type_visual = {}
        for content_type, formatter_fn, colorizer_fn in [
            (
                "application/json",
                formatter.format_json_string,
                colorizer.colorize_json_string,
            ),
            ("text/xml", formatter.format_xml_string, colorizer.colorize_xml_string),
            ("text/html", formatter.format_html_string, colorizer.colorize_html_string),
        ]:
            self.content_type_visual[content_type] = self.Visual(
                formatter_fn, colorizer_fn
            )

    # Sends an HTTP request based on the provided file and processes the response.
    def yeet(self, request_filepath):
        request_data: dict = read_request_file(request_filepath)
        response: Response = request(**request_data)

        metadata_text = json.dumps(
            dict(
                **response.headers,
                **{"status": response.status_code, "url": response.url}
            )
        )
        write(
            metadata_text,
            sys.stderr,
            formatter=formatter.format_metadata,
            colorizer=(
                colorizer.colorize_metadata_string if self.colorize_stderr else None
            ),
        )

        content_type: str = self._get_content_type(response)
        if content_type in self.content_type_visual.keys():
            write(
                response.content.decode("utf-8"),
                sys.stdout,
                formatter=self.content_type_visual[content_type].formatter,
                colorizer=(
                    self.content_type_visual[content_type].colorizer
                    if self.colorize_stdout
                    else None
                ),
            )
        else:
            write(response.content, sys.stdout.buffer, formatter=None, colorizer=None)

    # Extracts and returns the content type from the HTTP response.
    @staticmethod
    def _get_content_type(res: Response) -> str:
        content_type, *_ = res.headers["content-type"].split(";")
        return content_type.strip().lower()
