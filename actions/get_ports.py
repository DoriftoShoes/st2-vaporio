from lib.base import BaseVaporIOAction

__all__ = [
    'GetPorts'
]


class GetPorts(BaseVaporIOAction):
    def run(self, host, board_id, ssl=True):
        endpoint = "scan/%i" % board_id
        board = self._get_request(host=host, endpoint=endpoint, ssl=ssl)
        ports = board['ports']

        return ports
