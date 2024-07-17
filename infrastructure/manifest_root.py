from infrastructure.manifest_response import ManifestResponse


class ManifestRoot:

    def __init__(self, Response: dict, ErrorCode: int, ThrottleSeconds: int, ErrorStatus: str, Message: str, MessageData: dict):
        self.Response = ManifestResponse.From(Response)
        self.ErrorCode = ErrorCode
        self.ThrottleSeconds = ThrottleSeconds
        self.ErrorStatus = ErrorStatus
        self.Message = Message
        self.MessageData = MessageData

    @classmethod
    def From(cls, data: dict) -> "ManifestRoot":
        return cls(**data)

    def as_dict(self):
        return {
            "Response": self.Response.as_dict(),
            "ErrorCode": self.ErrorCode,
            "ThrottleSeconds": self.ThrottleSeconds,
            "ErrorStatus": self.ErrorStatus,
            "Message": self.Message,
            "MessageData": self.MessageData
        }

    def __len__(self):
        return len(self.as_dict())
