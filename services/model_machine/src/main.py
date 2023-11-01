from concurrent import futures
from pathlib import Path
import logging
from ns.logging.config import apply_logging_config

import grpc
from fasttext import FastText, load_model
from ns.grpc.protobufs.lang_detection.lang_detection_pb2 import (
    LangModelResponse,
    LangModelResult,
    LangModelRequest,
)
from ns.grpc.protobufs.lang_detection.lang_detection_pb2_grpc import (
    LanguageDetectorServicer,
    add_LanguageDetectorServicer_to_server,
)

apply_logging_config()
logger = logging.getLogger(__name__)
model_path = Path(Path(__file__).parent.resolve(), "../resources/lang-detection.ft")
model: FastText = load_model(model_path.as_posix())


class LanguageDetectorService(LanguageDetectorServicer):
    def detect(self, request: LangModelRequest, context):
        logger.info('get model prediction for "%s"', request.text)
        predictions, scores = model.predict(request.text, k=request.max_results)
        logger.info("found %s predictions", len(predictions))

        results: list[LangModelResult] = []
        for prediction, score in zip(predictions, scores):
            prediction = prediction.replace("__label__", "")
            score = round(score, 4)
            result = LangModelResult(lang=prediction, score=score)
            results.append(result)

        languages = [result.lang for result in results]
        logger.info("returning predictions: %s", languages)

        return LangModelResponse(results=results)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_LanguageDetectorServicer_to_server(LanguageDetectorService(), server)
    server.add_insecure_port("0.0.0.0:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
