#!/usr/bin/python3
"""Base Initialization"""


from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()