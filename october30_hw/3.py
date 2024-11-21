import asyncio
import aiofiles
import json
from pathlib import Path

async def read_and_process_file(file_path):
    """
    Asynchronously reads a JSON file and extracts user names and total purchase amounts.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict: Extracted information including user names and total purchase amounts.
    """
    try:
        async with aiofiles.open(file_path, 'r') as file:
            content = await file.read()
            data = json.loads(content)

            result = []
            for user in data:
                name = user["name"]
                total_purchase = sum(item["amount"] for item in user.get("purchases", []))
                result.append({"name": name, "total_purchase": total_purchase})
            
            return {"file": file_path, "users": result}
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in file {file_path}: {e}")
    except Exception as e:
        print(f"Unexpected error while processing file {file_path}: {e}")

async def main():
    """
    Main function to process multiple JSON files concurrently.
    """
    directory = Path('./')
    files = list(directory.glob('*.json'))

    if not files:
        print("No JSON files found in the directory.")
        return

    tasks = [read_and_process_file(file) for file in files]
    results = await asyncio.gather(*tasks)

    print("\nProcessed Data:")
    for result in results:
        if result:
            print(f"File: {result['file']}")
            for user in result['users']:
                print(f"  Name: {user['name']}, Total Purchases: {user['total_purchase']:.2f}")

if __name__ == "__main__":
    asyncio.run(main())
