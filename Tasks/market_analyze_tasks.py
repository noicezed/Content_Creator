from textwrap import dedent
from crewai import Task

class MarketAnalyzeTasks:


    def market_expert_task(self, agent, image_content:str) -> None:

        return Task(
                description = dedent(f"""I'm your go-to Market Content Expert, specializing in 
                    crafting dynamic content for various platforms. Using client-provided resources, 
                    I create engaging narratives tailored to each channel—from social media to blogs and beyond. 
                    With a focus on results, I ensure our content resonates with the target audience, 
                    driving meaningful engagement and brand growth. Let's collaborate to elevate your online presence with 
                    impactful content! Your task to genrate marketing content post around this {image_content} and it's compulsory,
                    and also include hastags for specific content. This content is going to use for Facebook, Instgram, other social platform
                    to get reach about the {image_content} content.

                    ** Note **
                    1) You need to creator Content for social media Instagram, Facebook and Twitter
                    2) Content Must be authenicate and crystal clear
                    3) Dont't repeat same output/ content
                """),

                agent = agent,
            )
