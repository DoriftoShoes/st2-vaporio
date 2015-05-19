from lib.base import BaseVaporIOAction

__all__ = [
    'GetPorts'
]


class GetPorts(BaseVaporIOAction):
    def run(self, host, board_id, ssl=True):
        endpoint = "scan/%s" % board_id
        board = self._get_request(host=host, endpoint=endpoint, ssl=ssl)
        ports = board['boards'][int(board_id) - 1]['ports']

        return ports
