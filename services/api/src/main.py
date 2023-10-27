from fastapi import FastAPI
from ns.grpc.protobufs.lang_detection.lang_detection_pb2 import (
    LangModelResponse,
    LangModelResult,
    LangModelRequest,
)
from ns.grpc.protobufs.lang_detection.lang_detection_pb2_grpc import (
    LanguageDetector,
    LanguageDetectorStub,
)
import grpc
from google.protobuf.json_format import MessageToDict

app = FastAPI()

model_machine_channel = grpc.insecure_channel("model_machine:50051")
model_machine_client = LanguageDetectorStub(model_machine_channel)


@app.get("/api/v1/lang-detect")
def detect_language(text: str, max_results: int = 3):
    model_machine_request = LangModelRequest(text=text, max_results=max_results)
    model_machine_response = model_machine_client.detect(model_machine_request)
    serialized_response = MessageToDict(model_machine_response)
    print(f"model machine response: {serialized_response}")
    return {"results": serialized_response.get("results")}
