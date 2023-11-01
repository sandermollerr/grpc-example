from opentelemetry.trace import format_span_id, format_trace_id, get_current_span
from pythonjsonlogger import jsonlogger


class TraceJsonFormatter(jsonlogger.JsonFormatter):
    """Logging formatter for extra traceability fields"""

    def add_fields(self, log_record, record, message_dict):
        """
        Add customs fields to json output log
        :param log_record:
        :param record:
        :param message_dict:
        :return:
        """
        super().add_fields(log_record, record, message_dict)

        span_ctx = get_current_span().get_span_context()

        if span_ctx.span_id:
            span_id = format_span_id(span_ctx.span_id)
        else:
            span_id = '0'

        if span_ctx.trace_id:
            trace_id = f'0x{format_trace_id(span_ctx.trace_id)}'
        else:
            trace_id = '0'

        log_record['traceID'] = trace_id
        log_record['spanID'] = span_id

