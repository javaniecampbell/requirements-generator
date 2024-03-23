from openinference.instrumentation.openai import OpenAIInstrumentor
from opentelemetry import trace as trace_api
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk import trace as trace_sdk
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

def instrument():
    endpoint = "http://127.0.0.1:6006/v1/traces"
    trace_provider = trace_sdk.TracerProvider()
    trace_provider.add_span_processor(SimpleSpanProcessor(OTLPSpanExporter(endpoint=endpoint)))
    trace_provider.add_span_processor(ConsoleSpanExporter(service_name="requirements-generator"))
    trace_api.set_tracer_provider(trace_provider)

    OpenAIInstrumentor().instrument()