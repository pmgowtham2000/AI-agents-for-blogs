from crewai import Agent
from tools import YoutubeChannelSearchTool
yt_tool = YoutubeChannelSearchTool(youtube_channel_handle='@krishnaik06')
import os
os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"

blog_researcher=Agent(
    role="Blog Researcher from Youtube Videos",
    goal="get the relevant video content for the topic {topic} from YT channel",
    verbose=True,
    memory=True,
    backstory=("Expert in  understanding videos in AI Data Science, Machine Learning and GenAI and providing solutions"),
    tools=[],
    allow_delegation=True
)

blog_writer=Agent(
    role="Blog Writer",
    goal="Narrate compiling tech stories about the video {topic} from YT channel",
    verbose=True, 
    memory=True,
    backstory=("With a flair for simplifying complex topics, you craft engaging narratives that captivate "
    "and educate, bringing new discoveries to light in an accessible manner"),
    tools=[yt_tool],
    allow_delegation=False
)

