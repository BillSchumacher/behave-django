from behave import *

use_step_matcher("re")


@given("A user exists")
def step_impl(context):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    context.user = User.objects.create_user(
        username='test',
        password='test',
        is_active=True
    )


@when("I query the user groups and permissions")
def step_impl(context):
    print(context.user.groups.all())
    print(context.user.user_permissions.all())


@then("No error is raised")
def step_impl(context):
    context.test.assertTrue(True)
