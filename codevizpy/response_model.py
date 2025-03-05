json_schema = {
    "title": "CodeGraph",
    "description": "Represents the structure of code and its entry point",
    "type": "object",
    "properties": {
        "code_entry": {
            "type": "string",
            "description": "The method or class that is the entry point for the source code"
        },
        "code_graph": {
            "type": "object",
            "description": "A dictionary where each key is a method or class and the value is a list of methods or classes that are directly called by the key",
            "additionalProperties": {
                "type": "array",
                "items": {
                    "type": "string"
                }
            }
        }
    },
    "required": ["code_entry", "code_graph"]
}