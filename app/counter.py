from nicegui import ui

class CounterModel:
    def __init__(self):
        self.value = 0

def create() -> None:
    @ui.page('/counter')
    def page():
        # Using a CounterModel instance for the counter to easily bind and update the display
        counter_model = CounterModel()

        with ui.card().classes('w-full max-w-sm mx-auto p-6 bg-white shadow-xl rounded-lg border border-gray-200'):
            with ui.column().classes('items-center w-full gap-6'):
                ui.label('Simple Counter').classes('text-4xl font-extrabold text-gray-800 mb-4')

                # Display for the counter value, convert to string for display
                ui.label().bind_text_from(counter_model, 'value', lambda v: str(v)).classes('text-8xl font-bold text-blue-600 mb-8').mark('counter_display')

                with ui.row().classes('w-full justify-center gap-4'):
                    # Decrement button
                    ui.button('Decrement', on_click=lambda: setattr(counter_model, 'value', counter_model.value - 1)) \
                        .props('icon=remove') \
                        .classes('w-32 bg-red-600 hover:bg-red-700 text-white font-semibold py-3 rounded-lg shadow-md transition duration-300 ease-in-out') \
                        .mark('decrement_button')

                    # Increment button
                    ui.button('Increment', on_click=lambda: setattr(counter_model, 'value', counter_model.value + 1)) \
                        .props('icon=add') \
                        .classes('w-32 bg-green-600 hover:bg-green-700 text-white font-semibold py-3 rounded-lg shadow-md transition duration-300 ease-in-out') \
                        .mark('increment_button')

                # Reset button
                ui.button('Reset', on_click=lambda: setattr(counter_model, 'value', 0)) \
                    .props('icon=restart_alt') \
                    .classes('w-full mt-6 bg-yellow-500 hover:bg-yellow-600 text-white font-semibold py-3 rounded-lg shadow-md transition duration-300 ease-in-out') \
                    .mark('reset_button')

        # Responsive styling for the page itself (optional, but enhances overall look)
        ui.add_head_html('''
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body {
                    background-color: #f0f2f5; /* Light grey background */
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    min-height: 100vh;
                    margin: 0;
                }
            </style>
        ''')