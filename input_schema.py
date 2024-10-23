INPUT_SCHEMA = {
    "prompt": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["A cat holding a sign that says hello world"]
    },
     "workflow": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["https://github.com/Nirmal2000/ComfyUI-Inferless-template/raw/main/workflows/flux_workflow.json"]
    },    
}
