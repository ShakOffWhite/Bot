from aiohttp import web
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings
from botbuilder.schema import Activity

# Настройка адаптера
settings = BotFrameworkAdapterSettings(app_id="YOUR_APP_ID", app_password="YOUR_APP_SECRET")
adapter = BotFrameworkAdapter(settings)

# Простая функция для обработки сообщений
async def handle_incoming_message(request):
    body = await request.json()
    activity = Activity().deserialize(body)
    await adapter.process_activity(activity, auth_header="", bot_callback=process_message)
    return web.Response(status=200)

async def process_message(context):
    await context.send_activity("Hello! This is a simple bot.")

app = web.Application()
app.router.add_post("/api/messages", handle_incoming_message)

if __name__ == "__main__":
    web.run_app(app, port=8000)
