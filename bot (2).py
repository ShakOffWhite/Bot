from flask import Flask, request
from botbuilder.core import BotFrameworkAdapter, TurnContext
from botbuilder.schema import Activity

app = Flask(__name__)

# Создайте адаптер Bot Framework, используя Bot ID и Bot Secret
adapter = BotFrameworkAdapter(app_id="YOUR_BOT_ID", app_password="YOUR_BOT_SECRET")

class MyBot:
    async def on_turn(self, turn_context: TurnContext):
        if turn_context.activity.type == "message":
            await turn_context.send_activity(f"Hello, {turn_context.activity.from_property.name}")

bot = MyBot()

@app.route("/api/messages", methods=["POST"])
def messages():
    if "application/json" in request.headers["Content-Type"]:
        body = request.json
    else:
        return {"status": "Unsupported media type"}, 415

    activity = Activity().deserialize(body)
    auth_header = request.headers["Authorization"] if "Authorization" in request.headers else ""

    async def aux_func(turn_context):
        await bot.on_turn(turn_context)

    task = adapter.process_activity(activity, auth_header, aux_func)
    task.wait()
    return {"status": "ok"}

if __name__ == "__main__":
    app.run()
