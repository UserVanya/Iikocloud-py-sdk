class PipelineError(RuntimeError):
    """Expected pipeline failure with a user-actionable message."""


class SafetyError(PipelineError):
    """A live, secret, mutation, or publish safety invariant failed."""


class ValidationError(PipelineError):
    """The upstream or effective OpenAPI document is invalid."""


class StaleOverlayError(ValidationError):
    """An overlay no longer matches the upstream fragment it was written for."""
