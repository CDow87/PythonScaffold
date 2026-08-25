from __future__ import annotations

import platform

import uvicorn

from app.core.config import get_settings


def _loop_implementation() -> str:
    return "asyncio" if platform.system() == "Windows" else "uvloop"


def run() -> None:
    settings = get_settings()
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
        loop=_loop_implementation(),
    )


if __name__ == "__main__":
    run()
