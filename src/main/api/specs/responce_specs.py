from http import HTTPStatus
from requests import Response


class ResponceSpecs:
    @staticmethod
    def request_ok():
        def confirm(responce: Response):
            assert responce.status_code == HTTPStatus.OK, responce.text
        return confirm
    @staticmethod
    def request_created():
        def confirm(responce: Response):
            assert responce.status_code == HTTPStatus.CREATED, responce.text
        return confirm
    @staticmethod
    def request_bad():
        def confirm(responce: Response):
            assert responce.status_code == HTTPStatus.BAD_REQUEST, responce.text
        return confirm
    @staticmethod
    def request_error():
        def confirm(responce: Response):
            assert responce.status_code == HTTPStatus.UNPROCESSABLE_CONTENT, responce.text
        return confirm
