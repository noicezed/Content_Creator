from crewai import Crew
from textwrap import dedent
from Agents.market_analyze_agent import MarketAnalyzeAgents
from Tasks.market_analyze_tasks import MarketAnalyzeTasks
from llm.gemin_vision_pro_client import Retreive



class MarketContent:
    
    def __init__(self, image_url) -> None:
        self.image_url = image_url

        self.content = Retreive().retrieval_image_content(self.image_url)

    
    def run(self):
        agents = MarketAnalyzeAgents()
        tasks = MarketAnalyzeTasks()

        market_analyse_agent = agents.market_expert_agent()

        market_analyse_task = tasks.market_expert_task(agent=market_analyse_agent, image_content=self.content)

        crew = Crew(
            agents = [market_analyse_agent],

            tasks = [market_analyse_task],

            verbose = True,
        )

        result = crew.kickoff()

        return result

if __name__ == "__main__":

    print("## Welcome to  Market Analyse")
    print('----------------------------')

    # file_path = input(
    #     dedent("""
    #     Give file Path:- """)
    # )
    file_path = 'src/bouncetagfun.jpg'


    market_analyser_crew = MarketContent(image_url=file_path)
    result = market_analyser_crew.run()

    print("\n\n########################")
    print(f"## Here is the Content for Image")
    print("########################\n")
    print(result)