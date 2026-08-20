from backend.schemas.models import QueryRequest

class QueryService:
    @staticmethod
    def process_query(request: QueryRequest) -> dict:
        """Processes the input query and returns the default skeleton response.
        
        This will later integrate with retriever and LLM agents.
        """
        return {
            "answer": "Query received successfully.",
            "citations": []
        }
