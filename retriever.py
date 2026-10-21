from smolagents import Tool

class RetrieverTool(Tool):
    name = 'retriever'
    description = 'Leverages semantic search to retrieve the most contextually relevant sections from the documentation based on a user query.'
    inputs = {
        'query': {
            'type': 'string',
            'description': 'The search query to match against documentation. Phrase it as a natural language statement that reflects the kind of information you\'re seeking (e.g., \'How do I configure logging?\').'
        }
    }
    output_type = 'string'

    def __init__(self,vector_db,**kwargs):
        super().__init__(**kwargs)
        self.vector_db = vector_db # save the vector db reference

    def forward(self,query: str) -> str:
        if not isinstance(query, str):
            raise ValueError('Query must be a string.')

        results = self.vector_db.similarity_search(query,k=10)
        formatted_docs = '\n'.join(f'\n\n===== Document {i} =====\n{doc.page_content}' for i, doc in enumerate(results))
        return f'\nRetrieved documents:\n{formatted_docs}'
