# aioblox

Asynchronous roblox api wrapper

## Example code

```python
import asyncio
import aioblox

async def main():
    async with aioblox.Client() as client:
        user = await client.fetch_user(1)
        print(user)

asyncio.get_event_loop().run_until_complete(main())
```
