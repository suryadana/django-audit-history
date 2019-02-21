from django.utils.deprecation import MiddlewareMixin

from audit_history.models import (
    AuditRequest, AuditException, AuditResponse
)


def get_public_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class AuditHistoryMiddleware(MiddlewareMixin):
    request = None

    def process_request(self, request):
        self.request = AuditRequest.objects.create(
            ip=get_public_ip(request),
            user=request.user,
            user_agent=request.META.get('HTTP_USER_AGENT', ''),
            url=request.build_absolute_uri(request.get_full_path()),
            data=request.body
        )

    def process_exception(self, request, exception):
        import traceback
        AuditException.objects.create(
            request=self.request,
            exception=traceback.format_exc()
        )
        return None

    def process_response(self, request, response):
        data = response.content
        status_code = response.status_code
        AuditResponse.objects.create(
            request=self.request,
            data=data,
            status_code=status_code
        )
        return response
