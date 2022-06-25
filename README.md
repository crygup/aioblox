# aioblox

Asynchronous roblox api wrapper

## Example code

```python
import asyncio
import aioblox

async def main():
    client = aioblox.Client()
    user = await client.fetch_user(1)
    print(user)
    await client.close()

asyncio.new_event_loop().run_until_complete(main())
```
