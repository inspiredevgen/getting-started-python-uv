import asyncio
from agent import DatabaseConn, SupportDependencies, support_agent

async def test_support_agent():
    deps = SupportDependencies(user_id=103, db=DatabaseConn())

    #Test query 1: subscription plan
    result = await support_agent.run("What is my subscription plan ?", deps=deps)
    print(result.data)

if __name__ == "__main__":
    asyncio.run(test_support_agent)