from lib.base import BaseVaporIOAction

__all__ = [
    'BoardVersion'
]


class BoardVersion(BaseVaporIOAction):
    def run(self, host, board_id, ssl=True):
        endpoint = "version/%i" % board_id
        version = self._get_request(host=host, endpoint=endpoint, ssl=ssl)

        return version
