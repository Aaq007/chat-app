from djangochannelsrestframework.decorators import action
from djangochannelsrestframework.consumers import AsyncAPIConsumer


class MyConsumer(AsyncAPIConsumer):

    @action()
    async def an_async_action(self, some=None, **kwargs):
        # do something async
        return {'response_with': 'some message'}, 200
