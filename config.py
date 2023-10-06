"""QR Code Generator Configuration"""
import os


class Config:
    QR_CODE_IMAGE_DIRECTORY = os.environ.get('QR_CODE_IMAGE_DIRECTORY', 'qrcodes')
    QR_CODE_DEFAULT_URL = os.environ.get('QR_CODE_DEFAULT_URL', 'www.github.com/phillipebarreto1')
    QR_CODE_DEFAULT_FILE_NAME = os.environ.get('QR_CODE_DEFAULT_FILE_NAME', 'default.png')