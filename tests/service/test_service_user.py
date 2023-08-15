import tests.models.parameters
import tests.models.messages
from src.service.service_user import ServiceUser


class TestServiceUser:
    def test_add_user_success(self):
        service = ServiceUser()
        returned_msg = service.add_user(tests.models.parameters.user_valid, tests.models.parameters.job_valid)
        expected_msg = tests.models.messages.msg_user_ok
        assert returned_msg == expected_msg

    def test_add_user_existing(self):
        service = ServiceUser()
        service.add_user(tests.models.parameters.user_valid, tests.models.parameters.job_valid)
        returned_msg = service.add_user(tests.models.parameters.user_valid, tests.models.parameters.job_valid)
        expected_msg = tests.models.messages.msg_user_exist
        assert returned_msg == expected_msg

    def test_add_user_failed(self):
        service = ServiceUser()
        returned_msg = service.add_user(tests.models.parameters.user_invalid, tests.models.parameters.job_invalid)
        expected_msg = tests.models.messages.msg_user_nok
        assert returned_msg == expected_msg

    def test_add_user_none(self):
        service = ServiceUser()
        returned_msg = service.add_user(tests.models.parameters.user_none, tests.models.parameters.job_valid)
        expected_msg = tests.models.messages.msg_params_invalid
        assert returned_msg == expected_msg

    def test_update_user_success(self):
        service = ServiceUser()
        service.add_user(tests.models.parameters.user_valid, tests.models.parameters.job_valid)
        returned_msg = service.update_user(tests.models.parameters.user_valid, tests.models.parameters.job_update)
        expected_msg = tests.models.messages.msg_user_update
        assert returned_msg == expected_msg

    def test_update_user_not_existing(self):
        service = ServiceUser()
        service.add_user(tests.models.parameters.user_valid, tests.models.parameters.job_valid)
        returned_msg = service.update_user(tests.models.parameters.user_nonexistent, tests.models.parameters.job_update)
        expected_msg = tests.models.messages.msg_user_nonexistent
        assert returned_msg == expected_msg

    def test_update_user_failed(self):
        service = ServiceUser()
        service.add_user(tests.models.parameters.user_valid, tests.models.parameters.job_valid)
        returned_msg = service.update_user(tests.models.parameters.user_invalid, tests.models.parameters.job_valid)
        expected_msg = tests.models.messages.msg_user_nok
        assert returned_msg == expected_msg

    def test_update_user_none(self):
        service = ServiceUser()
        service.add_user(tests.models.parameters.user_valid, tests.models.parameters.job_valid)
        returned_msg = service.update_user(tests.models.parameters.user_none, tests.models.parameters.job_valid)
        expected_msg = tests.models.messages.msg_params_invalid
        assert returned_msg == expected_msg

    def test_get_user_by_name_success(self):
        service = ServiceUser()
        service.add_user(tests.models.parameters.user_valid, tests.models.parameters.job_valid)
        returned_msg = service.get_user_by_name(tests.models.parameters.user_valid)
        assert returned_msg.name == tests.models.parameters.user_valid

    def test_get_user_by_name_not_existing(self):
        service = ServiceUser()
        service.add_user(tests.models.parameters.user_valid, tests.models.parameters.job_valid)
        returned_msg = service.get_user_by_name(tests.models.parameters.user_nonexistent)
        expected_msg = tests.models.messages.msg_user_not_found
        assert returned_msg == expected_msg

    def test_get_user_by_name_failed(self):
        service = ServiceUser()
        service.add_user(tests.models.parameters.user_valid, tests.models.parameters.job_valid)
        returned_msg = service.get_user_by_name(tests.models.parameters.user_invalid)
        expected_msg = tests.models.messages.msg_user_nok
        assert returned_msg == expected_msg

    def test_get_user_by_name_none(self):
        service = ServiceUser()
        service.add_user(tests.models.parameters.user_valid, tests.models.parameters.job_valid)
        returned_msg = service.get_user_by_name(tests.models.parameters.user_none)
        expected_msg = tests.models.messages.msg_params_invalid
        assert returned_msg == expected_msg

    def test_remove_user_success(self):
        service = ServiceUser()
        service.add_user(tests.models.parameters.user_valid, tests.models.parameters.job_valid)
        returned_msg = service.remove_user(tests.models.parameters.user_valid)
        expected_msg = tests.models.messages.msg_user_removed
        assert returned_msg == expected_msg

    def test_remove_user_not_existing(self):
        service = ServiceUser()
        service.add_user(tests.models.parameters.user_valid, tests.models.parameters.job_valid)
        returned_msg = service.remove_user(tests.models.parameters.user_nonexistent)
        expected_msg = tests.models.messages.msg_user_not_found
        assert returned_msg == expected_msg
