from crewai import task
from tools import YoutubeChannelSearchTool
yt_tool = YoutubeChannelSearchTool(youtube_channel_handle='@krishnaik06')

from agents import blog_researcher, blog_writer

research_task=task(description= ("Identify the video {topic}."
                                "Get detailed information about the video form the channel."),
                                expected_output="A comprehensive 3 paragraphs long report based on the {topic} of video content",
                                tools=[yt_tool],
                                agent=blog_researcher,)

write_task=task(description=("get the info from the youtube channel on the topic {topic},"
                                ), expected_output="Summarize the info from the youtube channel video on the topic{topic}",
                                tools=[yt_tool],
                                agent=blog_writer,
                                async_execution=False,
                                output_file="new-blog-post.md")

