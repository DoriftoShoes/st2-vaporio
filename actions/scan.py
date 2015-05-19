from lib.base import BaseVaporIOAction

__all__ = [
    'Scan'
]


class Scan(BaseVaporIOAction):
    def run(self, host, board_id=255, ssl=True):
        if board_id == 'all':
            board_id = "255"
        endpoint = "scan/%s" % board_id
        boards = self._get_request(host=host, endpoint=endpoint, ssl=ssl)

        return boards
