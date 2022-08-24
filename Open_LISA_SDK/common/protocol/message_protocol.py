from time import time


class MessageProtocolTrack:
    def __init__(self, begin_ts, finish_ts, rcv_bytes, snt_bytes):
        self.begin_timestamp = begin_ts
        self.finish_timestamp = finish_ts
        self.bytes_received = rcv_bytes
        self.bytes_sent = snt_bytes


class MessageProtocol:
    def __init__(self):
        self.MSG_LEN_BYTES_AMOUNT = 4

        # track
        self._begin_track_timestamp = time()
        self._finish_track_timestamp = time()
        self._received_bytes_amount_track = 0
        self._sent_bytes_amount_track = 0

    # Initiates track information until

    def start_track(self):
        self._begin_track_timestamp = time()
        self._finish_track_timestamp = time()
        self._received_bytes_amount_track = 0
        self._sent_bytes_amount_track = 0

    # Returns the track information since the previous call to start_track
    def get_track(self) -> MessageProtocolTrack:
        self._finish_track_timestamp = time()
        return MessageProtocolTrack(
            begin_ts=self._begin_track_timestamp,
            finish_ts=self._finish_track_timestamp,
            rcv_bytes=self._received_bytes_amount_track,
            snt_bytes=self._sent_bytes_amount_track
        )

    def disconnect(self):
        raise NotImplementedError("Please Implement this method: disconnect")

    def send_msg(self, msg, encode=True):
        raise NotImplementedError("Please Implement this method: send_msg")

    def receive_msg(self, decode=True):
        raise NotImplementedError("Please Implement this method: receive_msg")

    def __recvall(self, n):
        raise NotImplementedError("Please Implement this method: __recvall")
