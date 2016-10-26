from fontanabau.web.testing import FONTANABAU_FUNCTIONAL
from ftw.lawgiver.tests.base import WorkflowTest


class TestFONTANABAUWebWorkflowSpecification(WorkflowTest):
    layer = FONTANABAU_FUNCTIONAL
    workflow_path = '../profiles/default/workflows/fontanabau_web_workflow'
