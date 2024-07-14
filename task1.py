import argparse
import os
import shutil
import asyncio
import aiofiles

async def read_folder(source_folder, destination_folder):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            await copy_file(os.path.join(root, file), destination_folder)

async def copy_file(file_path, destination):
    _, extension = os.path.splitext(file_path)
    toCopy = os.path.join(destination, extension.lstrip('.'))
    os.makedirs(toCopy, exist_ok=True)
    async with aiofiles.open(file_path, 'rb') as read_file:
        content = await read_file.read()
        async with aiofiles.open(os.path.join(toCopy, os.path.basename(file_path)), 'wb') as write_file:
            await write_file.write(content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sort files based on extension.')
    parser.add_argument('source')
    parser.add_argument('destination')
    args = parser.parse_args()

    asyncio.run(read_folder(args.source, args.destination))