from json import dumps

from application.dto.ManifestResponseDto import ManifestResponseDto


class ManifestDto:

    def __init__(self,
                 Response: dict,
                 ErrorCode: int,
                 ThrottleSeconds: int,
                 ErrorStatus: str,
                 Message: str,
                 MessageData: dict[str, str]):
        """
        :type self.Response: ManifestResponseDto
        """
        self.Response = ManifestResponseDto.From(Response)
        self.ErrorCode = ErrorCode
        self.ThrottleSeconds = ThrottleSeconds
        self.ErrorStatus = ErrorStatus
        self.Message = Message
        self.MessageData = MessageData

    @classmethod
    def From(cls, value: dict):
        return cls(
            value['Response'],
            value['ErrorCode'],
            value['ThrottleSeconds'],
            value['ErrorStatus'],
            value['Message'],
            value['MessageData']
        )

    def __iter__(self):
        return iter([self.Response, self.ErrorCode, self.ThrottleSeconds, self.ErrorStatus, self.Message, self.MessageData])

    def __dict__(self):
        return {
            "Response": self.Response.__dict__(),
            "ErrorCode": self.ErrorCode,
            "ThrottleSeconds": self.ThrottleSeconds,
            "ErrorStatus": self.ErrorStatus,
            "Message": self.Message,
            "MessageData": self.MessageData
        }

    def __str__(self):
        return dumps(self.__dict__())

    def __repr__(self):
        return dumps(self.__dict__(), indent=4)