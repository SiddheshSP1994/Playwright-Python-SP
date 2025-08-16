
from __future__ import annotations
import os, time
try:
    from opentelemetry import trace
    from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
    from opentelemetry.sdk.resources import Resource
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor
except Exception:
    trace = None

tracer = None

def pytest_sessionstart(session):
    global tracer
    if trace is None:
        return
    if not os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT"):
        return
    provider = TracerProvider(resource=Resource.create({"service.name": "pytest-playwright"}))
    processor = BatchSpanProcessor(OTLPSpanExporter())
    provider.add_span_processor(processor)
    trace.set_tracer_provider(provider)
    tracer = trace.get_tracer(__name__)

def pytest_runtest_protocol(item, nextitem):
    if tracer is None:
        return
    with tracer.start_as_current_span("test", attributes={"nodeid": item.nodeid}):
        return
