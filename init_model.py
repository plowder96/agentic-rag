from smolagents import OpenAIServerModel

def initialize_model(base,key):
    agent = OpenAIServerModel(
        model_id='gpt-4o-mini',
        api_base=base,
        api_key=key
    )
    return agent
