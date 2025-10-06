import asyncio
import aiohttp
import time

async def fetch_data(session, url, player_id):
    try:
        async with session.get(url) as response:
            data = await response.json()
            return {"player_id": player_id, "data": data, "status": "success"}
    except Exception as e:
        return {"player_id": player_id, "error": str(e), "status": "failed"}

async def main():
    base_url = "https://api.sampleapis.com/baseball/hitsSingleSeason/"
    
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1, 51):
            url = f"{base_url}{i}"
            task = fetch_data(session, url, i)
            tasks.append(task)
        
        results = await asyncio.gather(*tasks)
        return results

if __name__ == "__main__":
    start_time = time.time()
    
    # Run the async function
    results = asyncio.run(main())
    
    end_time = time.time()
    
    # Print results
    for result in results:
        print(f"Player {result['player_id']}: {result['status']}")
    
    print(f"\nTotal time taken: {end_time - start_time:.2f} seconds")