from runtime import Args
from typings.crawl4ai.crawl4ai import Input, Output

import asyncio
from crawl4ai import AsyncWebCrawler

async def async_handler(args: Args[Input]) -> Output:
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://www.nbcnews.com/business",
        )

    return {"message": result.markdown}

"""
Each file needs to export a function named `handler`. This function is the entrance to the Tool.

Parameters:
args: parameters of the entry function.
args.input - input parameters, you can get test input value by args.input.xxx.
args.logger - logger instance used to print logs, injected by runtime.

Remember to fill in input/output in Metadata, it helps LLM to recognize and use tool.


Return:
The return data of the function, which should match the declared output parameters.
"""
def handler(args: Args[Input]) -> Output:
    return asyncio.run(async_handler(args))