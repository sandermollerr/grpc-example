from ns.grpc.protobufs.lang_detection.lang_detection_pb2 import (
    LangModelResponse,
    LangModelResult,
    LangModelRequest,
)
from ns.grpc.protobufs.lang_detection.lang_detection_pb2_grpc import (
    LanguageDetectorServicer,
    add_LanguageDetectorServicer_to_server,
)
from fasttext import FastText, load_model
from pathlib import Path
from concurrent import futures
import grpc

model_path = Path("../resources/lang-detection.ft")
model: FastText = load_model(model_path.as_posix())


class LanguageDetectorService(LanguageDetectorServicer):
    def detect(self, request: LangModelRequest, context):
        print(f'get model prediction for "{request.text}"')
        predictions, scores = model.predict(request.text, k=request.max_results)
        print(f"found {len(predictions)} predictions")

        results: list[LangModelResult] = []
        for prediction, score in zip(predictions, scores):
            prediction = prediction.replace("__label__", "")
            score = round(score, 4)
            result = LangModelResult(lang=prediction, score=score)
            results.append(result)

        languages = [result.lang for result in results]
        print(f"returning predictions: {languages}")

        return LangModelResponse(results=results)


def serve():
    print("hi")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_LanguageDetectorServicer_to_server(LanguageDetectorService(), server)
    server.add_insecure_port("0.0.0.0:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
