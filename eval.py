import weave

eval_dataset = load_your_dataset(path)

# define your model in the abstract sense
class Model(weave.Model):
    model_id: str
    
    @weave.op
    def predict(self, input):
        # call your LLM and process the response
        return {"model_output": model_output}

# define a scorer function
def accuracy(model_output, target):
    return {"accuracy": model_output == target}

# start tracking the evaluation
weave.init("project_name")

# define the model
model = Model(model_id="claude-sonnet")

# define the evaluation
evaluation = weave.Evaluation(dataset=eval_dataset, scorers=[accuracy])

# evaluate the model
evaluation.evaluate(model)