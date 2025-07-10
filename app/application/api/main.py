from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(
        title="Simple Kafka Chat",
        docs_url="/api/v1/docs",
        description="A simple chat application using Kafka as a message broker.",
    )
    return app
