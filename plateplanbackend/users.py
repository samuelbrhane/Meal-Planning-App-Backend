from channels.generic.websocket import AsyncWebsocketConsumer
import json
from mealapp.models import Meal
from mealapp.serializers import MealSerializer

class MealUsers(AsyncWebsocketConsumer):
    async def connect(self):
        print("connect")
        self.user = self.scope["user"]
        self.group_name = "user_%s" % self.user.id

        # Join the group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()
        print("WebSocket connection established")

    async def disconnect(self, close_code):
        # Leave the group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)

        # Check if the action is 'delete'
        if data['action'] == 'delete':
            meal_id = data['id']
            print("meal_id",meal_id)

            try:
                meal = Meal.objects.get(id=meal_id, user=self.user)
                meal.delete()

                # Send a message to the group
                await self.channel_layer.group_send(
                    self.group_name,
                    {
                        'type': 'meal_deleted',
                        'id': meal_id
                    }
                )

            except Meal.DoesNotExist:
                pass

        # Check if the action is 'update'
        elif data['action'] == 'update':
            meal_data = data['meal']
            print("update data",meal_data)

            try:
                meal = Meal.objects.get(id=meal_data['id'], user=self.user)
                serializer = MealSerializer(meal, data=meal_data)

                if serializer.is_valid():
                    serializer.save()

                    # Send a message to the group
                    await self.channel_layer.group_send(
                        self.group_name,
                        {
                            'type': 'meal_updated',
                            'meal': serializer.data
                        }
                    )

            except Meal.DoesNotExist:
                pass

    async def meal_deleted(self, event):
        meal_id = event['id']

        # Send a message to the WebSocket
        await self.send(text_data=json.dumps({
            'action': 'delete',
            'id': meal_id
        }))

    async def meal_updated(self, event):
        meal_data = event['meal']

        # Send a message to the WebSocket
        await self.send(text_data=json.dumps({
            'action': 'update',
            'meal': meal_data
        }))
