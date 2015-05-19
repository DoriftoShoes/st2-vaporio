from lib.base import BaseVaporIOAction

__all__ = [
    'ReadSensor'
]


class ReadSensor(BaseVaporIOAction):
    def run(self, host, sensor_type, board_id, port_id, ssl=False):
        endpoint = "read/%s/%i/%i" % (sensor_type, board_id, port_id)
        data = self._get_request(host=host, endpoint=endpoint, ssl=ssl)

        return data
