from nicegui.testing import User
import pytest

async def test_counter_application(user: User) -> None:
    # Open the counter page
    await user.open('/counter')

    # Check initial counter value
    await user.should_see(content='0', marker='counter_display')

    # Click increment button and check value
    user.find('increment_button').click()
    await user.should_see(content='1', marker='counter_display')

    # Click increment button again
    user.find('increment_button').click()
    await user.should_see(content='2', marker='counter_display')

    # Click decrement button and check value
    user.find('decrement_button').click()
    await user.should_see(content='1', marker='counter_display')

    # Click decrement button again, going below zero
    user.find('decrement_button').click()
    await user.should_see(content='0', marker='counter_display')
    
    user.find('decrement_button').click()
    await user.should_see(content='-1', marker='counter_display')

    # Click reset button and check value
    user.find('reset_button').click()
    await user.should_see(content='0', marker='counter_display')